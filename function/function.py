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


def RGB2YCbCr(I):
    Ir = I[:,:,0]
    Ig = I[:,:,1]
    Ib = I[:,:,2]
    [m,n] = np.shape(Ir)

    k = [0,128,128]
    T = [[0.299, 0.587, 0.114],[-0.168, -0.331, 0.500],[0.500, -0.419, -0.081]]

    Iy = np.zeros((m, n), dtype=np.uint8)
    Icb = np.zeros((m, n), dtype=np.uint8)
    Icr = np.zeros((m, n), dtype=np.uint8)

    for i in range(m):
        for j in range(n):
            rgb = [Ir[i,j],Ig[i,j],Ib[i,j]]
            ycbcr = k + np.dot(T, np.transpose(rgb))
            Iy[i,j] = np.uint8(ycbcr[0])
            Icb[i,j] = np.uint8(ycbcr[1])
            Icr[i,j] = np.uint8(ycbcr[2])

    Iycbcr = np.zeros_like(I)
    Iycbcr[:,:,0] = Iy
    Iycbcr[:,:,1] = Icb
    Iycbcr[:,:,2] = Icr

    return Iycbcr

def RGB2NTSC(I):
    Ir = I[:,:,0]
    Ig = I[:,:,1]
    Ib = I[:,:,2]
    [m,n] = np.shape(Ir)

    k = np.array([[0.299, 0.587, 0.114], [-0.516, -0.274, 0.322], [0.211, -0.523, -0.312]])

    Iy = np.zeros((m, n), dtype=np.uint8)
    Iu = np.zeros((m, n), dtype=np.uint8)
    Iv = np.zeros((m, n), dtype=np.uint8)

    for i in range(m):
        for j in range(n):
            rgb = [Ir[i,j], Ig[i,j], Ib[i,j]]
            yiq = np.dot(k, rgb)
            Iy[i,j] = yiq[0] / 255.0
            Iu[i,j] = yiq[1] / 255.0
            Iv[i,j] = yiq[2] / 255.0

    IYiq = np.zeros_like(I)
    IYiq[:,:,0] = Iy
    IYiq[:,:,1] = Iu
    IYiq[:,:,2] = Iv
    IYiq = np.clip(IYiq, 0, 1)  # memotong nilai piksel di bawah 0 dan di atas 1
    IYiq = (IYiq - np.min(IYiq)) / (np.max(IYiq) - np.min(IYiq))  # min-max scaling

    return IYiq

