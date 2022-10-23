import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
from mpmath import mp
import gmpy2 as g2

#Partial partion functions of which there are i=4
#T is the temperature and n^2 is the size of the lattice (square)


def c(l, K, n):
    # c = (np.cosh(2.0 * K) * (1.0 / np.tanh(2.0 * K)) - np.cos(l * np.pi / n))
    c = (g2.cosh(g2.mpfr(2.0) * K) * g2.coth(g2.mpfr(2.0) * K) - g2.cos(g2.mpfr(l) * np.pi / g2.mpfr(n)))
    return c


def gamma(l, K, n):
    # print("This is l: "+str(l))
    if l == 0:
        gamma_0 = (2.0 * K + g2.log(g2.tanh(K)))
        # print("this is gamma_0: " +str(gamma_0))
        return gamma_0
    else:
        gamma = g2.log(c(l, K, n) + (c(l, K, n)**2 - 1.0)**0.5)
        # print("This is gamma_"+str(l)+": " + str(gamma))
        return gamma
	

def Z_i(i, K, n):
    if i == 0:
        Z_1 = []
        for r in range(n):
            z = (2.0 * g2.cosh(0.5 * n * gamma((2.0 * r + 1.0), K, n)))
            Z_1.append(2.0 * g2.cosh(0.5 * n * gamma((2.0 * r + 1.0), K, n)))
        return np.product(Z_1)

    elif i == 1:
        Z_2 = []
        for r in range(n):
            Z_2.append(2.0 * g2.sinh(0.5 * n * gamma((2.0 * r + 1.0), K, n)))
        return np.product(Z_2)

    elif i == 2:
        Z_3 = []
        for r in range(n):
            Z_3.append(2 * g2.cosh(0.5 * n * gamma((2.0 * r), K, n)))
        return np.product(Z_3)

    elif i == 3:
        Z_4 = []
        for r in range(n):
            Z_4.append(2.0 * g2.sinh(0.5 * n * gamma((2.0 * r), K, n)))
        return np.product(Z_4)
    else:
        print("error")


def Z(K, n):
    Z_partial = 0
    for i in range(4):
        Z_partial += Z_i(i, K, n)
        # print('i: ', i, 'Z_partial: ', Z_partial)

    partial_correction = 0.5 * (2.0 * g2.sinh(2.0 * K))**(0.5 * n**2)
    return partial_correction * Z_partial


def d_log_Z(K, d_K, n):
    return (g2.log(Z(K + d_K, n)) - g2.log(Z(K-d_K, n))) / (2 * d_K)


def d2_log_Z(K, d_K, n):
    return (g2.log(Z(K + d_K, n)) - 2.0 * g2.log(Z(K, n)) + g2.log(Z(K-d_K, n))) / (d_K**2)


def U(T, d_T, n):
    return -d_log_Z(1.0 / T, d_T, n)


def F(T, n):
    return (-g2.log(Z(1.0 / T, n)) * T)


def S(T, n):
    return ( U(T, d_T, n) - F(T, n) ) / (T*n**2)


def C(K, d_K, n):
    return (K**2) * d2_log_Z(K, d_K, n)


# def S(T,n,Z,F,d_T):
#     return(-(F(Z,T+d_T,n)-F(Z,T-d_T,n))/(2*d_T))


d_T = g2.mpfr(1e-4)
# n = 4
# T_array = np.linspace(0.0, 10.0, 100)
# Z_array = np.zeros(len(T_array))
# S_array = np.zeros(len(T_array))
# C_array = np.zeros(len(T_array))
# for t_n in range(len(T_array)):
    # Z_array[t_n] = Z(1.0 / g2.mpfr(T_array[t_n]), n)
    # S_array[t_n] = S(g2.mpfr(T_array[t_n]), n)
    # C_array[t_n] = C(1.0 / g2.mpfr(T_array[t_n]), d_T, n)

# plt.plot(T_array, Z_array)
# plt.plot(T_array, S_array)
# plt.plot(T_array, C_array / n**2, '--')
# plt.show()
