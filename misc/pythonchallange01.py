encrypted = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

encrypted = 'map'

decrypted = ""

for letter in encrypted:
    # print(letter)
    new_letter = chr(ord(letter) + 2)
    if letter in 'yz':
        new_letter = chr(ord(letter) - 24)
    decrypted += new_letter

print(decrypted)
