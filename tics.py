numero = input('Ingrese el numero: ')
num = str(numero)
arr = [num[max(i-3,0):i] for i in range(len(num),0,-3)][::-1]

tabla = []

tabla.append(["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"])
tabla.append(["","ciento ","docientos ","trecientos ","cuatrocientos ","quinientos ","seiscientos ","setecientos ",
	"ochocientos ","novecientos ","","","","","",""])
tabla.append(["","dieci","veinti","treinta","cuarenta","cincuenta","sesenta","setenta",
	"ochenta","noventa","diez","once","doce","trece","catorce","quince"])
tabla.append(["","un","dos","tres","cuatro","cinco","seis","siete","ocho","nueve","","","","","",""])

def numapalabra(num):
	st = ''
	if num == '100':
		return 'cien'
	if num == '0':
		return 'cero' 
	if len(num) == 3:
	
		for j in range(len(tabla[0])):
			if num[0] == tabla[0][j]:
				st = st + tabla[1][j]
		for j in range(len(tabla[0])):
			if num[1:] == tabla[0][j]:
				st = st + tabla[2][j]
				return st
	
		for j in range(len(tabla[0])):
			if num[1] == tabla[0][j]:
				st = st + tabla[2][j]

		for j in range(len(tabla[0])):
			if num[2] == tabla[0][j] and num[2] != '0' and num[1] != '0' and num[1] != '1' and num[1] != '2':
				st = st + ' y ' + tabla[3][j]
			elif num[2] == tabla[0][j] and num[2] != '0' and num[1] != '0' and (num[1] == '1' or num[1] == '2'):
				st = st + tabla[3][j]
			elif num[2] == tabla[0][j] and num[2] != '0' and num[1] == '0':
				st = st + tabla[3][j]
			elif num[2] == tabla[0][j] == '0':
				st = st + tabla[3][j]
		return st
	elif len(num) == 2:
		for j in range(len(tabla[0])):
			if num == tabla[0][j]:
				st = st + tabla[2][j]
				return st
		
		for j in range(len(tabla[0])):
			if num[0] == tabla[0][j]:
				st = st + tabla[2][j]

		for j in range(len(tabla[0])):
			if num[1] == tabla[0][j] and num[1] != '0' and num[0] != '0' and num[0] != '1' and num[0] != '2':
				st = st + ' y ' + tabla[3][j]
			elif num[1] == tabla[0][j] and num[1] != '0' and num[0] != '0' and (num[0] == '1' or num[0] == '2'):
				st = st + tabla[3][j]
			elif num[1] == tabla[0][j] and num[1] != '0' and num[0] == '0':
				st = st + tabla[3][j]
			elif num[1] == tabla[0][j] == '0':
				st = st + tabla[3][j]
		return st
	elif len(num) == 1:
		for j in range(len(tabla[0])):
			if num[0] == tabla[0][j]:
				st = st + tabla[3][j]
		return st

if len(arr) == 1:
	st = numapalabra(arr[0])
elif len(arr) == 2:
	if arr[0] == '1':
		st = 'mil ' + numapalabra(arr[1])
	else:
		st = numapalabra(arr[0]) + ' mil ' + numapalabra(arr[1])
elif len(arr) == 3:
	if arr[0] == '1':
		if arr[1] == '000':
			st = 'un millon ' + numapalabra(arr[2])
		elif arr[1] == '001':
			st = 'un millon mil ' + numapalabra(arr[2])
		else:
			st = 'un millon ' + numapalabra(arr[1]) + ' mil ' + numapalabra(arr[2])
	else:
		if arr[1] == '000':
			st = numapalabra(arr[0]) + ' millones ' + numapalabra(arr[2])
		elif arr[1] == '001':
			st = numapalabra(arr[0]) + ' millones mil ' + numapalabra(arr[2])
		else:
			st = numapalabra(arr[0]) + ' millones ' + numapalabra(arr[1]) + ' mil ' + numapalabra(arr[2])
elif len(arr) == 4:
	if arr[0] == '1':
		if arr[1] == '001':
			if arr[2] == '000':
				st = ' mil un millon ' + numapalabra(arr[2])
			elif arr[2] == '001':
				st = ' mil un millon mil' + numapalabra(arr[3])
			else:
				st = ' mil ' + numapalabra(arr[1]) + ' millones ' + numapalabra(arr[2]) + ' mil ' + numapalabra(arr[3])
		else:
			if arr[2] == '000':
				st = ' mil millones ' + numapalabra(arr[2])
			elif arr[2] == '001':
				st = ' mil millones mil' + numapalabra(arr[3])
			else:
				st = ' mil ' + numapalabra(arr[1]) + ' millones ' + numapalabra(arr[2]) + ' mil ' + numapalabra(arr[3])
	else:
		if arr[1] == '001':
			if arr[2] == '000':
				st = numapalabra(arr[0]) + ' mil un millon ' + numapalabra(arr[3])
			elif arr[2] == '001':
				st = numapalabra(arr[0]) + ' mil un millon mil' + numapalabra(arr[3])
			else:
				st = numapalabra(arr[0]) + ' mil ' + numapalabra(arr[1]) + ' millones ' + numapalabra(arr[2]) + ' mil ' + numapalabra(arr[3])
		else:
			if arr[2] == '000':
				st = numapalabra(arr[0]) + ' mil millones ' + numapalabra(arr[3])
			elif arr[2] == '001':
				st = numapalabra(arr[0]) + ' mil millones mil' + numapalabra(arr[3])
			else:
				st = numapalabra(arr[0]) + ' mil ' + numapalabra(arr[1]) + ' millones ' + numapalabra(arr[2]) + ' mil ' + numapalabra(arr[3])



if st[-2:] == 'un':
	st= st + 'o'
print(st)
