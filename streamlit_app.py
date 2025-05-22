import streamlit as st

st.title("🍓 straawberryshortcake")
st.write(
    "welcome to my page"
)
st.image("628caba7d04b254e5986a9c69c3f6d96.jpg", width=200)
st.header("aplikasi Mengecek Nilai Genap/Ganjil")
angka= st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
     st.write(f"{angka} adalah Bilangan Genap")
else:
     st.write(f"{angka} adalah Bilangan Ganjil")
