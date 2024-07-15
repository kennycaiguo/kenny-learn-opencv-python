import numpy as np

with np.load('./knn_data.npz') as f:
    # print(f.files)
    print(f['train'])