# Eksperimen Dataset & Data Preprocessing  
## Breast Cancer Dataset

Repository ini dibuat untuk memenuhi **Kriteria 1: Eksperimen Dataset & Data Preprocessing**  
pada submission **Membangun Sistem Machine Learning (MSML)**.

Pada tahap ini dilakukan proses:
- Pemilihan dataset
- Exploratory Data Analysis (EDA)
- Data preprocessing
- Otomatisasi preprocessing menggunakan script Python
- Workflow CI untuk menjalankan preprocessing secara otomatis

---

## 📁 Struktur Repository
```bash
Eksperimen_SML_DiahAyu
├── namadataset_raw
│ └── breast_cancer_raw.csv
├── preprocessing
│ ├── Eksperimen_DiahAyu.ipynb
│ ├── automate_DiahAyu.py
│ ├── breast_cancer_preprocessing
│ └── requirements.txt
├── .github
│ └── workflows
│ └── preprocessing.yml
└── README.md
```


---

## 📊 Dataset

- **Nama Dataset:** Breast Cancer Dataset
- **Sumber:** Scikit-learn (Breast Cancer Wisconsin Dataset)
- **Tipe Data:** Tabular
- **Task:** Classification
- **Target:** Diagnosis kanker payudara (Benign / Malignant)

Dataset disimpan dalam bentuk **file CSV** dan ditempatkan langsung pada folder: namadataset_raw/breast_cancer_raw.csv


---

## 🔍 Exploratory Data Analysis (EDA)

EDA dilakukan di dalam notebook: preprocessing/Eksperimen_DiahAyu.ipynb

Tahapan EDA meliputi:
- Pemeriksaan struktur data
- Statistik deskriptif
- Distribusi label target
- Pemeriksaan missing values
- Analisis fitur numerik

---

## 🧹 Data Preprocessing

Tahapan preprocessing yang dilakukan:
1. Pemisahan fitur dan target
2. Encoding label target
3. Normalisasi fitur numerik
4. Split data menjadi data latih dan data uji
5. Penyimpanan dataset hasil preprocessing

Hasil preprocessing digunakan sebagai input untuk tahap modelling (Kriteria 2).

---

## ⚙️ Automasi Preprocessing

Proses preprocessing diotomatisasi menggunakan script: preprocessing/automate_DiahAyu.py


Script ini bertugas untuk:
- Membaca dataset mentah
- Melakukan preprocessing
- Menyimpan dataset hasil preprocessing

---

## 🔄 Workflow CI – Preprocessing

Workflow CI dibuat menggunakan **GitHub Actions** untuk menjalankan preprocessing secara otomatis.

Workflow akan ter-trigger ketika:
- Terjadi push ke branch `main`
- Workflow dijalankan secara manual (`workflow_dispatch`)

Lokasi workflow: .github/workflows/preprocessing.yml


---

## 📦 Dependency

Library yang digunakan tercantum pada file: preprocessing/requirements.txt
Beberapa library utama:
- pandas
- numpy
- scikit-learn

---




