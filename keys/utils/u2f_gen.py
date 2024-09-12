from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import b64decode
import re

key_hex = [0xc9, 0xc6, 0x3d, 0x53, 0xca, 0x25, 0xac, 0x28, 0x4f, 0xfc, 0x9b, 0xf3, 0x86, 0xac, 0x1f, 0x1a, 0x81, 0x20, 0x1a, 0x96, 0x86, 0x06, 0x04, 0x9f, 0x50, 0x7e, 0x27, 0xa6, 0x34, 0xc4, 0x0f, 0x97]
iv_hex = [0xE1, 0x56, 0xCE, 0x83, 0x98, 0xFA, 0x59, 0x0D, 0x45, 0xEC, 0x1C, 0xEB, 0x34, 0xFC, 0x08, 0xC9]
private_key_b64 = 'MHcCAQEEIF452oh6BOsfR5KQ4b/nQGjukxiO2hK+S50w5cY0tbajoAoGCCqGSM49AwEHoUQDQgAE8VTEgpaRdW9AnmM+mFNZfn36TYG4SAlER2PFrYUpuvQtL/Dh/CoMaVZgmgtT4Fs9zZhxFNu1N49jfL/EVGyN9Q=='

key = bytes(key_hex)
iv = bytes(iv_hex)
data = pad(b64decode(private_key_b64), 32)

cipher = AES.new(key, AES.MODE_CBC, iv)
cipher.block_size = 32
encrypted_data = cipher.encrypt(data)

encrypted_data_hex = encrypted_data.hex().upper()
print(re.sub(r"(?<=\w)(?=(?:\w\w)+$)", " ", encrypted_data_hex))