import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

nltk.download('stopwords')

nltk.download('punkt_tab')

stop_words = set(stopwords.words('english'))

def remove_punctuation(text):
  return text.translate(str.maketrans('', '', string.punctuation))
  
def remove_numbers(text):
  new = ''
  for i in text:
    if not i.isdigit():
      new += i
  return new

def remove_url(text: str) -> str:
    # Remove http, https, www URLs
    return re.sub(r'http\S+|www\S+|https\S+', '', text)
	
	
def remove_emojies(text):
    new = ""
    for i in text:
        if i.isascii():  # <-- method call
            new += i
    return new
	
def remove_stopword(text):
  words = word_tokenize(text)
  cleaned_text = []

  for i in words:
    if i not in stop_words:
      cleaned_text.append(i)

  return ' '.join(cleaned_text)



def custom_preprocessor(text):
  text = text.lower()
  text = remove_punctuation(text)
  text = remove_numbers(text)
  text = remove_url(text)
  text = remove_emojies(text)
  text = remove_stopword(text)

  return text
