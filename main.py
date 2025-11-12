import numpy as np
from scipy.integrate import quad

# Fungsi untuk Integral pertama: f(x) = cos(x)
def integrand1(x):
    return np.cos(x)

# Fungsi untuk Integral kedua: f(x) = x^2
def integrand2(x):
    return x**2

# 1. Hitung Integral cos(x) dari 0 sampai pi/2
# quad mengembalikan dua nilai: (hasil integral, estimasi error)
result1, error1 = quad(integrand1, 0, np.pi/2)

# 2. Hitung Integral x^2 dari 0 sampai 1
result2, error2 = quad(integrand2, 0, 1)

# --- Menampilkan Hasil ---
print(f"-------------------------------------------")
print(f"------------ Hasil Perhitungan ------------")

print(f"\nIntegral 1: ∫ cos(x) dx dari 0 sampai π/2")
print(f"Hasil   : {result1}")
print(f"Error   : {error1}")
print(f"Secara analitik hasilnya adalah 1.0")
print(f"_________________________________________________")

print(f"\nIntegral 2: ∫ x^2 dx dari 0 sampai 1")
print(f"Hasil   : {result2}")
print(f"Error   : {error2}")
print(f"Secara analitik hasilnya adalah 1/3 atau 0.333...")
print(f"_________________________________________________")