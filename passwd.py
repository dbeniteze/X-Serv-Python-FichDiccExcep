#!usr/bin/python 

fich = open("/etc/passwd", "r")
lineas= fich.readlines()
dicc = {}

for linea in lineas:
    separada = linea.split(":", len(lineas))
    user = separada[0]
    shell = separada[-1][:-1]
    dicc[user] = shell
print "Numero de usuarios: " + str(len(lineas)), '\n'
try:
	print 'Shell root:', dicc['root'], '\n'
	print 'Shell imaginario:', dicc['imaginario'],
except KeyError:
	print 'imaginario no existe',
