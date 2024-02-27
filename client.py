import socket
import threading
host = '127.0.0.1'#10.30.56.102
port = 9000
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()
clients= []
nicknames = []

#broadcast
def broadcast(message):
	for client in clients:
		client.send(message)

def handle(client):
	while True:
		try:
			message = client.recv(1024)
			m = message
			message = message.decode('utf-8')
			result = message.split()
			print('outside = ',result)
			if 'calculate:' in message:
				expression = message.split('calculate:')[1].strip()
				try:
					result = eval(expression)
					client.send(f"Server: Result: {result}".encode('utf-8'))
				except Exception as e:
					client.send(f"Server: Error: {str(e)}".encode('utf-8'))
			elif result[0]=='@':
				print('bol bhai ',result)
				client2 = result[2]
				#client2 = b+'\''+client2+'\''
				client2 = bytes(client2,'utf-8')

				#client2 = b'\'{}\''.format(client2)
				print("mujhe bhejana ",client2)
				print("nicknames = ",nicknames)
				if client2 in nicknames:
					print("inside ",result)
					#index = clients.index(client2)
					#indices_to_exclude = [1]
					result_string = ' '.join(result[3:])
					result_string = result[1]+result_string
					#length_result = len(result)
					#for l in range(length_result):
					#	if l!=2:
					#		result_string = result_string+ " "+ result[l]
					#result_string = ' '.join([string for i, string in enumerate(string_list) if i not in indices_to_exclude])
					clients[nicknames.index(client2)].send(result_string.encode('utf-8'))
				else:
					client.send("not able to send to the suggest user".encode('utf-8'))
			else:
				#message = client.recv(1024)
				print(f"{nicknames[clients.index(client)]} says {m}")
				broadcast(m)


			#mine
			'''message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                nickname = client.recv(1024).decode('utf-8')
                nicknames.append(nickname)
                clients.append(client)
                broadcast(f"{nickname} has joined the chat!\n".encode('utf-8'))
            else:
                if 'calculate:' in message:
                    # Extract the expression after 'calculate:'
                    expression = message.split('calculate:')[1].strip()
                    try:
                        result = eval(expression)
                        client.send(f"Server: Result: {result}".encode('utf-8'))
                    except Exception as e:
                        client.send(f"Server: Error: {str(e)}".encode('utf-8'))'''
		except Exception as e:
			print("exception as ",e)
			index = clients.index(client)
			clients.remove(client)
			client.close()
			nickname = nicknames[index]
			broadcast(f"{nickname} has left the chat!\n".encode('utf-8'))
			nicknames.remove(nickname)
			break
#receive
def receive():
	while True:
		client,address= server.accept()
		print(f"Connected with {str(address)} ")
		client.send("NICK".encode('utf-8'))
		nickname = client.recv(1024)
		nicknames.append(nickname)
		clients.append(client)
		print(f"nickname of the clinet is {nickname}")
		broadcast(f"{nickname} connected to the server\n".encode('utf-8'))
		client.send("Connected to the server\n".encode('utf-8'))
		thread = threading.Thread(target=handle,args=(client,))
		thread.start()

print("Server")
receive()

