import operator 

def xor_string(x, y):
    return chr(ord(x) ^ ord(y))

def check(sym, i):
    val = 0
    
    for chunk in chunks:
        if i > len(chunk):
            return True
        v = xor_string(sym, chunk[i])
        #print(v)
        if v == val or val == 0:
            val = v
            continue
        else:
            return False
    return True

def get_key(a):
    key = []
    head = 0
    
    for sym in a:
        if check(sym, head):
            key.append(sym)
            head += 1
        if head == key_len:
            break
    return ''.join(key)
            
key_len = 24

alf = 'qwertyuiopasdfghjklzxcvbnm_'
alf_len = 27

with open("encrypted_text", "rb") as fin:
    s = fin.read().decode("utf-8")
    #s = [line.rstrip().decode("utf-8") for line in fin.readlines()]
    #s = ''.join(s)
    l = len(s)
    n = l // key_len
    chunks = [s[i:i + key_len] for i in range(0, l, key_len)]
    
print(get_key(alf))