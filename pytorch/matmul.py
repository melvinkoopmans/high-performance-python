import time
import torch
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    cpu_result = []
    gpu_result = []
    sizes = np.logspace(1, 3.5, 40)

    for size in sizes:
        # Initialize an s x s matrix with random values.
        s = round(size)
        A = np.random.rand(s, s)
        B = np.random.rand(s, s)

        # Matrix multiply with NumPy using CPU
        start_time = time.time()
        np.matmul(A, B)
        end_time = time.time()
        cpu_result.append(end_time - start_time)

        # Initialize Tensor from data and move from system memory to GPU memory.
        A_tensor = torch.tensor(A).cuda()
        B_tensor = torch.tensor(B).cuda()
        start_time = time.time()
        torch.matmul(A_tensor, B_tensor)
        end_time = time.time()
        gpu_result.append(end_time - start_time)

    print(sizes)
    plt.plot(sizes, cpu_result, label='CPU')
    plt.plot(sizes, gpu_result, label='GPU')
    plt.legend()
    plt.show()




