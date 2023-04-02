import streamlit as st
import numpy as np
import cv2

def RGB2XYZ(img):
    # Ambil komponen R,G,B dari gambar
    B = img[:, :, 0].astype(float) / 255
    G = img[:, :, 1].astype(float) / 255
    R = img[:, :, 2].astype(float) / 255

    # Nilai white point
    xn = 0.95047
    yn = 1
    zn = 1.08883

    # Transformasi RGB ke XYZ
    X = 0.4124 * R + 0.3576 * G + 0.1805 * B
    Y = 0.2126 * R + 0.7152 * G + 0.0722 * B
    Z = 0.0193 * R + 0.1192 * G + 0.9505 * B

    # Hitung nilai Xn, Yn, Zn
    Xn = xn / yn
    Yn = 1
    Zn = zn / yn

    # Normalisasi XYZ
    Xn = X / Xn
    Yn = Y / Yn
    Zn = Z / Zn

    # Gabungkan komponen X,Y,Z menjadi gambar XYZ
    img_xyz = np.dstack((Xn, Yn, Zn))

    # Konversi gambar XYZ ke RGB
    img_rgb = cv2.cvtColor((img_xyz * 255).astype(np.uint8), cv2.COLOR_XYZ2BGR)

    return img_rgb

def flab(q):
    qn = np.double(q)
    if qn > 0.008856:
        x = np.power(qn, 1/3)
    else:
        x = 7.787 * qn + 16/116
    return x
