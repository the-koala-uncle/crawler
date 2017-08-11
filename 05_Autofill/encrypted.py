#!python3
#encrypted about password
import random

def encryption(cipher):
    out=''
    listt=list(cipher)
    for n in listt:
        out=out+str(ord(n))
    M=len(out)
    print(M)
    if M<=24:
        L=32-M
    else:
        L=64-M

    for i in range(L-2):
        random.seed()
        abc=random.randint(97,122)
        abc=chr(abc)
        n=random.randint(0,M+1)
        out=out[:n]+abc+out[n:]
    abc=chr(random.randint(97,122))
    out=out+abc
    abc=chr(random.randint(97,122))
    out=abc+out
    return(out)


def decryption(cipher):
    outt=''
    ott=''
    for n in cipher: 
        if n in '0123456789':
            outt=outt+n   
    while len(outt)!=0:
        if int(outt[0:2])>40:
            ott=ott+chr(int(outt[0:2]))
            outt=outt[2:]
        else:
            ott=ott+chr(int(outt[0:3]))
            outt=outt[3:]
    return(ott)


