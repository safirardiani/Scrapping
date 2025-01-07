import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_flair_data(csv_path):
    """Visualisasi distribusi flair dari CSV."""
    try:
        df = pd.read_csv(csv_path)
        flair_counts = df['flair'].value_counts()
        
        plt.figure(figsize=(10, 6))
        sns.barplot(x=flair_counts.index, y=flair_counts.values, palette='viridis')
        plt.title('Distribusi Flair pada Postingan Reddit')
        plt.xlabel('Flair')
        plt.ylabel('Jumlah Postingan')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"❌ Kesalahan: {e}")

csv_path = os.path.join(os.getcwd(), 'data', 'flair_data.csv')
visualize_flair_data(csv_path)
