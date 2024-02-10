# Tps Canlı Skor

Bu küçük panel sayesinde TPS:Street Soccer maçları esnasında Discord üzerinden maç skorlarını canlı bir şekilde yayınlayabilirsiniz. 

# Özellikler
## Maç Başlangıç Ve Bitiş Mesajları
![image](https://github.com/POTATOX35/tpscanli/assets/81747015/813c77bb-b62b-4f8f-872d-2f3a0afe6336)

## Anlık Skor Geri Bildirimi
![image](https://github.com/POTATOX35/tpscanli/assets/81747015/2a03c79e-30a4-4ed0-9232-d469f8b6f696)

## Maç Sonu Gol Tablosu
![image](https://github.com/POTATOX35/tpscanli/assets/81747015/b94f9418-a1d8-4050-a602-31498b2639a5)


# Nasıl Kurulur

Öncelikle Discord sunucusunda bir "Webhook" oluşturmamız gerek. Bunun için Sunucu Ayarları>Entegrasyonlar>Webhook'ları Görüntüle
sekmesine gelip yeni bir webhook oluşturuyoruz. 

![Ssfromdiscord](https://github.com/POTATOX35/tpscanli/assets/81747015/e7a35387-2982-4141-9db6-5039f50e1c44)

Kendi tercihlerinize dayalı isim, logo ve kanal gibi etmenleri seçtikten sonra "Webhook URL'sini Kopyala" seçeneğine basıyoruz ve gerekli olan URL'yi panoya kopyalmış oluyoruz. 

    {"URL": "Your webhook url", "Everyonecheck": "True", "Lang": "tr_TR"}

Daha sonrasında klasör dizinin içindeki "settings.json" isimli dosyayı not defteri tarzı bir text editor ile açıyoruz.Bu dosyanın içindeki "URL: " Kısımdaki "Your Webhook Url" yazan karşılığı kendi panomuzdaki url ile değiştiriyoruz. 

Ayrıca aynı dosyadan "Everyonecheck: " kısımdaki karşılığı, "True"dan "False" hale getirerek everyone etiketlerini kapatabilirsiniz.

Kurulum bu kadardı...

# Nasıl Kullanılır

Klasör dizinindeki "main.exe" isimli dosyayı çalıştırıyoruz. Karşımıza çıkan menüde "Oyuncu Adı", "Takım Adı" gibi değerleri kendimize göre dolduruyoruz. Ardından "Maçı Başlat", "Maçı Bitir" butonlarla paneli kullanıyoruz.

![image](https://github.com/POTATOX35/tpscanli/assets/81747015/4c840f36-fd3d-4641-92c2-45a0e636ba58)
