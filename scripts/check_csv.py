import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT / "src"))

from job_market.data_loader import load_job_postings


csv_path = PROJECT_ROOT / "data" / "raw" / "job_postings_sample.csv"

df = load_job_postings(csv_path)

print("=== head ===")
print(df.head())
print("=== shape ===")
print(df.shape)
print("=== columns ===")
print(df.columns)
print("=== info ===")
df.info()
print("=== isna ===")
print(df.isna().sum())
