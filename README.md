# Twitter Scrapping Project

Objective: 

The primary goal of this project is to gain hands-on experience in data scraping from social media platforms, and Twitter is one of the most widely used social media platforms that allow users to share their thoughts, opinions, news, and information with their followers in real-time via short messages called tweets.

Our project involves scraping tweets and their attributes based on certain user-defined parameters such as keywords, start date, end date, and the maximum number of tweets to display. We then process the scraped data and store it in a MongoDB database server. Additionally, we provide users with the option to download the scraped data in either CSV or JSON formats for their future reference and analysis.

By using this project, we can gain valuable insights into various aspects of the Twitter platform, such as user behavior, trending topics, and sentiment analysis. It also allows us to analyze the data using various statistical and machine learning tools to draw meaningful conclusions and insights.


# Instructions:

To use this tool, you can download the "00_Twitting_Scraping_WorkingCode.py" file from GitHub and save it in a folder on your computer. 

Open the command prompt and navigate to the folder where the file is stored using DOS commands. 
To run the tool, type "streamlit run 00_Twitting_Scraping_WorkingCode.py" in the command prompt and press enter. For example, if your file is stored in "D:\Projects\02_Twitter_Scraping", type "streamlit run 00_Twitting_Scraping_WorkingCode.py" in the prompt and press enter. 

Once the page is opened in the browser, you can enter the keyword or phrase you want to search for in the "Enter a keyword / word to search for:" field. For this project, we will be searching for "elon musk".

You can also select a start date from the "Enter a start date:" field and an end date from the "Enter an end date:" field. 

After entering all the required inputs, click on the "Search" button to retrieve the search results. 

Once the search operation is completed, the results will be displayed in a dataframe format with Twitter attributes as column headers.

You can also upload the search results along with the search parameters to a MongoDB server by clicking on the "Upload data to MongoDB" button. 

If you want to retrieve the data in a CSV file, click on the "Download data as CSV" button. If you want to retrieve the data in a JSON format, click on the "Download data as JSON" button.

This tool can be helpful for anyone looking to scrape and analyze Twitter data for research, business or personal purposes. It allows users to easily search for tweets based on keywords and dates, and provides options to download the data in different formats for further analysis.
