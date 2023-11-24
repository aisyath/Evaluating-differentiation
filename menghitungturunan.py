import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menghitung turunan numerik menggunakan metode Euler
def euler_method(x, y, h):
    n = len(x)
    dy = np.zeros(n)
    for i in range(0, n - 1):
        dy[i] = (y[i + 1] - y[i]) / h
    dy[n - 1] = dy[n - 2]
    return dy

# Fungsi untuk menghitung turunan numerik menggunakan metode Modified Euler
def modified_euler_method(x, y, h):
    n = len(x)
    dy = np.zeros(n)
    for i in range(0, n - 1):
        k1 = (y[i + 1] - y[i]) / h
        k2 = (y[i + 1] - y[i] + h * k1) / h
        dy[i] = (k1 + k2) / 2
    dy[n - 1] = dy[n - 2]
    return dy

# Fungsi untuk menghitung turunan numerik menggunakan metode Runge-Kutta orde kedua
def runge_kutta_second_order(x, y, h):
    n = len(x)
    dy = np.zeros(n)
    for i in range(0, n - 1):
        k1 = (y[i + 1] - y[i]) / h
        k2 = (y[i] + h * k1) / h
        dy[i] = (k1 + k2) / 2
    dy[n - 1] = dy[n - 2]
    return dy

# Fungsi untuk menghitung turunan numerik menggunakan metode Runge-Kutta orde lebih tinggi (cth: orde keempat)
def runge_kutta_higher_order(x, y, h):
    n = len(x)
    dy = np.zeros(n)
    for i in range(0, n - 1):
        k1 = (y[i + 1] - y[i]) / h
        k2 = (y[i] + 0.5 * h * k1) / h
        k3 = (y[i] + 0.5 * h * k2) / h
        k4 = (y[i] + h * k3) / h
        dy[i] = (k1 + 2 * k2 + 2 * k3 + k4) / 6
    dy[n - 1] = dy[n - 2]
    return dy

# Contoh Penggunaan
x_values = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
y_values = np.array([1.0, 2.0, 4.0, 8.0, 16.0])

h_value = x_values[1] - x_values[0]

# Menghitung turunan numerik menggunakan metode-metode yang berbeda
euler_dy = euler_method(x_values, y_values, h_value)
modified_euler_dy = modified_euler_method(x_values, y_values, h_value)
rk_second_order_dy = runge_kutta_second_order(x_values, y_values, h_value)
rk_higher_order_dy = runge_kutta_higher_order(x_values, y_values, h_value)

# Menampilkan hasil
print("Turunan Numerik (Euler Method):", euler_dy)
print("Turunan Numerik (Modified Euler Method):", modified_euler_dy)
print("Turunan Numerik (Runge-Kutta Second Order):", rk_second_order_dy)
print("Turunan Numerik (Runge-Kutta Higher Order):", rk_higher_order_dy)

# Menampilkan plot hasil turunan numerik
plt.plot(x_values, euler_dy, label='Euler Method')
plt.plot(x_values, modified_euler_dy, label='Modified Euler Method')
plt.plot(x_values, rk_second_order_dy, label='Runge-Kutta Second Order')
plt.plot(x_values, rk_higher_order_dy, label='Runge-Kutta Higher Order')
plt.legend()
plt.xlabel('Nilai x')
plt.ylabel('Turunan Numerik')
plt.title('Perbandingan Metode Turunan Numerik')
plt.show()
