import streamlit as st
import pandas as pd
import requests
import json 
if __name__ == "__main__":
    import sys
    sys.path.append('code')
    from apicalls import get_google_place_details, get_azure_sentiment, get_azure_named_entity_recognition
else:
    from code.apicalls import get_google_place_details, get_azure_sentiment, get_azure_named_entity_recognition

PLACE_IDS_SOURCE_FILE = "cache/place_ids.csv"
CACHE_REVIEWS_FILE = "cache/reviews.csv"
CACHE_SENTIMENT_FILE = "cache/reviews_sentiment_by_sentence.csv"
CACHE_ENTITIES_FILE = "cache/reviews_sentiment_by_sentence_with_entities.csv"


def reviews_step(place_ids: str|pd.DataFrame) -> pd.DataFrame:
    '''
      1. place_ids --> reviews_step --> reviews: place_id, name (of place), author_name, rating, text 
    '''
    if isinstance(place_ids, str):
        place_ids_df = pd.read_csv(place_ids)
    else:
        place_ids_df = place_ids

    #involved in the transformation
    google_places = []
    for index, row in place_ids_df.iterrows():
        place = get_google_place_details(row['Google Place ID'])
        google_places.append(place['result'])
    
    #time to construct the dataframe 
    reviews_df = pd.json_normalize(google_places, record_path="reviews", meta=["place_id", 'name'])
    #pair down to the columns we want
    reviews_df = reviews_df[['place_id', 'name',  'author_name', 'rating', 'text']]
    #important to save all of this to the cache!!!!
    reviews_df.to_csv(CACHE_REVIEWS_FILE, index=False, header=True)
    return reviews_df
    #pass # TODO: implement this function

def sentiment_step(reviews: str|pd.DataFrame) -> pd.DataFrame:
    '''
      2. reviews --> sentiment_step --> review_sentiment_by_sentence
    '''
    if isinstance(reviews, str):
        reviews_df = pd.read_csv(reviews)
    else:
        reviews_df = reviews

  #  # TRANSFORMATIONS
    # get sentiment for each review
    sentiment_data = []
    for index, row in reviews_df.iterrows():
        sentiment = get_azure_sentiment(row['text'])
        sentiment_item = sentiment['sentiment']
        sentiment_item['place_id'] = row['place_id']
        sentiment_item['name'] = row['name']
        sentiment_item['author_name'] = row['author_name']
        sentiment_item['rating'] = row['rating']
        sentiment_item['text'] = row['text']
        sentiment_data.append(sentiment_item)
    # create a dataframe from the sentiment data
    sentiment_df = pd.DataFrame(sentiment_data)
    # save to cache, return dataframe
    # this is a dataframe with the sentiment data for each review
    sentiment_df.rename(columns={'text': 'sentence_text'}, inplace=True)
    sentiment_df.rename(columns={'sentiment': 'sentence_sentiment'}, inplace=True)
    # save to cache, return dataframe
    # save the dataframe to a csv file
    sentiment_df = sentiment_df[['place_id', 'name', 'author_name', 'rating', 'sentence_text', 'sentence_sentiment', 'confidenceScores.positive', 'confidenceScores.neutral', 'confidenceScores.negative']]
    # save to cache, return dataframe
    sentiment_df.to_csv(CACHE_SENTIMENT_FILE, index=False, header=True)
    return sentiment_df
    #pass # TODO: implement this function


def entity_extraction_step(sentiment: str|pd.DataFrame) -> pd.DataFrame:
    '''
      3. review_sentiment_by_sentence --> entity_extraction_step --> review_sentiment_entities_by_sentence
    '''
    if isinstance(sentiment, str):
        sentiment_df = pd.read_csv(sentiment)
    else:
        sentiment_df = sentiment
    
#     pass # TODO: implement this function


if __name__ == '__main__':
    # helpful for debugging as you can view your dataframes and json outputs
    import streamlit as st 
    st.write("What do you want to debug?")