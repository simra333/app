def add_metadata(joke):
    """Adds a nested metadata structure to the joke"""
    joke["metadata"] = {
        "source": "Official Joke API",
        "rating": {
            "likes": 120,
            "dislikes": 10
        }
    }
    return joke

def search_jokes(keyword, jokes):
    """Searches for jokes containing keyword"""
    return [joke for joke in jokes if keyword.lower() in joke[1].lower() or keyword.lower() in joke[2].lower()]