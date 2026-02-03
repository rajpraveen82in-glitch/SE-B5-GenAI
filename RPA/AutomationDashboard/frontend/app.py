import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="RPA News Automation", layout="centered")

st.title("📰 RPA News Automation Dashboard")
st.write("Trigger Selenium automation via FastAPI and view results")

keyword = st.text_input("Enter search keyword:", "AI")

if st.button("Run Automation"):
    with st.spinner("Running Selenium automation..."):
        response = requests.get(f"http://127.0.0.1:8000/news/{keyword}")

        if response.status_code == 200:
            data = response.json()["articles"]

            if data:
                df = pd.DataFrame(data)
                st.success("Automation completed successfully!")
                st.dataframe(df)

                st.download_button(
                    label="⬇ Download CSV",
                    data=df.to_csv(index=False),
                    file_name="news_results.csv",
                    mime="text/csv"
                )
            else:
                st.warning("No articles found.")
        else:
            st.error("Failed to connect to FastAPI backend.")
