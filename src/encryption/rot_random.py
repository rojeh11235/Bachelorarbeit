import random


def random_str_group(path):
    group = []
    group.append(chr(36))
    group.append(chr(37))
    group.append(chr(38))
    group.append(chr(42))
    group.append(chr(43))
    group.append(chr(44))
    group.append(chr(45))
    group.append(chr(46))
    group.append(chr(47))
    for i in range(65, 91):
        group.append(chr(i))
    for i in range(97, 123):
        group.append(chr(i))
    group1 = random.sample(group, len(group))
    g = open(path, 'w')
    for item in group1:
        g.write(item)
    return group1


def random_numeric_group(path):
    group = []
    for i in range(48, 58):
        group.append(chr(i))
    group1 = random.sample(group, len(group))
    g = open(path, 'w')
    for item in group1:
        g.write(item)
    return group1


def rot_random(s, group1, group2, key):
    x = []
    for i in range(len(s)):
        if (s[i] != ' ' and s[i] != "\n"):
            if s[i].isnumeric():
                j = group2.index(s[i])
                x.append(group2[((j + int(key)) % (len(group2) - 1))])
            else:
                j = group1.index(s[i])
                if j in range(len(group1)):
                    x.append(group1[((j + int(key)) % (len(group1) - 1))])
        else:
            x.append(s[i])
    return ''.join(x)


def de_rot_random(s, group1, group2, key):
    x = []
    for i in range(len(s)):
        if (s[i] != ' ' and s[i] != "\n"):
            if s[i].isnumeric():
                j = group2.index(s[i])
                x.append(group2[((j - int(key)) % (len(group2) - 1))])
            else:
                j = group1.index(s[i])
                if j in range(len(group1)):
                    x.append(group1[((j - int(key)) % (len(group1) - 1))])
        else:
            x.append(s[i])
    return ''.join(x)

# group1 = open("C:\\NAK\\BachelorArbeit\\Filesprotecter\\output\\random_str_group.txt").read()
# group2 = open("C:\\NAK\\BachelorArbeit\\Filesprotecter\\output\\random_numeric_group.txt").read()
