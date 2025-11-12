import math

MATH_CONTEXT = {
    "math": math,
    "pi": math.pi,
    "e": math.e,
    "sin": math.sin, "cos": math.cos, "tan": math.tan,
    "sqrt": math.sqrt, "exp": math.exp, "log": math.log,
    "abs": abs, "pow": math.pow
}

def simpson(f, a, b):
    c = (a + b) / 2.0
    h = abs(b - a) / 2.0
    return (h / 3.0) * (f(a) + 4.0 * f(c) + f(b))

def adaptive_recursive(f, a, b, eps, whole):
    c = (a + b) / 2.0
    left = simpson(f, a, c)
    right = simpson(f, c, b)
    if abs(left + right - whole) <= 15 * eps:
        return left + right + (left + right - whole) / 15.0
    return adaptive_recursive(f, a, c, eps / 2.0, left) + \
           adaptive_recursive(f, c, b, eps / 2.0, right)

def adaptive_integration(f, a, b, tol=1e-6):
    whole = simpson(f, a, b)
    return adaptive_recursive(f, a, b, tol, whole)

def print_value_table(f, a, b, steps=10):
    print(f"\n{'x':^12} | {'f(x)':^12}")
    print("-" * 27)
    step_size = (b - a) / steps
    for i in range(steps + 1):
        x = a + i * step_size
        try:
            y = f(x)
            print(f"{x:^12.4f} | {y:^12.4f}")
        except ValueError:
            print(f"{x:^12.4f} | {'Error':^12}")
    print("-" * 27)

def input_math_eval(prompt):
    user_str = input(prompt)
    try:
        value = float(eval(user_str, MATH_CONTEXT))
        return value
    except Exception:
        print(f"   [!] Error: Input '{user_str}' tidak valid.")
        return None

def main():
    while True:
        print("\n" + "-"*50)
        print("   ADAPTIVE INTEGRATION CALCULATOR   ")
        print("-"*50)
        print("1. Integral cos(x) dari 0 sampai pi/2")
        print("2. Integral x^2 dari 0 sampai 1")
        print("3. Input Custom Fungsi dan Batas")
        print("4. Logout ")
        print("-" * 50)
        
        choice = input("Pilih menu (1-4): ")

        if choice == '4':
            print("\nProgram selesai. Terima kasih!")
            break
        
        elif choice == '1':
            f = math.cos
            a, b = 0, math.pi/2
            print(f"\n[Preset] Integral cos(x) dari 0 s.d {b:.4f} (pi/2)")
            try:
                print(f"Hasil: {adaptive_integration(f, a, b)}")
                print_value_table(f, a, b)
            except Exception as e:
                print(f"Terjadi kesalahan perhitungan: {e}")
            
        elif choice == '2':
            f = lambda x: x**2
            a, b = 0, 1
            print(f"\n[Preset] Integral x^2 dari 0 s.d 1")
            try:
                print(f"Hasil: {adaptive_integration(f, a, b)}")
                print_value_table(f, a, b)
            except Exception as e:
                print(f"Terjadi kesalahan perhitungan: {e}")
            
        elif choice == '3':
            print("\n--- Mode Custom ---")
            
            func_str = input("Masukkan fungsi f(x) (contoh: sin(x) + x): ")
            
            a = input_math_eval("Masukkan batas bawah (a): ")
            if a is None:
                input("\nInput batas bawah salah. Tekan [Enter] untuk kembali ke menu...")
                continue 
            
            b = input_math_eval("Masukkan batas atas (b): ")
            if b is None:
                input("\nInput batas atas salah. Tekan [Enter] untuk kembali ke menu...")
                continue 

            try:
                f = lambda x: eval(func_str, {**MATH_CONTEXT, "x": x})
                
                try:
                    f(a) 
                except Exception as e:
                    print(f"\n[!] Error pada rumus fungsi: {e}")
                    input("Tekan [Enter] untuk kembali ke menu...")
                    continue

                print(f"\n[Hitung] Integral dari {a:.4f} sampai {b:.4f}")
                result = adaptive_integration(f, a, b)
                print(f"Hasil Integral: {result}")
                print_value_table(f, a, b)
                
            except Exception as e:
                print(f"\n[ERROR] Gagal menghitung: {e}")
        
        else:
            print("\n[!] Pilihan menu tidak valid (Gunakan angka 1-4).")

        input("\nTekan [Enter] untuk kembali ke menu...")

if __name__ == "__main__":
    main()