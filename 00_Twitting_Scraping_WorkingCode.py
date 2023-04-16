import streamlit as st
import snscrape.modules.twitter as twitterScraper
import pandas as pd
#import datetime
import pymongo
import base64
import json



client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["twitter_db"]
collection = db ["twitter_data"]

def search_tweets(query, start_date, end_date, max_tweets):

    newtweets = []
    search_query = (f"{query} since:{start_date} until:{end_date} -filter:safe")
    for tweet in twitterScraper.TwitterSearchScraper(search_query).get_items():
        if len(newtweets) >= max_tweets:
            break
        newtweets.append(tweet)

    df = pd.DataFrame({
        'id': [tweet.id for tweet in newtweets],
        'date': [tweet.date.strftime('%Y-%m-%d %H:%M:%S') for tweet in newtweets],
        'url': [tweet.url for tweet in newtweets],
        'tweet content': [tweet.content for tweet in newtweets],
        'username': [tweet.user.username for tweet in newtweets],
        'reply count':[tweet.replyCount for tweet in newtweets],
        'language': [tweet.lang for tweet in newtweets],
        'source': [tweet.source for tweet in newtweets],
        'likes': [tweet.likeCount for tweet in newtweets]})

    return df


def app():
    st.title("Twitter Data Scrapping")

    st.header("Capstone Project Work by Anbazhagan SR")

    query = st.text_input("Enter a keyword / word to search for:")
    start_date = st.date_input("Enter a start date:")
    end_date = st.date_input("Enter an end date:")
    max_tweets = st.number_input("Enter the maximum number of tweets to display:", min_value=1, value=100)

    search = st.button("Search")
    upload_data = st.button("Upload data to MongoDB")
    download_csv = st.button("Download data as CSV")
    download_json = st.button("Download data as JSON")

    df = search_tweets(query, start_date, end_date, max_tweets)
    if search:
        st.write(df)

    if upload_data and 'df' in locals():
        scraped_data = {
            "Scraped Word": query,
            "scraped Start Date": str(start_date),
            "Scraped End Date": str(end_date),
            "Scraped Data": df.to_dict('records')}
        collection.insert_one(scraped_data)
        st.write("Data uploaded to MongoDB!")

    if download_csv and 'df' in locals():
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        st.markdown(f'<a href="data:file/csv;base64,{b64}" download="twitter_data.csv">Download CSV File</a>', unsafe_allow_html = True)

    if download_json and 'df' in locals():
        json_data = df.to_json(orient='records')
        b64 = base64.b64encode(json_data.encode()).decode()
        st.markdown(f'<a href="data:file/json;base64,{b64}" download="twitter_data.json">Download JSON File</a>', unsafe_allow_html = True)

def main():
    app()

if __name__ == "__main__":
    main()