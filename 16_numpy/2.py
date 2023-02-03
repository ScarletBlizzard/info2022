import imageio
import numpy as np

img = imageio.imread("image.png")
weights = np.array([0.299, 0.587, 0.114, 1])
imageio.imwrite("image_gray.png", img.dot(weights))
