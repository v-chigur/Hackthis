def check(bt, i):
    cnt = 0
    for chunk in chunks:
        if i >= len(chunk):
            return True
        x = bt ^ chunk[i]
        cnt += 1
        if (x < ord('a') or x > ord('z')) and not (x in [ord(' '), ord('_'), ord('\n')]):
            return False
    return True

def get_key():
    key = []
    
    for i in range(key_len):
        for b in range(byte):
            if check(b, i):
                key.append(b)
                break
    return key
            
key_len = 24
byte = 256

alf = 'qwertyuiopasdfghjklzxcvbnm_'
alf_len = 27

with open("encrypted_text", "rb") as fin:
    s = fin.read()
    l = len(s)
    n = l // key_len
    chunks = [s[i:i + key_len] for i in range(0, l, key_len)]
    
k = get_key()
print('in bytes: ', *k)
print('in string: ', ''.join([chr(s) for s in k]))