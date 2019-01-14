import json
import pickle
import pandas as pd
from elasticsearch import Elasticsearch

def toJson(path):
    df = pd.read_csv(path)
    df['datetime'] = df['datetime'].apply(transformdate)
    return json.loads(df.to_json(orient='records'))

def indexit(it):
    es = Elasticsearch()
    for i,j in enumerate(it[:1000]):
        r = es.index(index='ufos', doc_type='ufosighting', body=j)
        print(r)
        print(i)

def pickleit(it):
    with open('scrubbed.pickle', 'wb') as f:
        pickle.dump(it, f)

def safeJson(it):
    with open('scrubbed.json', 'w') as f:
        f.write(it)

def loadpickle():
    with open('scrubbed.pickle', 'rb') as f:
        return pickle.load(f)

def transformdate(d):
    date,time = d.split()
    month,day,year = date.split('/')
    if len(month) == 1:
        month = '0' + month
    if len(day) == 1:
        day = '0' + day
    hour,minute = time.split(':')
    if int(hour) == 24:
        hour = '00'
    return f'{year}-{month}-{day}T{hour}:{minute}:01+00:00'

if __name__ == '__main__':
    print('Start indexing...')
    #collection = toJson('scrubbed.csv')
    #pickleit(collection)
    collection = loadpickle()
    indexit(collection)
    print('Done.')
