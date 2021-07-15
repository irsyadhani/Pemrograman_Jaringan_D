from file_client_cli import remote_get
import time
import datetime
import threading
import socket

def kirim_semua():
    texec = dict()
    daftar = 'pokijan.jpg'

    catat_awal = datetime.datetime.now()
    for k in range(100):
        print(f"mengirim {k}")
        texec[k] = threading.Thread(target=remote_get, args=(daftar,))
        texec[k].start()
        
    for k in range(100):
        texec[k].join()

    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")

if __name__=='__main__':
    kirim_semua()