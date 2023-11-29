import string
from nltk.corpus import stopwords
from nltk import wordpunct_tokenize
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('stopwords')
nltk.download('wordnet')

import pandas as pd

# Replace 'file_name.csv' with the path to your CSV file
file_name = 'movie_reviews.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_name)


def clean_review(review_text, *arg):
    allword =list()
    #separate words from sentence
    for sentence in review_text:
        punct_token = wordpunct_tokenize(sentence)
        #remove stopwords
        stops = set(stopwords.words("english"))
        stops.update({'br','i','the'})
        punct_token = [word for word in punct_token if word not in
        stops]
        #remove string.punctuation
        punct_token = [word for word in punct_token if word not in
        string.punctuation]
        #remove word that is not alphabat or number
        punct_token = [word for word in punct_token if
        word.isalnum()==True]
        #lower words
        punct_token = [word.lower() for word in punct_token ]
        allword.append(punct_token)
    return allword
clean_tokens = clean_review(df['Review Text'])

word_dict_count = dict()
for line in clean_tokens:
    for word in line:
        if word not in word_dict_count:
            word_dict_count[word] = 1
        else:
            word_dict_count[word] += 1
pd.DataFrame([word_dict_count]).T.sort_values(by=0, ascending=False).head(10)

tokens = [y for x in clean_tokens for y in x]
freq = nltk.FreqDist(tokens)
# plot the frequency of words
freq.plot(20,cumulative=False)


import matplotlib.pyplot as plt
from wordcloud import WordCloud
cloud = WordCloud(background_color = "white",max_words = 2000)

with open('token_words.txt', "w") as f1:
    for line in clean_tokens:
        test=','.join(line)
        f1.write(test)
text = open('token_words.txt').read()

cloud.generate(text)
plt.imshow(cloud)
plt.axis('off')
plt.figure(figsize=(7, 3)  , dpi=200)
plt.show()
