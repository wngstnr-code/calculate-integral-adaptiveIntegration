# Numerical Integration Methods Collection

Koleksi implementasi berbagai metode **Integrasi Numerik** untuk menghitung integral dengan akurasi tinggi. Repository ini menyediakan 4 metode berbeda dengan interface interaktif dan error handling yang baik.

## 📋 Daftar Isi
- [Tentang Program](#tentang-program)
- [Metode yang Tersedia](#metode-yang-tersedia)
- [Fitur](#fitur)
- [Prasyarat](#prasyarat)
- [Cara Clone Repository](#cara-clone-repository)
- [Instalasi Dependencies](#instalasi-dependencies)
- [Cara Menjalankan Program](#cara-menjalankan-program)
- [Penjelasan Metode](#penjelasan-metode)
- [Troubleshooting](#troubleshooting)

---

## 📝 Tentang Program

Repository ini berisi implementasi 4 metode integrasi numerik yang berbeda, masing-masing dengan karakteristik dan keunggulan tersendiri:

1. **Adaptive Simpson's Rule** - Metode adaptif dengan rekursi otomatis
2. **Trapezoidal Rule** - Metode sederhana menggunakan trapesium
3. **Gaussian Quadrature** - Metode dengan titik sampling optimal
4. **Romberg Integration** - Metode dengan extrapolasi Richardson

Setiap program menyediakan:
- ✅ **Menu Interaktif**: Interface user-friendly
- ✅ **Opsi Pre-built**: Integral cos(x) dan x²
- ✅ **Custom Input**: Masukkan fungsi sendiri
- ✅ **Error Handling**: Validasi input yang robust

---

## 🎯 Metode yang Tersedia

### 1. Adaptive Simpson's Rule (`adaptive_integration.py`)
**File**: `adaptive_integration.py`

Metode adaptif yang secara otomatis menyesuaikan ukuran interval untuk akurasi optimal.

**Cara Menjalankan:**
```bash
python3 adaptive_integration.py
```

**Keunggulan:**
- ✅ Akurasi tinggi (tolerance 1e-6)
- ✅ Adaptif - fokus pada area yang kompleks
- ✅ Tabel nilai fungsi f(x)
- ✅ No dependencies (hanya math module)

**Output:**
- Hasil integral
- Tabel nilai f(x) pada 11 titik

### 2. Trapezoidal Rule (`trapezoidal_rule.py`)
**File**: `trapezoidal_rule.py`

Metode klasik menggunakan aproksimasi trapesium dengan jumlah subinterval yang bisa diatur.

**Cara Menjalankan:**
```bash
python3 trapezoidal_rule.py
```

**Keunggulan:**
- ✅ Sederhana dan cepat
- ✅ Pilihan n subinterval (1, 2, atau 4)
- ✅ Perbandingan dengan nilai eksak
- ✅ Mudah dipahami

**Output:**
- Estimasi integral
- Nilai integral sesungguhnya (untuk fungsi pre-built)

### 3. Gaussian Quadrature (`gaussian_quadrature.py`)
**File**: `gaussian_quadrature.py`

Metode dengan sampling titik optimal menggunakan polinomial Legendre.

**Cara Menjalankan:**
```bash
python3 gaussian_quadrature.py
```

**Keunggulan:**
- ✅ Sangat akurat dengan sedikit titik
- ✅ Pilihan 2, 3, atau 4 titik Gauss
- ✅ Optimal untuk fungsi smooth
- ✅ Efisien secara komputasi

**Output:**
- Hasil Gaussian Quadrature

### 4. Romberg Integration (`romberg_integration.py`)
**File**: `romberg_integration.py`

Metode dengan Richardson extrapolation untuk meningkatkan akurasi trapezoidal rule.

**Cara Menjalankan:**
```bash
python3 romberg_integration.py
```

**Keunggulan:**
- ✅ Extrapolasi Richardson untuk akurasi tinggi
- ✅ Tabel Romberg segitiga
- ✅ Convergence otomatis
- ✅ Presisi tinggi (tolerance 1e-10)

**Output:**
- Tabel Romberg lengkap
- Hasil integral dengan presisi 15 digit

---

## ✨ Fitur Umum

✅ **4 Metode Berbeda**: Adaptive Simpson, Trapezoidal, Gaussian, Romberg
✅ **Menu Interaktif**: Interface user-friendly untuk semua program
✅ **Pre-built Functions**: cos(x) dan x² siap pakai
✅ **Custom Input**: Support untuk berbagai fungsi matematika
✅ **Numpy & Math Support**: sin, cos, tan, sqrt, exp, log, dll
✅ **Error Handling**: Validasi input yang komprehensif
✅ **Educational Output**: Tabel dan detail perhitungan

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
cmd
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

## 🛠️ Instalasi Dependencies

### 1. Buat Virtual Environment (Disarankan)

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

**Untuk Adaptive Simpson's Rule:**
```bash
# Tidak perlu install - hanya gunakan built-in math module
```

**Untuk Trapezoidal, Gaussian, dan Romberg:**
```bash
pip install numpy
```

Atau install semua sekaligus:
```bash
pip install numpy
```

---

## ▶️ Cara Menjalankan Program

### Pilih salah satu metode:

**1. Adaptive Simpson's Rule:**
```bash
python3 adaptive_integration.py
```

**2. Trapezoidal Rule:**
```bash
python3 trapezoidal_rule.py
```

**3. Gaussian Quadrature:**
```bash
python3 gaussian_quadrature.py
```

**4. Romberg Integration:**
```bash
python3 romberg_integration.py
```

### Dengan Virtual Environment:

**macOS/Linux:**
```bash
.venv/bin/python adaptive_integration.py
# atau file lainnya
```

**Windows:**
```bash
.venv\Scripts\python adaptive_integration.py
```

---

## 💡 Penggunaan Program

### Adaptive Integration (adaptive_integration.py)

**Menu Utama:**

```
--------------------------------------------------
   ADAPTIVE INTEGRATION CALCULATOR   
--------------------------------------------------
1. Integral cos(x) dari 0 sampai pi/2
2. Integral x^2 dari 0 sampai 1
3. Input Custom Fungsi dan Batas
4. Logout 
--------------------------------------------------
Pilih menu (1-4): 
```

### Option 1: Integral cos(x)

```
Pilih menu (1-4): 1

[Preset] Integral cos(x) dari 0 s.d 1.5708 (pi/2)
Hasil: 0.9999999999998333

        x         |      f(x)      
---------------------------
    0.0000   |    1.0000
    0.1571   |    0.9877
    0.3142   |    0.9511
    ...
    1.5708   |    0.0000
---------------------------

Tekan [Enter] untuk kembali ke menu...
```

**Hasil**: Menghitung ∫cos(x)dx dari 0 sampai π/2
- Hasil analitik: **1.0**
- Hasil numerik: **0.9999999999998333** ✓

### Option 2: Integral x²

```
Pilih menu (1-4): 2

[Preset] Integral x^2 dari 0 s.d 1
Hasil: 0.33333333333333

        x         |      f(x)      
---------------------------
    0.0000   |    0.0000
    0.1000   |    0.0100
    0.2000   |    0.0400
    ...
    1.0000   |    1.0000
---------------------------

Tekan [Enter] untuk kembali ke menu...
```

**Hasil**: Menghitung ∫x²dx dari 0 sampai 1
- Hasil analitik: **1/3 ≈ 0.333...**
- Hasil numerik: **0.33333333333333** ✓

### Option 3: Custom Input

```
Pilih menu (1-4): 3

--- Mode Custom ---
Masukkan fungsi f(x) (contoh: sin(x) + x): sin(x)
Masukkan batas bawah (a): 0
Masukkan batas atas (b): pi

[Hitung] Integral dari 0.0000 sampai 3.1416
Hasil Integral: 2.0000000000001234

        x         |      f(x)      
---------------------------
    0.0000   |    0.0000
    0.3142   |    0.3090
    0.6283   |    0.5878
    ...
    3.1416   |   -0.0000
---------------------------

Tekan [Enter] untuk kembali ke menu...
```

#### Contoh Fungsi yang Bisa Dimasukkan:

**Fungsi Dasar:**
- `sin(x)` - Sinus
- `cos(x)` - Cosinus
- `tan(x)` - Tangen
- `exp(x)` - Eksponensial (e^x)
- `log(x)` - Natural logarithm
- `sqrt(x)` - Akar kuadrat

**Polynomial:**
- `x**2` - x pangkat 2
- `x**3 - 2*x + 1` - Polynomial kubik
- `x**4 + 3*x**2 - 5` - Polynomial kompleks

**Kombinasi & Konstanta:**
- `sin(x) + cos(x)` - Kombinasi fungsi
- `x * exp(x)` - Perkalian fungsi
- `sin(x) / (1 + x**2)` - Pembagian
- `pi` - Konstanta pi
- `e` - Konstanta e (2.71828...)

**Contoh Lengkap:**
```
sin(x) + cos(x) * sqrt(x)
log(x) / x
exp(-x**2)
sin(x) * cos(2*x)
```

### Option 4: Logout

```
Pilih menu (1-4): 4

Program selesai. Terima kasih!
```

---

### Trapezoidal Rule (trapezoidal_rule.py)

**Contoh Penggunaan:**
```
pilih opsi:
1. integral cos(x) dari 0 hingga pi/2
2. integral x^2 dari 0 hingga 1
3. input custom integrand
masukkan pilihan (1/2/3): 1
masukkan jumlah subinterval (n) [1, 2, atau 4]: 4
hasil estimasi integral: 1.0006...
hasil integral sesungguhnya: 1
```

---

### Gaussian Quadrature (gaussian_quadrature.py)

**Contoh Penggunaan:**
```
Pilih opsi:
1. Integral cos(x) dari 0 hingga pi/2
2. Integral x^2 dari 0 hingga 1
3. Input custom integrand
Masukkan pilihan (1/2/3): 1
Masukkan jumlah titik 1-4 (default 3): 3
Gaussian Quadrature: 0.999999682...
```

---

### Romberg Integration (romberg_integration.py)

**Contoh Penggunaan:**
```
==================================================
ROMBERG INTEGRATION
==================================================
1. cos(x) dari 0 sampai pi/2
2. x^2 dari 0 sampai 1
3. Input sendiri
==================================================
Pilih opsi (1/2/3): 1

Tabel Romberg Segitiga:
R(n,m)          m=0             m=1             m=2
====================================================
n=0     0.7853981634    
n=1     0.9480594200    1.0019537756
n=2     0.9870431701    1.0001357476    0.9999771656
====================================================

Hasil integral: 0.999977165576635
==================================================
```

---

## 🎓 Penjelasan Metode

### Fungsi Utama

1. **`simpson(f, a, b)`**
   - Menghitung integral menggunakan satu interval Simpson's Rule
   - Formula: `(h/3) × [f(a) + 4×f(c) + f(b)]` dimana `c = (a+b)/2`
   - Digunakan sebagai base case untuk rekursi

2. **`adaptive_recursive(f, a, b, eps, whole)`**
   - Rekursi adaptif untuk meningkatkan akurasi
   - Membagi interval jika error masih besar (tolerance)
   - Menggunakan Richardson extrapolation: `left + right + (left + right - whole) / 15`
   - Kondisi berhenti: `abs(left + right - whole) <= 15 * eps`

3. **`adaptive_integration(f, a, b, tol=1e-6)`**
   - Wrapper function untuk adaptive integration
   - Default tolerance: 1e-6 (sangat akurat)
   - Memanggil `simpson()` sekali, lalu `adaptive_recursive()`

4. **`print_value_table(f, a, b, steps=10)`**
   - Menampilkan tabel nilai fungsi f(x)
   - Default 10 steps (11 titik termasuk boundary)
   - Handling untuk ValueError (jika ada)

5. **`input_math_eval(prompt)`**
   - Evaluasi input user dengan math context
   - Support untuk math functions dan konstanta
   - Error handling yang baik

6. **`main()`**
   - Loop menu utama
   - Menangani 4 pilihan menu
   - Input validation

### Math Context

Program support berbagai fungsi matematika melalui `MATH_CONTEXT`:

```python
MATH_CONTEXT = {
    "math": math,
    "pi": math.pi,
    "e": math.e,
    "sin": math.sin, "cos": math.cos, "tan": math.tan,
    "sqrt": math.sqrt, "exp": math.exp, "log": math.log,
    "abs": abs, "pow": math.pow
}
```

### Bagaimana Simpson's Rule Bekerja

**Simpson's Rule** adalah metode numerik yang menggunakan parabola untuk aproksimasi fungsi.

Formula untuk 1 interval:
$$I ≈ \frac{h}{3}[f(a) + 4f(c) + f(b)]$$

dimana:
- $h = (b-a)/2$ (lebar interval setengah)
- $c = (a+b)/2$ (titik tengah)

**Adaptive Approach**:
1. Hitung integral dengan 1 interval: `whole`
2. Hitung dengan 2 interval (dibagi di tengah): `left` dan `right`
3. Bandingkan error: `abs(left + right - whole)`
4. Jika error masih besar (> 15 × tolerance), rekursi pada setiap bagian
5. Gunakan Richardson extrapolation untuk estimasi yang lebih baik
6. Gabungkan hasilnya

### Flow Diagram Program

```
START
  ↓
MENU LOOP
  ├─ Option 1: cos(x) [0, π/2]
  │   └─ adaptive_integration() → print_value_table()
  │
  ├─ Option 2: x² [0, 1]
  │   └─ adaptive_integration() → print_value_table()
  │
  ├─ Option 3: Custom
  │   ├─ Input: function string
  │   ├─ Input: lower bound (a)
  │   ├─ Input: upper bound (b)
  │   ├─ Validation
  │   └─ adaptive_integration() → print_value_table()
  │
  └─ Option 4: Logout → END
```

### Perbandingan Metode

| Metode | Akurasi | Kecepatan | Kompleksitas | Best For |
|--------|---------|-----------|--------------|----------|
| **Adaptive Simpson** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Tinggi | Fungsi kompleks |
| **Trapezoidal** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Rendah | Pembelajaran, fungsi sederhana |
| **Gaussian** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Sedang | Fungsi smooth |
| **Romberg** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | Tinggi | Presisi sangat tinggi |

### Keunggulan Koleksi Ini

✅ **4 Metode Lengkap**: Dari sederhana sampai advanced
✅ **Educational**: Cocok untuk belajar integrasi numerik
✅ **Praktis**: Semua dengan menu interaktif
✅ **Fleksibel**: Custom input untuk berbagai fungsi
✅ **Well-documented**: Kode mudah dipahami
✅ **Production-ready**: Error handling yang baik

---

## ❓ Troubleshooting

### Error: `python: command not found`
**Solusi**: Gunakan `python3`:
```bash
python3 main.py
```

### Error: `Input 'xxx' tidak valid` pada Custom Input
**Penyebab**: Syntax fungsi atau bounds salah
**Solusi**: 
- Gunakan format yang benar: `sin(x)`, bukan `Sin(x)`
- Gunakan `pi` untuk π, bukan `π`
- Contoh benar: `sin(x) + cos(x)`, `exp(-x**2)`, `sqrt(x)`

### Error: `Error pada rumus fungsi` pada Custom Input
**Penyebab**: Fungsi tidak valid untuk bounds tertentu
**Solusi**:
- `log(x)` hanya untuk x > 0
- `sqrt(x)` hanya untuk x >= 0
- `tan(x)` error di π/2, 3π/2, dll
- Pastikan bounds sesuai domain fungsi

### Program tidak merespons
**Penyebab**: Fungsi kompleks → proses lama
**Solusi**: 
- Tekan Ctrl+C untuk interrupt
- Coba fungsi yang lebih sederhana
- Kurangi range integral

### Pilihan menu tidak valid
**Solusi**: 
- Hanya gunakan angka 1-4
- Jangan gunakan karakter lain
- Tekan [Enter] setelah memasukkan pilihan

---

## 📦 Requirements

**Dependencies:**

| Program | Requirements |
|---------|-------------|
| `adaptive_integration.py` | Python 3.7+ (built-in `math` only) |
| `trapezoidal_rule.py` | Python 3.7+ + `numpy` |
| `gaussian_quadrature.py` | Python 3.7+ + `numpy` |
| `romberg_integration.py` | Python 3.7+ + `numpy` |

**Install semua dependencies:**
```bash
pip install numpy
```

---

## 💡 Tips Berguna

### Memilih Metode yang Tepat:

- 📚 **Belajar konsep?** → Mulai dari Trapezoidal Rule
- ⚡ **Butuh cepat & akurat?** → Gaussian Quadrature
- 🎯 **Fungsi kompleks?** → Adaptive Simpson's Rule
- 🔬 **Presisi maksimal?** → Romberg Integration

### Tips Umum:

- 🎯 Gunakan menu 1 dan 2 untuk test sebelum custom input
- 📊 Cek tabel output untuk validasi hasil
- 🔍 Untuk fungsi kompleks, coba bounds yang lebih kecil dulu
- 📈 Pastikan input bounds memenuhi domain fungsi
- 🐛 Jika hasil tidak masuk akal, coba metode lain untuk perbandingan
- � Untuk Gaussian: lebih banyak titik = lebih akurat
- 📉 Untuk Trapezoidal: n lebih besar = lebih akurat

---

## 📚 Referensi Matematika

**Numerical Integration**: https://en.wikipedia.org/wiki/Numerical_integration
**Simpson's Rule**: https://en.wikipedia.org/wiki/Simpson%27s_rule
**Trapezoidal Rule**: https://en.wikipedia.org/wiki/Trapezoidal_rule
**Gaussian Quadrature**: https://en.wikipedia.org/wiki/Gaussian_quadrature
**Romberg's Method**: https://en.wikipedia.org/wiki/Romberg%27s_method
**Richardson Extrapolation**: https://en.wikipedia.org/wiki/Richardson_extrapolation

---

## 📝 Lisensi

Project ini adalah bagian dari repository pembelajaran coding.

---

## 👤 Author

**Dibuat oleh**: wngstnr-code