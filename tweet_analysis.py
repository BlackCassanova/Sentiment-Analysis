import GetOldTweets3 as got
# Cleaning Text Steps
# 1. Create a text file and take text from it
# 2. Convert the letter into lowercase
# 3. Remove punctuations

import string
from collections import Counter
import matplotlib.pyplot as plt


def get_tweets():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('ISIS') \
        .setSince("2016-01-01") \
        .setUntil("2016-05-01") \
        .setMaxTweets(1000)

    # List of tweets stored in 'tweets' variable
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)

    # Tweets are stored in text by iterating through all of it.
    text_tweets = [[tweet.text] for tweet in tweets]
    return (text_tweets)


text = ""
txt_twts = get_tweets()
length = len(txt_twts)

for i in range(0, length):
    text = txt_twts[i][0] + " " + text


# text = open('read.txt', encoding='utf-8').read()
lower_case = text.lower()
print(string.punctuation)
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
print(cleaned_text)

# tokenization
tokenized_words = cleaned_text.split()
print(tokenized_words)

# Stop Words
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final_words = []
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)

print(final_words)

# NLP Emotion Algorithm
# 1. Check if word in final word list is also present in emotion.txt
# - open emotion file
# - Loop through each line and clear it
# - Extract the word and emotion using split

# 2. If word is present -> Add the emotion to emotion_list
# 3. Finally count each emotion in the emotion list

emotion_list = []
with open('emotion.txt', 'r') as file:
    for line in file:
        # print(line)
        clear_line = line.replace('\n', '').replace(',', '').replace("'", '').strip()
        # print(clear_line)
        word, emotion = clear_line.split(':')
        # print("Word:" + word + "\t\t" + "Emotion:" + emotion)

        if word in final_words:
            emotion_list.append(emotion)


print(emotion_list)
w = Counter(emotion_list)
print(w)

fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('emotiongraph.png')
plt.show()
