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
