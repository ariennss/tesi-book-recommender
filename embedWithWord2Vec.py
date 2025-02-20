import pandas as pd
import numpy as np
import csv
import gensim.downloader as api
from gensim.models import KeyedVectors
import string

model_path = "C:\\Downloads\\GoogleNews-vectors-negative300.bin"
model = KeyedVectors.load_word2vec_format(model_path, binary=True)
print("model loaded / created")
df = pd.read_csv("C:\\Users\\arianna.franchetto\\source\\repos\\WebApplication1\\books.csv")

with open("C:\\dataset tesi\\stopwordsKaggle.txt", 'r') as f:
    stopwords = f.read().splitlines()

with open('C:\\Users\\arianna.franchetto\\source\\repos\\WebApplication1\\w2vdescriptions.csv', 'w', newline='',
          encoding='utf-8') as csvfile:
    fieldnames = ['id', 'vector']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    print("nuovo csv aperto")

    for _, row in df.iterrows():
        book_id = row['book_id']
        description = str(row['description']).lower()

        # Remove punctuation
        description = description.translate(str.maketrans('', '', string.punctuation))

        # Tokenize the description: split the description into words
        words = [word for word in description.split() if word not in stopwords]
        print(words)

        # Create an empty list for words in the description
        words_in_a_description = []

        # Check if words in the description have a match in the model
        # If found, add the corresponding word vector to the list
        for word in words:
            if word in model.key_to_index:  # Use key_to_index for word existence check
                words_in_a_description.append(model[word])

        # If the array of word vectors is not empty, calculate the average embedding
        if words_in_a_description:
            embedding = np.mean(words_in_a_description, axis=0)
            print(embedding)
        else:
            # If no words are found in the vocabulary, use a zero vector
            embedding = np.zeros(model.vector_size)

        # Write the book ID and its vector to the CSV file
        writer.writerow({'id': book_id, 'vector': embedding.tolist()})
