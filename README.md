# Exploring-Airbnb-Market-Trend

Background
===============
Welcome to New York City, one of the most-visited cities in the world. There are many Airbnb listings in New York City to meet the high demand for temporary lodging for travelers, which can be anywhere between a few nights to many months. In this project, we will take a closer look at the New York Airbnb market by combining data from multiple file types like .csv, .tsv, and .xlsx.

Recall that CSV, TSV, and Excel files are three common formats for storing data. Three files containing data on 2019 Airbnb listings are available to you:

__data/airbnb_price.csv__ This is a CSV file containing data on Airbnb listing prices and locations.

* listing_id: unique identifier of listing
* price: nightly listing price in USD
* nbhood_full: name of borough and neighborhood where listing is located

__data/airbnb_room_type.xlsx__ This is an Excel file containing data on Airbnb listing descriptions and room types.

* listing_id: unique identifier of listing
* description: listing description
* room_type: Airbnb has three types of rooms: shared rooms, private rooms, and entire homes/apartments

__data/airbnb_last_review.tsv__ This is a TSV file containing data on Airbnb host names and review dates.

* listing_id: unique identifier of listing
* host_name: name of listing host
* last_review: date when the listing was last reviewed

Tasks
===============
As a consultant working for a real estate start-up, you have collected Airbnb listing data from various sources to investigate the short-term rental market in New York. You'll analyze this data to provide insights on private rooms to the real estate company.

There are three files in the <em>**data**</em> folder: <em>**airbnb_price.csv**</em>, <em>**airbnb_room_type.xlsx**</em>, <em>**airbnb_last_review.tsv**</em>.

What are the dates of the earliest and most recent reviews? Store these values as two separate variables with your preferred names.
How many of the listings are private rooms? Save this into any variable.
What is the average listing price? Round to the nearest two decimal places and save into a variable.
Combine the new variables into one DataFrame called <em>**review_dates**</em> with four columns in the following order: <em>**first_reviewed**</em>, <em>**last_reviewed**</em>, <em>**nb_private_rooms**</em>, and <em>**avg_price**</em>. The DataFrame should only contain one row of values.

