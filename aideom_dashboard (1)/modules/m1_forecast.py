# modules/m1_forecast.py
# M1: DỰ BÁO KINH TẾ (từ Bài 1)
# Tác giả: [Tên bạn]
# Ngày: 2025

import numpy as np

def run_m1():
    """
    Chạy module M1 - Dự báo kinh tế
    Returns:
        dict: {
            'years': list các năm,
            'GDP': list GDP thực tế,
            'TFP': list TFP từng năm,
            'GDP_2025': GDP năm 2025,
            'GDP_2030': GDP dự báo 2030,
            'TFP_growth': tốc độ tăng TFP bình quân,
            'phan_ra': phân rã đóng góp tăng trưởng
        }
    """
    # Dữ liệu 2020-2025
    years = np.array([2020, 2021, 2022, 2023, 2024, 2025])
    Y = np.array([8044.4, 8487.5, 9513.3, 10221.8, 11511.9, 12847.6])  # GDP nghìn tỷ
    K = np.array([16500, 17800, 19600, 21300, 23500, 25900])           # Vốn
    L = np.array([53.6, 50.5, 51.7, 52.4, 52.9, 53.4])                 # Lao động
    D = np.array([12.0, 12.7, 14.3, 16.5, 18.3, 19.5])                 # Kinh tế số
    AI = np.array([55.6, 60.2, 65.4, 67.0, 73.8, 80.1])                # DN số
    H = np.array([24.1, 26.1, 26.2, 27.0, 28.4, 29.2])                 # LĐ qua đào tạo

    alpha, beta, gamma, delta, theta = 0.33, 0.42, 0.10, 0.08, 0.07

    # Tính TFP
    A = Y / (K**alpha * L**beta * D**gamma * AI**delta * H**theta)

    # Dự báo GDP 2030
    K_2030 = K[-1] * (1.06)**5
    L_2030 = L[-1] * (1.06)**5
    A_2030 = A[-1] * (1.012)**5
    Y_2030 = A_2030 * (K_2030**alpha * L_2030**beta * 30**gamma * 100**delta * 35**theta)

    # Phân rã tăng trưởng
    logY, logK, logL = np.log(Y), np.log(K), np.log(L)
    logD, logAI, logH = np.log(D), np.log(AI), np.log(H)

    dlogY = np.diff(logY)
    dlogK = np.diff(logK)
    dlogL = np.diff(logL)
    dlogD = np.diff(logD)
    dlogAI = np.diff(logAI)
    dlogH = np.diff(logH)

    # Đóng góp từng yếu tố (trung bình 2021-2025)
    phan_ra = {
        'Vốn (K)': float((alpha * dlogK).mean() * 100),
        'Lao động (L)': float((beta * dlogL).mean() * 100),
        'Số hóa (D)': float((gamma * dlogD).mean() * 100),
        'Năng lực AI': float((delta * dlogAI).mean() * 100),
        'Nhân lực số (H)': float((theta * dlogH).mean() * 100),
        'TFP': float((dlogY - (alpha*dlogK + beta*dlogL + gamma*dlogD + delta*dlogAI + theta*dlogH)).mean() * 100)
    }

    result = {
        'years': years.tolist(),
        'GDP': Y.tolist(),
        'TFP': A.tolist(),
        'GDP_2025': float(Y[-1]),
        'GDP_2030': float(Y_2030),
        'TFP_growth': float(((A[-1]/A[0])**(1/5)-1)*100),
        'phan_ra': phan_ra
    }
    return result

if __name__ == "__main__":
    print(run_m1())
