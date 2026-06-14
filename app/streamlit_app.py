import sys
from pathlib import Path

import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT / "src"))

from job_market.data_loader import load_job_postings


st.set_page_config(
    page_title="KC Internship Dashboard",
    page_icon="📊",
    layout="wide",
)

st.title("KC Internship & Job Market Intelligence Dashboard")

csv_path = PROJECT_ROOT / "data" / "raw" / "job_postings_sample.csv"
df = load_job_postings(csv_path)

st.subheader("Sample Job Postings")
st.dataframe(df)

st.subheader("Basic Summary")
st.write(f"Total job postings: {len(df)}")
st.write(f"Companies: {df['company'].nunique()}")
st.write(f"Domains: {df['domain'].nunique()}")