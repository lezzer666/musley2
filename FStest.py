import mFS2ep2 as mfs
from libtvs import *
from time import sleep

import disc

mfs.__home=mfs.dir('/home','home',['valera'],[])
mfs.__home__valera=mfs.dir('/home/valera','valera',[],[])

__home=mfs.dir('/home','home',['valera'],[])
__home__valera=mfs.dir('/home/valera','valera',[],[])



def p(a=1):
    while a > 0:
        print()
        a-=1
def r(a=1):
    while a > 0:
        print('===')
        a-=1


print('ls(), make dir and ls():')

curdir='/home'

# file ls

lsdir=curdir.replace('/','__')
print('lsdir=' + lsdir)
print('lsdir.name=' + eval(lsdir).name )

print()

r()
print('ls\'ing (without musley API)')
r()
print()
sleep(0.5)

code='''
for dirt in eval(lsdir).subdirs:
    print(eval(eval(lsdir).path.replace('/','__') + '__' + dirt).name)
for dirt in eval(lsdir).files:
    print(eval(eval(lsdir).path.replace('/','__') + '__' + dirt).name)
'''
print('code: ')
print(code)

r()
print('result: ')
exec(code)

p(3)
r()
print('making dir (without musley API)')
sleep(0.5)
r()
p(2)

dirname='testdir'

#print(curdir.replace('/','__'))

pat=eval(curdir.replace('/','__')).path.replace('/','__')

line= pat 
line=line + '__' + dirname + ' = mfs.dir(\'' 
line=line + eval(curdir.replace('/','__')).path + '/' 
line=line + dirname + '\', \'' + dirname + '\', [], [])'




abc  = eval(curdir.replace('/','__')).path.replace('/','__') 
abcd = eval(curdir.replace('/','__')).path.replace('/','__') + '__' + dirname


# abc.replace('/','__')

eval(abc + '.subdirs').append(dirname)



exec(line)


print('ls\'ing (without musley API)')
r()
print()
sleep(0.5)                                                 



#print(mfs.__home__testdir.name)


for dirt in eval(lsdir).subdirs:
    print(eval(lsdir + '__' + dirt).name)
for dirt in eval(lsdir).files:
    print(eval(lsdir + '__' + dirt).name)


p()
r()
print('API test')
r()
p()

aread=open('mAPIv1.py','r')
aread=aread.read()

exec(aread)

r()
print('ls\'ing (with musley API)')
r()
p()

code='''
for subdir in GetSubdirsDic(curdir):
    print(GetNamePathStr(curdir, subdir))
for filet in GetFilesDic(curdir):
    print(GetNamePathStr(curdir, filet))
'''
print('code: ')
print(code)
r()
print('result: ')
exec(code)
