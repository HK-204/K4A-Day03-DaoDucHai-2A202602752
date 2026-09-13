"""
TOOL DEFINITIONS & EXECUTION BACKEND
Mã nguồn chứa danh sách Tool Schemas (JSON Schema) và Execution Layer phục vụ cho MCP Server.
(Đã tùy biến cho Đề tài: Trợ lý đặt lịch tập Gym)
"""

import json
from typing import Dict, Any

# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA (TASK 1.2)
# ==============================================================================

TOOLS_SCHEMA = [
    # Tool 1: Kiểm tra lịch trống của phòng Gym
    {
        "name": "check_gym_schedule",
        "description": "Kiểm tra xem phòng gym có còn chỗ trống trong khung giờ cụ thể không.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "Khu vực phòng tập, ví dụ: 'Trâu Quỳ, Gia Lâm'"
                },
                "date": {
                    "type": "string",
                    "description": "Ngày tập, ví dụ: '15/09/2026'"
                },
                "preferred_time": {
                    "type": "string",
                    "description": "Giờ muốn tập, ví dụ: '18:00'"
                }
            },
            "required": ["location", "date", "preferred_time"]
        }
    },
    
    # Tool 2: Đặt lịch tập
    {
        "name": "book_gym_slot",
        "description": "Thực hiện đặt chỗ phòng gym sau khi đã kiểm tra lịch trống thành công.",
        "parameters": {
            "type": "object",
            "properties": {
                "user_name": {
                    "type": "string",
                    "description": "Tên người đặt lịch"
                },
                "location": {
                    "type": "string",
                    "description": "Khu vực phòng tập"
                },
                "date": {
                    "type": "string",
                    "description": "Ngày tập"
                },
                "time": {
                    "type": "string",
                    "description": "Giờ tập"
                }
            },
            "required": ["user_name", "location", "date", "time"]
        }
    }
]

# ==============================================================================
# 2. MÔ PHỎNG DỮ LIỆU & HÀM THỰC THI TOOL (EXECUTION LAYER)
# ==============================================================================

MOCK_GYM_DATABASE = {
    "Trâu Quỳ, Gia Lâm": {
        "is_open": True,
        "trainer": "HLV Trần Văn B",
        "capacity_left": 3
    }
}

def execute_check_gym_schedule(location: str, date: str, preferred_time: str) -> str:
    """Thực thi kiểm tra lịch trống phòng gym"""
    # Dùng logic if-in để nhận diện linh hoạt "Trâu Quỳ"
    if "Trâu Quỳ" in location or "Gia Lâm" in location:
        return json.dumps({
            "status": "SUCCESS",
            "is_available": True,
            "available_slots": 3,
            "trainer_on_duty": "Trần Văn B",
            "facility": location,
            "message": f"Phòng tập tại {location} còn 3 chỗ trống vào lúc {preferred_time} ngày {date}."
        }, ensure_ascii=False)
    else:
        return json.dumps({
            "status": "NOT_FOUND",
            "is_available": False,
            "message": f"Xin lỗi, hiện tại không tìm thấy phòng tập hoặc đã hết chỗ ở khu vực '{location}'."
        }, ensure_ascii=False)

def execute_book_gym_slot(user_name: str, location: str, date: str, time: str) -> str:
    """Thực thi đặt lịch tập"""
    booking_id = f"GYM-{date.replace('/','')}-8821"
    return json.dumps({
        "status": "SUCCESS",
        "booking_id": booking_id,
        "user_name": user_name,
        "datetime": f"{time} {date}",
        "location": location,
        "message": f"Tuyệt vời! Đã đặt lịch thành công cho {user_name} tại {location} lúc {time} ngày {date}. Mã đặt chỗ của bạn là {booking_id}."
    }, ensure_ascii=False)

# Router gọi tool thực tế
TOOL_ROUTER = {
    "check_gym_schedule": execute_check_gym_schedule,
    "book_gym_slot": execute_book_gym_slot
}

def dispatch_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
    """Hàm trung chuyển thực thi tool"""
    if tool_name in TOOL_ROUTER:
        try:
            return TOOL_ROUTER[tool_name](**arguments)
        except Exception as e:
            return json.dumps({"status": "EXECUTION_ERROR", "error": str(e)}, ensure_ascii=False)
    return json.dumps({"status": "UNKNOWN_TOOL", "error": f"Tool '{tool_name}' không tồn tại!"}, ensure_ascii=False)