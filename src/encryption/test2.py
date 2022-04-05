from cryptography.fernet import Fernet

key = Fernet.generate_key()
print("key = ", key)
fernet = Fernet(key)
msg1 = b'Maria Musterfrau'
msg2 = b'BeethovenStrasse 311'
msg3 = b'DE37500700240324115500'
print('Message = ', msg1, ","," encrypted Message = ", fernet.encrypt(msg1))
print('Message = ', msg2, ","," encrypted Message = ", fernet.encrypt(msg1))
print('Message = ', msg3, ","," encrypted Message = ", fernet.encrypt(msg1))
