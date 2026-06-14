import os

path = r"C:\Users\rosha\Desktop"

for item in os.listdir(path):
    full_path = os.path.join(path, item)
    print(full_path)
