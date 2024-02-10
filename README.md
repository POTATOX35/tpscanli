# Tps Canlı Skor

Bu küçük panel sayesinde TPS:Street Soccer maçları esnasında Discord üzerinden maç skorlarını canlı bir şekilde yayınlayabilirsiniz. 

# Nasıl Kurulur

Öncelikle Discord sunucusunda bir "Webhook" oluşturmamız gerek. Bunun için Sunucu Ayarları>Entegrasyonlar>Webhook'ları Görüntüle
sekmesine gelip yeni bir webhook oluşturuyoruz. 


Kendi tercihlerinize dayalı isim, logo ve kanal gibi etmenleri seçtikten sonra "Webhook URL'sini Kopyala" seçeneğine basıyoruz ve gerekli olan URL'yi panoya kopyalmış oluyoruz. 

    {"URL": "Your webhook url", "Everyonecheck": "True", "Lang": "tr_TR"}

Daha sonrasında klasör dizinin içindeki "settings.json" isimli dosyayı not defteri tarzı bir text editor ile açıyoruz.Bu dosyanın içindeki "URL: " Kısımdaki "Your Webhook Url" yazan karşılığı kendi panomuzdaki url ile değiştiriyoruz. 

Ayrıca aynı dosyadan "Everyonecheck: " kısımdaki karşılığı, "True"dan "False" hale getirerek everyone etiketlerini kapatabilirsiniz.

Kurulum bu kadardı...

# Nasıl Kullanılır

Klasör dizinindeki "main.exe" isimli dosyayı çalıştırıyoruz. Karşımıza çıkan menüde "Oyuncu Adı", "Takım Adı" gibi değerleri kendimize göre dolduruyoruz. Ardından "Maçı Başlat", "Maçı Bitir" butonlarla paneli kullanıyoruz.
