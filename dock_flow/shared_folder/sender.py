import socket
import time

# Создаем сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязываем сокет к IP-адресу и порту
server_address = ('0.0.0.0', 8000)
sock.bind(server_address)

# Начинаем прослушивать входящие соединения
sock.listen(1)

# Счетчик
cnt = 0

while True:
    # Ждем входящего соединения
    print(f"[SENDER] Waiting for a connection...")
    connection, client_address = sock.accept()

    try:
        print('Connection from', client_address)

        # Увеличиваем счетчик
        cnt += 1

        # Отправляем значение счетчика на vm2
        connection.sendall(str(cnt).encode())

    finally:
        # Очищаем входящее соединение
        connection.close()

    # Ждем 5 секунд перед следующей итерацией
    time.sleep(5)