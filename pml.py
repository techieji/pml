import sys,os.path as p;l=lambda *m:[print((lambda l:f'\033[90m{l[0]}\033[0m:\033[36m{l[1]}\033[96m {" ".join(map(str,m))}\033[0m')((lambda x:(p.relpath(x.f_code.co_filename),x.f_lineno))(sys._getframe(1)))),m[0]][1]
