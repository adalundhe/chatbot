import json
from sys import argv
from time import sleep
from tqdm import tqdm

def convert_json_to_txt(**kwargs):
    loaded_sentiments = []

    try:
        with open(kwargs['to_file'],'r') as to_file:
            loaded_sentiments = [line for line in to_file]
    except:
        print("No file at:"+kwargs['to_file']+'...\nWill create.')

    new_sentiments = []

    with open(kwargs['from_file']) as from_file:
        file_in = [line for line in from_file]
        print("Processing...")
        for i in tqdm(range(len(file_in))):
            sentiment = json.loads(file_in[i])
            new_sentiments += [' '.join([sentiment['text'], sentiment['label'], '\n'])]

    with open(kwargs['to_file'], 'w') as to_file:
        total_sentiments = loaded_sentiments + new_sentiments
        print("Writing...")
        for i in tqdm(range(len(total_sentiments))):
            to_file.write(total_sentiments[i])

convert_json_to_txt(from_file=argv[1], to_file=argv[2])
