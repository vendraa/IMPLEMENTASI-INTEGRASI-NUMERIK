import time
import math

def f(x):
    return 4 / (1 + x**2)

def simpson_13(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n harus genap")
    h = (b - a) / n
    result = f(a) + f(b)

    for i in range(1, n, 2):
        result += 4 * f(a + i * h)
    for i in range(2, n, 2):
        result += 2 * f(a + i * h)

    result *= h / 3
    return result


nilai_N = [10, 100, 1000, 10000]
referensi_phi = 3.14159265358979323846

for N in nilai_N:
    start_time = time.time()
    approx_pi = simpson_13(f, 0, 1, N)
    end_time = time.time()
    galat_rms = math.sqrt((approx_pi - referensi_phi)**2)
    execution_time = end_time - start_time

    print(f"N = {N}")
    print(f"Approximated Pi = {approx_pi}")
    print(f"RMS Error = {galat_rms}")
    print(f"Execution Time = {execution_time} seconds")
    print()
