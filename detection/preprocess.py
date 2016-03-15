import cv2
from model import Sobel, SobelSum


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
