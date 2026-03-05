# Derin Sinir Ağları - Ödevler

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

* 60000 görüntü
* 10 farklı sınıf
* 32x32 piksel RGB görüntüler

Sınıflar:

* airplane
* automobile
* bird
* cat
* deer
* dog
* frog
* horse
* ship
* truck

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

### Program Kullanımı

Program çalıştırıldığında kullanıcıdan şu bilgiler istenir:

```
Mesafe seçin (L1 / L2):
k değerini giriniz:
Test örneği index giriniz (0-9999):
```

Program daha sonra:

* Seçilen görüntüyü gösterir
* Tahmin edilen sınıfı yazdırır
* Gerçek sınıfı yazdırır

### Klasör Yapısı

```
Derin-Sinir-Aglari
│
├── Odev-1
│     ├── knnAlgorithm.py
│     └── cifar-10-batches-py
```

### Amaç

Bu ödevin amacı **k-NN algoritmasının temel mantığını anlamak ve görüntü verileri üzerinde uygulamaktır.**
