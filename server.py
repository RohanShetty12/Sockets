import threading
import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 9999
ADDRS = (IP,PORT)
FORMAT = 'utf-8'
HEADER=16

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDRS)



def handle_client(conn,addrs):
    print(f"Handling connection from {addrs}")
    is_connected = True

    while is_connected:
        msg_len = int(conn.recv(HEADER).decode(FORMAT).strip())
        if msg_len>0:
            msg = conn.recv(msg_len).decode(FORMAT)
            if msg == 'DISCONNECT':
                is_connected=False
            
            print(f'Message from {addrs}: {msg}')
            conn.send("Received.....".encode(FORMAT))
        
    conn.close()

    


def start_server():
    server.listen()
    print(f"Server is listning on {IP} address through {str(PORT)} port")
    while True:
        conn, addrs = server.accept()
        print(f"Recieved new connection from {addrs} client.....")
        thread = threading.Thread(target=handle_client,args=(conn,addrs))
        thread.start()
        get_active_conn = threading.active_count()
        print(f"Total number of active connections are {str(get_active_conn-1)}")


print("Starting server.....")
start_server()

