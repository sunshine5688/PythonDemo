from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import MD5
import base64
def RSA_sign(data):
    privateKey = '''MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBAOG/8J9TP8cN7upNoZ+LoBs9xImv
                4hHAwO/gq7TLGjZ5IoUIxWPJbGtUI+muXsFf8tBfjE3p86ava1R1Ji0c0Sh98bPT4lFMqGFWV5OJ
                d2VbvLGG4DclFzkZxMuB4M7sSvXlKdfawHuFFG/HiEEzjuiROfqWlP3qZ6Ix0QLRhE9HAgMBAAEC
                gYBdPujnBn3rfIfY4+QEgKnLVsIdlTat2o5XBtglv1a+dV6a0LqnswVDd+e1mD6vZTBofW74p8/q
                Y77TjegM7kA90Nw9N4z2uuhn7kXFNI+RiA2MUXcqf4Vwb/64wRpqH70abZzCuyhxQYXqNqEmJuL4
                jAxMoxztxj4BvXt5zk9ekQJBAPLwghERrLNgu+ty/Fmdk15NWE/Eoazig15THPEgrZ5Ruaq90U9O
                4sTWbYgDLYJI75uDTgFoPE+VHkT40WspYZMCQQDt4tsPwVHtXEX4sYclEAbWzXEYDlNXCA3zvWf6
                9cb9N+oY4FfMuThFdfpC5H2D+5bhqCRLZUzuvthS7i18ljv9AkEApJkFVvFFtIc+60iN513XAhaf
                VfRgohUacqcXPdwpJdIzXJadIQHOrRSnQ3b7t4EZLqFpEZUA/96Fkq+Om+9+lwJBAK0fjwt9RrF2
                mNmv4UnAyyliZC78pfxNuVGsg1LpsYKxQaYPBvbPyTsL7DDodswpuhnJs3hHZeDOdUKNYf8smsUC
                QDhQqQHjf6Kf9ZI/zO6Ldvn0y5cMomzfFaH8ltRcjuNB8num1Vt0Oyk+k90q+OYak5twRvKGGsQD
                8v+gOIQ8ZfA='''
    private_keyBytes = base64.b64decode(privateKey)
    priKey = RSA.importKey(private_keyBytes)
    #priKey = RSA.importKey(privateKey)
    signer = PKCS1_v1_5.new(priKey)
    hash_obj = MD5.new(data.encode('utf-8'))
    signature = base64.b64encode(signer.sign(hash_obj))
    return signature

def verify(signature,data):
    publicKey = '''MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCJ3haUf1Tj0/XuknJqsxg/N8nu3NqXhvo6Mdbw
                UFuLYux0pjKlY2lCvV14Rlnl2bf0XoIaFcHZIvbexv8bXfakDhpQokyToKvK6kIlbkgKCqCzjVm0
                ZthNou5cnqVyRurn3UXxELn1VfHkLc4nSZie+pMwiBRB4ViuAH1+w/gyvwIDAQAB'''
    public_keyBytes = base64.b64decode(publicKey)
    pubKey = RSA.importKey(public_keyBytes)
    #pubKey = RSA.importKey(publicKey)
    h = MD5.new(data.encode('utf-8'))
    verifier = PKCS1_v1_5.new(pubKey)
    return verifier.verify(h, base64.b64decode(signature))


if __name__ == '__main__':
    data = '1234566666'
    sign = RSA_sign(data)
    print(str(sign, encoding = "utf-8"))
    print(verify(str(sign, encoding = "utf-8") ,data))