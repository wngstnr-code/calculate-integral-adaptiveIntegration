import numpy as np

def gaussian_quadrature(func, a, b, n=3):
    if n == 2:
        t = [-1/np.sqrt(3), 1/np.sqrt(3)]
        w = [1, 1]
    elif n == 3:
        t = [-np.sqrt(3/5), 0, np.sqrt(3/5)]
        w = [5/9, 8/9, 5/9]
    else:
        t = [-np.sqrt(3/7 + 2/7*np.sqrt(6/5)), -np.sqrt(3/7 - 2/7*np.sqrt(6/5)), 
             np.sqrt(3/7 - 2/7*np.sqrt(6/5)), np.sqrt(3/7 + 2/7*np.sqrt(6/5))]
        w = [(18-np.sqrt(30))/36, (18+np.sqrt(30))/36, (18+np.sqrt(30))/36, (18-np.sqrt(30))/36]
    
    result = 0
    for i in range(n):
        x = ((b - a) * t[i] + (b + a)) / 2
        result += w[i] * func(x)
    result *= (b - a) / 2
    return result

def func1(x):
    return np.cos(x)

def func2(x):
    return x**2

def main():
    print("Pilih opsi:")
    print("1. Integral cos(x) dari 0 hingga pi/2")
    print("2. Integral x^2 dari 0 hingga 1")
    print("3. Input custom integrand")
    choice = input("Masukkan pilihan (1/2/3): ")
    n = 3
    n = int(input("Masukkan jumlah titik 1-4 (default 3): ") or 3)
    if choice == "1":
        a = 0
        b = np.pi / 2
        result = gaussian_quadrature(func1, a, b, n)
        print(f"Gaussian Quadrature: {result}")
    
    elif choice == "2":
        a = 0
        b = 1
        result = gaussian_quadrature(func2, a, b, n)
        print(f"Gaussian Quadrature: {result}")
    
    elif choice == "3":
        print("Masukkan fungsi dalam bentuk Python (gunakan np untuk numpy)")
        print("Contoh: np.sin(x), x**2, np.exp(x)")
        func_str = input("f(x) = ")
        a = float(input("Batas bawah (float): "))
        b = float(input("Batas atas (float): "))

        def custom_func(x):
            return eval(func_str)
    
        result = gaussian_quadrature(custom_func, a, b, n)
        print(f"Gaussian Quadrature: {result}")

if __name__ == "__main__":
    main()