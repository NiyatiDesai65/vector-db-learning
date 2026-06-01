import chromadb
import anthropic
import json
import csv
import os
import time
from dotenv import load_dotenv


load_dotenv()

def read_reviews(filepath):
    reviews = []
    with open(filepath,'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            reviews.append(row)
    print(f"Read {len(reviews)} from {filepath}")
    return reviews

def safe_parse_json(reply):
    reply = reply.strip()
    #print("Before parse:", repr(reply[:50])) 
    if reply.startswith("```"):
        reply = reply.split("```")[1]
        if reply.startswith("json"):
            reply = reply[4:]
        reply = reply.strip()
    #print("After clean:", repr(reply[:50]))  
    return json.loads(reply)

def analyze_reviews(review_text):
    anthropic_client = anthropic.Anthropic()
    
    response = anthropic_client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=500,
        messages=[{"role":"user",
                  "content":f""" Analyze this customer review and respond only in JSON object.
                  no extra text. Just the JSON.
                  Review : {review_text}
                  
                  Respond with exactly this format :
                  {{
                        "sentiment": "positive or negative or neutral",
                        "category": "product quality or shipping or customer service or value for money",
                        "summary": "one sentence summary of the review"

                  }}
                  """
                    }  ]
    )
    print("Claude response:", response.content[0].text)
    result = safe_parse_json(response.content[0].text)
    return result

def process_reviews(reviews):
    results = []
    
    for review in reviews:
        print(f"Analyzing Review {review['id']} - {review['customer_name']}....")
        
        try:
            analysis = analyze_reviews(review['review'])
            result = {
                'id': review['id'],
                'customer_name': review['customer_name'],
                'product': review['product'],
                'review': review['review'],
                'sentiment': analysis['sentiment'],
                'category': analysis['category'],
                'summary': analysis['summary']
            }
            results.append(result)
            time.sleep(0.5)
            
        except Exception as e:
            print(f"Error Processing Review - {review['id']} : {e}")
            continue
    return results

def save_results(results,filepath):
    fieldnames = ['id', 'customer_name', 'product', 'review', 
                  'sentiment', 'category', 'summary']
    
    with open(filepath,'w',newline='') as f:
        writer = csv.DictWriter(f,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
        
    print(f"\nResults saved to {filepath}")
    
def generate_report(results):
    print("\n" + "="*50)
    print("         PIPELINE REPORT")
    print("="*50)
    
    total = len(results)
    
    # count sentiments
    sentiments = {}
    for r in results:
        s = r['sentiment']
        sentiments[s] = sentiments.get(s, 0) + 1
    
    #count categories
    categories = {}
    for r in results:
        c = r['category']
        categories[c]= categories.get(s,0)+1
        
    print(f"\nTotal reviews processed: {total}")
     
    print("\nSentiment breakdown:")
    for sentiment, count in sentiments.items():
        percentage = round((count / total) * 100)
        print(f"  {sentiment}: {count} ({percentage}%)")
    
    print("\nCategory breakdown:")
    for category, count in categories.items():
        print(f"  {category}: {count}")
    
    print("\nNegative reviews to action:")
    for r in results:
        if r['sentiment'] == 'negative':
            print(f"  - {r['customer_name']} ({r['product']}): {r['summary']}")
    
    print("\n" + "="*50)
      
    

def main():
    print("="*50)
    print("   Customer Review AI Pipeline")
    print("="*50 + "\n")
    
    #read
    reviews = read_reviews("reviews.csv")
    
    #process
    print("\nStarting AI analysis...\n")
    results = process_reviews(reviews)
    
    # save
    save_results(results, 'results.csv')
    
     # report
    generate_report(results)

if __name__ == "__main__":
    main()
    
        
        


