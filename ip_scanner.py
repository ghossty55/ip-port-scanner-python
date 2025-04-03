#IP Scanner + Port Scanner totalmente integrados\
#Detecta el sistema operativo (Windows/Linux)
#Escanea IPs activas y obtiene hostname
#Usa ARP para encontrar direcciones MAC
#Escanea puertos comunes de cada IP activa
#Muestra resultados completos al final

import os
import platform
import socket
import subprocess
import re


current_dir= os.path.dirname(os.path.abspath(__file__))
oui_path = os.path.join(current_dir,"oui_vendors.txt")


def load_oui_vendors(file_path):
    vendors={}
    try:
        with open(file_path, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    oui = parts[0].lower()
                    vendor= parts [1].strip()
                    vendors[oui] = vendor 
        
    except FileNotFoundError:
        print("⚠️    file not found. Vendor detection disabled.")
    return vendors





oui_vendors = load_oui_vendors(oui_path) 
# 🚪 Función para escanear puertos en una IP usando TCP (connect scan)
def scan_ports(ip, ports):
    open_ports=[]
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)# espera medio segundo por puerto digase 500 milisegundos
        result = s.connect_ex((ip,port))
        if result == 0:
            open_ports.append(port)
        s.close()    
    return open_ports    


# Detectar sistema operativo
is_windows = platform.system().lower() == "windows"
param = "-n" if is_windows else "-c"


# Obtener subred
subnet = input("Enter the base subnet 🌐: ")

print(f"\n🔍 Scanning devices on the network.......{subnet}.0/24.....\n")

devices = {}

common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]

for i in range(1, 255):
    ip = f"{subnet}.{i}"
    print(f"🔎 Scanning IP: {ip}")

    if is_windows:
        cmd = f"ping {param} 1 -w 300 {ip} > nul"
    else:
        cmd = f"ping {param} 1 {ip} > /dev/null"

    response = os.system(cmd)

    if response == 0:     #esto asegura si la ip respondio (0 es si y 1 es no) por eso ==0
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except socket.herror:
            hostname = "name not available ❌"

        # 📘 Aquí guardamos la IP activa con su hostname
        devices[ip] = {
            "hostname": hostname,
            "mac": "⏳ Searching...",
            "vendor" : "Unknown"
        
        }
        
        
     
    
    
    
    
        open_ports= scan_ports(ip, common_ports)
        devices[ip]["ports"] = open_ports
    
    
#ARP (addres resolution protocol)
# 🧪 Obtener tabla ARP y asociar MACs
try:
    arp_output = subprocess.check_output("arp -a", shell=True).decode()
    arp_matches = re.findall(r"(\d+\.\d+\.\d+\.\d+)\s+([-a-fA-F0-9:]{17})", arp_output)

    for ip, mac in arp_matches:
        mac=mac.lower().replace("-", ":")
        if ip in devices:
            devices[ip]["mac"] = mac
            oui =mac[:8]
            vendor=oui_vendors.get(oui, "Unknown")
            devices[ip]["vendor"] = vendor
            
except Exception as e:
    print(f"⚠️ Error while executing arp: {e}")


def save_results_to_txt(devices, filename="scan_results.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("📊 Network Scan Results\n\n")
        
        for ip, info in devices.items():  # ✅ Aquí se recorre todo el diccionario
            f.write(f"IP: {ip}\n")
            f.write(f"Hostname: {info.get('hostname', 'Unknown')}\n")
            f.write(f"MAC: {info.get('mac', 'N/A')}\n")
            f.write(f"Vendor: {info.get('vendor', 'Unknown')}\n")
            open_ports = info.get("ports", [])
            if open_ports:
                f.write("Open Ports: " + ", ".join(str(p) for p in open_ports) + "\n")
            else:
                f.write("Open Ports: None\n")
            f.write("-" * 40 + "\n")

    print(f"\n💾 Results saved to {filename}")



for ip, mac in arp_matches:
     mac=mac.lower()
     if ip in devices:
        devices[ip]["mac"] = mac
        oui =mac[:8]
        vendor=oui_vendors.get(oui, "Unknown")
        devices[ip]["vendor"] = vendor


# 📋 Mostrar resultados finales
print("\n📊 Devices found:")
for ip, info in devices.items():
    if "vendor" not in info:
        info["vendor"] = "Unknown"
    print(f"✅ IP: {ip} | 🖥️ Hostname: {info['hostname']} | 🔌 MAC: {info['mac']} | 🏷️ Vendor: {info['vendor']}")

save_results_to_txt(devices)
