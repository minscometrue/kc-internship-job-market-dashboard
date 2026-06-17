import streamlit as st
from job_market import load_job_postings


st.set_page_config(
    page_title="KC Internship Dashboard",
    page_icon="📊",
    layout="wide",
)

st.title("KC Internship & Job Market Intelligence Dashboard")

df = load_job_postings("data/raw/job_postings_sample.csv")

st.subheader("Sample Job Postings")
st.dataframe(df)

st.subheader("Basic Summary")
st.write(f"Total job postings: {len(df)}")
st.write(f"Companies: {df['company'].nunique()}")
st.write(f"Domains: {df['domain'].nunique()}")
