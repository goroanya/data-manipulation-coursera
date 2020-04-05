import sys, json

TERMS = {}


def get_tweets(filename):
    tweets = []
    with open(filename, 'r') as f:
        for line in f:
            tweets.append(json.loads(line))
    return tweets


def add_terms_from_tweet(tweet):
    if 'text' not in tweet:
        return

    terms = tweet['text'].split(' ')
    for new_term in terms:
        new_term = new_term.replace('\n', '')
        TERMS[new_term] = TERMS.get(new_term, 0) + 1


def calc_term_frequency(term):
    return TERMS.get(term, 0) / float(len(TERMS.keys()))


def main():
    tweets = get_tweets(sys.argv[1])
    for tweet in tweets:
        add_terms_from_tweet(tweet)

    all_terms = TERMS.keys()
    for term in all_terms:
        print term.encode('utf-8'), calc_term_frequency(term)


if __name__ == '__main__':
    main()
