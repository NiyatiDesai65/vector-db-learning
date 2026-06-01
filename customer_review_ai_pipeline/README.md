
# Customer Review AI Pipeline

An automated AI pipeline that analyses customer reviews using Claude AI
and generates business insights from raw review data.

## Problem it solves
Companies receive thousands of customer reviews daily.
Reading them manually is impossible.
This pipeline automatically analyses every review and tells you:
- Is the customer happy or unhappy?
- What are they complaining about?
- What needs to be fixed urgently?

## What it does
- Reads customer reviews from a CSV file
- Sends each review to Claude AI for analysis
- Extracts sentiment, category and summary for each review
- Saves results to a new CSV file
- Generates a business report with key insights

## Tech used
- Python
- Anthropic Claude API
- CSV processing
- JSON parsing

## How to run
pip install anthropic python-dotenv

Create a .env file:
ANTHROPIC_API_KEY=your-key-here

Run:
python ai_pipeline.py

## Sample output
Total reviews processed: 10

Sentiment breakdown:
  positive: 5 (50%)
  negative: 3 (30%)
  neutral: 2 (20%)

Negative reviews to action:
  - Sarah Jones (Headphones): Product broke after 2 days
  - James Wilson (Charger): Stopped working after one week
  - Robert Taylor (Mouse): Wrong item delivered

## Real world use case
Any company selling products online can use this pipeline
to automatically monitor customer satisfaction at scale.