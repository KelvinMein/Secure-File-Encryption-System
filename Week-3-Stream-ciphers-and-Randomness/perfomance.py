import time

start = time.time()

data = "A" * 100000
encrypted = ''.join(chr(ord(c) ^ 5) for c in data)

end = time.time()

print("Time taken:", end - start)