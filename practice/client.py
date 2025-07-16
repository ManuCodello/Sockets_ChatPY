import socket
import threading

HOST = "127.0.0.1"
PORT = 55555

def recibir_mensaje(cliente):
    while True:
        try:
            respuesta = cliente.recv(1024)
            if not respuesta:
                print(" El servidor se desconectó.")
                break
            print(respuesta.decode('utf-8'))
        except Exception as e:
            print("Error al recibir mensaje:", e)
            break

def main():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((HOST, PORT))

    nombre = input("Tu nombre: ")
    cliente.send(nombre.encode('utf-8'))

    threading.Thread(target=recibir_mensaje, args=(cliente,), daemon=True).start()

    while True:
        mensaje = input()
        if mensaje.lower() == "/salir":
            cliente.close()
            break
        cliente.send(mensaje.encode('utf-8'))

if __name__ == "__main__":
    main()





