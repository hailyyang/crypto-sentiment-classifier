# Crypto Sentiment Classifier

NLP project analyzing cryptocurrency sentiment from social media and news.

## Project Goal
Build a sentiment analysis model to classify crypto-related text and explore correlations with price movements.


## Project Structure
```
crypto-sentiment-project/
├── data/
│   ├── raw/              # Raw collected data
│   └── processed/        # Cleaned data with sentiment labels
├── notebooks/
│   └── 01_data_collection.ipynb
│   └── 02_model_training.ipynb
├── results/              # Visualizations and outputs
├── models/               # Saved trained model
├── reddit_matrix_scrape.py  # Script for scraping Reddit posts
└── requirements.txt
```

## Tech Stack
- Python 3.9+
- pandas, numpy, matplotlib
- snscrape (Twitter scraping)
- VADER Sentiment Analysis
- Jupyter Notebooks

## Weekly Progress overview 
- Week 1: Bitcoin price data and Reddit posts scrape. Applied VADER sentiment analysis baseline
- Week 2: Fine-tune transformer model (FinBERT) and compare its results with the VADER baseline
- Week 3: Correlate sentiment with price movements
- Week 4: Build interactive dashboard

## Setup
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

*Part of a 6-project NLP portfolio for blockchain/crypto analysis*