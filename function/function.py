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