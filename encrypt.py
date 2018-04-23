import sys
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import qrcode
import base64 as b64

def main(message):
    
    qr = qrcode.QRCode(
        version=4,
        error_correction=qrcode.constants.ERROR_CORRECT_M,        
    )

    key = RSA.importKey(open('/Users/danbiya/.ssh/id_rsa.pub').read())
    cipher = PKCS1_OAEP.new(key)
    with open(message, 'r') as m:
        msg = m.readline()
    ciphertext = cipher.encrypt(msg.encode())
    secret = b64.b64encode(ciphertext)
    
    qr.add_data(secret)
    img = qr.make_image()

    return secret,img    
    

if __name__ == '__main__':
    message = sys.argv[1]
    imgname = sys.argv[2]    
    secret,img = main(message)
    
    img.show()
    img.save(imgname)
    print(secret)

