# try to open file and check if they are saved or not withour any error use try n except
try:
    with open('file1.txt', 'r') as f:
        print(f.read())
except Exception as e :
    print(e)

try:
    with open('Apps.txt', 'r') as file:
        print(file.read())
    print("Files opened and read successfully.")
except Exception as e:
    print(e)    