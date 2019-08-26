

def GetSubdirsDic(stri):
    return eval(stri.replace('/','__')).subdirs
def GetFilesDic(stri):
    return eval(stri.replace('/','__')).files
def MkPath(stri):
    return stri.replace('/','__')

def DirBootstrap(name,indir):
    pat=eval(indir.replace('/','__')).path.replace('/','__')
    line=pat + '__' + name + ' = dir(\''
    line=line + eval(indir.replace('/','__')).path + '/'
    line=line + dirname + '\', \'' + dirname + '\', [], [])'
def GetNameStr(st):
    return eval(st).name


def GetNamePathStr(pat, st):
    return eval(pat.replace('/','__') + '__' + st).name

def AddToDir(filet, dirt):
    eval(dirt).files.append(filet)
