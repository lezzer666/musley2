def purple(what):
    return '\033[35m' + what + '\033[0m'
def red(what):
    return '\033[31m' + what + '\033[0m'
def yellow(what):
    return '\033[33m' + what + '\033[0m'
def blue(what):
    return '\033[94m' + what + '\033[0m'
def green(what):
    return '\033[92m' + what + '\033[0m'
#import tvslogo
from os import system
import itertools
import time

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

def ok(what):
	print('[' + green('OK') + '] ' + what)
def error(what):
	print('[' + red('FAILED') + '] ' + what)
def loading(what):
	print('[' + blue('***') + '] ' + what)
def wsnloading(what, t, r):
	print('[' + blue('***') + '] ' + what, end='')
	it = itertools.cycle(['.'] * 3 + ['\b \b'] * 3)
	for x in range(r):
		time.sleep(t)
		print(next(it), end='', flush=True)
	#print'('\n')

def logo():
	print(red("""
@@  @@  @@  @@ @@@@@ @@   @@@@@ @@  @@
@@@@@@  @@  @@ @@    @@   @@     @  @
@@@@@@  @@  @@ @@@@@ @@   @@@@@   @@
@@  @@  @@  @@    @@ @@   @@      @@
@@  @@  @@@@@@ @@@@@ @@@@ @@@@@   @@

"""))
	print("""
======================================
by tvsclass & lezzer
======================================
""")
def clear():
	system('clear')

