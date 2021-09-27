import pandas as pd
import argparse
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import PorterStemmer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

parser = argparse.ArgumentParser(description = 'Getting recommendations using \
                                cosine similarity method')

parser.add_argument('-f', '--file', dest = 'product_data', required = True,
                    type = argparse.FileType('r'),
                    help = 'File conatining prodct data')
parser.add_argument('-p', '--prod_name', required = True,
                    help = 'Name of product to get recommendations')
parser.add_argument('-n', '--number', type = int, default = 5,
                    help = 'number of recommendations required')
args = parser.parse_args()

df = pd.read_csv(args.product_data)
pre_df = pd.read_csv('clean_flipkart_data')

# feature extraction
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(analyzer = 'word', ngram_range=(1, 2), min_df=0)
extracted_features = vectorizer.fit_transform(df['combined_features'])

#using cosine similarity
cos_sim = cosine_similarity(extracted_features, extracted_features)

# function to get recommendations
df = df.reset_index()
products = pre_df['product_name']
indices = pd.Series(df.index, index = pre.df['product_name'])

# function to get recommendations
def get_reccomendations(product):
    ind = indices[product]
    sim_scores = list(enumerate(cos_sim[ind]))
    sim_scores = sort(sim_scores, key = lambda x:x[1], reverse = True)
    product_indices = [i[0] for i in sim_scores[0:args.number]]
    return products.iloc[product_indices]

get_reccomendations(args.prod_name)
