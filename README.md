# 🧠 Fuzzy Membership Function Visualizer

A graphical Python application that allows users to **visualize and compute** various **fuzzy membership functions** dynamically using **Tkinter** and **Matplotlib**.

---


## 📘 Project Overview

This project provides an **interactive GUI** to calculate and visualize the **degree of membership (μ)** for different fuzzy sets.  
Users can input parameters dynamically, view the corresponding **membership function graph**, and observe the computed membership value for a given `x`.

---

## ⚙️ Features

✅ Interactive GUI built using **Tkinter**  
✅ Real-time plotting using **Matplotlib**  
✅ Supports **10 major membership functions**  
✅ Shows both **graphical and numeric** membership degree  
✅ Displays **developer information** on GUI and plots  
✅ Modular design for easy extension  

---

## 🧩 Supported Membership Functions

| Type | Formula / Description |
|------|------------------------|
| **Triangular** | Defined by three parameters (a, b, c) forming a triangle |
| **Trapezoidal** | Defined by four parameters (a, b, c, d) forming a trapezium |
| **Gaussian** | Bell-shaped curve controlled by mean `n` and standard deviation `σ` |
| **Generalized Bell (GBell)** | Smooth curve with adjustable steepness `(a, b, c)` |
| **Sigmoidal** | Smooth increasing curve defined by `(a, c)` |
| **S-shaped** | Smooth “S” curve from 0 to 1 |
| **Z-shaped** | Smooth “Z” curve from 1 to 0 |
| **Pi-shaped** | Combination of S and Z shapes `(a, b, c, d)` |
| **Singleton** | Sharp crisp value (1 at x = a) |
| **Difference of Sigmoids** | Bounded region between two sigmoid functions |

---

## 🖥️ Technologies Used

| Component | Technology |
|------------|-------------|
| GUI | Tkinter |
| Plotting | Matplotlib |
| Computation | NumPy, Math |
| Language | Python 3.x |

---

## 🚀 How to Run

### Prerequisites
Make sure you have Python and required libraries installed:
```bash
pip install tkinter matplotlib numpy
python Fuzzy_mem.py
