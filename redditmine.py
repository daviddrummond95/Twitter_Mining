import tweepy
import time
auth ="z2Cv26gIIMPDm72w2Njce4Jjt"
authsecret ="Jb1KBCDrCP5M6g70N3NnCNHfOBMJCjvBzxu9hlYPhsuNfuhx3H"
token = "1165713578156015617-BBFnNhRpGaSmfkqal013Z5GrfX736U"
tokensecret= "HzVjNKPKoZQLnDa03syDOPbLoxYkJaSpUSkXSHcHCorEp"
auth = tweepy.OAuthHandler(auth, authsecret)
auth.set_access_token(token, tokensecret)

API = tweepy.API(auth)
query = "Cybertruck"
file = open('data.txt', 'a')
influencer1 = open('29873662.txt', 'a')
influencer2 = open('44196397.txt', 'a')
influencer3 = open('239672340.txt', 'a')
influencer4 = open('1720701343.txt', 'a')
influencer5 = open('3239203002.txt', 'a')
influencer6 = open('568418252.txt', 'a')
influencer7 = open('2151196938.txt', 'a')
influencer8 = open('148911566.txt', 'a')
influencer9 = open('15676492.txt', 'a')
influencer10 = open('295325513.txt', 'a')
influencer11 = open('824802244092522497.txt', 'a')
tweetdump = open('tweet.txt', 'a')
datacount1 = 0; datacount2 = 0; datacount3 = 0; datacount4 = 0; datacount5 = 0; datacount6 = 0; datacount7 = 0
datacount8 = 0; datacount9 = 0; datacount10 = 0; datacount11 = 0
influencers = [29873662, 44196397, 239672340, 1720701343, 3239203002, 568418252, 2151196938, 148911566, 15676492, 295325513, 824802244092522497]
network = open('network.txt', 'a')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
opentemp = open('data.txt', 'r')
lines = opentemp.readlines()
lines = [item.replace('\n', '')for item in lines]
lines = [text.split(",") for text in lines]
tweeters = [[j[0], float(j[1])] for j in lines]
tweeters.append([44196397, 1.0])
tweeters.append([29873662, 0.5])
tweeters.append([239672340, 1.0])
tweeters.append([1720701343, 1.0])
tweeters.append([3239203002, 1.0])
tweeters.append([568418252, 0])
tweeters.append([2151196938, -1.0])
tweeters.append([148911566, -1.0])
tweeters.append([15676492, -1.0])
tweeters.append([295325513, -1.0])
tweeters.append([824802244092522497, 1.0])
waittime = 150
def sentiment_value(paragraph):
    analyser = SentimentIntensityAnalyzer()
    result = analyser.polarity_scores(paragraph)
    score = result['compound']
    return round(score, 1)
for i in range(0, 20):
    print(i)
    results = API.search(q=query, lang="en", count=200, result_type="recent")
    data = []
    k = 0
    for tweet in results:
        file = open('data.txt', 'a')
        influencer1 = open('29873662.txt', 'a')
        influencer2 = open('44196397.txt', 'a')
        influencer3 = open('239672340.txt', 'a')
        influencer4 = open('1720701343.txt', 'a')
        influencer5 = open('3239203002.txt', 'a')
        influencer6 = open('568418252.txt', 'a')
        influencer7 = open('2151196938.txt', 'a')
        influencer8 = open('148911566.txt', 'a')
        influencer9 = open('15676492.txt', 'a')
        influencer10 = open('295325513.txt', 'a')
        influencer11 = open('824802244092522497.txt', 'a')
        tweetdump = open('tweet.txt', 'a')
        network = open('network.txt', 'a')
        k += 1
        print(k)
        friends = []
        needbreak = 15*60
        starttime = time.time()
        try:
            friends = API.friends_ids(id=tweet.user.id)
        except Exception:
            print("Waittime:", waittime)
            time.sleep(waittime)
            try:
                friends = API.friends_ids(id=tweet.user.id)
            except Exception:
                pass
        score = sentiment_value(tweet.text)
        for k in friends:
            for l in tweeters:
                if str(k) == str(l[0]):
                    network.write('['+str(tweet.user.id) + ',' + str(score) + ']'+ ',' + '[' + str(l[0]) + ',' + str(l[1]) + ']' + '\n')
        network.close()
        if influencers[0] in friends:
            influencer1.write(str(tweet.user.id) + ',' + str(score)+'\n')
            datacount1 += 1
            influencer1.close()
            print('influencer1 datacount:', datacount1)
        if influencers[1] in friends:
            influencer2.write(str(tweet.user.id) + ',' + str(score)+'\n')
            datacount2 += 1
            influencer2.close()
            print('influencer2 datacount:', datacount2)
        if influencers[2] in friends:
            influencer3.write(str(tweet.user.id) + ',' + str(score)+'\n')
            datacount3 += 1
            influencer3.close()
            print('influencer3 datacount:', datacount3)
        if influencers[3] in friends:
            influencer4.write(str(tweet.user.id) + ',' + str(score)+'\n')
            datacount4 += 1
            print('influencer4 datacount:', datacount4)
            influencer4.close()
        if influencers[4] in friends:
            influencer5.write(str(tweet.user.id) + ',' + str(score)+'\n')
            datacount5 += 1
            print('influencer5 datacount:', datacount5)
            influencer5.close()
        if influencers[5] in friends:
            influencer6.write(str(tweet.user.id) + ',' + str(score)+'\n')
            datacount6 += 1
            print('influencer6 datacount:', datacount6)
            influencer6.close()
        if influencers[6] in friends:
            influencer7.write(str(tweet.user.id) + ',' + str(score)+'\n')
            datacount7 += 1
            print('influencer7 datacount:', datacount7)
            influencer7.close()
        if influencers[7] in friends:
            influencer8.write(str(tweet.user.id) + ',' + str(score)+'\n')
            datacount8 += 1
            print('influencer8 datacount:', datacount8)
            influencer8.close()
        if influencers[8] in friends:
            influencer9.write(str(tweet.user.id) + ',' + str(score)+'\n')
            datacount9 += 1
            print('influencer9 datacount:', datacount9)
            influencer9.close()
        if influencers[9] in friends:
            influencer10.write(str(tweet.user.id) + ',' + str(score)+'\n')
            datacount10 += 1
            print('influencer10 datacount:', datacount10)
            influencer10.close()
        if influencers[10] in friends:
            influencer11.write(str(tweet.user.id) + ',' + str(score)+'\n')
            datacount11 += 1
            print('influencer11 datacount:', datacount11)
            influencer11.close()
        file.write(str(tweet.user.id)+','+str(score)+'\n')
        tweeters.append([tweet.user.id, score])
        try:
            tweetdump.write(str(tweet.user.id)+'|'+str(tweet.text)+'\n')
        except Exception:
            tweetdump.write(str(tweet.user.id) + '|' + 'error' + '\n')
        file.close()
        tweetdump.close()
        endtime = time.time()
        waittime = needbreak-(endtime - starttime)
