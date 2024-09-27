import time

n = 1000
a = list(range(n))
b = list(range(1000, 1000 + n))

start_time = time.time()

result = 0
for i in range(n):
    result += a[i] * b[i]

end_time = time.time()
running_time = (end_time - start_time) * 1000

print(f"计算结果为: {result}")
print(f"运行时长为: {running_time:.2f}ms")