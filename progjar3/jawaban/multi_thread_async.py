from library import download_gambar,get_url_list, kirim_gambar
import time
import datetime
import concurrent.futures

def kirim_server():
    texec = dict()
    urls = get_url_list()
    status_task = dict()
    temp = 0
    task = concurrent.futures.ThreadPoolExecutor(max_workers=4)
    catat_awal = datetime.datetime.now()
    for k in urls:
        download_gambar(urls[k], k)
        print(f"mendownload {urls[k]}")
        waktu = time.time()
        UDP_IP_ADDRESS = "192.168.122.208"
        UDP_IP_ADDRESS2 = "192.168.122.214"
        PORT = 5003
        if temp == 0:
            texec[k] = task.submit(kirim_gambar, UDP_IP_ADDRESS,PORT,f"{k}.jpg")
            print('Masuk server 1')
            temp = temp+1
        elif temp == 1:
            print('Masuk server 2')
            texec[k] = task.submit(kirim_gambar, UDP_IP_ADDRESS2,PORT,f"{k}.jpg")
    for k in urls:
        status_task[k]=texec[k].result()
    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")
    print("hasil task yang dijalankan")
    print(status_task)
if __name__=='__main__':
    kirim_server()