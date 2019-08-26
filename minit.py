import sys

# import disc
aread=open('disc.py','r')
aread=aread.read()
exec(aread)

# import musley API
aread=open('mAPIv1.py','r')
aread=aread.read()
exec(aread)

#=#=#=#=#=#

if '__etc__minit' in locals():
    pass
else:
    print('minit: can\'t find /etc/minit/. exiting...')
    sys.exit(2)

for filet in eval('__etc__minit').files:
    print('minit: running ' + eval(filet).name + '...')
    exec(eval(filet).content)
