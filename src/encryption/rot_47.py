import random


def random_group():
    group = []
    group.append(chr(20))
    group.append(chr(36))
    group.append(chr(37))
    group.append(chr(38))
    group.append(chr(42))
    group.append(chr(43))
    group.append(chr(44))
    group.append(chr(45))
    group.append(chr(46))
    group.append(chr(47))

    for i in range(48, 58):
        group.append(chr(i))
    for i in range(65, 91):
        group.append(chr(i))
    for i in range(97, 123):
        group.append(chr(i))
    group1 = random.sample(group, len(group))
    g = open("C:\\NAK\\BachelorArbeit\\Filesprotecter\\output\\random_group.txt", 'w')
    for item in group1:
        g.write(item)


def rot47(s):
    x = []
    for i in range(len(s)):
        j = ord(s[i])
        if j >= 33 and j <= 126:
            x.append(chr(33 + ((j + 14) % 94)))
        else:
            x.append(s[i])
    return ''.join(x)


def rot_random(s, key, group1):
    x = []
    for i in range(len(s)):
        j = group1.index(s[i])
        if j in range(len(group1)):
            x.append(group1[((j + 14) % int(key)) % (len(group1)-1)])
        else:
            x.append(s[i])
    return ''.join(x)


def re_rot_random(s, group, key):
    x = []
    for i in range(len(s)):
        j = group1.index(s[i])
        if j in range(len(group)):
            x.append(group1[((j - 14) % int(key)) % len(group)])
        else:
            x.append(s[i])
    return ''.join(x)


# random_group()
group1 = open("C:\\NAK\\BachelorArbeit\\Filesprotecter\\output\\random_group.txt", 'r').read()
print(rot_random('qwuhgtfdgsdfsdfe', 55, group1))
print(re_rot_random(rot_random('qwuhgtfdgsdfsdfe', 55, group1),group1,55))

print(rot47(rot47('123456')))
