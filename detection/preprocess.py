import cv2
from model import Sobel, SobelSum, Entry


class Preprocessor():
    def resize(self, frame, size):
        # resize the image to have a fixed width
        ratio = float(size)/frame.shape[1]
        dim = (size, int(frame.shape[0] * ratio))
        frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
        return frame

    def square_crop(self, frame, size):
        # square crop the center of the image
        center = (len(frame)/2, len(frame[0])/2)
        frame = frame[center[0]-size/2:center[0]+size/2, center[1]-size/2:center[1]+size/2]
        return frame

    def sobel(self, frame):
        # convert to greyscale
        gr = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # blur
        blur = cv2.GaussianBlur(frame, (7, 7), 0)
        # edge detection (aka edge emphasis)
        sobelx = cv2.Sobel(blur, cv2.CV_8UC1, 1, 0, ksize=3)
        sobely = cv2.Sobel(blur, cv2.CV_8UC1, 0, 1, ksize=3)
        return Sobel(sobelx, sobely)

    def reduce(self, sobels):
        sumx = cv2.reduce(sobels.x, 0, cv2.REDUCE_SUM, dtype=cv2.CV_64F)
        sumx = [sum(v) for v in sumx[0]]
        sumy = cv2.reduce(sobels.y, 1, cv2.REDUCE_SUM, dtype=cv2.CV_64F)
        sumy = [sum(v[0]) for v in sumy]
        return SobelSum(sumx, sumy)

    def preprocess(self, pattern_type, filename):
        frame = cv2.imread(filename)

        size = 500
        frame = self.resize(frame, size + 100)  # 100px padding for cropping
        frame = self.square_crop(frame, size)

        # edge detection
        sobels = self.sobel(frame)
        sobel_sums = self.reduce(sobels)

        # remove outliers 95% percentile
        # figure out how to remove outliers without screwing up the image -- removed for now
        # outliers = percentile_based_outlier(sobel_sums.x, 95)
        # sobel_sums.x = [v for k, v in enumerate(sobel_sums.x) if outliers[k] == 0]
        # outliers = percentile_based_outlier(sobel_sums.y, 95)
        # sobel_sums.y = [v for k, v in enumerate(sobel_sums.y) if outliers[k] == 0]

        # prepare for NN
        entry = Entry(pattern_type, sobels, sobel_sums)

        # output
        # plt.subplot(3, 2, 1), plt.imshow(frame, cmap="gray")
        # plt.title('Original'), plt.xticks([]), plt.yticks([])

        # color = ('b', 'g', 'r')
        # for i, col in enumerate(color):
        #     histr = cv2.calcHist([frame], [i], None, [256], [0, 256])
        #     plt.subplot(3, 2, 2), plt.plot(histr, color=col)

        # plt.title('Histo'), plt.xticks([0, 256]), plt.yticks([]), plt.yscale('log')
        # plt.subplot(3, 2, 3), plt.imshow(sobels.x, cmap='gray')
        # plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
        # plt.subplot(3, 2, 4), plt.imshow(sobels.y, cmap='gray')
        # plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
        # plt.subplot(3, 2, 5), plt.plot(sobel_sums.x)
        # plt.title('Sum X'), plt.xticks([0, 500]), plt.yticks([0, max(sobel_sums.x)])
        # plt.subplot(3, 2, 6), plt.plot(sobel_sums.y)
        # plt.title('Sum Y'), plt.xticks([0, 500]), plt.yticks([0, max(sobel_sums.y)])

        # plt.show()

        return entry
