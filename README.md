# Tugas Besar Datamining Prediksi Rasio Hujan Menggunakan Metode Regresi dan Algoritma SGD

## Deskripsi singkat

Repository ini berisi semua file yang dibutuhkan untuk melakukan deployment model Machine Learning Regresi dengan algoritma SGD. Adapun model yang digunakan merupakan model untuk memprediksi rasio hujan berdasarkan:

-   `Humidity` atau kelembaban 
-   `Longitude` atau 'Sumbu X' nya bumi
-   `Latitude` atau 'Sumbu Y' nya bumi

#


## Folder, file, dan kegunaannya

-   templates/
    -   index.html --> Berisi template website
-   app.py --> Berisi konfigurasi route untuk API
-   model.pkl --> Model Regresi yang sudah di-training
-   request.py --> Berisi percobaan pemanggilan API dengan payload data JSON
-   requirements.txt --> Berisi daftar dependency/package Python yang diperlukan untuk menjalankan API dan model Regresi

#

## Cara menjalankan API pada komputer Anda

### Menjalankan API
Note: Pastikan anda memiliki python terinstall di komputer anda

1. Buka vs code
2. Buka terminal pada vscode
3. jalankan perintah flask run

### Akses melalui Website

Setelah API berjalan:

1. Anda akan diberikan URL untuk membuka website berupa `localhost:5000/` atau `127.0.0.1:5000/`
2. Buka URL dengan browser, coba masukkan data yang ingin di prediksi
3. Anda akan diberikan estimasi rasio hujan hari ini
