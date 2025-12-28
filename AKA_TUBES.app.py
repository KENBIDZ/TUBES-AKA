import streamlit as st
import time
import sys

# Meningkatkan limit rekursi untuk angka yang besar
sys.setrecursionlimit(2000)

def find_factors_iterative(n):
    """Mencari faktor dengan pendekatan perulangan (Iteratif)"""
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def find_factors_recursive(n, current=1, factors=None):
    """Mencari faktor dengan pendekatan pemanggilan fungsi (Rekursif)"""
    if factors is None:
        factors = []
    
    if current > n:
        return factors
    
    if n % current == 0:
        factors.append(current)
    
    return find_factors_recursive(n, current + 1, factors)

# --- UI STREAMLIT ---
st.set_page_config(page_title="Analisis Algoritma Faktor Ganjil", layout="wide")

st.title("📊 Studi Kasus: Pencarian Faktor Bilangan Ganjil")
st.write("Tugas Besar Analisis Kompleksitas Algoritma (AKA)")

st.info("""
**Deskripsi:** Aplikasi ini membandingkan efisiensi antara metode **Iteratif** dan **Rekursif** untuk mencari faktor dari bilangan ganjil dalam rentang 1 hingga $n$.
""")

# Input User
n = st.number_input("Masukkan bilangan ganjil (n):", min_value=1, step=2, value=15)

if n % 2 == 0:
    st.warning("⚠️ Mohon masukkan bilangan ganjil sesuai instruksi studi kasus.")
else:
    col1, col2 = st.columns(2)

    # --- Eksekusi Iteratif ---
    with col1:
        st.subheader("🔄 Pendekatan Iteratif")
        start_time = time.perf_counter()
        res_iter = find_factors_iterative(n)
        end_time = time.perf_counter()
        
        st.success(f"Faktor ditemukan: {res_iter}")
        st.metric("Waktu Eksekusi", f"{end_time - start_time:.6f} detik")
        st.code("""
for i in range(1, n + 1):
    if n % i == 0:
        factors.append(i)
        """, language="python")

    # --- Eksekusi Rekursif ---
    with col2:
        st.subheader("🔂 Pendekatan Rekursif")
        try:
            start_time = time.perf_counter()
            res_recur = find_factors_recursive(n)
            end_time = time.perf_counter()
            
            st.success(f"Faktor ditemukan: {res_recur}")
            st.metric("Waktu Eksekusi", f"{end_time - start_time:.6f} detik")
            st.code("""
def recur(n, current):
    if current > n: return
    if n % current == 0: ...
    return recur(n, current + 1)
            """, language="python")
        except RecursionError:
            st.error("Recursion Depth Exceeded! Bilangan terlalu besar untuk metode rekursif standar.")

    # --- Analisis Singkat ---
    st.divider()
    st.subheader("📝 Kesimpulan Analisis")
    st.write(f"""
    1. **Kompleksitas Waktu:** Kedua algoritma memiliki kompleksitas waktu $O(n)$ karena harus mengecek setiap angka dari 1 hingga $n$.
    2. **Kompleksitas Ruang:** Iteratif lebih efisien ($O(1)$ tambahan) dibandingkan Rekursif ($O(n)$ pada stack) karena setiap pemanggilan fungsi memakan memori.
    3. **Observasi:** Untuk nilai $n$ yang sangat besar, metode Rekursif akan mengalami 'Stack Overflow', sedangkan Iteratif tetap berjalan stabil.
    """)
