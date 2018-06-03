import json
from sys import argv
from time import sleep
from tqdm import tqdm

def convert_text_to_json(**kwargs):
    loaded_sentiments = []
    try:
        with open(kwargs['to_file'],'r') as to_file:
            loaded_sentiments = json.load(to_file)
    except:
        print("No file at: "+kwargs['to_file']+'...\nWill create.')

    new_sentiments = []
    score_default = float(kwargs['score_default'])
    print("You have selected a score threshold of:", score_default)

    with open(kwargs['from_file']) as from_file:
        if '.txt' in kwargs['from_file']:
            file_in = [line for line in from_file]
            for i in tqdm(range(len(file_in))):
                score = '__label__pos' if parsed_sentiment['stars'] > score_default else '__label__neg'
                line = file_in[i]
                line = line.replace('\n', '')
                sentiment_dict = {'word': line, 'score': score}
                new_sentiments.append(sentiment_dict)
        elif '.json' in kwargs['from_file']:
            file_in = [line for line in from_file]
            print("Processing...")
            for i in tqdm(range(len(file_in))):
                new_sentiment = {}
                parsed_sentiment = json.loads(file_in[i])
                new_sentiment['stars'] = parsed_sentiment['stars']
                new_sentiment['label'] = '__label__pos' if parsed_sentiment['stars'] > score_default else '__label__neg'
                new_sentiment['text'] = parsed_sentiment['text'].replace('\n', ' ')
                new_sentiments += [new_sentiment]


    with open(kwargs['to_file'],"w") as to_file:
        sentiments = loaded_sentiments + new_sentiments
        print("Writing...")
        for i in tqdm(range(len(sentiments))):
             converted_data = json.dumps(sentiments[i])
             to_file.write(converted_data + '\n')


convert_text_to_json(from_file=argv[1], to_file=argv[2], score_default=argv[3])
