# Import necessary packages
import pandas as pd
import numpy as np

# Begin coding here ...

df_review = pd.read_csv('data/airbnb_last_review.tsv', sep='\t')
#convert format to datetime
df_review['last_review'] = pd.to_datetime(df_review['last_review']).dt.date
#first review
first_review = df_review['last_review'].min()
#last review
last_review = df_review['last_review'].max()

#private room listing
df_room = pd.read_excel('data/airbnb_room_type.xlsx')
#Value consistency
df_room['room_type'] = df_room['room_type'].str.lower()

private_room = df_room[df_room['room_type'] == 'private room']
private_room_num = private_room['room_type'].count()

#average room listing pirce
df_price = pd.read_csv('data/airbnb_price.csv')
#remove unused string and change type to float
df_price = df_price['price'].str.strip('dollars')
df_price = df_price.astype('float')
avg = df_price.mean()
avg = round(avg, 2)


#Result tibble - reviews_dates
data = {
    'first_reviewed':[first_review],
    'last_reviewed':[last_review],
    'nb_private_rooms':[private_room_num],
    'avg_price':[avg],
}
review_dates = pd.DataFrame(data, index=[0])
print(review_dates)
