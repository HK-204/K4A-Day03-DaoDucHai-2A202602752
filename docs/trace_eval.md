# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** Đào Đức Hải 
> **Mã Sinh Viên / Mã Học viên:** 2A202602752 
> **Chủ đề Lựa chọn:** Trợ lý đặt lịch tập Gym

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | 5 / 5 | Bài toán yêu cầu bóc tách intent rõ ràng: Đầu tiên phân tích thời gian/địa điểm, sau đó kiểm tra lịch trống, và cuối cùng tiến hành đặt lịch nếu thỏa mãn điều kiện |
| **2. Tool Interaction** | 5 / 5 | Bắt buộc kết nối với MCP Server để giao tiếp với các tool `check_gym_schedule` (tra cứu database phòng tập) và `book_gym_slot` (ghi nhận đặt chỗ) |
| **3. Dynamic Decision** | 5 / 5 | Hành động tiếp theo phụ thuộc hoàn toàn vào kết quả quan sát (Observation). Ví dụ: Nếu ca tập hết chỗ, Agent phải linh hoạt thông báo thay vì gọi tool đặt lịch |
| **4. Long Horizon Goal** | 4 / 5 | Agent phải duy trì mục tiêu hỗ trợ khách hàng xuyên suốt hội thoại, ghi nhớ các ràng buộc (khu vực, khung giờ) cho đến khi chốt giao dịch |
| **TỔNG ĐIỂM AGENTIC FIT** | **19 / 20** | *Đề tài hoàn toàn phù hợp để triển khai kiến trúc ReAct Agent (Agentic System)* |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
[
  {
    "step": 1,
    "query": "Tôi muốn kiểm tra xem ở phòng Gym Trâu Quỳ, Gia Lâm vào lúc 18:00 ngày 15/09/2026 có còn chỗ trống không?",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "check_gym_schedule",
    "arguments": {
      "location": "Trâu Quỳ, Gia Lâm",
      "preferred_time": "18:00",
      "date": "15/09/2026"
    },
    "observation": {
      "status": "SUCCESS",
      "is_available": true,
      "available_slots": 3,
      "trainer_on_duty": "Trần Văn B",
      "facility": "Trâu Quỳ, Gia Lâm",
      "message": "Phòng tập tại Trâu Quỳ, Gia Lâm còn 3 chỗ trống vào lúc 18:00 ngày 15/09/2026."
    },
    "latency_ms": 2301.38
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [x] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).
- **Tổng số Test Cases đã chạy thành công:** 5 / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** 4 lượt.
- **Kết quả đẩy Repo nộp bài:** [x] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
