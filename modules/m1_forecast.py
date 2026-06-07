
# modules/m1_forecast.py
import numpy as np

def run_m1():
    """Chạy module M1 - Dự báo kinh tế"""
    years = np.array([2020, 2021, 2022, 2023, 2024, 2025])
    Y = np.array([8044.4, 8487.5, 9513.3, 10221.8, 11511.9, 12847.6])
    K = np.array([16500, 17800, 19600, 21300, 23500, 25900])
    L = np.array([53.6, 50.5, 51.7, 52.4, 52.9, 53.4])
    D = np.array([12.0, 12.7, 14.3, 16.5, 18.3, 19.5])
    AI = np.array([55.6, 60.2, 65.4, 67.0, 73.8, 80.1])
    H = np.array([24.1, 26.1, 26.2, 27.0, 28.4, 29.2])

    alpha, beta, gamma, delta, theta = 0.33, 0.42, 0.10, 0.08, 0.07
    A = Y / (K**alpha * L**beta * D**gamma * AI**delta * H**theta)

    K_2030 = K[-1] * (1.06)**5
    L_2030 = L[-1] * (1.06)**5
    A_2030 = A[-1] * (1.012)**5
    Y_2030 = A_2030 * (K_2030**alpha * L_2030**beta * 30**gamma * 100**delta * 35**theta)

    return {
        'years': years.tolist(),
        'GDP': Y.tolist(),
        'TFP': A.tolist(),
        'GDP_2025': float(Y[-1]),
        'GDP_2030': float(Y_2030),
        'TFP_growth': float(((A[-1]/A[0])**(1/5)-1)*100)
    }
