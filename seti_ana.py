import csv
from textblob import TextBlob

reviews = []
# read the file
with open('review.csv', 'r') as csv_file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file)

    # skip the first row(the title review)
    next(csv_reader, None)

    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Each row is a list of values
        reviews.append(row)

csv_filename = 'movie_reviews.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Review Text', 'Sentiment'])

    # Loop through the reviews and perform sentiment analysis
    for review in reviews:
        review_text = review[0]
        analysis = TextBlob(review_text)

        # Determine sentiment polarity (positive, negative, neutral)
        if analysis.sentiment.polarity > 0:
            sentiment = 'Positive'
        elif analysis.sentiment.polarity < 0:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'

        # Write the review text and sentiment to the CSV file
        writer.writerow([review_text, sentiment])

print(f'Reviews saved to {csv_filename}')



