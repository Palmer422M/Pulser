import importlib
import os
import shutil

from constants import DEFAULT_SWEEP_DEF_MODULE

SWEEP_LIB_DIR = 'sweeplib'
SWEEP_DEFAULT_FILENAME = DEFAULT_SWEEP_DEF_MODULE + '.py'

flist = os.listdir(SWEEP_LIB_DIR)

for k, f in enumerate(flist):
    r,e = os.path.splitext(f)
    if e == '.py':
        modpath = SWEEP_LIB_DIR + '.' + r
        m = importlib.import_module(modpath)
        print('%2d %s:%s' % (k+1, r, m.DESCRIPTION))

kstr = input('Load (0 to cancel): ')
kint = int(kstr) - 1
if kint == -1:
    print('Cancelled')
    exit()
if kint >= len(flist):
    print('k too large, no copy')
    exit()

src = os.path.join(SWEEP_LIB_DIR, flist[kint])
dst = os.path.join('.\\', SWEEP_DEFAULT_FILENAME)
print('Copying %s -> %s' % (src, dst))
shutil.copyfile(src, dst)


