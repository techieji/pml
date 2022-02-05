import sys,os.path as p,datetime as d
l=lambda m:print((lambda l:f'{d.datetime.now().ctime()[11:19]} \033[90m{l[0]}\033[0m:\033[36m{l[1]}\033[31m:{l[2]}\033[96m {m}\033[0m')((lambda x:(p.relpath(x.f_code.co_filename),x.f_lineno,x.f_code.co_name))(sys._getframe(1))))
