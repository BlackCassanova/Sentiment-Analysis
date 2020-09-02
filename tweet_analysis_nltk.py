import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import GetOldTweets3 as got

def get_tweets():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('COVID-19') \
        .setSince("2020-01-01") \
        .setUntil("2020-08-31") \
        .setMaxTweets(5000)

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


lower_case = text.lower()
print(string.punctuation)
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
print(cleaned_text)

tokenized_words = word_tokenize(cleaned_text, "english")
print(tokenized_words)

final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

emotion_list = []
with open('emotion.txt', 'r') as file:
    for line in file:
        clear_line = line.replace('\n', '').replace(',', '').replace("'", '').strip()
        word, emotion = clear_line.split(':')
        if word in final_words:
            emotion_list.append(emotion)
print(emotion_list)
w = Counter(emotion_list)
print(w)


def senti_analysis(senti_text):
    score = SentimentIntensityAnalyzer().polarity_scores(senti_text)
    neg = score['neg']
    pos = score['pos']
    if neg > pos:
        print("Negative")
    elif pos > neg:
        print("Positive")
    else:
        print("Neutral")


senti_analysis(cleaned_text)

fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('emotiongraph.png')
plt.show()
