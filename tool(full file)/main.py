from subdomain_finder import fetch_subdomains, save_to_json

def main():
    domain = input("Hedef Domain Giriniz: ").strip()
    subdomains = fetch_subdomains(domain)

    if subdomains:
        print(f"[+] Bulundu: {len(subdomains)} subdomains:")
        for subdomain in subdomains:
            print(f" - {subdomain}")
        
       
        output_data = {
            "domain": domain,
            "subdomains": subdomains
        }
       
        save_to_json(output_data)
    else:
        print("[-] Subdomain Bulunamadı.")

if __name__ == "__main__":
    main()
