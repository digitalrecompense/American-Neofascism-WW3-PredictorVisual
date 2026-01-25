# American Neofascism WW3-Predictor Plot


###### I’ve created using Grok an updated visualizer prgoram that can be used in realtime for multiple purposes.


# Robust News Analyzer & Risk Visualizer (no scikit-learn)
# Works in Colab, local Jupyter, even restricted browser environments
# Run in Google Colab: paste → run cells → enter topic when prompted

import feedparser
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime
import re

# Download required NLTK data (only once)
nltk.download('vader_lexicon', quiet=True)
nltk.download('punkt', quiet=True)

class NewsRiskAnalyzer:
    def __init__(self, topic, max_articles=15):
        self.topic = topic.strip()
        self.max_articles = max_articles
        self.articles = []
        self.sentiments = []
        self.dates = []
        self.risk_scores = []           # 0–1 heuristic risk
        self.sia = SentimentIntensityAnalyzer()
        
        # Keywords that increase perceived risk (customize if you want)
        self.risk_keywords = [
            'war', 'conflict', 'escalation', 'crisis', 'attack', 'strike', 'invasion',
            'nuclear', 'missile', 'tension', 'confrontation', 'military', 'troops',
            'deployment', 'threat', 'retaliation', 'bomb', 'sanction', 'proxy'
        ]

    def clean_text(self, text):
        """Remove junk: scripts, styles, very short lines, excessive whitespace"""
        if not text:
            return ""
        # Remove HTML tags (in case any slipped through)
        text = re.sub(r'<[^>]+>', '', text)
        # Remove common boilerplate patterns
        text = re.sub(r'(read more|click here|subscribe|sign up|©|\d{4} all rights reserved)', '', text, flags=re.I)
        # Collapse whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        # Keep only reasonably long meaningful content
        if len(text) < 50:
            return ""
        return text[:8000]  # cap length to avoid memory issues

    def fetch_and_parse(self):
        url = f"https://news.google.com/rss/search?q={self.topic.replace(' ', '+')}&hl=en-US&gl=US&ceid=US:en"
        feed = feedparser.parse(url)
        
        fetched = 0
        for entry in feed.entries:
            if fetched >= self.max_articles:
                break
                
            try:
                resp = requests.get(entry.link, timeout=6, headers={'User-Agent': 'Mozilla/5.0'})
                soup = BeautifulSoup(resp.text, 'html.parser')
                
                # Try to get main article text
                paragraphs = soup.find_all('p')
                content = ' '.join(p.get_text(strip=True) for p in paragraphs if len(p.get_text(strip=True)) > 30)
                content = self.clean_text(content)
                
                if not content and entry.summary:
                    content = self.clean_text(entry.summary)
                
                if content:
                    self.articles.append({
                        'title': entry.title,
                        'link': entry.link,
                        'published': entry.get('published', ''),
                        'content': content
                    })
                    fetched += 1
                    
            except Exception as e:
                # Silent fail on single article – don't crash whole run
                continue
        
        print(f"Fetched and parsed {len(self.articles)} usable articles on '{self.topic}'.")

    def analyze(self):
        if not self.articles:
            print("No usable content found. Try a different topic or later.")
            return
        
        for art in self.articles:
            # Sentiment
            score = self.sia.polarity_scores(art['content'])['compound']
            self.sentiments.append(score)
            
            # Parse date
            try:
                dt = datetime.strptime(art['published'], '%a, %d %b %Y %H:%M:%S %Z')
            except:
                dt = datetime.now()
            self.dates.append(dt)
            
            # Heuristic risk contribution
            text_lower = art['content'].lower()
            keyword_hits = sum(1 for kw in self.risk_keywords if kw in text_lower)
            neg_strength = max(0, -score)  # 0 to 1
            risk = (neg_strength * 0.6) + (min(1.0, keyword_hits / 5) * 0.4)
            self.risk_scores.append(min(1.0, risk))

    def visualize(self):
        if not self.sentiments:
            print("Nothing to plot.")
            return
        
        df = pd.DataFrame({
            'Date': self.dates,
            'Sentiment': self.sentiments,
            'Risk': self.risk_scores
        }).sort_values('Date')
        
        avg_sent = df['Sentiment'].mean()
        avg_risk = df['Risk'].mean()
        
        fig, ax1 = plt.subplots(figsize=(12, 7))
        
        # Sentiment line
        ax1.plot(df['Date'], df['Sentiment'], 'b-o', linewidth=2, label='Sentiment (VADER)')
        ax1.axhline(0, color='gray', linestyle='--', alpha=0.7)
        ax1.set_xlabel('Publication Date')
        ax1.set_ylabel('Sentiment Score\n(-1 = very negative, +1 = very positive)', color='b')
        ax1.tick_params(axis='y', labelcolor='b')
        
        # Risk bars on twin axis
        ax2 = ax1.twinx()
        ax2.bar(df['Date'], df['Risk'], alpha=0.35, color='orangered', label='Heuristic Risk')
        ax2.set_ylabel('Estimated Risk Score (0–1)', color='darkred')
        ax2.tick_params(axis='y', labelcolor='darkred')
        
        # Risk zones
        ax2.axhspan(0.0, 0.35, facecolor='green', alpha=0.08)
        ax2.axhspan(0.35, 0.65, facecolor='orange', alpha=0.12)
        ax2.axhspan(0.65, 1.0, facecolor='red', alpha=0.15)
        
        plt.title(f"News Sentiment & Risk Analysis:  \"{self.topic}\"\n"
                  f"Avg Sentiment: {avg_sent:.2f}    |    Avg Heuristic Risk: {avg_risk:.0%}", 
                  fontsize=14, pad=20)
        
        fig.legend(loc='upper center', ncol=2, bbox_to_anchor=(0.5, -0.02))
        plt.xticks(rotation=30, ha='right')
        plt.tight_layout()
        plt.show()

def main():
    print("Enter topic to analyze (e.g. 'world war 3 potential', 'iran us tensions', 'trump iran armada')")
    topic = input("> ").strip()
    if not topic:
        topic = "world war 3 potential"
    
    analyzer = NewsRiskAnalyzer(topic)
    analyzer.fetch_and_parse()
    analyzer.analyze()
    analyzer.visualize()

if __name__ == "__main__":
    main()
