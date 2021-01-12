import sys
from importlib import import_module as _i
sys.dont_write_bytecode = True

args = []
try:
    args = sys.argv[:]
    for p in args:
        print(p)
except Exception as e:
    print(e)
    exit()



# p = _i("packages."+package)
# if len(args) > 1:
#     args = args[1:]
# else:
#     args = []

# a = {}
# b = []
# typ = None
# for x in args:
#     if typ is not None:
#         a[typ] = x
#         typ = None
#     if x.startswith('-'):
#         typ=x[1:]
# for x in args:
#     if not x.startswith("-"):
#         if x not in a.values():
#             b.append(x)
# cmd = p.Pkg(package)
# cmd.run(b,a)