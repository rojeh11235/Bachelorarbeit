import time

from src.encryption import rot_random


def is_dtazv(dtazv):
    return is_qsatz(dtazv) & is_tsatz(dtazv)


def is_qsatz(dtazv):
    return dtazv[0:5] == "0256Q"


def is_tsatz(dtazv):
    return dtazv[256:261] == "0768T"


def get_qsatz(dtazv):
    if is_qsatz(dtazv):
        return dtazv[0:255]
    else:
        print('No Qsatz')


def get_tsatz(dtazv):
    if is_tsatz(dtazv):
        return dtazv[256:]
    else:
        print('No Tsatz')


def capitalize_group(list):
    list1=[]
    for i in range(len(list)):
        list1.append(list[i].upper())
    return list1


def protect_dtazv(file_path, output_path, group_str, group_num, key):
    dtazv = open(file_path).read()
    for i in range(14, 24):
        dtazv = dtazv[:i] + rot_random.rot_random(dtazv[i], capitalize_group(group_str), group_num, key) + dtazv[i + 1:]
    for i in range(23, 163):
        dtazv = dtazv[:i] + rot_random.rot_random(dtazv[i], capitalize_group(group_str), group_num, key) + dtazv[i + 1:]
    for i in range(272, 282):
        dtazv = dtazv[:i] + rot_random.rot_random(dtazv[i], capitalize_group(group_str), group_num, key) + dtazv[i + 1:]
    for i in range(299, 309):
        dtazv = dtazv[:i] + rot_random.rot_random(dtazv[i], capitalize_group(group_str), group_num, key) + dtazv[i + 1:]
    for i in range(323, 463):
        dtazv = dtazv[:i] + rot_random.rot_random(dtazv[i], capitalize_group(group_str), group_num, key) + dtazv[i + 1:]
    for i in range(466, 606):
        dtazv = dtazv[:i] + rot_random.rot_random(dtazv[i], capitalize_group(group_str), group_num, key) + dtazv[i + 1:]
    for i in range(676, 711):
        dtazv = dtazv[:i] + rot_random.rot_random(dtazv[i], capitalize_group(group_str), group_num, key) + dtazv[i + 1:]
    for i in range(935, 970):
        dtazv = dtazv[:i] + rot_random.rot_random(dtazv[i], capitalize_group(group_str), group_num, key) + dtazv[i + 1:]
    protected_file = open(
        '{}/protected_DTAZV_file_{}.txt'.format(output_path, time.strftime(
            "%Y%m%d-%H%M%S")),
        'w', )
    protected_file.write(dtazv)


def return_dtazv(file_path, output_path, group_str, group_num, key):
    dtazv = open(file_path).read()
    for i in range(11, 23):
        dtazv = dtazv[:i] + rot_random.de_rot_random(dtazv[i], capitalize_group(group_str), group_num, key) + dtazv[i + 1:]
    for i in range(23, 163):
        dtazv = dtazv[:i] + rot_random.de_rot_random(dtazv[i], capitalize_group(group_str), group_num, key) + dtazv[i + 1:]
    for i in range(272, 282):
        dtazv = dtazv[:i] + rot_random.de_rot_random(dtazv[i], capitalize_group(group_str), group_num, key) + dtazv[i + 1:]
    for i in range(299, 309):
        dtazv = dtazv[:i] + rot_random.de_rot_random(dtazv[i], capitalize_group(group_str), group_num, key) + dtazv[i + 1:]
    for i in range(323, 463):
        dtazv = dtazv[:i] + rot_random.de_rot_random(dtazv[i], capitalize_group(group_str), group_num, key) + dtazv[i + 1:]
    for i in range(466, 606):
        dtazv = dtazv[:i] + rot_random.de_rot_random(dtazv[i], capitalize_group(group_str), group_num, key) + dtazv[i + 1:]
    for i in range(676, 711):
        dtazv = dtazv[:i] + rot_random.de_rot_random(dtazv[i], capitalize_group(group_str), group_num, key) + dtazv[i + 1:]
    for i in range(935, 970):
        dtazv = dtazv[:i] + rot_random.de_rot_random(dtazv[i], capitalize_group(group_str), group_num, key) + dtazv[i + 1:]
    protected_file = open(
        '{}/output/DTAZV_file_{}.txt'.format(output_path, time.strftime(
            "%Y%m%d-%H%M%S")),
        'w', )
    protected_file.write(dtazv)

# group1 = rot_random.random_str_group(True)
# group2 = rot_random.random_numeric_group()
# protect_dtazv("../../../data/dtazv.txt", group1, group2,152)
# group1 = open("../../../output/random_str_group.txt").read()
# group2 = open("C:\\NAK\\BachelorArbeit\\Filesprotecter\\output\\random_numeric_group.txt").read()
# return_dtazv("C:\\NAK\\BachelorArbeit\\Filesprotecter\\output\\protected_DTAZV_file_20220325-170818.txt", group1,group2,152)
