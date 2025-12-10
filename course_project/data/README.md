# Data Directory

- `data/raw/`: raw downloads from FRED API (`unrate_raw.csv`, `pce_raw.csv`).
- `data/processed/`: cleaned/merged dataset (`unemployment_pce_merged.csv`) and quick profile.
- `data/box/`: place any large outputs shared via Box (not tracked; add your Box link in README). Create this directory if needed.

All data files are gitignored except documentation. Regenerate raw/processed data via `python scripts/run_all.py` after setting `FRED_API_KEY`.
