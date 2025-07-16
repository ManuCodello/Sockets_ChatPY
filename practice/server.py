import socket
import threading


HOST = "127.0.0.1" #ip del servidor 
PORT = 55555

clientnames = {}
servidor_activo = False
server = None


def manejar_clientes (cliente_socket, direccion):
    try:
        # 1. Recibir nombre una sola vez
        nombre = cliente_socket.recv(1024).decode('utf-8')
        clientnames[cliente_socket] = nombre
        print(f"Cliente conectado desde {direccion}")
        broadcast(f"🔵 {nombre} se ha unido al chat.", cliente_socket)

        # 2. Loop de mensajes
        while True:
            mensaje = cliente_socket.recv(1024).decode('utf-8')
            if mensaje:
                broadcast(f"{nombre}: {mensaje}", cliente_socket)
    except Exception as e:
        nombre_cliente = clientnames.get(cliente_socket, "Desconocido")
        print(f"Error, {nombre_cliente} se ha desconectado: {e}")
        broadcast(f"{nombre_cliente} se fue del chat.", cliente_socket)


def eliminar_cliente(cliente_socket):
    if cliente_socket in clientnames:
        del clientnames[cliente_socket]
    
    try:
        cliente_socket.close()
    except:
        pass  # o loguear si querés


def broadcast (mensaje_enviado, cliente_excluido):
    for cliente in list(clientnames.keys()):
        if cliente != cliente_excluido:
            try:
                cliente.send(mensaje_enviado.encode('utf-8'))
            except Exception as e:
                cliente.close()
                print(f"Error, al enviar mensaje {e}")
                eliminar_cliente(cliente, clientnames)


def aceptar_clientes ():   
    while True:
        try:
            cliente_socket, direccion = server.accept()
            hilo = threading.Thread(target=manejar_clientes, args=(cliente_socket, direccion), daemon=True)
            hilo.start()
        except Exception as e:
            print(f"Error aceptando clientes: {e}")
            break


def control_servidor():
    global server, servidor_activo

    while True:
        comando = input("🛠️  Comando (abrir / cerrar / salir): ").strip().lower()

        if comando == "abrir" and not servidor_activo:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind((HOST, PORT))
            server.listen()
            servidor_activo = True
            print("Servidor ABIERTO y escuchando...")
            
            # Acá arrancás el hilo que acepta clientes
            threading.Thread(target=aceptar_clientes, daemon=True).start()
            

        elif comando == "cerrar" and servidor_activo:
            servidor_activo = False
            server.close()
            print("Servidor CERRADO (no acepta nuevos clientes)")

        elif comando == "salir":
            print("Cerrando servidor y terminando...")
            if servidor_activo:
                server.close()
            break

        else:
            print("Comando inválido o acción no disponible en este estado.")


if __name__ == "__main__":
    control_servidor()







