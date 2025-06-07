# design_engineer.py – Thiết kế khuôn và tạo DXF, 3D
from utils.ocr_tools import extract_dimensions

def run_design_pipeline(task_id, file_path):
    state = {}
    state['dimensions'] = extract_dimensions(file_path)
    print(f"Thiết kế khuôn cho task {task_id} với kích thước: {state['dimensions']}")
    # Gọi các bước tiếp theo: tạo DXF, dựng 3D, kiểm tra lỗi
