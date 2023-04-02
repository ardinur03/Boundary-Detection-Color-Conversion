import streamlit as st
import numpy as np
import cv2

def RGB2XYZ(I):
    Ir = I[:,:,0]
    Ig = I[:,:,1]
    Ib = I[:,:,2]
    [m,n] = Ir.shape
    k = np.array([[0.49, 0.31, 0.20], [0.17697, 0.81240, 0.01063], [0.00, 0.01, 0.99]])

    Ixyz = np.zeros((m, n, 3))
    for i in range(m):
        for j in range(n):
            rgb = np.array([Ir[i,j], Ig[i,j], Ib[i,j]])
            xyz = (1/0.17697) * np.dot(k, rgb)
            Ixyz[i,j,:] = xyz

    return Ixyz.astype(np.uint8)

def flab(q):
    qn = np.double(q)
    if qn > 0.008856:
        x = np.power(qn, 1/3)
    else:
        x = 7.787 * qn + 16/116
    return x

def RGB2LAB(I):
    Ixyz = RGB2XYZ(I)
    Ix = Ixyz[:,:,0]
    Iy = Ixyz[:,:,1]
    Iz = Ixyz[:,:,2]
    [m,n] = Ix.shape

    xn = 0.95047
    yn = 1
    zn = 1.08883

    Ilab = np.zeros((m, n, 3))
    for i in range(m):
        for j in range(n):
            IL = 116 * flab(Iy[i,j]/yn) - 16
            Ia = 500 * (flab(Ix[i,j]/xn) - flab(Iy[i,j]/yn))
            Ib = 200 * (flab(Iy[i,j]/yn) - flab(Iz[i,j]/zn))
            Ilab[i,j,:] = [IL, Ia, Ib]

    return Ilab.astype(np.uint8)


def RGB2LUV(I):
    Ixyz = RGB2XYZ(I)
    Ix = Ixyz[:,:,0]
    Iy = Ixyz[:,:,1]
    Iz = Ixyz[:,:,2]
    [m,n] = np.shape(Ix)

    xn = 0.95047
    yn = 1
    zn = 1.08883

    IL = np.zeros_like(Ix)
    Iu = np.zeros_like(Ix)
    Iv = np.zeros_like(Ix)

    for i in range(m):
        for j in range(n):
            Li = Iy[i,j]/yn
            if Li > 0.008856:
                IL[i,j] = 116 * Li**(1/3) - 16
            else:
                IL[i,j] = 903.3 * Li

            u = 4 * Ix[i,j] / (Ix[i,j] + 15 * Iy[i,j] + 3 * Iz[i,j])
            un = 4 * xn / (xn + 15 * yn + 3 * zn)
            v = 9 * Iy[i,j] / (Ix[i,j] + 15 * Iy[i,j] + 3 * Iz[i,j])
            vn = 9 * yn / (xn + 15 * yn + 3 * zn)
            Iu[i,j] = 13 * IL[i,j] * (u - un)
            Iv[i,j] = 13 * IL[i,j] * (v - vn)

    ILuv = np.zeros_like(I)
    ILuv[:,:,0] = IL
    ILuv[:,:,1] = Iu
    ILuv[:,:,2] = Iv

    return ILuv