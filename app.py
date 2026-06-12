import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from agents.rss_agent import fetch_rss_news
from agents.filter_agent import filter_topic
from agents.classify_agent import classify_news
from agents.sentiment_agent import sentiment
from agents.summary_agent import summarize
from agents.trending_agent import get_trending_topics

st.title("Agentic AI News Segregation")

topic = st.text_input(
    "Enter Topic (leave blank for all news)",
    ""
)

if st.button("Fetch News"):

    articles = fetch_rss_news()

    filtered = filter_topic(
        articles,
        topic
    )

    data = []

    for article in filtered:

        text = (
            article["title"] +
            " " +
            article["summary"]
        )

        category = classify_news(text)

        senti = sentiment(text)

        short = summarize(text)

        data.append({
            "Title": article["title"],
            "Category": category,
            "Sentiment": senti,
            "Summary": short,
            "Link": article["link"]
        })

    if len(data) == 0:
        st.warning("No matching news found")

    else:

        df = pd.DataFrame(data)

        st.dataframe(df)

        st.subheader("News Articles")

        for row in data:

            st.markdown(
                f"### {row['Title']}"
            )

            st.write(
                f"Category: {row['Category']}"
            )

            st.write(
                f"Sentiment: {row['Sentiment']}"
            )

            st.write(
                row["Summary"]
            )

            st.markdown(
                f"[Read More]({row['Link']})"
            )

        st.subheader(
            "Category Analytics"
        )

        counts = (
            df["Category"]
            .value_counts()
        )

        fig, ax = plt.subplots()

        counts.plot(
            kind="bar",
            ax=ax
        )

        st.pyplot(fig)

        st.subheader("Trending Topics")

        trends = get_trending_topics(filtered)

        trend_df = pd.DataFrame(
            trends,
            columns=["Keyword", "Frequency"]
        )

        st.dataframe(trend_df)

        st.subheader("Trending Keywords Chart")

        fig2, ax2 = plt.subplots()

        ax2.bar(
            trend_df["Keyword"],
            trend_df["Frequency"]
        )

        ax2.set_title(
            "Top Trending Keywords"
        )

        plt.xticks(rotation=45)

        st.pyplot(fig2)
