import time

from src.encryption import rot_47


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


def protect_dtazv(file_path):
    dtazv = open(file_path).read()
    for i in range(11, 23):
        dtazv = dtazv[:i] + rot_47.rot47(dtazv[i]) + dtazv[i + 1:]
    for i in range(23, 163):
        dtazv = dtazv[:i] + rot_47.rot47(dtazv[i]) + dtazv[i + 1:]
    for i in range(272, 282):
        dtazv = dtazv[:i] + rot_47.rot47(dtazv[i]) + dtazv[i + 1:]
    for i in range(299, 309):
        dtazv = dtazv[:i] + rot_47.rot47(dtazv[i]) + dtazv[i + 1:]
    for i in range(323, 463):
        dtazv = dtazv[:i] + rot_47.rot47(dtazv[i]) + dtazv[i + 1:]
    for i in range(466, 606):
        dtazv = dtazv[:i] + rot_47.rot47(dtazv[i]) + dtazv[i + 1:]
    for i in range(676, 711):
        dtazv = dtazv[:i] + rot_47.rot47(dtazv[i]) + dtazv[i + 1:]
    for i in range(935, 970):
        dtazv = dtazv[:i] + rot_47.rot47(dtazv[i]) + dtazv[i + 1:]
    protected_file = open(
        'C:\\NAK\\BachelorArbeit\\Filesprotecter\\output\\protected_DTAZV_file_{}.txt'.format(time.strftime(
            "%Y%m%d-%H%M%S")),
        'w', )
    protected_file.write(dtazv)


def return_dtazv(file_path):
    dtazv = open(file_path).read()
    for i in range(11, 23):
        dtazv = dtazv[:i] + (rot_47.rot47(dtazv[i])) + dtazv[i + 1:]
    for i in range(23, 163):
        dtazv = dtazv[:i] + (rot_47.rot47(dtazv[i])) + dtazv[i + 1:]
    for i in range(272, 282):
        dtazv = dtazv[:i] + (rot_47.rot47(dtazv[i])) + dtazv[i + 1:]
    for i in range(299, 309):
        dtazv = dtazv[:i] + (rot_47.rot47(dtazv[i])) + dtazv[i + 1:]
    for i in range(323, 463):
        dtazv = dtazv[:i] + (rot_47.rot47(dtazv[i])) + dtazv[i + 1:]
    for i in range(466, 606):
        dtazv = dtazv[:i] + (rot_47.rot47(dtazv[i])) + dtazv[i + 1:]
    for i in range(676, 711):
        dtazv = dtazv[:i] + (rot_47.rot47(dtazv[i])) + dtazv[i + 1:]
    for i in range(935, 970):
        dtazv = dtazv[:i] + (rot_47.rot47(dtazv[i])) + dtazv[i + 1:]
    protected_file = open(
        'C:\\NAK\\BachelorArbeit\\Filesprotecter\\output\\original_DTAZV_file_{}.txt'.format(time.strftime(
            "%Y%m%d-%H%M%S")),
        'w', )
    protected_file.write(dtazv)
