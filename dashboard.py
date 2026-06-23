import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Data Intelligence Dashboard",
    layout="wide"
)

st.title("🚀 AI Data Intelligence Dashboard")

# Load Data
startups = pd.read_csv("../output/startups.csv")
products = pd.read_csv("../output/products.csv")
papers = pd.read_csv("../output/research_papers.csv")
jobs = pd.read_csv("../output/jobs.csv")
news = pd.read_csv("../output/news.csv")
mapping = pd.read_csv("../output/entity_mapping.csv")

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

st.success("Pipeline data loaded successfully ✅")