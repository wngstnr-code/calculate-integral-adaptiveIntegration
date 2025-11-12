# Adaptive Integration - Simpson's Rule Calculator

Program ini mengimplementasikan metode **Adaptive Integration** menggunakan **Simpson's Rule** untuk menghitung integral numerik dengan akurasi tinggi, dilengkapi dengan visualisasi grafik.

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

Program ini adalah kalkulator integral adaptif yang menggunakan **Simpson's Rule** untuk menghitung integral numerik. Program menyediakan:

1. **Opsi Pre-built**: Integral cos(x) dan x²
2. **Custom Input**: Masukkan fungsi sendiri
3. **Visualisasi**: Grafik hasil integral dengan area shading

---

## ✨ Fitur

✅ **Simpson's Rule**: Metode numerik akurat dengan error control
✅ **Adaptive Recursion**: Otomatis menyesuaikan ketelitian pada area sulit
✅ **Visualisasi Grafik**: Matplotlib untuk visualisasi fungsi dan area integral
✅ **Custom Input**: Hitung integral dari fungsi apapun
✅ **User-friendly Menu**: Interface interaktif yang mudah digunakan

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

```bash
pip install numpy matplotlib
```

Atau install sekaligus dengan semua dependensi:
```bash
pip install -r requirements.txt
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

## � Penggunaan Program

### Menu Utama

Ketika program dijalankan, akan muncul menu:

```
1. Integral cos(x) from 0 to pi/2
2. Integral x^2 from 0 to 1
3. Custom Input

Select option (1/2/3):
```

### Option 1: Pre-built Integral (cos x)

```
Select option (1/2/3): 1
0.9999999999998333
[Grafik akan ditampilkan]
```

**Hasil**: Menghitung ∫cos(x)dx dari 0 sampai π/2
- Hasil analitik: **1.0**
- Hasil numerik: **0.9999999999998333** ✓

### Option 2: Pre-built Integral (x²)

```
Select option (1/2/3): 2
0.33333333333333
[Grafik akan ditampilkan]
```

**Hasil**: Menghitung ∫x²dx dari 0 sampai 1
- Hasil analitik: **1/3 ≈ 0.333...**
- Hasil numerik: **0.33333333333333** ✓

### Option 3: Custom Input

```
Select option (1/2/3): 3
Enter function (use np for numpy, e.g., np.sin(x) + x**2): np.sin(x)
Enter lower bound (a): 0
Enter upper bound (b): 3.14159

[Hasil integral akan ditampilkan]
[Grafik akan ditampilkan]
```

#### Contoh Fungsi yang Bisa Dimasukkan:
- `np.sin(x)` - Sinus
- `np.cos(x)` - Cosinus
- `np.tan(x)` - Tangen
- `np.exp(x)` - Eksponensial
- `np.sqrt(x)` - Akar kuadrat
- `x**2` - x pangkat 2
- `x**3 + 2*x` - Polynomial
- `np.sin(x) + x**2` - Kombinasi fungsi

---

## 🎓 Penjelasan Program

### Fungsi Utama

1. **`simpson(f, a, b)`**
   - Menghitung integral menggunakan satu interval Simpson's Rule
   - Formula: (h/3) × [f(a) + 4×f(c) + f(b)] dimana c = (a+b)/2

2. **`adaptive_recursive(f, a, b, eps, whole)`**
   - Rekursi adaptif untuk meningkatkan akurasi
   - Membagi interval jika error masih besar
   - Menggunakan Richardson extrapolation untuk estimasi error

3. **`adaptive_integration(f, a, b, tol=1e-6)`**
   - Wrapper function untuk adaptive integration
   - Default tolerance: 1e-6

4. **`plot_integral(f, a, b, title)`**
   - Menampilkan grafik fungsi
   - Shading area di bawah kurva
   - Menandai batas a dan b dengan garis vertikal

### Bagaimana Simpson's Rule Bekerja

**Simpson's Rule** adalah metode numerik yang menggunakan parabola untuk aproksimasi fungsi.

Formula untuk 1 interval:
$$I ≈ \frac{h}{3}[f(a) + 4f(c) + f(b)]$$

dimana:
- $h = (b-a)/2$ (lebar interval setengah)
- $c = (a+b)/2$ (titik tengah)

**Adaptive Approach**:
1. Hitung integral dengan 1 interval
2. Hitung dengan 2 interval (dibagi di tengah)
3. Bandingkan error
4. Jika error besar, rekursi untuk setiap bagian
5. Gabungkan hasilnya

### Keunggulan Program Ini

✅ **Akurasi Tinggi**: Simpson's Rule + adaptive recursion
✅ **Otomatis**: Tidak perlu tuning parameter banyak
✅ **Visualisasi**: Grafik membantu memahami integral
✅ **Fleksibel**: Bisa handle hampir semua fungsi
✅ **User-friendly**: Menu interaktif yang mudah

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

### Error: `ModuleNotFoundError: No module named 'numpy'`
**Solusi**: Install numpy:
```bash
pip install numpy
```

### Error: `ModuleNotFoundError: No module named 'matplotlib'`
**Solusi**: Install matplotlib:
```bash
pip install matplotlib
```

### Error: `Error in input format` pada Custom Input
**Solusi**: 
- Pastikan syntax function benar
- Gunakan `np.` untuk fungsi numpy (contoh: `np.sin(x)`, bukan `sin(x)`)
- Gunakan `np.pi` untuk π
- Contoh yang benar: `np.sin(x) + x**2`

### Grafik tidak muncul
**Solusi**: 
- Pastikan display support (jika via SSH, gunakan X11 forwarding)
- Atau save grafik dengan memodifikasi `plt.show()` → `plt.savefig('output.png')`

---

## � Requirements.txt

```
numpy>=1.20.0
matplotlib>=3.3.0
```

---

## 💡 Tips Berguna

- 🎯 Selalu gunakan virtual environment untuk project isolation
- 📊 Custom input sangat powerful - jangan takut bereksperimen
- 🔍 Jika tolerance 1e-6 terlalu kasar, Anda bisa modify kode untuk tolerance lebih ketat
- 📈 Visualisasi grafik membantu debug jika hasil tidak sesuai ekspektasi

---

## 📝 Lisensi

Project ini adalah bagian dari repository pembelajaran coding.

---

## 👤 Author

**Dibuat oleh**: wngstnr-code