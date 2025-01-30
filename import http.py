from subdomain_finder import fetch_subdomains, save_to_json

def main():
    domain = input("Domain ismi giriniz: ").strip()
    subdomains = fetch_subdomains(domain)

    if subdomains:
        print(f"[+] Bulunan {len(subdomains)} Domainler:")
        for subdomain in subdomains:
            print(f" - {subdomain}")
        
       
        output_data = {
            "domain": domain,
            "subdomains": subdomains
        }
       
        save_to_json(output_data)
    else:
        print("[-] Domain bulunamadi.")

if __name__ == "__main__":
    main()
