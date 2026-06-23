import streamlit as st
import pandas as pd
import os

# Page Config
st.set_page_config(
    page_title="AI Data Intelligence Dashboard",
    layout="wide"
)

st.title("🚀 AI Data Intelligence Dashboard")

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

# Safe CSV Loader
def load_csv(filename):
    filepath = os.path.join(OUTPUT_DIR, filename)

    if os.path.exists(filepath):
        return pd.read_csv(filepath)
    else:
        st.warning(f"⚠️ {filename} not found")
        return pd.DataFrame()

# Load Data
startups = load_csv("startups.csv")
products = load_csv("products.csv")
papers = load_csv("research_papers.csv")
jobs = load_csv("jobs.csv")
news = load_csv("news.csv")
mapping = load_csv("entity_mapping.csv")

# Metrics
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Startups", len(startups))

with col2:
    st.metric("Products", len(products))

with col3:
    st.metric("Research Papers", len(papers))

with col4:
    st.metric("Jobs", len(jobs))

with col5:
    st.metric("News", len(news))

st.divider()

# Tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🏢 Startups",
    "📦 Products",
    "📚 Research Papers",
    "💼 Jobs",
    "📰 News",
    "🔗 Entity Mapping"
])

with tab1:
    st.subheader("Startups Dataset")
    st.dataframe(startups, use_container_width=True)

with tab2:
    st.subheader("Products Dataset")
    st.dataframe(products, use_container_width=True)

with tab3:
    st.subheader("Research Papers Dataset")
    st.dataframe(papers, use_container_width=True)

with tab4:
    st.subheader("Jobs Dataset")
    st.dataframe(jobs, use_container_width=True)

with tab5:
    st.subheader("News Dataset")
    st.dataframe(news, use_container_width=True)

with tab6:
    st.subheader("Entity Resolution Mapping")
    st.dataframe(mapping, use_container_width=True)

st.success("✅ Pipeline data loaded successfully")