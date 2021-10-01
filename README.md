# Recommendation system for e-commerce using collaborative filtering

This project features a recommendation system to recommend products using item-based collaborative filtering. Required number of recommendations are obtained for a given product. Collaborative filtering is carried out on the basis of item details (item name, category, brand etc.)

# An introduction to some terms
## Recommendation System

A recommendation system is a system that uses available data to provide suggestions for a specific item or object that a user is interested in. In the case of recommendation systems for e-commerce, they are used to recommend a list of products with respect to a given product.

## Collaborative filtering

This project focuses on using item-based collaborative filtering to obtain recommendations. Item-based collaborative filtering uses the similarity between items to filter data.

## Cosine Similarity

In this project, collaborative filtering is done using cosine similarity. A cosine similarity matrix is obtained having similarity scores between each item. This in turn is used to get the top recommendations for a specific product.

# Objectives
1. To create a recommendation system to provide recommendations for a given product
2. To create a command line interface to give recommendations using command-line arguments

# Data
The data for this project was downloaded from kaggle.
[Click here](https://www.kaggle.com/PromptCloudHQ/flipkart-products) to view the dataset source.

# Repository structure

```sh
.
├── data
├── notebooks
└── src
```
# Instructions to execute the recommendation system

1. Create and activate python virtual environment
2. Install packages
3. Clone repository
4. Run notebooks in order
5. Execute CLI by running ```recco.py```

Note : *This project was created using python version 3.9.5*

## Create and activate virtual environment

```sh
python -m venv venv
source venv/bin/activate

```

## Install packages

```sh
pip install -r requirements.txt
```

## Clone repository

```sh
git clone https://github.com/amruthaa08/Recommendation-system.git
```

## Notebooks

1. flipkart_data_cleaning.ipynb

```
- removing unwanted columns from data
- removing duplicates
- adding fill values
- saving data to clean_flipkart_data
```


2. flipkart_data_preprocessing.ipynb

``` 
- data preprocessing using nltk
- tokenizing data
- removing stopwords and punctuation
- stemming data
- saving data to preprocessed_flipkart_data
```

*Executing the final step in the above mentioned notebooks will create and save two files 'clean_flipkart_data' and 'preprocessed_flipkart_data' to the ```notebook``` directory. You can choose to skip this step since these files are already available in ```data``` directory. Subsequent notebooks and scripts also use data already present in the ```data``` directory*


3. cosine_similarity model

```
- extract features from preprocessed data
- apply cosine similarity
- create function to get recommendations
```

## src

- recco.py

```
- creates command-line arguments to obtain file name, product name, and the number of recommendations required
- use command-line arguments to execute recommendation system through CLI 
```

**How to use:**

The CLI uses three arguments:
1. ```-f``` or ```--file_name``` obtains the file containing required data. The CLI uses the preprocessed_flipkart_data to provide recommendations. Hence  ```../data/preprocessed_flipkart_data``` must be passed as the ```-f``` argument when executing the CLI
2. ```-p``` or ```--prod_name``` obtains the name of the product for which we require recommendations
3. ```-n``` or ```--number``` obtains the number of recommendations required. This is an optional argument for which the default value is 5.

**Code example:**

```py
python recco.py -f ..data/preprocessed_flipkart_data -p "Ladela Bellies" -n3
```
Executing this code returns 3 product recommendations for "Ladela Bellies".

Thank you for visiting my repository.
