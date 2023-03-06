import random

s1 = [random.randint(50, 80) for _ in range(10)]
s2 = [random.randint(30, 50) for _ in range(10)]

s3 = [('выжил' if s1[d] + s2[d] < 100 else 'труп') for d in range(10)]

print(s3)