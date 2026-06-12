def classify_news(text):

    categories = {
        "Technology": ["ai", "software", "tech", "computer", "app", "cyber", "gadget"],
        "Sports": ["cricket", "football", "sports", "player", "match", "tournament"],
        "Politics": ["government", "election", "minister", "parliament", "policy"],
        "Business": ["market", "finance", "stock", "economy", "trade", "company"],
        "Health": ["health", "hospital", "doctor", "medicine", "disease", "vaccine"],
        "Entertainment": ["movie", "film", "music", "actor", "celebrity", "tv"],
        "World": ["country", "nation", "international", "war", "united nations"],
        "Science": ["research", "study", "space", "discovery", "experiment"]
    }

    text = text.lower()

    for category, words in categories.items():

        for word in words:

            if word in text:
                return category

    return "General"
