import streamlit as st
import numpy as np
import cv2

from function.function import RGB2XYZ
from function.function import flab

st.set_page_config(page_title="Pertemuan 11")
st.title("Praktikum Pertemuan  11👋")

# add subtitle 
st.markdown("""
    ©Created by Jebret Team - 2023
    """)

uploaded_file = st.file_uploader("Choose an image", type=["jpg","jpeg","png"])


if uploaded_file is not None:
    # Load the image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Original Image","RGB2XYZ", "RGB ke CIElab",  "Image Processing", "Merge Vertical"])
    with tab1:
        st.markdown("<h2 style='text-align: center; color: white;'>Original Image</h2>", unsafe_allow_html=True)
        st.image(img, channels='Original Image')
    with tab2:
        st.markdown("<h2 style='text-align: center; color: white;'>RGB2XYZ</h2>", unsafe_allow_html=True)
        img_xyz = RGB2XYZ(img)
        st.image(img_xyz, channels='RGB2XYZ')

        # cetak nilai XYZ
        st.markdown("<h2 style='text-align: center; color: white;'>Nilai</h2>", unsafe_allow_html=True)
        st.write(img_xyz)

    with tab3:
        st.markdown("<h2 style='text-align: center; color: white;'>RGB ke CIElab</h2>", unsafe_allow_html=True)
        img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        st.image(img_lab, channels='RGB ke CIElab')

        # cetak nilai LAB
        st.markdown("<h2 style='text-align: center; color: white;'>Nilai</h2>", unsafe_allow_html=True)
        st.write(img_lab)
