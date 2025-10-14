import numpy as np

# build big matrix
A = np.random.rand(20, 20)

print(f'A: {A}')

sample = np.random.choice(A.shape[0], size=5, replace=True)

print(f'sample: {A[np.random.choice(A.shape[0], size=2, replace=True), :]}')