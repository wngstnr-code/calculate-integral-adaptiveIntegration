# Adaptive Integration - Calculate Integral

Program ini mengimplementasikan metode **Adaptive Integration** menggunakan `scipy.integrate.quad` untuk menghitung integral numerik dengan akurasi tinggi.

## 📋 Daftar Isi
- [Tentang Program](#tentang-program)
- [Prasyarat](#prasyarat)
- [Cara Clone Repository](#cara-clone-repository)
- [Instalasi](#instalasi)
- [Cara Menjalankan Program](#cara-menjalankan-program)
- [Output Program](#output-program)
- [Penjelasan Program](#penjelasan-program)

---

## 📝 Tentang Program

Program ini menghitung integral dari dua fungsi menggunakan metode adaptive integration:

1. **Integral 1**: ∫ cos(x) dx dari 0 sampai π/2
   - Hasil analitik: 1.0

2. **Integral 2**: ∫ x² dx dari 0 sampai 1
   - Hasil analitik: 1/3 ≈ 0.333...

---

## 🔧 Prasyarat

Sebelum menjalankan program, pastikan Anda memiliki:

- **Python 3.7 atau lebih baru**
- **Git** (untuk clone repository)
- **Terminal/Command Prompt**

### Cek versi Python:
```bash
python --version
# atau
python3 --version
```

---

## 📥 Cara Clone Repository

### 1. Buka Terminal/Command Prompt

**macOS/Linux:**
```bash
open Terminal
```

**Windows:**
```bash
Win + R
ketik: cmd
tekan Enter
```

### 2. Navigate ke folder yang diinginkan

```bash
cd /path/ke/folder/anda
# Contoh pada macOS:
cd ~/Documents
```

### 3. Clone repository

```bash
git clone https://github.com/wngstnr-code/calculate-integral-adaptiveIntegration.git
```

### 4. Masuk ke folder project

```bash
cd calculate-integral-adaptiveIntegration
```

---

## 🛠️ Instalasi

### 1. Buat Virtual Environment (Opsional tapi Disarankan)

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install numpy scipy
```

Atau jika ada file `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

## ▶️ Cara Menjalankan Program

### Jika menggunakan Virtual Environment:

**macOS/Linux:**
```bash
.venv/bin/python main.py
```

**Windows:**
```bash
.venv\Scripts\python main.py
```

### Jika tidak menggunakan Virtual Environment:

**macOS/Linux:**
```bash
python3 main.py
```

**Windows:**
```bash
python main.py
```

---

## 📊 Output Program

Ketika program dijalankan, output akan terlihat seperti ini:

```
-------------------------------------------
------------ Hasil Perhitungan ------------

Integral 1: ∫ cos(x) dx dari 0 sampai π/2
Hasil   : 0.9999999999999999
Error   : 1.1102230246251564e-14
Secara analitik hasilnya adalah 1.0
_________________________________________________

Integral 2: ∫ x^2 dx dari 0 sampai 1
Hasil   : 0.3333333333333333
Error   : 3.700743415417188e-15
Secara analitik hasilnya adalah 1/3 atau 0.333...
_________________________________________________
```

---

## 🎓 Penjelasan Program

### Fungsi Utama

**`scipy.integrate.quad`** digunakan untuk:
- Menghitung integral secara numerik
- Menggunakan adaptive quadrature
- Memberikan estimasi error otomatis

### Bagaimana Cara Kerjanya

1. Program mendefinisikan 2 fungsi (integrand):
   - `integrand1(x)` = cos(x)
   - `integrand2(x)` = x²

2. `quad()` menghitung integral dengan metode adaptive:
   - Secara otomatis menyesuaikan ukuran interval
   - Fokus pada daerah dengan perubahan fungsi besar
   - Menghentikan saat error mencapai toleransi

3. Hasilnya dibandingkan dengan nilai analitik

### Keunggulan Adaptive Integration

✅ **Presisi Tinggi**: Hasil sangat akurat dengan error < 1e-14
✅ **Efisien**: Evaluasi fungsi minimal
✅ **Otomatis**: Tidak perlu mengatur parameter rumit
✅ **Fleksibel**: Bisa handle berbagai jenis fungsi

---

## ❓ Troubleshooting

### Error: `python: command not found`
**Solusi**: Gunakan `python3` atau path lengkap ke python:
```bash
python3 main.py
```

### Error: `ModuleNotFoundError: No module named 'numpy'`
**Solusi**: Install dependencies:
```bash
pip install numpy scipy
```

### Error: `ModuleNotFoundError: No module named 'scipy'`
**Solusi**: Install scipy:
```bash
pip install scipy
```

---

## 📝 Lisensi

Project ini adalah bagian dari repository pembelajaran coding.

---

## 👤 Author

**Dibuat oleh**: wngstnr-code

---

## 💡 Tips Berguna

- Selalu gunakan virtual environment untuk menghindari konflik package
- Pastikan internet terhubung saat install dependencies pertama kali
- Jika mengalami masalah, coba uninstall dan install ulang dependencies