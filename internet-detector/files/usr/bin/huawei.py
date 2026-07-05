#!/usr/bin/env python3
from huawei_lte_api.Client import Client
from huawei_lte_api.Connection import Connection
import time

def main():
    # Kredensial modem
    router_ip = '192.168.8.1'
    username = 'admin'
    password = 'admin'

    # Masukkan username dan password langsung ke dalam Connection
    # Ini adalah cara yang lebih kompatibel untuk berbagai versi library
    connection_url = f'http://{username}:{password}@{router_ip}/'

    try:
        print("Menghubungkan ke modem...")
        with Connection(connection_url) as connection:
            client = Client(connection)
            
            print("="*40)
            print("Berhasil Login - Mengambil Info...")
            print("="*40)
            
            # Ambil info perangkat
            wan_info = client.device.information()
            wan_ip = wan_info.get('WanIPAddress')
            device_name = wan_info.get('DeviceName')
            
            print(f"Device Name: {device_name}")
            print(f"IP WAN Sekarang: {wan_ip}")
            
            # Memicu perubahan IP
            print("Memicu proses perubahan IP...")
            client.net.plmn_list()
            
            print("\033[92mPerintah perubahan IP terkirim!\033[0m")

    except Exception as e:
        print(f"\033[91mError: {e}\033[0m")
        print("Jika error 125002, berarti sesi masih tersangkut di modem.")

if __name__ == "__main__":
    main()
