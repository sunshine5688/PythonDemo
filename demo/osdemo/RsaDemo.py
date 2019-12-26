# -*- coding: utf-8 -*-
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from base64 import b64decode, b64encode

origin_data = 'hello world'
public_key = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDcpr7m19SU0Fa7Dfg7fQ0ueUSRWWDA577VsoSceQtd2whDYlI0I5Q4jZAxfPTZCECaft3eFWyBPn41lRP1GP4kWI/FLdYr3TVMx3kVzeF52IzF34EheuNmRlPCGvQY1RXcsAkFaVwEDUiads4dwxTW6hLVrbecqEnfOKKnCAFbFQIDAQAB'
signature = 'Xx5mj1RBfwkmA3of3U9Bxt5ttanY4R9Rzk/fe6IyqtT7ZN1On44tWGMFP5NSCNAnEA5jUJMqr9vnjpUH+rXD0tII49IlHiTavHqhZU1MAws+O82FViI56i9j8qCqTodkiX9Qi38u1XQlV1ZyIdelShyL1JRdtGU1V2XL23cUanE='
private_key = 'MIICXAIBAAKBgQDcpr7m19SU0Fa7Dfg7fQ0ueUSRWWDA577VsoSceQtd2whDYlI0I5Q4jZAxfPTZCECaft3eFWyBPn41lRP1GP4kWI/FLdYr3TVMx3kVzeF52IzF34EheuNmRlPCGvQY1RXcsAkFaVwEDUiads4dwxTW6hLVrbecqEnfOKKnCAFbFQIDAQABAoGANYrk4iFXfXD8ytE9/jl/HFri755Pox/ZKAP0t/+LaY//9lICfpJvojV/2vJme8/L1XGZpw1t0gL3H0t4l04kRPwTy+utjZBsrXA/rkE1lDQ3KJybhv/sXT8wx6TryvVPfJrGbg96U5B8IlFvciYWxClhqkrzfYRMxJKlIwwBseECQQD6Ze1eKOsV2aBaLxmtDrTGtBOMM3hJ6roKgsX7ztj1HIn9GkKv2wjxOYTHXq10uoC7UO/0YsiOrmkGwAYR0tZ5AkEA4ZZ0GFmKqsPPoi8LpeegKUdarYMUO6eBiK6SI9Knmypn7W5FtlONhS5Zcm3iSNUwfu0bySzFKjMFx1soCMMyfQJBAN/f7+lnBkDj8eWQBRHgeyrJaEzK2/qinjG1mJQ57WrBWHJuXz9hw84BUkD62nTqJxzTEadcBtri/04ks4iODGkCQFVPYHgU5KvPgSYERJNpFNiHc3NKrswgfIwD+KAzec7kKolPum1JC6vh61Gq3HhOpxhY8rkRhT6ALR9HCczGhMECQA4LjQ+sYDs8qROtGosx4pHX7JzAiY3ezPqKcBHh7DHaOsry1w5RZAQAeEUh9hr7S6pG4b5X4KuUPQIWTaPgjeI='


def sign():
    key_bytes = bytes(private_key, encoding="utf-8")
    key_bytes = b64decode(key_bytes)
    key = RSA.importKey(key_bytes)
    hash_value = SHA256.new(bytes(origin_data, encoding="utf-8"))
    signer = PKCS1_v1_5.new(key)
    signature = signer.sign(hash_value)
    return b64encode(signature)


def verify():
    key_bytes = bytes(public_key, encoding="utf-8")
    key_bytes = b64decode(key_bytes)
    key = RSA.importKey(key_bytes)
    hash_value = SHA256.new(bytes(origin_data, encoding="utf-8"))
    verifier = PKCS1_v1_5.new(key)
    if verifier.verify(hash_value, b64decode(signature)):
        print("The signature is authentic.")
    else:
        print("The signature is not authentic.")


if __name__ == '__main__':
    print(sign())
    verify()

'''  输出结果:
b'cPz4BuUiKXDDBXjTx5VcMFgDFdCKVfn50Idv7pYhmiivrmx94zk0Fpk6IbKjReiqaNfRhEqGCIVpdFNiKLVKfA=='
The signature is authentic.
'''
