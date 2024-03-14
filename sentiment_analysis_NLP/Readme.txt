I created this project while doing my bootcamp.

This sentiment analysis program in Python uses NumPy, Pandas, Spacy, and TextBlob/SpacyTextBlob to process the reviews from a big dataset from amazon (downloaded from Kaggle https://www.kaggle.com/datasets/datafiniti/consumer-reviews-of-amazon-products ) and I renamed it 'amazon_product_reviews.csv'.

The output of this program is a percentage for Positive, Negative, and Neutral reviews from a given dataset.

For dependencies,

- install Spacy:

pip install -U pip setuptools wheel
pip install -U spacy 

- install english language (small) for spacy:

python -m spacy download en_core_web_sm

- install textblob:

pip install spacytextblob
python -m textblob.download_corpora

