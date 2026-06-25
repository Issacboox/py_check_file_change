# Excel Change Detection Tool

This script scans Excel files inside the `results/input` folder, detects files that contain added data, and copies them into the appropriate output folders.

## Prerequisites

Install Python:

https://www.python.org/downloads/

Recommended versions:

* Minimum: Python 3.10
* Recommended: Python 3.11 or 3.12

---

## Input Folder Structure

Before running the script, place the source files inside:

```text
results/
└── input/
    ├── 5607/
    │   ├── [5646] สตว/
    │   │   └── [5646] กวพ.xlsx
    │   └── [5647] ฝกพ/
    │       └── [5647] กวพ.xlsx
    │
    └── 10811/
        ├── [10672] กจส/
        │   └── [10672] กจส.xlsx
        └── [10811] รยก. ป/
            └── [10811] รยก. ป.xlsx
```

### Important

* Files must be placed inside the `results/input` folder before running the script.
* First-level folders must contain numbers only.
* Subfolders must follow the format:

```text
[xxxx] Folder Name
```

* Excel files must follow the format:

```text
[xxxx] filename.xlsx
```

---

## Setup

### macOS / Linux

```bash
cd project

python3 -m venv .venv
source .venv/bin/activate

python3 -m pip install -r requirements.txt
```

### Windows

```cmd
cd project

python -m venv .venv
.venv\Scripts\activate

python -m pip install -r requirements.txt
```

---

## Run

### macOS / Linux

```bash
python3 Python/check_file_changes.py
```

### Windows

```cmd
python Python\check_file_changes.py
```

---

## Output

All matching Excel files are copied to:

```text
results/output/
```

Example:

```text
results/
└── output/
    ├── 5646/
    │   └── [5646] กวพ.xlsx
    └── 10672/
        └── [10672] กจส.xlsx
```

---

## Changed Files

If a file contains added data, it will also be copied to:

```text
results/changes/
```

Example:

```text
results/
└── changes/
    ├── 5646/
    │   └── [5646] กวพ.xlsx
    └── 10672/
        └── [10672] กจส.xlsx
```

---

## Added Data Detection Logic

A file is considered changed when:

1. The first 5 rows are ignored.
2. Rows containing the word `ตัวอย่าง` are skipped.
3. If any subsequent row contains actual data, the file is marked as changed.

---

## JSON Result

The script outputs JSON containing only files that have added data.

Example:

```json
[
  {
    "original_file_path": "...",
    "copied_file_path": "...",
    "changed_file_path": "...",
    "extracted_folder_code": "5657",
    "added_data_found": true
  }
]
```




# Excel Change Detection Tool

เครื่องมือนี้ใช้สำหรับตรวจสอบไฟล์ Excel ว่ามีการกรอกข้อมูลเพิ่มเติมหรือไม่ โดยจะคัดลอกไฟล์ไปยังโฟลเดอร์ที่กำหนด และแสดงผลลัพธ์เป็น JSON

---

# ความต้องการของระบบ

ติดตั้ง Python จาก:

https://www.python.org/downloads/

เวอร์ชันที่แนะนำ:

* ขั้นต่ำ: Python 3.10
* แนะนำ: Python 3.11 หรือ 3.12

---

# โครงสร้างโฟลเดอร์

ก่อนรันโปรแกรม ให้นำไฟล์ต้นทางมาวางในโฟลเดอร์:

```text
results/
└── input/
```

ตัวอย่าง:

```text
results/
└── input/
    ├── 5607/
    │   ├── [5646] สตว/
    │   │   └── [5646] กวพ.xlsx
    │   └── [5647] ฝกพ/
    │       └── [5647] ฝกพ.xlsx
    │
    └── 10811/
        ├── [10672] กจส/
        │   └── [10672] กจส.xlsx
        └── [10811] รยก. ป/
            └── [10811] รยก. ป.xlsx
```

ข้อกำหนด:

* โฟลเดอร์ชั้นแรกต้องเป็นตัวเลขเท่านั้น เช่น `5607`, `10811`
* โฟลเดอร์ย่อยต้องอยู่ในรูปแบบ

```text
[xxxx] ชื่อโฟลเดอร์
```

* ไฟล์ Excel ต้องอยู่ในรูปแบบ

```text
[xxxx] ชื่อไฟล์.xlsx
```

---

# การติดตั้ง

## macOS / Linux

```bash
cd project

python3 -m venv .venv
source .venv/bin/activate

python3 -m pip install -r requirements.txt
```

## Windows

```cmd
cd project

python -m venv .venv
.venv\Scripts\activate

python -m pip install -r requirements.txt
```

---

# วิธีใช้งาน

## ขั้นตอนที่ 1

นำไฟล์ Excel ที่ต้องการตรวจสอบมาวางไว้ใน

```text
results/input
```

ตามโครงสร้างที่กำหนด

## ขั้นตอนที่ 2

รันโปรแกรม

### macOS / Linux

```bash
python3 Python/check_file_changes.py
```

### Windows

```cmd
python Python\check_file_changes.py
```

---

# ผลลัพธ์ที่ได้

## Output Folder

โปรแกรมจะคัดลอกไฟล์ Excel ที่ตรงตามเงื่อนไขไปยัง

```text
results/output
```

ตัวอย่าง:

```text
results/
└── output/
    ├── 5646/
    │   └── [5646] กวพ.xlsx
    └── 10672/
        └── [10672] กจส.xlsx
```

---

## Changes Folder

หากพบว่ามีการกรอกข้อมูลเพิ่มเติมในไฟล์ Excel โปรแกรมจะคัดลอกไฟล์ไปยัง

```text
results/changes
```

ตัวอย่าง:

```text
results/
└── changes/
    ├── 5646/
    │   └── [5646] กวพ.xlsx
    └── 10672/
        └── [10672] กจส.xlsx
```

---

# หลักการตรวจสอบข้อมูลที่เพิ่มเข้ามา

โปรแกรมจะพิจารณาว่าไฟล์มีการเปลี่ยนแปลงหรือไม่ตามเงื่อนไขดังนี้

1. ข้าม 5 แถวแรกของไฟล์
2. หลังจากนั้น ข้ามแถวที่มีคำว่า

```text
ตัวอย่าง
```

3. หากพบข้อมูลจริงในแถวถัดไป จะถือว่าไฟล์นั้นมีการกรอกข้อมูลเพิ่มเติม (Added Data)

---

# ตัวอย่างผลลัพธ์ JSON

โปรแกรมจะแสดงเฉพาะไฟล์ที่พบข้อมูลเพิ่มเติม

```json
[
  {
    "original_file_path": "/path/to/original.xlsx",
    "copied_file_path": "/path/to/output.xlsx",
    "changed_file_path": "/path/to/changes.xlsx",
    "extracted_folder_code": "5657",
    "added_data_found": true
  }
]
```

---

# หมายเหตุ

* โปรแกรมจะสร้างโฟลเดอร์ `results/input`, `results/output` และ `results/changes` ให้อัตโนมัติหากยังไม่มี
* หากไฟล์ Excel ไม่สามารถเปิดอ่านได้ โปรแกรมจะข้ามไฟล์นั้นและแสดงข้อความแจ้งเตือน
* ไฟล์ใน `output` และ `changes` อาจถูกเขียนทับได้หากมีชื่อไฟล์ซ้ำกัน
* แนะนำให้สำรองข้อมูลก่อนใช้งานกับไฟล์จริง
