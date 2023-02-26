import sqlite3
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# Connect to the SQLite database
conn = sqlite3.connect('crawler.db')

# Load the data from the database
df = pd.read_sql_query("SELECT * FROM pages", conn)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['content'], df['relevance_score'], test_size=0.2, random_state=42)

# Create a tokenizer to convert text to sequences
tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(X_train)

# Convert text to sequences and pad them to the same length
X_train = pad_sequences(tokenizer.texts_to_sequences(X_train), maxlen=1000)
X_test = pad_sequences(tokenizer.texts_to_sequences(X_test), maxlen=1000)

# Create a neural network model with one hidden layer
model = tf.keras.models.Sequential([
  tf.keras.layers.Embedding(5000, 64, input_length=1000),
  tf.keras.layers.Dropout(0.5),
  tf.keras.layers.Conv1D(64, 5, activation='relu'),
  tf.keras.layers.GlobalMaxPooling1D(),
  tf.keras.layers.Dense(10, activation='relu'),
  tf.keras.layers.Dense(1, activation='linear')
])

# Compile the model and specify the loss function and optimizer
model.compile(loss='mse', optimizer='adam')

# Train the model on the training set
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

# Evaluate the performance of the model on the testing set
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print('Mean squared error:', mse)

# Rank new websites based on their content
new_website_content = ["This is a new website with some content."]
new_website = pad_sequences(tokenizer.texts_to_sequences(new_website_content), maxlen=1000)
relevance_score = model.predict(new_website)
print('Relevance score:', relevance_score[0][0])
