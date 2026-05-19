import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Page Config
st.set_page_config(
    page_title="Indian EV AI Dashboard",
    layout="wide"
)

# Title
st.title("🚗 Indian EV Sentiment Dashboard")

st.write(
    "AI-powered analysis of Indian EV customer reviews"
)

# Upload CSV
uploaded_file = st.file_uploader(
    "Upload EV Sentiment CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    # Read Data
    df = pd.read_csv(uploaded_file)

    # =========================
    # KPI METRICS
    # =========================

    st.subheader("📌 Dashboard Metrics")

    total_comments = len(df)

    positive_count = len(
        df[df['sentiment'] == 'Positive']
    )

    negative_count = len(
        df[df['sentiment'] == 'Negative']
    )

    neutral_count = len(
        df[df['sentiment'] == 'Neutral']
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Comments",
        total_comments
    )

    col2.metric(
        "Positive",
        positive_count
    )

    col3.metric(
        "Negative",
        negative_count
    )

    col4.metric(
        "Neutral",
        neutral_count
    )

    # =========================
    # DATA PREVIEW
    # =========================

    st.subheader("📊 Dataset Preview")

    st.dataframe(df.head())

    # =========================
    # SENTIMENT CHART
    # =========================

    st.subheader("📈 Sentiment Distribution")

    sentiment_counts = (
        df['sentiment']
        .value_counts()
    )

    fig, ax = plt.subplots()

    sentiment_counts.plot(
        kind='bar',
        ax=ax
    )

    ax.set_title("Sentiment Distribution")
    ax.set_xlabel("Sentiment")
    ax.set_ylabel("Count")

    st.pyplot(fig)

    # =========================
    # WORD CLOUD
    # =========================

    st.subheader("☁️ EV Discussion Word Cloud")

    text = " ".join(
    df['clean_comment']
    .dropna()
    .astype(str)
)

    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white'
    ).generate(text)

    fig_wc, ax_wc = plt.subplots(
        figsize=(10, 5)
    )

    ax_wc.imshow(wordcloud)

    ax_wc.axis("off")

    st.pyplot(fig_wc)

    # =========================
    # AI BUSINESS INSIGHTS
    # =========================

    st.subheader("🤖 AI Business Insights")

    positive_percent = round(
        (positive_count / total_comments) * 100,
        1
    )

    negative_percent = round(
        (negative_count / total_comments) * 100,
        1
    )

    neutral_percent = round(
        (neutral_count / total_comments) * 100,
        1
    )

    st.write(f"""
    • Positive sentiment is {positive_percent}%,
      showing strong interest in Indian EVs.

    • Negative sentiment is {negative_percent}%,
      indicating limited but important customer concerns.

    • Neutral sentiment is {neutral_percent}%,
      meaning many users are still exploring EV options.

    • Common discussion topics include:
      battery, charging, range, and EV pricing.
    """)
