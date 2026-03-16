# Derin Sinir Ağları

Bu repo, **Derin Sinir Ağları** dersi kapsamında yapılan ödevleri içermektedir.

## 📁 Ödev-1: CIFAR-10 k-NN Sınıflandırma

Bu ödevde **k-Nearest Neighbors (k-NN)** algoritması kullanılarak CIFAR-10 veri seti üzerinde görüntü sınıflandırması yapılmıştır.

### Kullanılan Teknolojiler

* Python
* NumPy
* Matplotlib

### Veri Seti

Bu projede **CIFAR-10** veri seti kullanılmıştır.

Veri seti özellikleri:

* 60000 görüntü, 10 farklı sınıf, 32x32 piksel RGB görüntüler

Sınıflar:

* airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck

### Programın Çalışma Mantığı

Program aşağıdaki adımlarla çalışır:

1. CIFAR-10 eğitim ve test verileri yüklenir
2. Kullanıcıdan mesafe türü seçmesi istenir

   * L1 (Manhattan)
   * L2 (Euclidean)
3. Kullanıcı **k değeri** girer
4. Test veri setinden bir görüntü seçilir
5. Bu görüntü ile tüm eğitim verileri arasındaki mesafeler hesaplanır
6. En yakın **k komşu** belirlenir
7. Çoğunluk oyu ile sınıf tahmini yapılır


### Klasör Yapısı

```
Derin-Sinir-Aglari
│
├── Odev-1
│     ├── knnAlgorithm.py
│     └── cifar-10-batches-py
```
## 📁 Ödev-2: Deep Learning Makale Sunumu ve CNN Matematiksel İşlemler

Bu ödev iki bölümden oluşmaktadır.

### 1️⃣ Deep Learning Makalesinin İncelenmesi ve Sunum Hazırlama

Bu bölümde **“An Introductory Review of Deep Learning for Prediction Models With Big Data”** adlı makale incelenmiş ve içeriği özetlenerek bir sunum hazırlanmıştır.

Sunumda ele alınan başlıca konular:

* Deep Learning ve Big Data
* Sinir ağlarının tarihsel gelişimi
* Yapay nöron modeli
* Sinir ağı mimarileri
* Convolutional Neural Networks (CNN)
* Deep Belief Networks (DBN)
* Autoencoder
* Long Short-Term Memory (LSTM)
* Deep Learning uygulamaları, avantajları ve sınırlamaları

### 2️⃣ CNN Slaytlarındaki Matematiksel İşlemlerin İncelenmesi

Bu bölümde **DL_L5_CNNs** ders slaytlarında bulunan matematiksel işlemler detaylı olarak araştırılmıştır. Özellikle **22. ve 29. sayfalarda** yer alan işlemler incelenmiştir.

İncelenen konular:

* CNN mimarisinde **Stride ve Padding**
* Padding işlemi ile giriş matrisinin yeni boyutunun hesaplanması
* Convolution sonrası **feature map (çıktı boyutu) hesaplama**
* **Softmax fonksiyonunun matematiksel yapısı**
* Softmax ile olasılık hesaplama örneği

### Klasör Yapısı

```
Derin-Sinir-Aglari
│
├── Odev-1
│     ├── knnAlgorithm.py
│     └── cifar-10-batches-py
│
├── Odev-2
│     ├── makaleSunumu.pptx
│     ├── CNN_odev.pdf

```
