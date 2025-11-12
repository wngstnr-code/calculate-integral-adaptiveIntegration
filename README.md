# Adaptive Integration - Simpson's Rule Calculator

Program ini mengimplementasikan metode **Adaptive Integration** menggunakan **Simpson's Rule** untuk menghitung integral numerik dengan akurasi tinggi. Program dilengkapi dengan menu interaktif, tabel nilai fungsi, dan error handling yang baik.

## 📋 Daftar Isi
- [Tentang Program](#tentang-program)
- [Fitur](#fitur)
- [Prasyarat](#prasyarat)
- [Cara Clone Repository](#cara-clone-repository)
- [Instalasi Dependencies](#instalasi-dependencies)
- [Cara Menjalankan Program](#cara-menjalankan-program)
- [Penggunaan Program](#penggunaan-program)
- [Penjelasan Program](#penjelasan-program)
- [Troubleshooting](#troubleshooting)

---

## 📝 Tentang Program

Program ini adalah kalkulator integral adaptif yang menggunakan **Simpson's Rule** untuk menghitung integral numerik dengan akurasi tinggi. Program menyediakan:

1. **Menu Interaktif**: Interface user-friendly dengan loop menu
2. **Opsi Pre-built**: Integral cos(x) dan x²
3. **Custom Input**: Masukkan fungsi dan batas integral sendiri
4. **Tabel Nilai**: Menampilkan nilai f(x) pada berbagai titik
5. **Error Handling**: Validasi input yang robust

---

## ✨ Fitur

✅ **Simpson's Rule**: Metode numerik akurat dengan adaptive recursion
✅ **Menu Loop**: Interface interaktif yang user-friendly
✅ **Value Table**: Tabel nilai fungsi f(x) di berbagai titik
✅ **Custom Input**: Support untuk berbagai fungsi matematika
✅ **Math Context**: Support untuk fungsi math lengkap (sin, cos, tan, sqrt, exp, log, dll)
✅ **Error Handling**: Validasi input yang komprehensif
✅ **Logout Option**: Exit program dengan aman

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

Program ini hanya memerlukan standard library Python (math module). Tidak perlu install package tambahan!

```bash
# Program langsung bisa dijalankan - tidak perlu install apapun
# Ini adalah keuntungan menggunakan built-in math module!
```

---

## ▶️ Cara Menjalankan Program

### Dengan Virtual Environment (Recommended):

**macOS/Linux:**
```bash
.venv/bin/python main.py
```

**Windows:**
```bash
.venv\Scripts\python main.py
```

### Tanpa Virtual Environment:

**macOS/Linux:**
```bash
python3 main.py
```

**Windows:**
```bash
python main.py
```

---

## 💡 Penggunaan Program

### Menu Utama

Ketika program dijalankan, akan muncul menu utama:

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

## 🎓 Penjelasan Program

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

### Keunggulan Program Ini

✅ **Akurasi Tinggi**: Simpson's Rule + adaptive recursion (default tol=1e-6)
✅ **User-friendly**: Menu loop dengan input validation
✅ **Informatif**: Tabel nilai membantu visualisasi fungsi
✅ **Fleksibel**: Support hampir semua fungsi matematika
✅ **Robust**: Error handling untuk invalid input
✅ **Efficient**: Adaptive approach hanya detail di area yang perlu
✅ **No Dependencies**: Hanya menggunakan standard library Python

---

## 📊 Contoh Grafik Output

Program akan menampilkan grafik dengan:
- **Kurva biru**: Fungsi f(x)
- **Area shading**: Area integral (dari a sampai b)
- **Garis merah putus**: Batas bawah (a)
- **Garis hijau putus**: Batas atas (b)
- **Grid**: Untuk membantu membaca nilai

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

Program ini hanya menggunakan **standard library Python**, tidak memerlukan package eksternal!

**Keuntungan:**
- ✅ Bisa langsung dijalankan
- ✅ Tidak perlu install package
- ✅ Lebih ringan dan cepat
- ✅ Tidak ada dependency issues

---

## 💡 Tips Berguna

- 🎯 Gunakan menu 1 dan 2 untuk test sebelum custom input
- 📊 Tabel nilai berguna untuk debug fungsi
- 🔍 Untuk fungsi kompleks, coba bounds yang lebih kecil dulu
- � Pastikan input bounds memenuhi domain fungsi
- 🐛 Jika hasil tidak masuk akal, lihat tabel nilai untuk debug
- 🔄 Gunakan Option 4 untuk exit program dengan aman

---

## 📚 Referensi Matematika

**Simpson's Rule**: https://en.wikipedia.org/wiki/Simpson%27s_rule
**Numerical Integration**: https://en.wikipedia.org/wiki/Numerical_integration
**Adaptive Quadrature**: https://en.wikipedia.org/wiki/Adaptive_quadrature

---

## 📝 Lisensi

Project ini adalah bagian dari repository pembelajaran coding.

---

## 👤 Author

**Dibuat oleh**: wngstnr-code