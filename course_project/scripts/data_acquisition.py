import os
import argparse
import json
from pathlib import Path
from datetime import datetime
import requests
import pandas as pd
from dotenv import load_dotenv

FRED_URL = "https://api.stlouisfed.org/fred/series/observations"

def fetch_series(series_id: str, api_key: str, start: str, end: str) -> pd.DataFrame:
    params = {
        "series_id": series_id,
        "api_key": api_key,
        "file_type": "json",
        "observation_start": start,
        "observation_end": end,
    }
    resp = requests.get(FRED_URL, params=params, timeout=30)
    if resp.status_code != 200:
        raise RuntimeError(f"FRED request failed ({resp.status_code}): {resp.text[:200]}")
    payload = resp.json()
    observations = payload.get("observations", [])
    if not observations:
        raise RuntimeError(f"No observations returned for {series_id}")

    df = pd.DataFrame(observations)[["date", "value"]]
    df.rename(columns={"value": series_id.lower()}, inplace=True)
    df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
    df[series_id.lower()] = pd.to_numeric(df[series_id.lower()], errors="coerce")
    df.sort_values("date", inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

def save_series(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)


def main():
    parser = argparse.ArgumentParser(description="Download UNRATE and PCE series from FRED")
    parser.add_argument("--start-date", default="1990-01-01", help="Observation start date (YYYY-MM-DD)")
    parser.add_argument("--end-date", default="2024-12-31", help="Observation end date (YYYY-MM-DD)")
    parser.add_argument("--outdir", default="data/raw", help="Output directory for raw CSV files")
    args = parser.parse_args()

    # Load local .env if present (for FRED_API_KEY)
    load_dotenv()

    api_key = os.getenv("FRED_API_KEY")
    if not api_key:
        raise EnvironmentError("FRED_API_KEY environment variable not set")

    outdir = Path(args.outdir)

    print(f"Fetching UNRATE from {args.start_date} to {args.end_date}...")
    unrate = fetch_series("UNRATE", api_key, args.start_date, args.end_date)
    save_series(unrate, outdir / "unrate_raw.csv")

    print(f"Fetching PCE from {args.start_date} to {args.end_date}...")
    pce = fetch_series("PCE", api_key, args.start_date, args.end_date)
    save_series(pce, outdir / "pce_raw.csv")

    print(f"Saved raw files to {outdir}")

if __name__ == "__main__":
    main()
