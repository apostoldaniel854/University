def caesar_cipher(str, key):
    encoded = ""
    for ch in str:
        if ch >= 'a' and ch <= 'z':
            ch = chr(ord('a')+ (ord(ch) - ord('a') + key) % 26)
        encoded += ch;
    return encoded

print(caesar_cipher("abc", 25))
