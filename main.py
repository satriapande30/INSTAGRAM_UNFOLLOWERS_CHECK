import os
import sys
from bs4 import BeautifulSoup
import argparse
import json
from datetime import datetime

class InstagramUnfollowerTracker:
    def __init__(self, followers_file='followers_1.html', following_file='following.html'):
        """
        Inisialisasi tracker dengan file followers dan following
        
        Args:
            followers_file (str): Path file HTML followers
            following_file (str): Path file HTML following
        """
        self.followers_file = followers_file
        self.following_file = following_file
        self.followers = set()
        self.following = set()
        self.not_following_back = set()
        self.history_file = 'unfollower_history.json'

    def load_data(self):
        """
        Memuat data followers dan following dari file HTML
        """
        try:
            with open(self.followers_file, 'r', encoding='utf-8') as followers_file:
                followers_soup = BeautifulSoup(followers_file, 'html.parser')
                self.followers = {elem.text.strip() for elem in followers_soup.find_all('a')}

            with open(self.following_file, 'r', encoding='utf-8') as following_file:
                following_soup = BeautifulSoup(following_file, 'html.parser')
                self.following = {elem.text.strip() for elem in following_soup.find_all('a')}
        except FileNotFoundError as e:
            print(f"Error: File tidak ditemukan - {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Error membaca file: {e}")
            sys.exit(1)

    def find_unfollowers(self):
        """
        Mencari akun yang tidak mengikuti balik
        """
        self.not_following_back = self.following - self.followers
        return self.not_following_back

    def save_history(self):
        """
        Menyimpan riwayat unfollowers ke file JSON
        """
        try:
            # Baca history sebelumnya jika ada
            if os.path.exists(self.history_file):
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    history = json.load(f)
            else:
                history = []

            # Tambahkan data unfollowers baru
            current_entry = {
                'timestamp': datetime.now().isoformat(),
                'unfollowers': list(self.not_following_back)
            }
            history.append(current_entry)

            # Simpan kembali ke file
            with open(self.history_file, 'w', encoding='utf-8') as f:
                json.dump(history, f, indent=4, ensure_ascii=False)

            print(f"Riwayat unfollowers disimpan di {self.history_file}")
        except Exception as e:
            print(f"Gagal menyimpan riwayat: {e}")

    def compare_with_history(self):
        """
        Membandingkan unfollowers dengan riwayat sebelumnya
        """
        try:
            if os.path.exists(self.history_file):
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    history = json.load(f)
                
                if history:
                    previous_unfollowers = set(history[-1]['unfollowers'])
                    new_unfollowers = self.not_following_back - previous_unfollowers
                    removed_unfollowers = previous_unfollowers - self.not_following_back

                    print("\nPerbandingan dengan riwayat sebelumnya:")
                    print(f"Unfollowers baru: {len(new_unfollowers)}")
                    print(f"Unfollowers yang sudah tidak lagi: {len(removed_unfollowers)}")

                    if new_unfollowers:
                        print("\nAkun baru yang tidak mengikuti:")
                        for user in new_unfollowers:
                            print(user)

                    if removed_unfollowers:
                        print("\nAkun yang sudah tidak lagi tidak mengikuti:")
                        for user in removed_unfollowers:
                            print(user)
        except Exception as e:
            print(f"Gagal membandingkan riwayat: {e}")

    def print_summary(self):
        """
        Mencetak ringkasan informasi
        """
        print("\n=== Ringkasan Instagram Unfollower ===")
        print(f"Total Followers: {len(self.followers)}")
        print(f"Total Following: {len(self.following)}")
        print(f"Akun yang tidak mengikuti balik: {len(self.not_following_back)}")
        print("\nDaftar Akun yang Tidak Mengikuti Balik:")
        for user in sorted(self.not_following_back):
            print(user)

    def run(self, save_history=True, compare_history=True):
        """
        Menjalankan proses tracking unfollowers
        
        Args:
            save_history (bool): Simpan riwayat unfollowers
            compare_history (bool): Bandingkan dengan riwayat sebelumnya
        """
        self.load_data()
        self.find_unfollowers()
        self.print_summary()
        
        if save_history:
            self.save_history()
        
        if compare_history:
            self.compare_with_history()

def main():
    parser = argparse.ArgumentParser(description='Instagram Unfollower Tracker')
    parser.add_argument('--followers', default='followers_1.html', 
                        help='Path file HTML followers')
    parser.add_argument('--following', default='following.html', 
                        help='Path file HTML following')
    parser.add_argument('--no-history', action='store_true', 
                        help='Nonaktifkan penyimpanan riwayat')
    
    args = parser.parse_args()
    
    tracker = InstagramUnfollowerTracker(
        followers_file=args.followers, 
        following_file=args.following
    )
    
    tracker.run(
        save_history=not args.no_history, 
        compare_history=not args.no_history
    )

if __name__ == '__main__':
    main()