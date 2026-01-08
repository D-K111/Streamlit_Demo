import streamlit as st
import pandas as pd

st.set_page_config(page_title="Simple HCP Steward", layout="wide")

st.title("🤖 Simple HCP Data Steward (Demo)")

# Create some fake data instead of using Snowflake
data = {
    "ID": [101, 102, 103],
    "NAME": ["Dr. Smith", "Dr. Adams", "Dr. Garcia"],
    "NPI": ["12345", "67890", "55555"],
    "CITY": ["New York", "Boston", "Chicago"]
}
df = pd.DataFrame(data)

st.write("### Current HCP Records")
st.dataframe(df, use_container_width=True)

# Simple Selection logic
selected_id = st.selectbox("Select an ID to Enrich:", df["ID"])

if st.button("Enrich with AI (Simulated)"):
    st.info(f"Simulating AI enrichment for ID {selected_id}...")
    st.success("Analysis Complete: This provider is verified at their New York location.")
