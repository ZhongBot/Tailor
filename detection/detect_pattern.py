import cv2
from matplotlib import pyplot as plt
from preprocess import Preprocessor
from model import Entry, PatternType
from remove_outlier import percentile_based_outlier

preprocessor = Preprocessor()

# frame = cv2.imread("training_set/dot/tiny_dot_dark_blue_head.jpg")
# frame = cv2.imread("training_set/dot/8.jpg")
frame = cv2.imread("training_set/stripe/7.jpg")
# frame = cv2.imread("training_set/check/13.jpg")
# frame = cv2.imread("training_set/check/black_white_no_head.jpg")
# frame = cv2.imread("training_set/solid/green.jpg")
# frame = cv2.imread("training_set/solid/white_no_head.jpg")

size = 500
frame = preprocessor.resize(frame, size + 100)  # 100px padding for cropping
frame = preprocessor.square_crop(frame, size)

# edge detection
sobels = preprocessor.sobel(frame)
sobel_sums = preprocessor.reduce(sobels)

# remove outliers 95% percentile
outliers = percentile_based_outlier(sobel_sums.x, 95)
sobel_sums.x = [v for k, v in enumerate(sobel_sums.x) if outliers[k] == 0]
outliers = percentile_based_outlier(sobel_sums.y, 95)
sobel_sums.y = [v for k, v in enumerate(sobel_sums.y) if outliers[k] == 0]

# prepare for NN
pattern_type = PatternType.Stripe  # need to detemined by location of the image
entry = Entry(pattern_type, sobels, sobel_sums)

# add entry to training set

# output
plt.subplot(3, 2, 1), plt.imshow(frame, cmap="gray")
plt.title('Original'), plt.xticks([]), plt.yticks([])

color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv2.calcHist([frame], [i], None, [256], [0, 256])
    plt.subplot(3, 2, 2), plt.plot(histr, color=col)

plt.title('Histo'), plt.xticks([0, 256]), plt.yticks([]), plt.yscale('log')
plt.subplot(3, 2, 3), plt.imshow(sobels.x, cmap='gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(3, 2, 4), plt.imshow(sobels.y, cmap='gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.subplot(3, 2, 5), plt.plot(sobel_sums.x)
plt.title('Sum X'), plt.xticks([0, 500]), plt.yticks([0, max(sobel_sums.x)])
plt.subplot(3, 2, 6), plt.plot(sobel_sums.y)
plt.title('Sum Y'), plt.xticks([0, 500]), plt.yticks([0, max(sobel_sums.y)])

plt.show()
