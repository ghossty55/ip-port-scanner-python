# 🛰️ IP + Port Scanner - Python Pentesting Tool

**Autor:** Ghossty  
**Descripción:**  
Este script escanea una subred completa (192.168.x.0/24) para encontrar dispositivos activos, obtener sus hostnames, direcciones MAC, fabricantes y puertos abiertos comunes.  
Es una herramienta de **reconocimiento (recon)** para pruebas de penetración (pentesting) en entornos controlados.

---

## 🧰 Características

- Escaneo completo de IPs activas (con ping)
- Resolución de nombres de host
- Escaneo de puertos comunes (21, 22, 23, 80, 443, etc.)
- Detección de direcciones MAC
- Identificación del fabricante mediante archivo local (OUI)
- Guarda los resultados en `scan_results.txt`

---

## ⚙️ Requisitos

- Python 3
- Sistema operativo Windows o Linux
- Archivo `oui_vendors.txt` (con datos de fabricantes) solo tiene datos basicos para mayor deteccion modifica este archivo de texto y agregalos siguiendo el mismo formato

### 🔌 En Windows:
Debés ejecutar la terminal como **administrador** para que `arp -a` funcione correctamente.

---

## 🚀 Uso

```bash
python3 ip_scanner.py
```

Cuando se te pida, ingresá la subred base:
```
Enter the base subnet 🌐: 192.168.1
```

El archivo `scan_results.txt` se generará automáticamente con todos los resultados.

---

## 📦 Ejemplo de salida

```txt
📊 Network Scan Results

IP: 192.168.1.1
Hostname: name not available ❌
MAC: cc-19-a8-e6-e8-4f
Vendor: Unknown
Open Ports: 22, 23, 80, 443
----------------------------------------
```

---

## 📈 Mejoras futuras

- Exportar resultados a `.csv` y `.json`
- Detección sin ping (`ARP scan`, `nmap -Pn`)
- Módulo con `python-nmap`
- Scan personalizado por rango de puertos
- UI en terminal con `rich` o `textual`

---

## ⚖️ Licencia

Este proyecto está licenciado bajo la **MIT License**.  
Podés usar, modificar y compartir el código libremente, pero **sin garantía**.  
Para más información, consultá el archivo `LICENSE`.
