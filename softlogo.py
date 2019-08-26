from libtvs import *
import os

if os.name != 'nt':
    rows, columns = os.popen('stty size', 'r').read().split()

def razdel():
	return (('=') * int(columns))
def probel(k):
	return (' ' * k)
print(yellow(razdel()))
print(yellow(probel(int(columns)//2-7) + 'libsoft'))
print(yellow(razdel()))

print(red('''

       @#################################
     @@@#################################
     @@@#################################
     @@@#########@@@@@@@@@@@@@@@@@@@@@@@
     @@@#########
     @@@#########
     @@@#################################
     @@@#################################
     @@@#################################
     @@@@@@@@@@@@@@@@@@@@@@@@@@@#########
			     @@@#########
			     @@@#########
       @#################################
     @@@#################################
     @@@#################################
     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
'''))
print(yellow(razdel()))
print(probel(int(columns)//2-7) + 'by lezzer')
print(yellow(razdel()))
