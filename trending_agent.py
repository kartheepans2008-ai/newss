import re
from collections import Counter

STOP_WORDS = {
    "the", "a", "an", "and", "or", "is", "are",
    "was", "were", "to", "of", "in", "on",
    "for", "with", "by", "from", "at", "as",
    "that", "this", "it", "be", "has", "have",
    "will", "after", "into", "about"
}


def get_trending_topics(articles, top_n=10):

    text = ""

    for article in articles:

        text += (
            article["title"] + " " +
            article["summary"] + " "
        )

    words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())

    filtered_words = [
        word
        for word in words
        if word not in STOP_WORDS
    ]

    counter = Counter(filtered_words)

    return counter.most_common(top_n)
