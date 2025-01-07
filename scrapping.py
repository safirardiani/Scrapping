import requests
import json
import os
import time

# URL dan headers
url = 'https://www.reddit.com/r/Technology/new/.json'
headers = {'User-Agent': 'Mozilla/5.0'}

def fetch_and_save_data():
    try:
        # Mengirim permintaan GET ke API Reddit
        response = requests.get(url, headers=headers)
        
        # Memeriksa status kode dari respons
        if response.status_code == 200:
            # Mengurai data JSON dari respons
            raw_data = response.json()

            # Transformasi data untuk menambahkan 'selftext' (isi) ke dalam data
            transformed_data = []
            posts = raw_data['data']['children']  # Mengakses daftar postingan

            for post in posts:
                post_data = post['data']
                transformed_data.append({
                    'title': post_data.get('title', 'N/A'),
                    'author': post_data.get('author', 'N/A'),
                    'upvotes': post_data.get('ups', 0),
                    'comments': post_data.get('num_comments', 0),
                    'url': post_data.get('url', 'N/A')
                })

            # Menentukan lokasi penyimpanan file JSON
            file_name = 'raw_data.json'
            file_path = os.path.join(os.getcwd(), file_name)  # Menyimpan di folder kerja
            
            # Menyimpan transformed data ke file JSON
            with open(file_path, 'w') as file:
                json.dump(transformed_data, file, indent=4)
            
            print(f"Raw data berhasil disimpan ke '{file_path}'")
        else:
            print(f"Gagal mengambil data. Status code: {response.status_code}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Loop untuk mengambil dan menyimpan data setiap 10 detik selama 1 menit
start_time = time.time()  # Waktu mulai
duration = 60  # Durasi total dalam detik

while True:
    fetch_and_save_data()
    time.sleep(10)  # Tunggu 10 detik sebelum iterasi berikutnya

    # Periksa apakah waktu berjalan melebihi durasi
    elapsed_time = time.time() - start_time
    if elapsed_time >= duration:
        print("Loop selesai setelah 1 menit.")
        break
