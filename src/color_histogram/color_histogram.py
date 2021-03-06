import numpy as np
import cv2
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

colors = ((0, 0, 0, "검은색"), (255, 0, 0, "빨간색"), (0, 255, 0, "연두색"), (0, 0, 255, "파란색"),
          (255, 165, 0, "주황색"), (255, 255, 0, "노란색"), (128, 0, 128, "보라색"),
          (255, 51, 153, "분홍색"), (165, 42, 42, "갈색"), (255, 255, 255, "흰색"),
          (128, 128, 128, "회색"), (210, 180, 140, "황갈색"), (255, 255, 240, "상아색"),
          (0, 255, 255, "옥색"), (0, 0, 128, "남색"), (0, 128, 0, "초록색"),
          (128, 0, 0, "고동색"), (0, 128, 128, "암청색"), (0, 255, 255, "하늘색"))

def nearest_color(subjects, query):
    return min(subjects, key=lambda subjects: sum((s - q) ** 2 for s, q in zip(subjects, query)))

#TODO : 웹에서 이미지 경로로 바로 가져오는 기능
image = cv2.imread('C:/Users/Mando/Desktop/drunkendrive.jpg')  #현재는 파일 절대경로로 탐색

print(image.shape)

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

image = image.reshape((image.shape[0] * image.shape[1], 3))
print(image.shape)

# 임의로 설정한 히스토그램 군집의 갯수 k
k = 3
clt = KMeans(n_clusters = k)
clt.fit(image)

ary = []
for center in clt.cluster_centers_:
    #print(center)
    ary.append(center)

resultColorSet = []
for i in ary:
    resultColorSet.append(nearest_color(colors, i))

#print(ary)
print(resultColorSet)

def centroid_histogram(clt):
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()

    # return the histogram
    return hist

hist = centroid_histogram(clt)
print(hist)

def plot_colors(hist, centroids):
    # initialize the bar chart representing the relative frequency
    # of each of the colors
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0

    # loop over the percentage of each cluster and the color of
    # each cluster
    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        startX = endX

    # return the bar chart
    return bar

bar = plot_colors(hist, clt.cluster_centers_)

# show our color bart
#TODO : 데이터로 저장 or 시각화 컴포넌트에 넘겨주기 필요
plt.figure()
plt.axis("off")
plt.imshow(bar)
plt.show()

#DB로 보낼 것들
#ary(추출된 색상 RGB코드)
#hist(추출된 색상의 구성비율)
#resultColorSet(ary 각 값에 가까운 색상)