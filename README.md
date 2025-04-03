# 🛰️ IP + Port Scanner - Python Pentesting Tool

**Author:** Ghossty  
**Description:**  
This script scans a full subnet (e.g., 192.168.x.0/24) to find active devices, retrieve their hostnames, MAC addresses, manufacturers, and commonly open ports.  
It is a **reconnaissance tool** for penetration testing in controlled environments.

---

## 🧰 Features

- Full active IP scan (with ping)
- Hostname resolution
- Scan for common ports (21, 22, 23, 80, 443, etc.)
- MAC address detection
- Manufacturer identification via local OUI file
- Saves results in `scan_results.txt`

---

## ⚙️ Requirements

- Python 3
- Operating system: Windows or Linux
- `oui_vendors.txt` file (contains basic vendor data; for better detection, you can edit and add more entries using the same format)

### 🔌 Windows note:
You must run the terminal as **administrator** for `arp -a` to work correctly.

---

## 🚀 Usage

```bash
python3 ip_scanner.py
```

When prompted, enter the base subnet:
```
Enter the base subnet 🌐: 192.168.1
```

The `scan_results.txt` file will be automatically created with all scan results.

---

## 📦 Example Output

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

## 📈 Future Improvements

- Export to `.csv` and `.json`
- Ping-less detection (`ARP scan`, `nmap -Pn`)
- Integration with `python-nmap`
- Custom port range scanning
- Terminal UI with `rich` or `textual`

---

## ⚖️ License

This project is licensed under the **MIT License**.  
You can use, modify, and share the code freely, but **without warranty**.  
For more details, check the `LICENSE` file.
