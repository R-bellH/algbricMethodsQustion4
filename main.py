from PIL import Image
import numpy as np
image = Image.open("bffs.jpeg")
pix=np.array(image)
print(pix.shape)
print(pix)

for()

A = np.array([[3, 3, 2], [2,3,-2]])
# perform SVD
U, singular, V_transpose = np.linalg.svd(A, full_matrices=True, compute_uv=True)
