# 📉 Instagram Unfollower Tracker

Cari tahu siapa saja yang tidak follow back akun Instagram kamu secara mudah dan offline!  
Instagram Unfollower Tracker memungkinkan kamu menganalisis dan melacak siapa saja yang tidak mengikuti balik akunmu, sekaligus menyimpan riwayatnya.

---

## ✨ Fitur

- **Deteksi Unfollowers:** Temukan siapa saja yang tidak follow back.
- **Simpan Riwayat:** Catatan sejarah unfollower otomatis tersimpan ke file JSON.
- **Perbandingan Riwayat:** Lihat unfollower baru dan siapa saja yang kembali follow kamu.
- **Output Informatif:** Statistik followers, following, dan ringkasan akun yang tidak follow back.
- **Command-Line Friendly:** Jalankan dan atur opsi dengan mudah lewat terminal.

---

## 📦 Instalasi

1. **Clone repository ini:**
    ```bash
    git clone https://github.com/username/instagram-unfollower-tracker.git
    cd instagram-unfollower-tracker
    ```

2. **Install dependencies:**
    ```bash
    pip install beautifulsoup4
    ```

---

## ⚡ Cara Pakai

1. **Export data followers dan following dari Instagram:**
    - Download data lewat [Instagram Data Download](https://www.instagram.com/download/request/).
    - Ekstrak file ZIP, lalu ambil file `followers_1.html` dan `following.html` dari folder `followers_and_following`.

2. **Jalankan script:**
    ```bash
    python unfollower_tracker.py
    ```

    Opsi kustomisasi:
    - Ganti nama file:
      ```bash
      python unfollower_tracker.py --followers namafollower.html --following namafollowing.html
      ```
    - Untuk **tanpa menyimpan riwayat**:
      ```bash
      python unfollower_tracker.py --no-history
      ```

---
