import pytest
import pandas as pd
from src.model.sentiment import extract_sentiment

# Load sentiment data from the CSV file
df = pd.read_csv('soccer_sentiment_analysis.csv')
testdata = df['Text'].tolist()

@pytest.mark.parametrize('sample', testdata)
def test_extract_sentiment(sample):
    sentiment = extract_sentiment(sample)
    # Modify assertion based on sentiment expected in your dataset.
    assert -1 <= sentiment <= 1
def test_positive_sentiment():
    positive_text = "Barcelona played brilliantly last Wednesday. Rafinia’s hat-trick was pure magic. Visca Barça!"
    sentiment = extract_sentiment(positive_text)
    assert sentiment > 0
