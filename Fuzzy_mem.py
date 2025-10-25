import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
import math

# === Plot Function with Signature === #
def plot_graph(x_vals, y_vals, title, result_x, result_y):
    plt.figure(figsize=(7, 4))
    plt.plot(x_vals, y_vals, label="Membership Function", color="blue")
    plt.scatter([result_x], [result_y], color='red', label=f"Result: ({result_x}, {result_y:.4f})", zorder=5)
    plt.annotate(f"({result_x}, {result_y:.4f})",
                 (result_x, result_y),
                 textcoords="offset points",
                 xytext=(10, 10),
                 ha='center', color='red')
    plt.xlabel("x")
    plt.ylabel("μ(x)")
    plt.title(title)
    plt.text(0.95, 0.02, "Ariharan A R (2022503005)",
             fontsize=9, color='gray', ha='right', transform=plt.gca().transAxes)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# === Membership Function Definitions === #

def mu_triangle(x, a, b, c):
    u = max(min((x - a) / (b - a), (c - x) / (c - b)), 0)
    result_label.config(text=f"Degree of Membership: μ({x}) = {u:.4f}")
    xs = np.linspace(a - 2, c + 2, 200)
    ys = [max(min((xi - a) / (b - a), (c - xi) / (c - b)), 0) for xi in xs]
    plot_graph(xs, ys, "Triangular Membership Function", x, u)

def mu_trapezoidal(x, a, b, c, d):
    u = max(min((x - a) / (b - a), 1, (d - x) / (d - c)), 0)
    result_label.config(text=f"Degree of Membership: μ({x}) = {u:.4f}")
    xs = np.linspace(a - 2, d + 2, 200)
    ys = [max(min((xi - a) / (b - a), 1, (d - xi) / (d - c)), 0) for xi in xs]
    plot_graph(xs, ys, "Trapezoidal Membership Function", x, u)

def gaussian_membership(x, n, sigma):
    mu = math.exp(-0.5 * ((x - n) / sigma) ** 2)
    result_label.config(text=f"Degree of Membership: μ({x}) = {mu:.4f}")
    xs = np.linspace(n - 4 * sigma, n + 4 * sigma, 200)
    ys = [math.exp(-0.5 * ((xi - n) / sigma) ** 2) for xi in xs]
    plot_graph(xs, ys, "Gaussian Membership Function", x, mu)

def bell_function(x, a, b, c):
    mu = 1 / (1 + abs((x - c) / a) ** (2 * b))
    result_label.config(text=f"Degree of Membership: μ({x}) = {mu:.4f}")
    xs = np.linspace(c - 5 * a, c + 5 * a, 200)
    ys = [1 / (1 + abs((xi - c) / a) ** (2 * b)) for xi in xs]
    plot_graph(xs, ys, "Generalized Bell Membership Function", x, mu)

def sigmoid_function(x, a, c):
    mu = 1 / (1 + math.exp(-a * (x - c)))
    result_label.config(text=f"Degree of Membership: μ({x}) = {mu:.4f}")
    xs = np.linspace(c - 10, c + 10, 200)
    ys = [1 / (1 + math.exp(-a * (xi - c))) for xi in xs]
    plot_graph(xs, ys, "Sigmoidal Membership Function", x, mu)

def s_shaped(x, a, b):
    if x <= a:
        mu = 0
    elif a < x <= (a + b) / 2:
        mu = 2 * ((x - a) / (b - a)) ** 2
    elif (a + b) / 2 < x < b:
        mu = 1 - 2 * ((x - b) / (b - a)) ** 2
    else:
        mu = 1
    result_label.config(text=f"Degree of Membership: μ({x}) = {mu:.4f}")
    xs = np.linspace(a - 2, b + 2, 200)
    ys = [0 if xi <= a else 2 * ((xi - a) / (b - a)) ** 2 if xi <= (a + b) / 2
          else (1 - 2 * ((xi - b) / (b - a)) ** 2 if xi < b else 1) for xi in xs]
    plot_graph(xs, ys, "S-shaped Membership Function", x, mu)

def z_shaped(x, a, b):
    if x <= a:
        mu = 1
    elif a < x <= (a + b) / 2:
        mu = 1 - 2 * ((x - a) / (b - a)) ** 2
    elif (a + b) / 2 < x < b:
        mu = 2 * ((x - b) / (b - a)) ** 2
    else:
        mu = 0
    result_label.config(text=f"Degree of Membership: μ({x}) = {mu:.4f}")
    xs = np.linspace(a - 2, b + 2, 200)
    ys = [1 if xi <= a else 1 - 2 * ((xi - a) / (b - a)) ** 2 if xi <= (a + b) / 2
          else (2 * ((xi - b) / (b - a)) ** 2 if xi < b else 0) for xi in xs]
    plot_graph(xs, ys, "Z-shaped Membership Function", x, mu)

