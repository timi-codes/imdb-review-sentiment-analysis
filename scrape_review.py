
import requests
from bs4 import BeautifulSoup
import csv
# from textblob import TextBlob
# import pandas as pd
url = (
    # "https://www.imdb.com/title/tt6320628/reviews/_ajax?ref_=undefined&paginationKey={}"
    "https://www.imdb.com/title/tt0111161/reviews/_ajax?ref_=undefined&paginationKey={}"
)
key = ''
# key = "g4w6ddbmqyzdo6ic4oxwjnrxrtt44bz62imdx6hfa7d7wvl5pjt6udkyoq4vjmzjb4dwuy2nk2lx4spnrpx3zjdrvspaw"
data = {"title": [], "review": []}

# Create a CSV file to save the reviews
csv_filename = 'movie_reviews.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    while True:
        response = requests.get(url.format(key))
        soup = BeautifulSoup(response.content, "html.parser")
        # Find the pagination key
        pagination_key = soup.find("div", class_="load-more-data")
        if not pagination_key:
            break

        # Update the `key` variable in-order to scrape more reviews
        key = pagination_key["data-key"]
        for title, review in zip(
            soup.find_all(class_="title"), soup.find_all(
                class_="text show-more__control")
        ):
            # data["title"].append(title.get_text(strip=True))
            data["review"].append(review.get_text())
            writer.writerow([review.get_text()])
print(f'Reviews saved to {csv_filename}')
