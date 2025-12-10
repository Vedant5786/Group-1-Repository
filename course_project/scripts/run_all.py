import os
import subprocess
import sys
from pathlib import Path
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent


def run(cmd, env=None):
    print("Running:", " ".join(cmd))
    result = subprocess.run(cmd, env=env or os.environ, check=True)
    return result


def main():
    load_dotenv()
    env = os.environ.copy()
    # Expect FRED_API_KEY in env
    if not env.get("FRED_API_KEY"):
        raise EnvironmentError("FRED_API_KEY environment variable not set")

    python = sys.executable
    run([python, str(ROOT / "scripts" / "data_acquisition.py"), "--start-date", "1990-01-01", "--end-date", "2024-12-31"] , env=env)
    run([python, str(ROOT / "scripts" / "data_cleaning_integration.py")], env=env)
    run([python, str(ROOT / "scripts" / "eda.py")], env=env)
    run([python, str(ROOT / "scripts" / "modeling.py")], env=env)
    print("Workflow complete.")


if __name__ == "__main__":
    main()
