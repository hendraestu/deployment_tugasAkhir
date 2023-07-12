from flask import request, jsonify, flash
from flask.templating import render_template
from app import app
import os
import snscrape.modules.twitter as sntwitter
import emoji
import pandas as pd
import config
import pickle
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# from nltk.stem import PorterStemmer
from app.models.dataTokohModel import db, Tokoh
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

class TokohSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nama', 'positif', 'negatif', 'netral', 'akurasi', 'image', 'update_at')

tokoh_schema = TokohSchema()
tokohs_schema = TokohSchema(many=True)


DATASET_PATH = config.DATASET_PATH
MODEL_PATH = config.MODELS_PATH
DATA_PATH = config.DATA_PATH

def update():
    id= request.form['id']
    nama = request.form['nama']
    # positif = request.form['positif']
    # negatif = request.form['negatif']
    # netral = request.form['netral']

    positif = 100
    negatif = 50
    netral = 80

    tokoh = Tokoh.query.get(id)
    tokoh.positif = positif
    tokoh.negatif = negatif
    tokoh.netral = netral
    db.session.commit()
    tokohUpdate = tokoh_schema.dump(tokoh)
    # konten = Tokoh.query.all()
    # tokos= tokohs_schema.dump(konten)
    
    return render_template('updateData.html', data = tokohUpdate)

# def update():

#     nama = request.form['nama']
#     since = request.form['awal_tanggal']
#     until = request.form['akhir_tanggal']

#     query = "({}) lang:id since:{} until:{}".format(nama, since, until)
#     tweets = []
#     limit = 100

#     for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
#         if len(tweets) == limit:
#             break
#         else:
#             content = tweet.content
#             # remove emoji
#             clean_tweet = remove_emoji(content)
#             # remove line break
#             clean_tweet = clean_tweet.replace("\n", " ")
#             # remove hashtag
#             clean_tweet = re.sub(r"#(\w+)", "", clean_tweet)
#             # remove annoying data
#             clean_tweet = re.sub(r"(?:\@|https?\://)\S+", "", clean_tweet)
#             # remove whitespace
#             clean_tweet = " ".join(clean_tweet.split())
#             # just use the tweet and date
#             tweets.append(clean_tweet)

#     df = pd.DataFrame(tweets, columns=['text'])
#     # cleaning the remaining dirty tweets
#     tweets_clean = df['text'].apply(lambda x: x.replace("\n", ""))

#     # remove duplicate tweets
#     tweet_fix = tweets_clean.drop_duplicates(keep='first')

#     df = pd.DataFrame(tweet_fix, columns=['text'])

#     data = loopingClean(df)
#     # cek data kosong
#     data = data.dropna()
#     data = data.reset_index(drop=True)

#     model_path = os.path.join(MODEL_PATH, f'{nama}.pkl')
#     model_vec = os.path.join(MODEL_PATH, f'{nama}-vector.pkl')

#     model = open(model_path, 'rb')
#     svm = pickle.load(model)
    
#     vec = open(model_vec, 'rb')
#     vectorizer = pickle.load(vec)

#     vector = vectorizer.transform(data['text'])
#     data['label'] = svm.predict(vector)
    
#     # y_pred = svm.predict(vector)

#     # x_train, x_test, y_train, y_test = train_test_split(data.text, data.sentiment,test_size=0.23, random_state=42)

#     # akurasi = metrics.accuracy_score(y_test, y_pred)

#     # to save to csv
#     data_path = os.path.join(DATA_PATH, f'{nama}.csv')
#     data.to_csv(data_path, index=False)

#     jumlah = data['label'].values.tolist()

#     positif = []
#     negatif = []
#     netral = []

#     for x in jumlah:
#         if x == 3:
#             positif.append(x)
#         if x == 1:
#             negatif.append(x)
#         if x == 2:
#             netral.append(x)
        
#     positif = len(positif)
#     negatif = len(negatif)
#     netral = len(netral)

#     tokoh = Tokoh.query.get(id)
#     tokoh.positif = positif
#     tokoh.negatif = negatif
#     tokoh.netral = netral
#     tokoh.update_at = until
#     db.session.commit()
#     tokohUpdate = tokoh_schema.dump(tokoh)
#     print (since)
#     print(until)
#     print(nama)
#     # return render_template('updateData.html')
#     return jsonify({"msg": "Success update tokoh", "status": 200, "data": tokohUpdate})
    
#     # return jsonify(positif, negatif, netral)

# def remove_emoji(text):
#     clean_text = emoji.demojize(text)
#     clean_text = re.sub(r':[^:\s]+:', '', clean_text)
#     return clean_text

# def cleansing(text):
#     text = re.sub('RT\s', '', text)
#     text = re.sub('\B@\w+', '', text)
#     text = re.sub('(http|https):\/\/\S+', '', text)
#     text = re.sub('http|https', '', text)
#     text = re.sub('#+', '', text)
#     text = text.lower()
#     text = re.sub(r'(.)\1+', r'\1\1', text)
#     text = re.sub(r'[\?\.\!]+(?=[\?.\!])', '', text)
#     text = re.sub(r'[^a-zA-Z]', ' ', str(text))
#     text = re.sub(r'b ', ' ', text)
#     text = text.translate(str.maketrans("", "", string.punctuation))

#     tokens = word_tokenize(text)
#     stop_words = set(stopwords.words('indonesian'))
#     filtered_tokens = [word for word in tokens if word not in stop_words]

#     tokens = word_tokenize(text)
#     # stemmer = PorterStemmer()
#     stop_words = set(stopwords.words('indonesian'))
#     filtered_tokens = [word for word in tokens if word not in stop_words]
#     # stemm = [stemmer.stem(word) for word in filtered_tokens]

#     text = " ".join(filtered_tokens)

#     print(text)
#     return text

# def loopingClean(df):

#     for i, r in df.iterrows():
#         y = cleansing(r['text'])
#         df.loc[i, 'text'] = y

#     return df

def getAllTokoh():
    konten = Tokoh.query.all()
    tokos= tokohs_schema.dump(konten)
    return render_template('updateData.html', data = tokos)