from pathlib import Path
import pandas as pd


def load_job_postings(csv_path: str | Path) -> pd.DataFrame:
    """
    Load job postings from a CSV file.

    Args:
        csv_path: Path to the job postings CSV file.

    Returns:
        pandas DataFrame containing job posting data.
    """
    csv_path = Path(csv_path)

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    df = pd.read_csv(csv_path)
    return df
