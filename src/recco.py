import pandas as pd
import argparse

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

parser = argparse.ArgumentParser(description = 'Recommendation system using \
                                Collaborative Filtering')

parser.add_argument('-f', '--file', dest = 'product_data', required = True,
                    type = argparse.FileType('r'),
                    help = 'File conatining prodct data')
parser.add_argument('-p', '--prod_name', required = True,
                    help = 'Name of product to get recommendations')
parser.add_argument('-n', '--number', type = int, default = 5,
                    help = 'Number of recommendations required')
args = parser.parse_args()

df = pd.read_csv(args.product_data)

# feature extraction
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(analyzer = 'word', ngram_range=(1, 2), min_df=0)
extracted_features = vectorizer.fit_transform(df['combined_features'])

#using cosine similarity
cos_sim = cosine_similarity(extracted_features, extracted_features)

df = df.reset_index()
products = df['product_names']
indices = pd.Series(df.index, index = df['product_names'])

# function to get recommendations
def get_recommendations(product):
    ind = indices[product]
    sim_scores = list(enumerate(cos_sim[ind]))
    sim_scores = sorted(sim_scores, key = lambda x:x[1], reverse=True)
    product_indices = [i[0] for i in sim_scores[1:args.number]]
    return products.iloc[product_indices]

get_recommendations(args.prod_name)
