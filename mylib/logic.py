import wikipedia
from textblob import TextBlob


def wiki(name="Uzbekistan", length=1):
    """this is a wikipedia fetcher"""
    my_wiki = wikipedia.summary(name, length)
    return my_wiki


def phrase(name):
    """returns phrases from Wikipedia"""
    page = wiki(name)
    blob = TextBlob(page)
    return blob.noun_phrases
