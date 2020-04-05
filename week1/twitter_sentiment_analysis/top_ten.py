import sys, json

HASHTAGS = {}


def get_tweets(filename):
    tweets = []
    with open(filename, 'r') as f:
        for line in f:
            tweets.append(json.loads(line))
    return tweets


def add_tweet_hashtags(tweet):
    if 'entities' not in tweet or 'hashtags' not in tweet['entities']:
        return
    else:
        tags = [e['text'] for e in tweet['entities']['hashtags']]
        for tag in tags:
            HASHTAGS[tag] = HASHTAGS.get(tag, 0) + 1


def top_ten_hashtags():
    hashtags = [(k, v) for k, v in HASHTAGS.items()]
    sorted_hashtags = sorted(hashtags, key=lambda x: x[1], reverse=True)
    return sorted_hashtags[:10]


def main():
    tweets = get_tweets(sys.argv[1])
    for tweet in tweets:
        add_tweet_hashtags(tweet)

    sorted(HASHTAGS.items(), key=lambda x: x[1], reverse=True)

    for tag, frequency in top_ten_hashtags():
        print tag.encode('utf-8'), frequency



if __name__ == '__main__':
    main()
