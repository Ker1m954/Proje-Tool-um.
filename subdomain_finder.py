import http.client
import json

def fetch_subdomains(domain):
    
    print(f"[+] Subdomainler bulunuyor... {domain}...")
    try:
        conn = http.client.HTTPSConnection("crt.sh")
     
        conn.request("AL", f"/?q=%.{domain}&output=json")
        response = conn.getresponse()
        
        if response.status == 200:
           
            data = response.read().decode("utf-8")
            
            json_data = json.loads(data)
            subdomains = set(entry['name_value'] for entry in json_data)
            return list(subdomains)  
        else:
            print(f"[-] crt.sh istegi başarisiz. Durum Kodu: {response.status}")
            return []
    except Exception as e:
        print(f"[-] crt.sh veri alirken hata meydana geldi {e}")
        return []

def save_to_json(data, filename="output.json"):
  
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"[+] Veri Kaydedildi: {filename}")
    except Exception as e:
        print(f"[-] veri JSON'a kaydedilirken hata meydana geldi. {e}")
