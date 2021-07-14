# Load Balancing

Semua backend berada pada port 9000 keatas (2 backend -> port 9000, 9001. 3 backend -> port 9000 - 9002. dst)
Load balancer ada di port 4444

## Threaded

1. Buat beberapa terminal untuk beberapa backend server. Pada setiap terminal jalankan `python3 server_thread_http -p <port berdasarkan jumlah server>`. Kalau 4 server, berarti `python3 server_thread_http -p 9000` sampai `python3 server_thread_http -p 9003`
2. Jalankan `python3 lb.py -n <jumlah backend server>`


## Asynchronous

masih otw gesss 😭😭😭
