import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import random

df = pd.read_csv("data.csv")
df.shape
df.columns
df.__dataframe__
df.head()

## Chương trình chính
def questions_random(data, so_luong=20):
  """
  Chọn ngẫu nhiên một số lượng câu hỏi từ DataFrame.

  Args:
    data: DataFrame chứa dữ liệu.
    so_luong: Số lượng câu hỏi cần chọn.

  Returns:
    Danh sách các câu hỏi được chọn ngẫu nhiên.
  """

  cau_hoi_ngau_nhien = random.sample(list(data['CÂU HỎI']), so_luong)
  return cau_hoi_ngau_nhien

# Đọc dữ liệu từ file CSV
data = pd.read_csv('data.csv')

# Chọn ngẫu nhiên 20 câu hỏi
cau_hoi_chon = questions_random(data, 20)

# Hàm để tung đồng xu
def flip_coin():
    return random.choice(["Ngửa", "Sấp"])
print("\nNếu mặt Ngửa thì khách hàng trả lời thật")
# Hàm để hỏi khách hàng và thu thập câu trả lời
def collect_answers(questions):
    answers = []
    for question in questions:
        print(f"{question} (YES/NO): ", end="")
        a = flip_coin()
        print("Đồng xu là mặt ",a)
        if a == "Ngửa":
            answer = input("Nhập đáp án (YES hoặc NO): ")
            while answer.upper() not in ["YES", "NO"]:
                print("Vui lòng nhập YES hoặc NO.")
                answer = input("Nhập lại đáp án (YES hoặc NO): ")
        elif(flip_coin() == "Ngửa"):
            answer = "YES"
        else:
            answer = "NO"
        answers.append(answer.strip().upper())
    return answers

# Thu thập câu trả lời từ khách hàng
customer_answers = collect_answers(cau_hoi_chon)

# Tạo DataFrame từ câu hỏi và câu trả lời
df = pd.DataFrame({'Câu hỏi': cau_hoi_chon, 'Câu trả lời': customer_answers})

# Tính toán số câu trả lời "YES"
so_cau_yes = df['Câu trả lời'].value_counts()['YES']

# Xếp loại trầm cảm
def xep_loai_tram_cam(so_cau_yes):
    if so_cau_yes >= 15:
        return "Nặng"
    elif so_cau_yes <= 14 | so_cau_yes >=8:
        return "Nhẹ"
    else:
        return "Bình thường"


loai_tram_cam = xep_loai_tram_cam(so_cau_yes)

# In kết quả
print("\nKết quả:")
print(f"Số câu trả lời 'YES': {so_cau_yes}")
print(f"Xếp loại trầm cảm: {loai_tram_cam}")

# Trực quan hóa dữ liệu
# Vẽ biểu đồ tròn thể hiện tỉ lệ câu trả lời YES/NO
labels = ['YES', 'NO']
sizes = [so_cau_yes, len(customer_answers) - so_cau_yes]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal') 
plt.title("Tỉ lệ câu trả lời 'YES' và 'NO'")
plt.show()

# Vẽ biểu đồ cột thể hiện số câu trả lời YES theo mức độ trầm cảm
unique_answers = list(set(customer_answers))
counts = [customer_answers.count(answer) for answer in unique_answers]
plt.bar(unique_answers, counts)
plt.title("Số câu trả lời 'YES' và 'NO'")
plt.show()
