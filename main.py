# main.py – Khởi chạy AI Agent TenBox
from modules.design_engineer import run_design_pipeline

if __name__ == "__main__":
    task_id = "demo_001"
    input_file = "data/samples/sample1.pdf"

    run_design_pipeline(task_id, input_file)
    print("\n🎯 Đã hoàn tất quy trình thiết kế khuôn!")
