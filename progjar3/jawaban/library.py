import logging
import requests
import socket
import os
import time
import datetime

def get_url_list():
    urls = dict()
    urls['ariana']='https://cdn0-production-images-kly.akamaized.net/w7IhEI_XqrT9rcN7M65Mq4CsYdI=/640x853/smart/filters:quality(75):strip_icc():format(webp)/kly-media-production/medias/1614051/original/021657000_1496631945-20170604-Ariana-Grande-Gelar-Konser-Amal-di-Manchester-AP-9.jpg'
    urls['oxford']='https://asset.kompas.com/crops/p4txjEosZq1J19zsXW8kYyTDQpE=/47x0:767x480/750x500/data/photo/2018/11/17/4058415081.jpg'
    return urls

def download_gambar(url=None,tuliskefile='image'):
    waktu_awal = datetime.datetime.now()
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/gif']='gif'
    tipe['image/jpeg']='jpg'
    tipe['application/zip']='jpg'
    tipe['video/quicktime']='mov'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        ekstensi = tipe[content_type]
        if (tuliskefile):
            fp = open(f"{tuliskefile}.{ekstensi}","wb")
            fp.write(ff.content)
            fp.close()
        waktu_process = datetime.datetime.now() - waktu_awal
        waktu_akhir =datetime.datetime.now()
        logging.warning(f"writing {tuliskefile}.{ekstensi} dalam waktu {waktu_process} {waktu_awal} s/d {waktu_akhir}")
        return waktu_process
    else:
        return False

def kirim_gambar(IP_ADDRESS, PORT, filename):
    print(IP_ADDRESS, PORT, filename)
    ukuran=os.stat(filename).st_size
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    fp=open(filename,'rb')
    k=fp.read()
    terkirim=0
    for x in k:
        k_bytes=bytes([x])
        clientSock.sendto(k_bytes,(IP_ADDRESS,PORT))
        terkirim=terkirim+1

if __name__=='__main__':
    k = download_gambar('https://cdn0-production-images-kly.akamaized.net/w7IhEI_XqrT9rcN7M65Mq4CsYdI=/640x853/smart/filters:quality(75):strip_icc():format(webp)/kly-media-production/medias/1614051/original/021657000_1496631945-20170604-Ariana-Grande-Gelar-Konser-Amal-di-Manchester-AP-9.jpg')
    print(k)