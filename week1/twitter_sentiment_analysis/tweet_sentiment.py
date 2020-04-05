import json, sys

NEW_WORDS = {}


def get_sentiment_scores(filename):
    afinnfile = open(filename)
    scores = {}  # initialize an empty dictionary
    for line in afinnfile:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    return scores


def calc_tweet_sentiment(tweet, sentiment_scores):
    if 'text' not in tweet:
        return

    tweet_score = 0
    words = tweet['text'].split(' ')
    for word in words:
        tweet_score += sentiment_scores.get(word, 0)

    for new_word in filter(lambda w: w not in sentiment_scores, words):
        if new_word not in NEW_WORDS:
            NEW_WORDS[new_word] = []
        NEW_WORDS[new_word].append(tweet_score)

    return tweet_score


def get_tweets(filename):
    tweets = []
    with open(filename, 'r') as f:
        for line in f:
            tweets.append(json.loads(line))
    return tweets


def get_tweet_text(tweet):
    if 'text' not in tweet:
        return
    else:
        return tweet['text']


def main():
    sentiment_scores = get_sentiment_scores(sys.argv[1])
    tweets = get_tweets(sys.argv[2])
    for tweet in tweets:
        score = calc_tweet_sentiment(tweet, sentiment_scores)
        # print score #task2

    for new_word in NEW_WORDS:
        if new_word:
            scores = NEW_WORDS[new_word]
            new_score = sum(scores) / len(scores)
            print new_word.encode('utf-8'), new_score  # task3


if __name__ == '__main__':
    main()
