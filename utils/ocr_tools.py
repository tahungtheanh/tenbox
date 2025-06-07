# ocr_tools.py – Trích xuất kích thước từ PDF bằng pdfplumber
import pdfplumber
import re

def extract_dimensions(file_path):
    print(f"📄 Đang OCR file: {file_path}...")
    with pdfplumber.open(file_path) as pdf:
        text = "\n".join(p.extract_text() or "" for p in pdf.pages)
    numbers = re.findall(r"(\d{2,4})\s*mm", text)
    return {"panel_data": list(map(int, numbers[:4])), "flap_height": int(numbers[4]) if len(numbers) > 4 else 150}
