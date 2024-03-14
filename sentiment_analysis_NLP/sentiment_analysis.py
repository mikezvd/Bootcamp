import numpy as np
import pandas as pd
import spacy

from textblob import TextBlob
from spacytextblob.spacytextblob import SpacyTextBlob


# first we need to get the data from the csv file given

reviews_data = pd.read_csv("amazon_product_reviews.csv")

# then we select the columns that are specific for the task given 
# in this case I decided to leave the id, reviews, title of reviews, and the username who wrote it

cleaned_data = reviews_data[['reviews.text']]

# we still need to drop all null values from our data which don't give any value for sentiment

cleaned_data.dropna(inplace=True, axis=0)

# after I select all reviews from the 'reviews.text' column to iterate through

reviews = cleaned_data['reviews.text']

# now it's time to do our sentiment function

# we load the english dictionary

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe('spacytextblob')

# function to prepare the text cleaning it from stop words and punctuation

def preprocess(text) :
    doc = nlp(text.lower().strip())
    processed = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    
    return ' '.join(processed)

cleaned_data['processed.text'] = cleaned_data['reviews.text'].apply(preprocess)

# For the sentiment analysis I built a function that not only returns the sentiment
# but it also returns entities, PoS tags, and dependency parsing of the given text
# in case in the future I want to build a more in depth analysis of the text 
# (i.e. checking which brands are mentioned more based on good or bad reviews).
# For that we just need to un-comment lines 44, 47, 50, and 52 by deleting the '#'
# for now it will return the sentiment only

def analyze_sentiment(text):
    doc = nlp(text)
    
    # Sentiment analysis (using polarity)

    polarity_score = doc._.blob.polarity  
    #sentiment_score = doc._.blob.subjectivity # in case we need later on
    
    # Named Entity Recognition (NER)
    #entities = [(ent.text, ent.label_) for ent in doc.ents]

    # Part-of-Speech (PoS) tagging
    #pos_tags = [(token.text, token.pos_) for token in doc]

    # Dependency parsing
    #dependencies = [(token.text, token.dep_, token.head.text) for token in doc]

    return polarity_score #, sentiment_score, entities, pos_tags, dependencies


# now we can apply this to our reviews
data = cleaned_data['processed.text'].values

sentiments = []      # this will save all sentiments 

for item in data:
    score = analyze_sentiment(item)
    sentiment = "Positive" if score > 0 else "Negative" if score < 0 else "Neutral"
    sentiments.append(sentiment)

# counting positive, negative and neutral sentiments
positive_count = sentiments.count('Positive')
negative_count = sentiments.count('Negative')
neutral_count = sentiments.count('Neutral')

total = len(sentiments)

# calculate the percentage of each one
positive_perc = (positive_count / total) * 100
negative_perc = (negative_count / total) * 100
neutral_perc = (neutral_count / total) * 100

print(f"Positive percentage: {positive_perc:.2f}%")
print(f"Negative percentage: {negative_perc:.2f}%")
print(f"Neutral percentage: {neutral_perc:.2f}%")


