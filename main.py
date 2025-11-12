import numpy as np
import matplotlib.pyplot as plt

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
    return adaptive_recursive(f, a, c, eps / 2.0, left) + adaptive_recursive(f, c, b, eps / 2.0, right)

def adaptive_integration(f, a, b, tol=1e-6):
    return adaptive_recursive(f, a, b, tol, simpson(f, a, b))

def plot_integral(f, a, b, title="Integral Plot"):
    x = np.linspace(a - (b-a)*0.1, b + (b-a)*0.1, 200)
    y = f(x)
    
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label='f(x)', color='blue')
    
    x_fill = np.linspace(a, b, 100)
    y_fill = f(x_fill)
    plt.fill_between(x_fill, y_fill, alpha=0.3, color='blue', label='Area')
    
    plt.axvline(a, color='red', linestyle='--', label=f'a={a}')
    plt.axvline(b, color='green', linestyle='--', label=f'b={b}')
    plt.axhline(0, color='black', linewidth=0.5)
    
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    print("1. Integral cos(x) from 0 to pi/2")
    print("2. Integral x^2 from 0 to 1")
    print("3. Custom Input")
    
    choice = input("Select option (1/2/3): ")

    if choice == '1':
        f = np.cos
        a, b = 0, np.pi/2
        result = adaptive_integration(f, a, b)
        print(result)
        plot_integral(f, a, b, "Integral of cos(x)")
        
    elif choice == '2':
        f = lambda x: x**2
        a, b = 0, 1
        result = adaptive_integration(f, a, b)
        print(result)
        plot_integral(f, a, b, "Integral of x^2")
        
    elif choice == '3':
        func_str = input("Enter function (use np for numpy, e.g., np.sin(x) + x**2): ")
        a_str = input("Enter lower bound (a): ")
        b_str = input("Enter upper bound (b): ")
        
        try:
            context = {"np": np, "sin": np.sin, "cos": np.cos, "tan": np.tan, "exp": np.exp, "sqrt": np.sqrt, "pi": np.pi}
            a = float(eval(a_str, context))
            b = float(eval(b_str, context))
            f = lambda x: eval(func_str, {**context, "x": x})
            
            result = adaptive_integration(f, a, b)
            print(result)
            plot_integral(f, a, b, f"Integral of {func_str}")
        except Exception:
            print("Error in input format.")
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()