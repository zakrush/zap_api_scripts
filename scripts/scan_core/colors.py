# -*- coding:utf -8 -*-
import colorama
colorama.init(autoreset=True)


class Bcolors:
    G = '\033[92m'  # Light green
    GN = '\033[32m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[97m'  # white
    M = '\x1b[35m'  # magenta
    C = '\x1b[36m'  # cyan
    CN = '\x1b[5;30;46m'  # cyan Фоновый цвет
    LG = '\x1b[102m'  # Light Green  Фоновый цвет
    GF = '\033[42m'  # green Фоновый цвет
    LR = '\x1b[101m'  # Light Red  Фоновый цвет
    BF = '\x1b[40m'  # Black  Фоновый цвет
    BLF = '\033[104m'  # blue Фоновый цвет
    YF = '\033[103m'  # yellow Фоновый цвет
    WF = '\x1b[107m'  # white  Фоновый цвет
    GR = '\033[0m'  # grey
    BL = '\x1b[30m'  # Black
    CL = '\033[0m'  # Clear