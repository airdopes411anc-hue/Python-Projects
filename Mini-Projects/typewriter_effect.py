import time

text = "welcome to vs code"
for char in text:
    print(char, end='', flush=False)
    time.sleep(0.1)
print()
