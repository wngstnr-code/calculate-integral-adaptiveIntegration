import numpy as np
import sys


def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    result = h * (0.5 * y[0] + np.sum(y[1:-1]) + 0.5 * y[-1])
    return result

def integral_1(x):
    return np.cos(x)

def integral_2(x):
    return x**2


def main():
    print("pilih opsi:")
    print("1. integral cos(x) dari 0 hingga pi/2")
    print("2. integral x^2 dari 0 hingga 1")
    print("3. input custom integrand")
    choice = input("masukkan pilihan (1/2/3): ")
    if choice == "1":
        a = 0
        b = np.pi / 2
        while True:
            n = int(input("masukkan jumlah subinterval (n) [1, 2, atau 4]: "))
            if n in [1, 2, 4]:
                break
            print("error: n harus 1, 2, atau 4")
        result = trapezoidal_rule(integral_1, a, b, n)
        print(f"hasil estimasi integral: {result}")
        print(f"hasil integral sesungguhnya: {1}")
    elif choice == "2":
        a = 0
        b = 1
        while True:
            n = int(input("masukkan jumlah subinterval (n) [1, 2, atau 4]: "))
            if n in [1, 2, 4]:
                break
            print("error: n harus 1, 2, atau 4")
        result = trapezoidal_rule(integral_2, a, b, n)
        print(f"hasil estimasi integral: {result}")
        print(f"hasil integral sesungguhnya: {1/3}")
        
    elif choice == "3":
        print("masukkan fungsi dalam bentuk Python (gunakan np untuk numpy)")
        print("contoh: np.sin(x), x**2, np.exp(x)")
        func_str = input("f(x) = ")
        a = float(input("Batas bawah (a): "))
        b = float(input("Batas atas (b): "))
        n = int(input("Jumlah subinterval (n): "))
        
        def custom_func(x):
            return eval(func_str)
        
        result = trapezoidal_rule(custom_func, a, b, n)
        print(f"hasil estimasi integral: {result}")

    else:
        print("pilihan tidak valid")
        sys.exit(1)


if __name__ == "__main__":
    main()