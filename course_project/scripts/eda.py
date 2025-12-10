import argparse
from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")


def main():
    parser = argparse.ArgumentParser(description="Exploratory data analysis for unemployment and PCE")
    parser.add_argument("--data", default="data/processed/unemployment_pce_merged.csv", help="Path to merged CSV")
    parser.add_argument("--outdir", default="outputs", help="Directory for output figures and summary")
    args = parser.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(args.data, parse_dates=["date"])

    # Basic stats
    summary_lines = []
    summary_lines.append("Rows: %d" % len(df))
    summary_lines.append("Date range: %s to %s" % (df["date"].min().date(), df["date"].max().date()))
    summary_lines.append("Correlation (Pearson) unrate vs pce: %.4f" % df["unrate"].corr(df["pce"]))
    summary_lines.append("Unrate describe:\n%s" % df["unrate"].describe())
    summary_lines.append("PCE describe:\n%s" % df["pce"].describe())
    (outdir / "eda_summary.txt").write_text("\n\n".join(map(str, summary_lines)))

    # Line chart over time
    plt.figure(figsize=(12, 6))
    ax1 = sns.lineplot(data=df, x="date", y="unrate", label="Unemployment Rate (%)")
    ax2 = ax1.twinx()
    sns.lineplot(data=df, x="date", y="pce", ax=ax2, color="orange", label="PCE (Billions)")
    ax1.set_ylabel("Unemployment Rate (%)")
    ax2.set_ylabel("PCE (Billions of $)")
    ax1.set_xlabel("Date")
    ax1.set_title("Unemployment vs. Personal Consumption Expenditures (1990-2024)")
    ax1.legend(loc="upper left")
    ax2.legend(loc="upper right")
    plt.tight_layout()
    plt.savefig(outdir / "trends_over_time.png", dpi=300)
    plt.close()

    # Scatter with regression line
    plt.figure(figsize=(8, 6))
    sns.regplot(data=df, x="unrate", y="pce", scatter_kws={"alpha":0.5})
    plt.title("Unemployment vs. PCE (level-level)")
    plt.xlabel("Unemployment Rate (%)")
    plt.ylabel("PCE (Billions of $)")
    plt.tight_layout()
    plt.savefig(outdir / "correlation_scatter.png", dpi=300)
    plt.close()

    # Month-over-month change scatter
    df_change = df.assign(
        unrate_change=df["unrate"].diff(),
        pce_change=df["pce"].diff()
    ).dropna()
    plt.figure(figsize=(8, 6))
    sns.regplot(data=df_change, x="unrate_change", y="pce_change", scatter_kws={"alpha":0.4})
    plt.title("Change vs. Change (MoM)")
    plt.xlabel("Change in Unemployment Rate (pp)")
    plt.ylabel("Change in PCE (Billions of $)")
    plt.tight_layout()
    plt.savefig(outdir / "change_scatter.png", dpi=300)
    plt.close()

    print(f"EDA outputs saved to {outdir}")


if __name__ == "__main__":
    main()
