import numpy as np
import pickle
import matplotlib.pyplot as plt

print("CIFAR-10 verileri okunuyor...")

# CIFAR dosyasını okuyan yardımcı kısım
def read_batch(path):
    with open(path, 'rb') as file:
        content = pickle.load(file, encoding='bytes')
        images = content[b'data']
        labels = content[b'labels']
    return images, labels


# Eğitim verilerini yükleme
train_images = []
train_labels = []

for batch_no in range(1, 6):
    data, label = read_batch("cifar-10-batches-py/data_batch_" + str(batch_no))
    train_images.append(data)
    train_labels.extend(label)

train_images = np.concatenate(train_images)
train_labels = np.array(train_labels)

# Test verisi
test_images, test_labels = read_batch("cifar-10-batches-py/test_batch")

print("Veriler başarıyla yüklendi.")

# Kullanıcıdan parametreleri alma
metric = input("Mesafe türü seçin (L1 / L2): ")
k_value = int(input("k değeri giriniz: "))
test_index = int(input("Test görüntüsü indexi (0-9999): "))

# Test görüntüsü
sample = test_images[test_index]

# Görüntüyü ekranda gösterme
image = sample.reshape(3, 32, 32).transpose(1, 2, 0)

plt.imshow(image)
plt.title("Seçilen Test Görüntüsü")
plt.axis("off")
plt.show()

distance_list = []

# Eğitim verileri ile mesafe hesaplama
for i in range(len(train_images)):

    if metric == "L1":
        distance = np.sum(np.abs(train_images[i] - sample))

    elif metric == "L2":
        distance = np.sqrt(np.sum((train_images[i] - sample) ** 2))

    else:
        print("Hatalı mesafe seçimi")
        exit()

    distance_list.append((distance, train_labels[i]))


# Mesafeye göre sıralama
distance_list = sorted(distance_list)

# En yakın k komşuyu seçme
nearest_neighbors = distance_list[:k_value]

vote_count = {}

# Oylama işlemi
for dist, label in nearest_neighbors:
    if label in vote_count:
        vote_count[label] += 1
    else:
        vote_count[label] = 1

# En çok oyu alan sınıf
prediction = max(vote_count, key=vote_count.get)

label_names = [
    "airplane",
    "automobile",
    "bird",
    "cat",
    "deer",
    "dog",
    "frog",
    "horse",
    "ship",
    "truck"
]

print("Tahmin edilen sınıf:", label_names[prediction])
print("Gerçek sınıf:", label_names[test_labels[test_index]])