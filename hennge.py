import time
import hmac
import hashlib
import struct

def totp_10_digits(email: str) -> str:
    secret = (email + "HENNGECHALLENGE004").encode("ascii")

    timestep = 30
    counter = int(time.time() // timestep)

    msg = struct.pack(">Q", counter)
    digest = hmac.new(secret, msg, hashlib.sha512).digest()

    offset = digest[-1] & 0x0F
    code_int = struct.unpack(">I", digest[offset:offset+4])[0] & 0x7FFFFFFF

    code = code_int % (10 ** 10)
    return str(code).zfill(10)

print(totp_10_digits("aliwangara63@gmail.com"))
