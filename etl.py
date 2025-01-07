import json
import pandas as pd
import os

def extract_flair_data(file_path, output_csv_path):
    """Ekstrak title dan flair dari JSON ke CSV."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        df = pd.DataFrame([{'flair': post.get('flair', 'N/A') } for post in data])
        df.to_csv(output_csv_path, index=False)
        print(f"✅ Data flair berhasil disimpan di {output_csv_path}")
    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")

# Path file JSON dan CSV
file_path = os.path.join(os.getcwd(), 'data', 'reddit_technology_data.json')
output_csv_path = os.path.join(os.getcwd(), 'data', 'flair_data.csv')

extract_flair_data(file_path, output_csv_path)