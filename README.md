# Final-Projem.
Bu benim İleri Sızma dersimin final projesidir. İçeriğinden istediğinizce yararlanabilirsiniz.
İsim Ve Numara: Mehmet Kerim SAİN - 2320191033

# Projenin işlevi ve içeriği.
Bu projede VSCode ile Python kodlarıyle crt.sh kullanarak bir bir domain adresinin alt alan adını (subdomain name) bulan bir tool yaptım. Denemeler ve testler sonuncunda
Bu tool'un kaynak kodlarınıda sizinle paylaşmaya karar verdim. 
Aklınızda olan soruları veya geliştirme için önerilerinizi profilimde bulunan E-mail adresime gönderebilirsiniz.
Bu tool'u üzerinde güvenlik zafiyeti deneyeceğiniz 
internet sitesinin domain adresini girerek adlarını öğrenebilir ve şüpheli veya zayıf 
gördüğünüz alanlara ekstra tarama veya zafiyet testi saldırıları yaparak açık oluşturabilirsiniz.
#Kurulum Ve Çalıştırma
"gerekenler.txt" dosyasını açarak gereken VSCode ve Python'u indiriyoruz. Sonrasında verdiğim Pyhton uzantılı iki dosyayı indirerek tek bir klasör içerisine koyuyoruz ve VSCode'u çalıştırıyoruz. Daha sonrasında ise "import http" dosyasını açıp F5 tuşuna basarak çalıştırabiliriz.
Terminalde karşımıza çıkan yere istediğimiz domain adını yazıyoruz ve sonuçların yazdırılarak "output.json" adında ve formatında bir dosyaya kaydedilmesini bekliyoruz.
# Zorunlu Parametre
def main():
    domain = input("Domain ismi giriniz: ").strip()
    subdomains = fetch_subdomains(domain)
