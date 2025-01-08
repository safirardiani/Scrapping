<<<<<<< HEAD
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
=======
import requests
import json
import csv
import os
import time

# 1. Proses Extract
def extract(file_path):
    """Baca file JSON dan ekstrak data."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)  # Memuat data JSON ke struktur Python
        print("Data berhasil diekstrak dari raw_data.json")
        return data
    except FileNotFoundError:
        print("File raw_data.json tidak ditemukan!")
        return None
    except json.JSONDecodeError as e:
        print(f"Kesalahan dalam membaca JSON: {e}")
        return None

# 2. Proses Transform
def transform(data):
    """Transformasi data menjadi bentuk tabular."""
    try:
        transformed_data = []
        for post in data:  # Iterasi langsung di daftar post
            transformed_data.append({
                'title': post.get('title', 'N/A'),
                'author': post.get('author', 'N/A'),
                'upvotes': post.get('upvotes', 0),
                'comments': post.get('comments', 0),
            })
        
        print(f"Data yang telah ditransformasi: {len(transformed_data)}")  # Debug jumlah data yang diproses
        return transformed_data
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return []

# 3. Proses Load
def load(transformed_data, output_file):
    """Menyimpan data hasil transformasi ke file CSV."""
    try:
        if not transformed_data:
            print("Tidak ada data untuk disimpan!")
            return
        
        with open(output_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['title', 'author', 'upvotes', 'comments'])
            writer.writeheader()  # Menulis header kolom
            writer.writerows(transformed_data)  # Menulis baris data
        print(f"Data berhasil disimpan ke {output_file}")
    except Exception as e:
        print(f"Kesalahan saat menyimpan file: {e}")

# 4. Proses Fetch Data
def fetch_and_save_data():
    """Mengambil dan menyimpan data dari Reddit."""
    url = 'https://www.reddit.com/r/Technology/new/.json'
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            raw_data = response.json()
            posts = raw_data['data']['children']  # Mengakses daftar postingan
            
            transformed_data = []
            for post in posts:
                post_data = post['data']
                transformed_data.append({
                    'title': post_data.get('title', 'N/A'),
                    'author': post_data.get('author', 'N/A'),
                    'upvotes': post_data.get('ups', 0),
                    'comments': post_data.get('num_comments', 0),
                })
            
            # Menyimpan data yang diambil ke raw_data.json
            file_name = 'all_reddit_data.json'
            with open(file_name, 'w', encoding='utf-8') as file:
                json.dump(transformed_data, file, indent=4)
            
            print(f"Data berhasil disimpan ke {file_name}")
        else:
            print(f"Gagal mengambil data. Status code: {response.status_code}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# 5. Fungsi untuk menemukan postingan dengan upvote terbanyak
def find_top_upvoted(data):
    """Menemukan postingan dengan jumlah upvote terbanyak."""
    if not data:
        print("Data kosong, tidak dapat mencari upvote tertinggi.")
        return None
    
    top_post = max(data, key=lambda x: x.get('upvotes', 0))  # Mencari postingan dengan upvote tertinggi
    print("\n=== Postingan dengan Upvote Tertinggi ===")
    print(f"Title: {top_post.get('title', 'N/A')}")
    print(f"Author: {top_post.get('author', 'N/A')}")
    print(f"Upvotes: {top_post.get('upvotes', 0)}")
    print(f"Comments: {top_post.get('comments', 0)}")
    return top_post

# Main Program untuk Real-Time ETL Process
if __name__ == "__main__":
    # Mengambil data setiap 10 detik dan menjalankan proses ETL
    while True:
        # Langkah 1: Ambil data terbaru dari Reddit
        fetch_and_save_data()
        
        # Langkah 2: Proses ETL
        input_file = 'raw_data.json'
        output_file = 'data.csv'

        if not os.path.exists(input_file):
            print(f"File '{input_file}' tidak ditemukan di direktori saat ini.")
        else:
            raw_data = extract(input_file)
            if raw_data:
                transformed_data = transform(raw_data)
                if transformed_data:
                    find_top_upvoted(transformed_data)  # Menampilkan upvote tertinggi
                    load(transformed_data, output_file)
            else:
                print("Tidak ada data yang berhasil diekstrak.")
        
        time.sleep(10)
>>>>>>> 98bdf276efe88739ddc527c8b4e272c2329613d9
