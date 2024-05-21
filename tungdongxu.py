import random
# Cần cài đặt keyboard : pip install keyboard
# Danh sách câu hỏi (20 câu hỏi ví dụ)
questions = [
    "Trong thời gian gần đây, bạn có thường xuyên cảm thấy buồn bã hoặc chán nản không?",
    "Bạn có cảm thấy mình là gánh nặng cho người khác, gia đình, bàn bè hay xã hội không?",
    "Bạn có bao giờ nghĩ mình nên ở một mình hay làm việc, vui chơi một mình thay vì cùng người khác?",
    "Bạn có cảm thấy khó kiểm soát những lo lắng, tâm trạng của mình không?",
    "Bạn có thường xuyên có những cơn hoảng loạn hoặc sợ hãi không rõ lý do không?",
    "Bạn có hay so sánh bản thân với người khác và cảm thấy mình kém cỏi hơn không?",
    "Bạn có cảm thấy tội lỗi hoặc tự trách mình về những sai lầm trong quá khứ hay bản thân ở hiện tại không?",
    "Bạn có dễ nổi nóng hoặc mất bình tĩnh dạo này không?",
    "Bạn có cảm thấy khó kiểm soát cơn giận của mình không?",
    "Bạn có cảm thấy tính tình hay tâm trạng bạn không ổn, và dễ thay đổi không ở dạo gần đây không?",
    "Bạn có thường xuyên có những suy nghĩ tiêu cực về bản thân, cuộc sống hoặc tương lai không?",
    "Bạn có bao giờ nghĩ về cái chết hoặc tự tử không?",
    "Bạn có cảm thấy cuộc sống không còn ý nghĩa gì nữa không?",
    "Bạn có cảm thấy bị ám ảnh bởi những suy nghĩ tiêu cực không?",
    "Bạn có gặp khó khăn trong việc đi vào giấc ngủ hoặc duy trì giấc ngủ không?",
    "Giấc ngủ của bạn có sâu và giúp bạn cảm thấy nghỉ ngơi không?",
    "Bạn có sử dụng thuốc ngủ hoặc các chất hỗ trợ giấc ngủ khác không?",
    "Bạn có cảm thấy chán ăn hoặc không thấy hứng thú với thức ăn không?",
    "Bạn có cảm thấy muốn ở một mình và tránh tiếp xúc với người khác không?",
    "Bạn có cảm thấy mất hứng thú với những hoạt động mà trước đây bạn từng yêu thích không?"
]

# Hàm để tung đồng xu
def flip_coin():
    return random.choice(["Ngửa", "Sấp"])

# Hàm để hỏi khách hàng và thu thập câu trả lời
def collect_answers(questions):
    answers = []
    print("\nNếu mặt Ngửa thì khách hàng trả lời thật")
    for question in questions:
        print(f"{question} (YES/NO): ", end="")
        a = flip_coin()
        print("Đồng xu là mặt: ",a)
        if a == "Ngửa":
            answer = input("Nhập đáp án")
        elif(flip_coin() == "Ngửa"):
            answer = "YES"
        else:
            answer = "NO"
        answers.append(answer.strip().upper())
    return answers

# Thu thập câu trả lời từ khách hàng
customer_answers = collect_answers(questions)

if customer_answers:
    # Hiển thị câu hỏi và câu trả lời thu thập được
    for question, answer in zip(questions, customer_answers):
        print(f"Câu hỏi: {question}")
        print(f"Câu trả lời: {answer}")

    # Thực hiện phân tích và dự đoán bệnh trầm cảm (ví dụ đơn giản)
    def predict_depression(answers):
        # Giả sử nếu có hơn 10 câu trả lời "YES" thì có nguy cơ trầm cảm
        yes_count = answers.count("YES")
        if yes_count == 10:
            print("Có nguy cơ bệnh trầm cảm.")
        elif(yes_count > 10): 
            print("Trầm cảm ở mức độ nặng")   
        else:
            print("Không có nguy cơ bệnh trầm cảm.")
    # Thực hiện dự đoán
    predict_depression(customer_answers)
else:
    print("Không thu thập đủ dữ liệu do hủy bỏ.")