import socket   
import threading


#delcaramos los paramaetros del servidor host y el port
host = '127.0.0.1' #localhost
port = 55555

#creamos el socket para el servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #le pasamos los argumentos de tipo de red AF_INET = IPV4 Y SOCK_STREAM = TCP

#pasamos los datos de connexion del servidor
server.bind((host, port))
#estamos a la escucha a las conexiones
server.listen()
#pintamos por consola que el server esta corriendo
print(f"Server running on {host}:{port}")

#creamos dos listas para los cientes y los usernames
clients = []
usernames = []

#Enviamos los mensajes a todos los clientes que esten conectados en el servidor
def broadcast(message, _client):
    for client in clients:
        #verificamos que el cliente es diferente del que envio el mensaje
        if client != _client:
            #enviamos el mensaje
            client.send(message)
            
#definimos una funcion para cuando el usuario se desconecte
def disconnected_client(client):
    #obtenemos el index del cliente de la lista clients
    index = clients.index(client)
    #obtenemos su username de la lista usernames
    username = usernames[index]
    #enviamos un mensaje de cuando el cliente se desconecta
    broadcast(f"ChatBot: {username} disconnected".encode('utf-8'), client)
    #removemos el cliente
    clients.remove(client)
    #removemos su username
    usernames.remove(username)
    #cerramos la conexion con el cliente
    client.close()
    print(f"{username} disconnected")

#con esta funcion manejaremos los mensajes de cada usuario
def handle_messages(client):
    #siempre estara a la escucha
    while True:        
        try:
            #obtenemos el mensajes del cliente
            message = client.recv(1024) 
            broadcast(message, client) #enviamos el mensaje
        except:
            disconnected_client(client) #llamamos la funcion disconnected para cuando un client se desconecte 
            break

#aqui aceptaremos y manejaremos la conecciones 
def receive_connections():
    #Estara siempre en escucha
    while True:
        #obtenemos el clientesocket y el address 
        client, address = server.accept()
        # obtenemos el mensaje del username del usuario
        username = client.recv(1024).decode('utf-8')#codificamos con utf-8

        #agregamos a la lista clientes el cliente, y a la lista usernames el username
        clients.append(client)
        usernames.append(username)
        #imprimimos la persona que se ha conectado
        print(f"{username} is connected with {str(address)}")
        #mandamos un mensaje de la persona que se conecta al server
        message = f"ChatBot: {username} has joined the chat!".encode("utf-8")
        broadcast(message, client)
        client.send("Connected to server".encode("utf-8"))
        #creamos un hilo para cada uno de los clientes que se conecten al servidor
        thread = threading.Thread(target=handle_messages, args=(client,))
        thread.start() #iniciamos los hilos

receive_connections()