import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download("stopwords")
nltk.download("punkt")

# read txt file
with open("paragraphs.txt", "r+") as file:
    text = file.read()

stop_words = set(stopwords.words("english"))

word_tokens = word_tokenize(text)

filtered_words = []
# create list of filted words = are not stops words
for w in word_tokens:
    if w not in stop_words:
        filtered_words.append(w)
# create the text from them
processed_text = " ".join(filtered_words)

# Open the file in write mode ('w')
with open("processed.txt", "w") as file:
    # Write some text to the file
    file.write(processed_text)

# turned to lower to not be count same word in case senstive as diffrenet words
text_to_count = processed_text.lower().split()
# here count words using Counter
wordfreq = Counter(text_to_count)
for word, freq in dict(wordfreq).items():
    print(f"{word}: {freq}")
