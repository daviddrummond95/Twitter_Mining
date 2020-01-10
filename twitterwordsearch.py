import tweepy
import pandas as pd
API = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
def sentiment_value(paragraph):
    analyser = SentimentIntensityAnalyzer()
    result = analyser.polarity_scores(paragraph)
    score = result['compound']
    return round(score, 1)
query = "AI"
from nltk.sentiment.vader import SentimentIntensityAnalyzer
def toDataFrame(tweets, query):

    DataSet = pd.DataFrame()

    DataSet['tweetID'] = [tweet.id for tweet in tweets]
    DataSet['tweetText'] = [tweet.text for tweet in tweets]
    DataSet['Sentiment'] = [sentiment_value(tweet.text) for tweet in tweets]
    DataSet['tweetRetweetCt'] = [tweet.retweet_count for tweet in tweets]
    DataSet['tweetFavoriteCt'] = [tweet.favorite_count for tweet in tweets]
    DataSet['tweetSource'] = [tweet.source for tweet in tweets]
    DataSet['tweetCreated'] = [tweet.created_at for tweet in tweets]
    DataSet['Query'] = [query for tweet in tweets]
    DataSet['userID'] = [tweet.user.id for tweet in tweets]
    DataSet['userScreen'] = [tweet.user.screen_name for tweet in tweets]
    DataSet['userName'] = [tweet.user.name for tweet in tweets]
    DataSet['userCreateDt'] = [tweet.user.created_at for tweet in tweets]
    DataSet['userDesc'] = [tweet.user.description for tweet in tweets]
    DataSet['userFollowerCt'] = [tweet.user.followers_count for tweet in tweets]
    DataSet['userFriendsCt'] = [tweet.user.friends_count for tweet in tweets]


    return DataSet
def searchall(earliest):
    Queries = ['AI', 'Artificial Intelligence', 'Robots', 'Bots', 'Machine Learning', 'Neural Networks']
    DF = pd.DataFrame()
    for query in Queries:
        results = API.search(q=query, lang="en", count=200, result_type="recent", max_id=earliest)
        tempDF = toDataFrame(results, query)
        DF = pd.concat([DF, tempDF], ignore_index=True)
    return(DF)
def searchallfirst():
    Queries = ['AI', 'Artificial Intelligence', 'Robots', 'Bots', 'Machine Learning', 'Neural Networks']
    DF = pd.DataFrame()
    for query in Queries:
        results = API.search(q=query, lang="en", count=200, result_type="recent")
        tempDF = toDataFrame(results, query)
        DF = pd.concat([DF, tempDF], ignore_index=True)
    return(DF)
for i in range(0, 1):
    query = "autonomous cars"
    DF = toDataFrame(API.search(q=query, lang="en", count=200, result_type="recent"), query)
    DF.to_csv('autocars.csv')
