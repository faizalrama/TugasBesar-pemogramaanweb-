# README - Aplikasi Online Shop

## Informasi Admin
- *Username:* wanilam04study@gmail.com
- *Password:* 12345

## Deskripsi
Aplikasi ini adalah menyedidakan barang barang yang bisa di beli secara online dan membayar COD


## Instalasi dan Konfigurasi
1. *Persyaratan Sistem:*
   - Python
   - Flask
   - MySQL
   - Paket Python: flask-mysqldb, docx, smtplib

2. *Langkah-langkah Instalasi:*
   - Clone repository ini atau unduh zip dan ekstrak.
   - Instal dependensi Python:
     bash
     pip install flask flask-mysqldb python-docx
     
   - Konfigurasikan database MySQL:
     - Buat database baru dengan nama toko_online.
     - Konfigurasikan koneksi MySQL di app.py:
       python
       app.config['MYSQL_HOST'] = 'localhost'
       app.config['MYSQL_USER'] = 'root'
       app.config['MYSQL_PASSWORD'] = 'your_password'
       app.config['MYSQL_DB'] = 'toko_online'
       

3. *Mengimpor Database melalui phpMyAdmin:*
   - Masuk ke phpMyAdmin menggunakan browser Anda.
   - Pilih database sekolah atau buat database baru dengan nama tersebut.
   - Klik pada tab *Import*.
   - Klik *Choose File* dan pilih file SQL yang akan diimpor (misalnya, sekolah.sql).
   - Pastikan format file adalah SQL dan klik *Go*.
   - Tunggu hingga proses impor selesai. Data dan struktur tabel akan ditambahkan ke database.

4. *Menjalankan Aplikasi:*
   - Jalankan aplikasi dengan perintah berikut:
     bash
     python app.py
     

## Struktur Proyek
- *app.py:* File utama aplikasi yang mengatur routing dan logika aplikasi.
- *templates/:* Folder berisi file HTML untuk tampilan antarmuka pengguna.
- *static/:* Folder untuk file statis seperti CSS, JavaScript, dan gambar.
