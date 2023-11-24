import numpy as np

def euler_method(x, y, h):
    n = len(x)
    dy = np.zeros(n)
    for i in range(0, n - 1):
        dy[i] = (y[i + 1] - y[i]) / h
    dy[n - 1] = dy[n - 2]
    return dy

# Contoh input x dan y
x_values = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
y_values = np.array([1.0, 2.0, 4.0, 8.0, 16.0])

# Pilih metode (euler, modified_euler, rk_second_order, atau rk_higher_order)
selected_method = 'euler'

# Hitung turunan numerik
if selected_method == 'euler':
    result_dy = euler_method(x_values, y_values, h=(x_values[1] - x_values[0]))
else:
    # Tambahkan kondisi untuk metode lain jika diperlukan
    print("Metode yang dipilih tidak valid")

# Menampilkan hasil
print("Hasil Turunan Numerik menggunakan", selected_method, ":", result_dy)
