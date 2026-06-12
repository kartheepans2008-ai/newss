def summarize(text):

    words = text.split()

    return " ".join(words[:25]) + "..."
