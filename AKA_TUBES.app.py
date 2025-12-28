import streamlit as st
import time
import matplotlib.pyplot as plt
import pandas as pd

# =========================
# ALGORITMA ITERATIF
# =========================
def faktor_ganjil_iteratif(n):
    faktor = []
    for i in range(1, n + 1, 2):  # hanya bilangan ganjil
        if n % i == 0:
            faktor.append(i)
    return faktor

# =========================
# ALGORITMA REKURSIF
# =========================
def faktor_ganjil_rekursif(n, i, faktor):
    if i > n:
        return faktor
    if n % i == 0:
        faktor.append(i)
    return faktor_ganjil_rekursif(n, i + 2, faktor)

# =========================
# STREAMLIT UI
# =========================
st.title("Analisis Kompleksitas Algoritma")
st.subheader("Mencari Faktor Bilangan Ganjil dalam Rentang n")

st.write(
    "Aplikasi ini membandingkan algoritma **iteratif** dan **rekursif** "
    "dalam mencari faktor bilangan ganjil."
)

# Input bilangan ganjil
n = st.number_input(
    "Masukkan bilangan ganjil (n):",
    min_value=1,
    step=2
)

# =========================
# PROSES UTAMA
# =========================
if st.button("Cari Faktor & Hitung Waktu"):
    if n % 2 == 0:
        st.error("Masukkan bilangan ganjil!")
    else:
        # Iteratif
        start_iter = time.time()
        faktor_iter = faktor_ganjil_iteratif(n)
        end_iter = time.time()
        waktu_iter = end_iter - start_iter

        # Rekursif
        start_rek = time.time()
        faktor_rek = faktor_ganjil_rekursif(n, 1, [])
        end_rek = time.time()
        waktu_rek = end_rek - start_rek

        # Output
        st.subheader("Hasil Faktor Bilangan Ganjil")
        st.write("**Iteratif:**", faktor_iter)
        st.write("**Rekursif:**", faktor_rek)

        st.subheader("Waktu Eksekusi")
        st.write(f"Iteratif  : {waktu_iter:.6f} detik")
        st.write(f"Rekursif : {waktu_rek:.6f} detik")

# =========================
# ANALISIS RUNNING TIME
# =========================
st.subheader("Analisis Running Time")

if st.button("Jalankan Analisis"):
    ukuran_input = [10, 100, 500, 1000, 5000, 10000]
    waktu_iteratif = []
    waktu_rekursif = []

    for val in ukuran_input:
        if val % 2 == 0:
            val += 1

        start = time.time()
        faktor_ganjil_iteratif(val)
        waktu_iteratif.append(time.time() - start)

        start = time.time()
        faktor_ganjil_rekursif(val, 1, [])
        waktu_rekursif.append(time.time() - start)

    # Tabel
    data = pd.DataFrame({
        "n": ukuran_input,
        "Iteratif (detik)": waktu_iteratif,
        "Rekursif (detik)": waktu_rekursif
    })

    st.subheader("Tabel Hasil Running Time")
    st.dataframe(data)

    # Grafik
    st.subheader("Grafik Perbandingan Running Time")
    fig, ax = plt.subplots()
    ax.plot(ukuran_input, waktu_iteratif, marker='o', label="Iteratif")
    ax.plot(ukuran_input, waktu_rekursif, marker='o', label="Rekursif")
    ax.set_xlabel("Ukuran Input (n)")
    ax.set_ylabel("Waktu Eksekusi (detik)")
    ax.legend()
    st.pyplot(fig)
