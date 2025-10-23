import re

_DEVANAGARI_PATTERN = re.compile(r'[\u0900-\u0963\u0966-\u097F]+')

with open("data/stopwords.txt", "r", encoding="utf-8") as f:
    _STOPWORDS = set(line.strip() for line in f)
    print("STOPWORDS: " + str(_STOPWORDS))

def tokenize(text):
    # extract words but ignore । and ॥
    words = _DEVANAGARI_PATTERN.findall(text)
    normalized = [word.replace("\u0940", "\u093F").replace("\u0942", "\u0941") for word in words]
    return [word for word in normalized if word not in _STOPWORDS]
