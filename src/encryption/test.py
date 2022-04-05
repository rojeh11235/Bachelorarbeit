from Crypto.Cipher import AES
import binascii, os

def encrypt_AES_GCM(msg, secretKey):
    aesCipher = AES.new(secretKey, AES.MODE_GCM)
    ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
    return (ciphertext, aesCipher.nonce, authTag)

def decrypt_AES_GCM(encryptedMsg, secretKey):
    (ciphertext, nonce, authTag) = encryptedMsg
    aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
    return plaintext

secretKey = os.urandom(32)  # 256-bit random encryption key
print("Encryption key:", binascii.hexlify(secretKey))


msg1 = b'Maria Musterfrau'
msg2 = b'BeethovenStrasse 311'
msg3 = b'DE37500700240324115500'
print('Massage :',msg1)
print( "encryptedMsg", {
    'ciphertext': binascii.hexlify(encrypt_AES_GCM(msg1, secretKey)[0])
})
print('Massage :',msg2)
print("encryptedMsg", {
    'ciphertext': binascii.hexlify(encrypt_AES_GCM(msg2, secretKey)[0])
})
print('Massage :',msg3)
print("encryptedMsg", {
    'ciphertext': binascii.hexlify(encrypt_AES_GCM(msg2, secretKey)[0])
})



