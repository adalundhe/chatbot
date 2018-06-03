import json
from sys import argv

def convert(**kwargs):
    loaded_sentiments = []

    with open(kwargs['to_file'],'r') as to_file:
        loaded_sentiments = json.load(to_file)

    new_sentiments = []

    with open(kwargs['from_file']) as from_file:
        for line in from_file:
            score = kwargs['score_default']
            line = line.replace('\n', '')
            sentiment_dict = {'word': line, 'score': score}
            new_sentiments.append(sentiment_dict)

    with open(kwargs['to_file'],"w") as to_file:
        json.dump(loaded_sentiments + new_sentiments, to_file)


convert(from_file=argv[1], to_file=argv[2], score_default=argv[3])
