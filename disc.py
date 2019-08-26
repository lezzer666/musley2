
from mFS2ep2 import *

# import api
aread=open('mAPIv1.py','r')
aread=aread.read()
exec(aread)



# dir ( 'path', 'name', subdirs[], files[] )
# file ( 'name', '''content''')

__etc=dir('__etc','etc',[],[])
__etc__minit=dir('__etc__minit','minit',[],[])
__etc__minit__hello=file('hello','''
from os import name as OSNAME
from os import system
if OSNAME == 'nt':
    system('cls')
else:
    system('clear')
print('Welcome to PyCherry!')

try:
    logo=open('musleylogo.py')
    logor=logo.read()
    exec(logor)
except FileNotFoundError:
    print('Musley logo not found. skipping...')

''', 'root')
AddToDir('__etc__minit__hello','__etc__minit')
__etc__minit__loadcomps=file('loadcomps','''
from libtvs import *

toimport=['libsoft','libtvs']

for comp in toimport:
    exec ('import ' + comp)

print('')
print('loadcomps: ' + 'imported ' + libtvs.green('sucsessfuly'))
print('')
''','root')
AddToDir('__etc__minit__loadcomps','__etc__minit')
__etc__minit__muslogin=file('__etc__
