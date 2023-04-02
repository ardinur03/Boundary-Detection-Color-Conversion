import streamlit as st
import numpy as np
from PIL import Image
import cv2

from function.function import RGB2XYZ
from function.function import RGB2LAB
from function.function import RGB2LUV
from function.function import RGB2YCbCr
from function.function import RGB2NTSC
from function.function import RGB2YUV
from function.function import RGB2HSV
from function.function import RGB2CMY

st.set_page_config(page_title="Pertemuan 11")
st.title("Praktikum Pertemuan  11👋")

# add subtitle 
st.markdown("""
    ©Created by Jebret Team - 2023
    """)

uploaded_file_1 = st.file_uploader("Choose an image", type=["jpg","jpeg","png"])


if uploaded_file_1 is not None:
    img = np.frombuffer(uploaded_file_1.read(), np.uint8)
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(["Original Image","RGB ke XYZ", "RGB ke CIElab",  "RGB ke LUV", "RGB ke YCbCr", "RGB ke NTSC", "RGB ke YUV", "RGB ke HSV", "RGB ke CMY"])
    with tab1:
        st.markdown("<h2 style='text-align: center; color: white;'>Original Image</h2>", unsafe_allow_html=True)
        newImg =  cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        st.image(newImg,  width=300)
    with tab2:
        st.markdown("<h2 style='text-align: center; color: white;'>RGB ke XYZ</h2>", unsafe_allow_html=True)
        img_xyz = RGB2XYZ(img)
        st.image(img_xyz, channels='RGB2XYZ', width=300)
        st.markdown("<h2 style='text-align: center; color: white;'>Nilai</h2>", unsafe_allow_html=True)
        st.write(img_xyz)
    with tab3:
        st.markdown("<h2 style='text-align: center; color: white;'>RGB ke CIElab</h2>", unsafe_allow_html=True)
        img_lab = RGB2LAB(img)
        st.image(img_lab, channels='RGB2LAB', width=300)
        st.markdown("<h2 style='text-align: center; color: white;'>Nilai</h2>", unsafe_allow_html=True)
        st.write(img_lab)
    with tab4:
        st.markdown("<h2 style='text-align: center; color: white;'>RGB ke LUV</h2>", unsafe_allow_html=True)
        img_luv = RGB2LUV(img)
        st.image(img_luv, channels='RGB2LAB', width=300)
        st.markdown("<h2 style='text-align: center; color: white;'>Nilai</h2>", unsafe_allow_html=True)
        st.write(img_luv)
    with tab5:
        st.markdown("<h2 style='text-align: center; color: white;'>RGB ke YCbCr</h2>", unsafe_allow_html=True)
        img_ycbcr = RGB2YCbCr(img)
        st.image(img_ycbcr, channels='RGB2YCbCr', width=300)
        st.markdown("<h2 style='text-align: center; color: white;'>Nilai</h2>", unsafe_allow_html=True)
        st.write(img_ycbcr)
    with tab6:
        st.markdown("<h2 style='text-align: center; color: white;'>RGB ke NTSC</h2>", unsafe_allow_html=True)
        img_ntsc = RGB2NTSC(img)
        st.image(img_ntsc, channels='RGB2NTSC', width=300)
        st.markdown("<h2 style='text-align: center; color: white;'>Nilai</h2>", unsafe_allow_html=True)
        st.write(img_ntsc)
    with tab7:
        st.markdown("<h2 style='text-align: center; color: white;'>RGB ke YUV</h2>", unsafe_allow_html=True)
        img_yuv = RGB2YUV(img)
        st.image(img_yuv, channels='RGB2YUV', width=300)
        st.markdown("<h2 style='text-align: center; color: white;'>Nilai</h2>", unsafe_allow_html=True)
        st.write(img_yuv)
    with tab8:
        st.markdown("<h2 style='text-align: center; color: white;'>RGB ke HSV</h2>", unsafe_allow_html=True)
        img_hsv = RGB2HSV(img)
        st.image(img_hsv, channels='RGB2HSV', width=300)
        st.markdown("<h2 style='text-align: center; color: white;'>Nilai</h2>", unsafe_allow_html=True)
        st.write(img_hsv)
    with tab9:
        st.markdown("<h2 style='text-align: center; color: white;'>RGB ke CMY</h2>", unsafe_allow_html=True)
        img_cmy = RGB2CMY(img)
        st.image(img_cmy, channels='RGB2CMY', width=300)
        st.markdown("<h2 style='text-align: center; color: white;'>Nilai</h2>", unsafe_allow_html=True)
        st.write(img_cmy)
        