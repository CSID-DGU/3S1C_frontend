import numpy as np
import cv2
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

#TODO : 웹에서 이미지 경로로 바로 가져오는 기능
image = cv2.imread('C:/Users/Mando/Desktop/iutest.jpg')  #현재는 파일 절대경로로 탐색

print(image.shape)

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

image = image.reshape((image.shape[0] * image.shape[1], 3))
print(image.shape)

# 임의로 설정한 히스토그램 군집의 갯수 k
k = 3
clt = KMeans(n_clusters = k)
clt.fit(image)

for center in clt.cluster_centers_:
    print(center)

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