def filter_topic(articles, topic):

    if topic.strip() == "":
        return articles

    results = []

    topic = topic.lower()

    for article in articles:

        text = (
            article["title"] +
            " " +
            article["summary"]
        ).lower()

        if topic in text:
            results.append(article)

    return results
