import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar : 
    selected = option_menu ('Hitung Luas Bangun',
    ['Hitung Luas persegi panjang',
    'Hitung Luas Segitiga',
    'Kalkulator Sederhana',
    'formulir pendaftaran',
    'uji coba cuaca'],
    default_index=0)

  

if (selected == 'Hitung Luas persegi panjang') :
    st.title('Hitung Luas persegi panjang')

    panjang = st.number_input ('Masukkan Nilai Panjang', 0)
    lebar = st.number_input ('masukkan Nilai Lebar', 0)
    hitung = st.button ("Hitung Luas")


    if hitung :
        luas = panjang * lebar
        st.write ('Luas persegi panjang adalah = ', luas)
        st.success (f'hasil persegi panjang adalah = {luas} ', )



if (selected == 'Hitung Luas Segitiga') :
    st.title('Hitung Luas Segitiga')

    alas = st.slider ('Masukkan Nilai Alas', 0, 100)
    tinggi = st.slider ('Masukkan Nilai tinggi', 0,100)
    hitung = st.button ('Hitung Luas')

    if hitung :
        luas = 0.5 * alas * tinggi
        st.write ('Luas Segitiga Adalah = ', luas)
        st.success (f'Luas Segitiga adalah = {luas} ', )



if (selected == 'Kalkulator Sederhana') : 
    st.title("Kalkulator Sederhana")

    nomor1 = st.number_input("Masukkan angka pertama :")
    nomor2 = st.number_input("Masukkan angka kedua :")
    operation = st.selectbox("Pilih operasi:", ("Tambah", "Kurang", "Kali", "Bagi"))

    if operation == "Tambah":
        result = nomor1 + nomor2
    elif operation == "Kurang":
        result = nomor1 - nomor2
    elif operation == "Kali":
        result = nomor1 * nomor2
    elif operation == "Bagi":
        if nomor2 != 0:
         result = nomor1 / nomor2
    else:
         result = "Tidak dapat membagi dengan nol"

    st.write ('hasil nya adalah = ', result)





if (selected == 'formulir pendaftaran') :
    st.title("Formulir Pendaftaran")


    name = st.text_input("Nama:")
    age = st.number_input("Usia:", min_value=1, max_value=100)
    gender = st.selectbox("Jenis Kelamin:", ("Laki-laki", "Perempuan", "transjender", "tomboy", "bencong"))


    if st.button("Daftar"):
        if age < 18:
            st.write("Anda harus berusia 18 tahun atau lebih untuk mendaftar.")
        else:
            st.write(f"Terima kasih {name}, pendaftaran Anda berhasil!")





if (selected == 'uji coba cuaca') :
    st.title("Uji Coba Cuaca")

    weather = st.selectbox("Pilih cuaca:", ("Cerah", "Hujan", "Badai"))

    if weather == "Cerah":
        st.write("Cuaca cerah! Cocok untuk beraktivitas di luar.")
    elif weather == "Hujan":
        st.write("Bawa payung jika Anda keluar dan jangan bawa perasaan.")
    elif weather == "Badai":
        st.write("Tetap di dalam rumah agar aman, jangan lupa ngopi!")