def remove_cuv():
    cuv = input("cuvant=")
    x = cuv[0]
    cuv = cuv.replace(x, "")
    print(cuv)

def find_substring_using_find():
    s = input("s=")
    t = input("t=")
    if s.find(t) != -1:
        pos = []
        for i in range(len(s) - len(t) + 1):
            if s[i : i + len(t)] == t:
                pos.append(i)
        print(pos)
    else:
        print(f"Nu exista {t} in {s}")

def find_substring_using_index():
    s = input("s=")
    t = input("t=")
    try: 
        i = s.index(t)
        pos = [i]
        while (s.find(t, i + len(t)) != -1):
            i = s.index(t, i + len(t))            
            pos.append(i)
        print(pos)
    except:
        print(f"Nu exista {t} in {s}")

def strip_word():
    cuv = input("word=")
    l = 0
    r = len(cuv)
    while l < r:
        print(cuv[l:r].center(10))
        l += 1
        r -= 1



def replace_word():
    propozitie = input("propozitie=")
    a = input("a=")
    b = input("b=")
    a = a.center(len(a) + 2)
    b = b.center(len(b) + 2)
    propozitie = propozitie.center(len(propozitie) + 2)
    print(propozitie.replace(a, b).strip())

def decodify():
    coded_string = input("coded string=")
    cnt = 0
    decoded_string = ""
    for ch in coded_string:
        if ch.isdigit():
            cnt = cnt * 10 + int(ch)
        else:
            decoded_string += cnt * ch
            cnt = 0
    print(decoded_string)

def codify():
    string_to_encode = input("string to encode=")
    lstch = "?"
    encoded_string = ""
    cnt = 0
    for ch in string_to_encode:
        cnt += 1
        if lstch != ch:
            if lstch != "?":
                encoded_string += str(cnt)
                encoded_string += lstch
            cnt = 0
        lstch = ch
    if cnt > 0:
        encoded_string += str(cnt)
        encoded_string += lstch
    print(encoded_string)



codify()
