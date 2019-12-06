import os

directory='C:/Users/teama/Desktop/NW/files'
for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".txt"):
        f=os.path.join(directory, filename)
        file= open(f,"rb")
        read_file=file.read()
        read_bytes=bytearray(read_file)
        print(len(read_bytes))
        print(os.path.join(directory, filename))
        continue
    else:
        continue
