import os, sys

var = "PATH"
longu = (80-len(var)) //2
separation = '\n'+ '='*longu + '{}' + '='*longu + '\n'
x = os.popen("echo ${}".format(var))
print(separation.format(var))
for chemin in x.readlines()[0][:-1].split(":"):
    print("{}".format(chemin))
print(separation.format('='*len(var)))
