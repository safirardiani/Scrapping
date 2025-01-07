import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time
import os

# Fungsi untuk memeriksa apakah file telah berubah
def file_has_changed(file_path, last_modified_time):
    """Periksa apakah file telah berubah berdasarkan waktu modifikasi terakhir."""
    current_modified_time = os.path.getmtime(file_path)
    return current_modified_time > last_modified_time

# Fungsi untuk menampilkan postingan dengan upvote paling banyak
def display_top_upvoted(data):
    """Menampilkan postingan dengan jumlah upvote paling banyak."""
    top_post = data.loc[data['upvotes'].idxmax()]  # Mengambil baris dengan upvotes tertinggi
    print("\n=== Postingan dengan Upvote Tertinggi ===")
    print(f"Title: {top_post['title']}")
    print(f"Author: {top_post.get('author', 'N/A')}")
    print(f"Upvotes: {top_post['upvotes']}")
    print(f"Comments: {top_post['comments']}")

# Fungsi untuk membuat visualisasi berdasarkan data CSV
def create_visualization(file_path):
    # Membaca data dari file CSV
    data = pd.read_csv(file_path)

    # Menampilkan postingan dengan upvote paling banyak
    display_top_upvoted(data)

    # 1. Visualisasi Jumlah Upvotes vs Title (Top 10 Posts)
    plt.figure(figsize=(12, 8))  # Memperbesar ukuran figur
    top_10_posts = data.nlargest(10, 'upvotes')  # Mengambil 10 posts dengan upvotes terbanyak
    sns.barplot(x='upvotes', y='title', data=top_10_posts, palette='viridis')
    plt.title('Top 10 Posts Based on Upvotes', fontsize=14)
    plt.xlabel('Upvotes', fontsize=12)
    plt.ylabel('Post Title', fontsize=12)
    plt.subplots_adjust(left=0.3)  # Memberi ruang tambahan agar label tidak terpotong
    plt.tight_layout()
    plt.show()

    # 2. Visualisasi distribusi Upvotes
    plt.figure(figsize=(10, 6))
    sns.histplot(data['upvotes'], kde=True, color='blue')
    plt.title('Distribusi Upvotes')
    plt.xlabel('Upvotes')
    plt.ylabel('Frekuensi')
    plt.tight_layout()
    plt.show()

    # 3. Visualisasi distribusi Comments
    plt.figure(figsize=(10, 6))
    sns.histplot(data['comments'], kde=True, color='green')
    plt.title('Distribusi Comments')
    plt.xlabel('Jumlah Komentar')
    plt.ylabel('Frekuensi')
    plt.tight_layout()
    plt.show()

    # 4. Visualisasi hubungan antara Upvotes dan Comments
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='upvotes', y='comments', data=data, color='orange')
    plt.title('Hubungan Antara Upvotes dan Comments')
    plt.xlabel('Upvotes')
    plt.ylabel('Comments')
    plt.tight_layout()
    plt.show()

# Main program untuk pembaruan visualisasi secara otomatis
if __name__ == "__main__":
    file_path = 'data.csv'  # Lokasi file CSV yang akan divisualisasikan
    last_modified_time = 0  # Waktu modifikasi file yang terakhir
    
    # Waktu mulai program berjalan
    start_time = time.time()
    run_duration = 60  # Durasi maksimum menjalankan loop (dalam detik)

    while True:
        # Cek waktu berjalan
        elapsed_time = time.time() - start_time
        if elapsed_time > run_duration:
            print("Program berhenti setelah berjalan selama 1 menit.")
            break  # Hentikan loop jika sudah mencapai 1 menit

        # Cek apakah file CSV diperbarui
        if file_has_changed(file_path, last_modified_time):
            print(f"File {file_path} telah diperbarui, memperbarui visualisasi..")
            create_visualization(file_path)
            last_modified_time = os.path.getmtime(file_path)
        else:
            print(f"Tidak ada perubahan pada {file_path}. Menunggu untuk pembaruan berikutnya...")

        # Tunggu 10 detik sebelum memeriksa file lagi
        time.sleep(10)
