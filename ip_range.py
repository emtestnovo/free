import urllib3
http = urllib3.PoolManager()


print('=========================================')
print('Precisa estar sem saldo, e sem credito')
print('=========================================')







def dominio_status(dominio,ip,porta):	
	if porta=='80':
		proxy = urllib3.ProxyManager(f'http://{ip}:{porta}/')
		
	elif porta=='443':
		proxy = urllib3.ProxyManager(f'https://{ip}:{porta}/')
		
	elif porta!='80' or porta!='443':
		proxy = urllib3.ProxyManager(f'socks5://{ip}:{porta}')

	r=proxy.request('POST', f'http://{dominio}',fields={'Upgrade':'websocket'},timeout=3)
	try:
		print(r.status,'\n',r.headers,'\n')
	except:
		pass
	return r.status

text=open(f'ips.txt','a+')

def tipo2():
	for x in range(0,257):
		ip=f"{sufixo}.{x}"
		try:
			status=dominio_status(dominio,ip,porta)
			if status==101:
				text.write(f'proxy:{ip}:80\n')
				print('=========================================')
				print(f'Adicionado proxy a lista {ip}')
				print('=========================================')
				text.close()
			elif status!=101:
				text.write(f'{ip}  -> {status} \n')
				print(f'{ip} -> {status}')
				text.close()
			else:
				print(f'ip: {x} -> {status}')
				
				
		except:
			print(f'sem resposta do  ip: -> {x}')
			pass
			
			
def tipo1():
	for x in range(0,257):
		for x2 in range(0,257):
			ip=f"{sufixo}.{x}.{x2}"
			try:
				status=dominio_status(dominio,ip,porta)
				if status==101:
					text.write(f'proxy:{ip}:80\n')
					print(f'Adicionado proxy a lista {ip}')
					text.close()
				if status!=200 or status!=101:
					text.write(f'{ip}  -> {status} \n')
					print('=========================================')
					print(f'{ip} -> {status}')
					print('=========================================')
					text.close()
			except:
				print(f'sem resposta do  ip: -> {x}.{x2}')
				pass
				




print('tipo de ip range:\n1: 10.23\n2: 10.23.0')

tipo=input()

if tipo=='1':
    print('ip adress ex: 10.24')
else:
    print("ip adress ex: 10.24.0")
    
sufixo=input()

print('portas aceitas 80,443 diferentes dessas portas sera reconhecido como socket5')

porta=input()

print('dominio ws')

dominio=input()

if tipo=="1":
    print("esse demora uma vida")
    print(f" Dominio: {dominio} Ip Rage:{sufixo} Porta: {porta}")
    tipo1()
    
elif tipo=="2":
    print("esse e mas suave")
    print(f" Dominio: {dominio} Ip Rage:{sufixo} Porta: {porta}")
    tipo2()
    
else:
    print("Qual tipo de ip range 1 ou 2")
