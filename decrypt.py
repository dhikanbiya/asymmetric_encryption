import sys
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

def main(privkey,message):
    with open(message,'rb') as m:
        msg = m.readline()

    key = RSA.importKey(open(privkey).read())
    cipher = PKCS1_OAEP.new(key)
    message = cipher.decrypt(msg)
    return message

if __name__ == '__main__':
    privkey = sys.argv[1]
    message = sys.argv[2]
    result = main(privkey,message)
    print(result)
