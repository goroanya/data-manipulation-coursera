import sys
import json

STATES = dict(AK='Alaska', AL='Alabama', AR='Arkansas', AS='American Samoa', AZ='Arizona', CA='California',
              CO='Colorado', CT='Connecticut', DC='District of Columbia', DE='Delaware', FL='Florida', GA='Georgia',
              GU='Guam', HI='Hawaii', IA='Iowa', ID='Idaho', IL='Illinois', IN='Indiana', KS='Kansas', KY='Kentucky',
              LA='Louisiana', MA='Massachusetts', MD='Maryland', ME='Maine', MI='Michigan', MN='Minnesota',
              MO='Missouri', MP='Northern Mariana Islands', MS='Mississippi', MT='Montana', NA='National',
              NC='North Carolina', ND='North Dakota', NE='Nebraska', NH='New Hampshire', NJ='New Jersey',
              NM='New Mexico', NV='Nevada', NY='New York', OH='Ohio', OK='Oklahoma', OR='Oregon', PA='Pennsylvania',
              PR='Puerto Rico', RI='Rhode Island', SC='South Carolina', SD='South Dakota', TN='Tennessee', TX='Texas',
              UT='Utah', VA='Virginia', VI='Virgin Islands', VT='Vermont', WA='Washington', WI='Wisconsin',
              WV='West Virginia', WY='Wyoming')

STATES_SCORES = {}


def load_sentiment_scores(filename):
    scores = {}
    with open(filename, 'r') as f:
        for line in f:
            term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
            scores[term] = int(score)  # Convert the score to an integer.
    return scores


def word_sentiment_score(word, sentiment_scores):
    return sentiment_scores.get(word, 0)


def load_tweets(filename):
    tweets = []
    with open(filename, 'r') as f:
        for line in f:
            tweets.append(json.loads(line))
    return tweets


def get_location_from_text(text):
    states = STATES.values()
    for state in states:
        if state.lower() in text.lower():
            return state


def calc_tweet_sentiment(tweet, sentiment_scores):
    if 'text' not in tweet:
        return
    state = get_location_from_text(tweet['text'])
    if not state:
        return

    score = 0
    words = tweet['text'].split(' ')
    for word in words:
        score += word_sentiment_score(word, sentiment_scores)

    if state not in STATES_SCORES:
        STATES_SCORES[state] = []
    STATES_SCORES[state].append(score)


def calculate_mean_state_score():
    max_mean_score = 0
    happiest_state = STATES.keys()[0]
    for state in STATES_SCORES:
        state_scores = STATES_SCORES[state]
        mean_score = sum(state_scores) / float(len(state_scores))
        if mean_score > max_mean_score:
            max_mean_score = mean_score
            happiest_state = state
    return happiest_state


def reverse_state_to_abbr(state):
    for abbr, state_name in STATES.items():
        if state == state_name:
            return abbr


def main():
    sentiment_scores = load_sentiment_scores(sys.argv[1])
    tweets = load_tweets(sys.argv[2])
    for tweet in tweets:
        calc_tweet_sentiment(tweet, sentiment_scores)
    happiest_state = calculate_mean_state_score()
    state_abbr = reverse_state_to_abbr(happiest_state)
    if state_abbr:
        print state_abbr
    else:
        print STATES.keys()[0]


if __name__ == '__main__':
    main()
