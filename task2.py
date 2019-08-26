import cv2
import numpy as np
correction_matrix = np.array([[1.18, -0.05, -0.13],
                             [-0.24, 1.29, -0.05],
                             [-0.18, -0.44, 1.62]])
print(correction_matrix)
img = cv2.imread('test1.bmp')
bilinear_img = cv2.resize(img, None, fx=10, fy=10, interpolation=cv2.INTER_LINEAR)
print(bilinear_img.shape)
slow_result = np.zeros_like(bilinear_img)
count = 0
for i in range(bilinear_img.shape[0]):
    for j in range(bilinear_img.shape[1]):
        count += 1
        print(count)
        # print(img[i, j, :])
        slow_result[i, j, :] = np.dot(correction_matrix, bilinear_img[i, j, :])
        # print(slow_result[i, j, :])

cv2.imwrite('test1_correctted.bmp', slow_result)
print(slow_result[10, 100])