def pi_shaped(x, a, b, c, d):
    if x <= a:
        mu = 0
    elif a < x <= b:
        mu = 2 * ((x - a) / (b - a)) ** 2
    elif b < x <= c:
        mu = 1
    elif c < x <= d:
        mu = 1 - 2 * ((x - d) / (d - c)) ** 2
    else:
        mu = 0
    result_label.config(text=f"Degree of Membership: μ({x}) = {mu:.4f}")
    xs = np.linspace(a - 2, d + 2, 200)
    ys = []
    for xi in xs:
        if xi <= a:
            ys.append(0)
        elif a < xi <= b:
            ys.append(2 * ((xi - a) / (b - a)) ** 2)
        elif b < xi <= c:
            ys.append(1)
        elif c < xi <= d:
            ys.append(1 - 2 * ((xi - d) / (d - c)) ** 2)
        else:
            ys.append(0)
    plot_graph(xs, ys, "Pi-shaped Membership Function", x, mu)

def singleton(x, a):
    mu = 1 if x == a else 0
    result_label.config(text=f"Degree of Membership: μ({x}) = {mu:.4f}")
    xs = np.linspace(a - 5, a + 5, 200)
    ys = [1 if abs(xi - a) < 1e-9 else 0 for xi in xs]
    plot_graph(xs, ys, "Singleton Membership Function", x, mu)

def diff_sigmoid(x, a1, c1, a2, c2):
    mu1 = 1 / (1 + math.exp(-a1 * (x - c1)))
    mu2 = 1 / (1 + math.exp(-a2 * (x - c2)))
    mu = mu1 - mu2
    result_label.config(text=f"Degree of Membership: μ({x}) = {mu:.4f}")
    xs = np.linspace(min(c1, c2) - 10, max(c1, c2) + 10, 200)
    ys = [(1 / (1 + math.exp(-a1 * (xi - c1))) - 1 / (1 + math.exp(-a2 * (xi - c2)))) for xi in xs]
    plot_graph(xs, ys, "Difference of Two Sigmoids", x, mu)

# === Dynamic Input Form === #
def update_input_fields(*args):
    for widget in input_frame.winfo_children():
        widget.destroy()

    selected_function = function_choice.get()
    global input_entries
    input_entries = {}

    input_fields = {
        "Triangular": ["x", "a", "b", "c"],
        "Trapezoidal": ["x", "a", "b", "c", "d"],
        "Gaussian": ["x", "n", "sigma"],
        "Bell": ["x", "a", "b", "c"],
        "Sigmoidal": ["x", "a", "c"],
        "S-shaped": ["x", "a", "b"],
        "Z-shaped": ["x", "a", "b"],
        "Pi-shaped": ["x", "a", "b", "c", "d"],
        "Singleton": ["x", "a"],
        "Diff. of Sigmoids": ["x", "a1", "c1", "a2", "c2"]
    }

    for i, field in enumerate(input_fields[selected_function]):
        tk.Label(input_frame, text=f"{field}:").grid(row=i, column=0, sticky="w")
        entry = ttk.Entry(input_frame, width=10)
        entry.grid(row=i, column=1)
        input_entries[field] = entry

    run_button.grid(row=i + 1, column=0, columnspan=2, pady=10)

# === Run Function === #
def run_selected_function():
    try:
        inputs = {key: float(entry.get()) for key, entry in input_entries.items()}
        selected_function = function_choice.get()

        if selected_function == "Triangular":
            mu_triangle(**inputs)
        elif selected_function == "Trapezoidal":
            mu_trapezoidal(**inputs)
        elif selected_function == "Gaussian":
            gaussian_membership(**inputs)
        elif selected_function == "Bell":
            bell_function(**inputs)
        elif selected_function == "Sigmoidal":
            sigmoid_function(**inputs)
        elif selected_function == "S-shaped":
            s_shaped(**inputs)
        elif selected_function == "Z-shaped":
            z_shaped(**inputs)
        elif selected_function == "Pi-shaped":
            pi_shaped(**inputs)
        elif selected_function == "Singleton":
            singleton(**inputs)
        elif selected_function == "Diff. of Sigmoids":
            diff_sigmoid(**inputs)
    except ValueError:
        result_label.config(text="Please enter valid numeric inputs!")

# === GUI Setup === #
root = tk.Tk()
root.title("Fuzzy Membership Function Visualizer")

main_frame = ttk.Frame(root, padding="10")
main_frame.grid()

ttk.Label(main_frame, text="Select Membership Function:").grid(row=0, column=0, sticky="w")
function_choice = tk.StringVar()
function_dropdown = ttk.OptionMenu(main_frame, function_choice, "Triangular", 
                                   "Triangular", "Trapezoidal", "Gaussian", "Bell",
                                   "Sigmoidal", "S-shaped", "Z-shaped", "Pi-shaped",
                                   "Singleton", "Diff. of Sigmoids")
function_dropdown.grid(row=0, column=1, pady=5)
function_choice.trace_add("write", update_input_fields)

input_frame = ttk.Frame(main_frame)
input_frame.grid(row=1, column=0, columnspan=2, pady=10)

run_button = ttk.Button(main_frame, text="Calculate and Plot", command=run_selected_function)
result_label = ttk.Label(main_frame, text="Result will appear here", foreground="blue")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Footer Signature
footer_label = ttk.Label(main_frame, text="Developed by Ariharan A R (2022503005)", foreground="gray")
footer_label.grid(row=4, column=0, columnspan=2, pady=5)

update_input_fields()
root.mainloop()
