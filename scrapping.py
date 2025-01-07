import requests
import json
import os
import time
from datetime import datetime

BASE_URL = 'https://www.reddit.com/r/Technology/new/.json'
HEADERS = {'User-Agent': 'Mozilla/5.0'}
LIMIT = 100

def append_to_json_file(file_path, post_entry):
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump([], file, indent=4)
    with open(file_path, 'r+', encoding='utf-8') as file:
        data = json.load(file)
        data.append(post_entry)
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()

def fetch_and_save_data(max_posts=1000):
    after, saved_posts = None, 0
    file_path = os.path.join(os.getcwd(), 'data', 'reddit_technology_data.json')
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    while saved_posts < max_posts:
        response = requests.get(BASE_URL, headers=HEADERS, params={'limit': LIMIT, 'after': after})
        if response.status_code != 200:
            print(f"Gagal mengambil data: {response.status_code}")
            break
        
        posts = response.json().get('data', {}).get('children', [])
        if not posts:
            break
        
        for post in posts:
            if saved_posts >= max_posts:
                break
            post_data = post['data']
            append_to_json_file(file_path, {
                'title': post_data.get('title', 'N/A'),
                'flair': post_data.get('link_flair_text', 'N/A'),
                'upvotes': post_data.get('ups', 0),
                'comments': post_data.get('num_comments', 0),
                'url': post_data.get('url', 'N/A'),
                'timestamp': datetime.utcfromtimestamp(post_data.get('created_utc', 0)).strftime('%Y-%m-%d %H:%M:%S')
            })
            saved_posts += 1
            print(f"[{saved_posts}] Postingan tersimpan")
        
        after = response.json().get('data', {}).get('after')
        if not after:
            break
        time.sleep(2)
    
    print(f"✅ Total postingan yang berhasil disimpan: {saved_posts}")

fetch_and_save_data(max_posts=1000)
