import argparse
from pathlib import Path
import pandas as pd
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")


def run_models(df: pd.DataFrame):
    # Level-level OLS
    X = sm.add_constant(df["unrate"])
    model_lvl = sm.OLS(df["pce"], X, missing="drop").fit()

    # Lagged unemployment to test predictive power
    df_lag = df.copy()
    df_lag["unrate_lag1"] = df_lag["unrate"].shift(1)
    df_lag = df_lag.dropna()
    X_lag = sm.add_constant(df_lag[["unrate", "unrate_lag1"]])
    model_lag = sm.OLS(df_lag["pce"], X_lag, missing="drop").fit()

    return model_lvl, model_lag, df_lag


def main():
    parser = argparse.ArgumentParser(description="Model relationship between unemployment and PCE")
    parser.add_argument("--data", default="data/processed/unemployment_pce_merged.csv", help="Path to merged CSV")
    parser.add_argument("--outdir", default="outputs", help="Directory for model outputs")
    args = parser.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(args.data, parse_dates=["date"])
    model_lvl, model_lag, df_lag = run_models(df)

    # Save summaries
    summary_path = outdir / "modeling_summary.txt"
    with summary_path.open("w") as f:
        f.write("Level model: PCE ~ Unemployment\n")
        f.write(model_lvl.summary().as_text())
        f.write("\n\nLag model: PCE ~ Unemployment + Lag1(Unemployment)\n")
        f.write(model_lag.summary().as_text())
    coef_df = pd.DataFrame({
        "level_model": model_lvl.params,
        "level_pvalues": model_lvl.pvalues,
        "lag_model": model_lag.params,
        "lag_pvalues": model_lag.pvalues,
    })
    coef_df.to_csv(outdir / "modeling_coefficients.csv")

    # Predicted vs actual plot for level model
    df_pred = df.copy()
    df_pred["pce_pred"] = model_lvl.predict(sm.add_constant(df_pred["unrate"]))
    plt.figure(figsize=(8, 6))
    sns.lineplot(x=df_pred["date"], y=df_pred["pce"], label="Actual")
    sns.lineplot(x=df_pred["date"], y=df_pred["pce_pred"], label="Predicted", linestyle="--")
    plt.title("Actual vs. Predicted PCE (OLS)")
    plt.ylabel("PCE (Billions of $)")
    plt.xlabel("Date")
    plt.tight_layout()
    plt.savefig(outdir / "predicted_vs_actual.png", dpi=300)
    plt.close()

    # Residuals vs fitted
    residuals = model_lvl.resid
    fitted = model_lvl.fittedvalues
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=fitted, y=residuals, alpha=0.5)
    plt.axhline(0, color="red", linestyle="--")
    plt.title("Residuals vs. Fitted (Level Model)")
    plt.xlabel("Fitted PCE")
    plt.ylabel("Residuals")
    plt.tight_layout()
    plt.savefig(outdir / "residuals_vs_fitted.png", dpi=300)
    plt.close()

    print(f"Model outputs saved to {outdir}")


if __name__ == "__main__":
    main()
