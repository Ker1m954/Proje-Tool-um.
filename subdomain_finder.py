import http.client
import json

def fetch_subdomains(domain):
    
    print(f"[+] Collecting subdomains for {domain}...")
    try:
        conn = http.client.HTTPSConnection("crt.sh")
        
        conn.request("GET", f"/?q=%.{domain}&output=json")
        response = conn.getresponse()
        
        if response.status == 200:
            
            data = response.read().decode("utf-8")
            
            json_data = json.loads(data)
            subdomains = set(entry['name_value'] for entry in json_data)
            return list(subdomains)  # Convert set to list for JSON compatibility
        else:
            print(f"[-] crt.sh istegi basarisiz. Durum Kodu: {response.status}")
            return []
    except Exception as e:
        print(f"[-] crt.sh'dan gelen istekler basarisiz. {e}")
        return []

def save_to_json(data, filename="output.json"):
   
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"[+] Veri kaydedildi: {filename}")
    except Exception as e:
        print(f"[-] veri JSON'a kaydedilirken haya {e}")
