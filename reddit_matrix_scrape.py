import requests
import pandas as pd
import time
import random

# --- CONFIGURATION ---
SUBREDDIT = "Bitcoin" 
POST_LIMIT = 1000             
DELAY_MIN = 2                # Minimum seconds to wait between pages (Ant-Ban)
DELAY_MAX = 5                # Maximum seconds to wait

# Mimic a real browser so Reddit doesn't block you
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def scrape_reddit_looped(subreddit, target_posts=100):
    all_posts = []
    after_token = None # This is our "Next Page" bookmark
    
    print(f"🚀 Starting scrape of r/{subreddit} for {target_posts} posts...")

    while len(all_posts) < target_posts:
        # Construct URL with pagination
        url = f"https://www.reddit.com/r/{subreddit}/new.json?limit=100"
        if after_token:
            url += f"&after={after_token}"
            
        try:
            response = requests.get(url, headers=HEADERS)
            
            if response.status_code != 200:
                print(f"❌ Error {response.status_code}. Stopping early.")
                break
                
            data = response.json()
            posts_batch = data['data']['children']
            
            # If no more posts, stop
            if not posts_batch:
                print("⚠️ No more posts found.")
                break
                
            # Extract data
            for child in posts_batch:
                post = child['data']
                all_posts.append({
                    'id': post.get('id'),
                    'title': post.get('title'),
                    'body': post.get('selftext'),
                    'subreddit': subreddit,
                    'score': post.get('score'),
                    'upvote_ratio': post.get('upvote_ratio'),
                    'url': post.get('url'),
                    'created_utc': post.get('created_utc')
                })
            
            # Update our "Next Page" token
            after_token = data['data']['after']
            print(f"✅ Collected {len(all_posts)} posts so far...")
            
            if not after_token:
                print("⚠️ Reached end of subreddit.")
                break
                
            # Random sleep to look human (Crucial!)
            time.sleep(random.uniform(DELAY_MIN, DELAY_MAX))
            
        except Exception as e:
            print(f"❌ Crash: {e}")
            break
            
    # Trim to limit and save
    df = pd.DataFrame(all_posts[:target_posts])
    return df

if __name__ == "__main__":
    # Run the scraper
    df = scrape_reddit_looped(SUBREDDIT, target_posts=POST_LIMIT)
    
    # Save to CSV
    filename = f"{SUBREDDIT}_data_{len(df)}.csv"
    df.to_csv(filename, index=False)
    print(f"\n🎉 Success! Saved {len(df)} rows to {filename}")