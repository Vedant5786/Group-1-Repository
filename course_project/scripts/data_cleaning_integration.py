import argparse
from pathlib import Path
import pandas as pd


def load_series(path: Path, column_name: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    if "date" not in df.columns:
        raise ValueError(f"Expected 'date' column in {path}")
    df["date"] = pd.to_datetime(df["date"])
    df[column_name] = pd.to_numeric(df[column_name], errors="coerce")
    df = df.sort_values("date").dropna(subset=[column_name])
    return df[["date", column_name]]


def main():
    parser = argparse.ArgumentParser(description="Clean and integrate UNRATE and PCE series")
    parser.add_argument("--raw-dir", default="data/raw", help="Directory containing raw CSV files")
    parser.add_argument("--outdir", default="data/processed", help="Directory for processed outputs")
    args = parser.parse_args()

    raw_dir = Path(args.raw_dir)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    unrate = load_series(raw_dir / "unrate_raw.csv", "unrate")
    pce = load_series(raw_dir / "pce_raw.csv", "pce")

    merged = (
        unrate.merge(pce, on="date", how="inner")
        .sort_values("date")
        .reset_index(drop=True)
    )

    # Basic checks
    if merged["date"].duplicated().any():
        raise ValueError("Duplicate dates found after merge")

    merged.to_csv(outdir / "unemployment_pce_merged.csv", index=False)

    # Save quick profiling info
    summary = {
        "rows": len(merged),
        "date_min": merged["date"].min().strftime("%Y-%m-%d"),
        "date_max": merged["date"].max().strftime("%Y-%m-%d"),
        "missing_unrate": int(merged["unrate"].isna().sum()),
        "missing_pce": int(merged["pce"].isna().sum()),
    }
    (outdir / "data_profile.txt").write_text("\n".join(f"{k}: {v}" for k, v in summary.items()))

    print(f"Merged dataset saved to {outdir / 'unemployment_pce_merged.csv'}")


if __name__ == "__main__":
    main()
