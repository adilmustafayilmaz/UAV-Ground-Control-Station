# İHA Yer Kontrol İstasyonu - Kullanım Kılavuzu

## İçindekiler
1. [Giriş](#giriş)
2. [Başlarken](#başlarken)
3. [Kullanıcı Arayüzü Genel Bakış](#kullanıcı-arayüzü-genel-bakış)
4. [Üst Durum Çubuğu](#üst-durum-çubuğu)
5. [Sol Kontrol Paneli](#sol-kontrol-paneli)
   - [Sunucu Girişi](#sunucu-girişi)
   - [Telemetri Ekranı](#telemetri-ekranı)
6. [Görselleştirme Paneli](#görselleştirme-paneli)
   - [Harita Görünümü](#harita-görünümü)
   - [Kamera Beslemesi](#kamera-beslemesi)
   - [Konum Bilgisi](#konum-bilgisi)
7. [Görev Kontrol Paneli](#görev-kontrol-paneli)
   - [Otonom Uçuş Kontrolü](#otonom-uçuş-kontrolü)
   - [Rota Takibi](#rota-takibi)
8. [Düşman Uçak Seçimi](#düşman-uçak-seçimi)
9. [Acil Durum Kontrolleri](#acil-durum-kontrolleri)
10. [Klavye Kısayolları](#klavye-kısayolları)
11. [Sorun Giderme](#sorun-giderme)

## Giriş

İHA Yer Kontrol İstasyonu, İnsansız Hava Araçlarını (İHA) gerçek zamanlı olarak kontrol etmek ve izlemek için tasarlanmış gelişmiş bir uygulamadır. Bu kullanım kılavuzu, arayüzün her bileşeninin nasıl etkili bir şekilde kullanılacağına dair ayrıntılı talimatlar sağlar.

## Başlarken

### Sistem Gereksinimleri
- İşletim Sistemi: Windows, macOS veya Linux
- Minimum ekran çözünürlüğü: 1280 x 720 (1920 x 1080 önerilen)
- Python 3.6 veya daha yüksek, PyQt5 yüklü

### Kurulum
1. Python ve PyQt5'in sisteminizde yüklü olduğundan emin olun
2. UAV-Ground-Control-Station deposunu klonlayın veya indirin
3. Gerekli bağımlılıkları pip kullanarak yükleyin:
   ```
   pip install -r requirements.txt
   ```
4. Uygulamayı şu komutu çalıştırarak başlatın:
   ```
   python updated_uav_control_interface.py
   ```

## Kullanıcı Arayüzü Genel Bakış

İHA Yer Kontrol İstasyonu arayüzü birkaç ana alana ayrılmıştır:

- **Üst Çubuk**: Logo ve durum göstergelerini içerir
- **Sol Panel**: Giriş kimlik bilgilerini ve telemetri verilerini içerir
- **Orta Panel**: Harita görünümü ve kamera beslemesini gösterir
- **Alt Panel**: Görev kontrol seçeneklerini ve acil durum kontrollerini içerir

Arayüz, kritik görsel bilgilerin (harita ve kamera) görünürlüğünü en üst düzeye çıkaracak şekilde tasarlanmıştır ve kontrol işlevlerine kolay erişim sağlar.

## Üst Durum Çubuğu

### Bağlantı Durumu
- **Konum**: Ekranın sağ üst köşesi
- **Açıklama**: Yer istasyonu ile İHA arasındaki bağlantı durumunu gösterir
- **Durumlar**:
  - "BAĞLI" (yeşil): Sistem İHA'ya başarıyla bağlanmıştır
  - "BAĞLI DEĞİL" (kırmızı): İHA ile bağlantı kurulmamıştır
  - "BAĞLANIYOR" (sarı): Bağlantı kurulmaya çalışılıyor

### Batarya Durumu
- **Konum**: Sağ üst, Bağlantı Durumu'nun yanında
- **Açıklama**: İHA'nın mevcut batarya seviyesini gösterir
- **Özellikler**:
  - Batarya yüzdesinin görsel temsilini gösteren ilerleme çubuğu
  - Sayısal yüzde gösterimi
  - Renk göstergeleri: Yeşil (>%50), Sarı (%20-50), Kırmızı (<%20)

### Uçuş Modu
- **Konum**: Sağ üst, Batarya Durumu'nun yanında
- **Açıklama**: Uçuş kontrol modunu seçmek için açılır menü
- **Seçenekler**:
  - "Manuel": Kullanıcı İHA üzerinde doğrudan kontrole sahiptir
  - "Otonom": İHA önceden programlanmış görevleri veya algoritmik kontrolü takip eder

## Sol Kontrol Paneli

### Sunucu Girişi
- **Konum**: Uygulamanın sol üst köşesi
- **Amaç**: Uzaktan çalıştırma için İHA kontrol sunucusuna bağlanın
- **Bileşenler**:
  - **Kullanıcı adı alanı**: Yetkili kullanıcı adınızı girin
  - **Şifre alanı**: Güvenli şifrenizi girin (güvenlik için nokta olarak gösterilir)
  - **Giriş düğmesi**: Sunucuda kimlik doğrulaması yapmak için tıklayın
  - **Durum göstergesi**: Giriş tamamlandığında yeşil renkte "Başarılı" gösterir

### Telemetri Ekranı
- **Konum**: Sol panel, giriş bölümünün altında
- **Amaç**: Kritik uçuş parametrelerinin gerçek zamanlı gösterimi
- **Görüntülenen Bilgiler**:
  - **Yükseklik**: İHA'nın yer seviyesinden mevcut yüksekliği (metre cinsinden)
  - **Hava Hızı**: İHA'nın havaya göre hızı (saniyede metre cinsinden)
  - **Yer Hızı**: İHA'nın yere göre hızı (saniyede metre cinsinden)
  - **Mesafe**: Başlangıç noktasından itibaren kat edilen mesafe (metre cinsinden)
  - **Dikey Hız**: Tırmanma veya alçalma oranı (saniyede metre cinsinden)
  - **Yön**: İHA'nın baktığı yön (derece cinsinden, 0° = Kuzey)

## Görselleştirme Paneli

### Harita Görünümü
- **Konum**: Ana merkezi alan, sol taraf
- **Amaç**: İHA'nın konumunu, uçuş yolunu ve çevredeki araziyi gösterir
- **Özellikler**:
  - Gerçek zamanlı konum takibi
  - Rota görselleştirme
  - Geçiş noktası işaretleri
  - Ölçek göstergesi
  - Etkileşimli öğeler (tam uygulamada)

### Kamera Beslemesi
- **Konum**: Ana merkezi alan, sağ taraf
- **Amaç**: İHA'nın yerleşik kamerasından canlı video akışı
- **Özellikler**:
  - Gerçek zamanlı video akışı
  - Hedef tanımlama işaretleri (mevcut olduğunda)
  - Kilitleme durumu için görsel göstergeler

### Konum Bilgisi
- **Konum**: Harita ve Kamera görünümlerinin altında
- **Amaç**: İHA'nın kesin konum verisi
- **Görüntülenen Bilgiler**:
  - **Enlem**: Mevcut kuzey-güney konumu (derece cinsinden)
  - **Boylam**: Mevcut doğu-batı konumu (derece cinsinden)
  - **Göreceli Yükseklik**: Kalkış noktasından yükseklik (metre cinsinden)
  - **Mutlak Yükseklik**: Deniz seviyesinden yükseklik (metre cinsinden)

## Görev Kontrol Paneli

### Otonom Uçuş Kontrolü
- **Konum**: Ekranın alt kısmı, sol taraf
- **Amaç**: Kalkış ve iniş işlemleri için kontroller
- **Düğmeler**:
  - **Otonom Kalkış** (Yeşil): Otonom kalkış dizisini başlatır
  - **Manuel Kalkış** (Açık Yeşil): Kullanıcı kontrollü kalkış için hazırlar
  - **Otonom İniş** (Yeşil): Otonom iniş dizisini başlatır
  - **Manuel İniş** (Açık Yeşil): Kullanıcı kontrollü iniş için hazırlar

### Rota Takibi
- **Konum**: Ekranın alt kısmı, sol taraf, Kalkış ve İniş'in altında
- **Amaç**: Önceden tanımlanmış rota navigasyonu için kontroller
- **Düğmeler**:
  - **Rota Takibini Başlat** (Mavi): Önceden planlanmış rota boyunca navigasyona başlar
  - **Rotayı Duraklat**: Konumu korurken rota takibini geçici olarak durdurur
  - **Rotaya Devam Et**: Mevcut konumdan rota takibine devam eder
  - **Rotayı İptal Et**: Rota takibini tamamen iptal eder

## Düşman Uçak Seçimi

- **Konum**: Sağ alt bölüm
- **Amaç**: Hedef uçakların tanımlanması ve seçilmesi
- **Bileşenler**:
  - **Bilgi etiketi**: Kullanıcıya bir hedef seçmesini belirtir
  - **Uçak listesi**: Algılanan uçakları Takım ID'si, Yükseklik ve Hız bilgileriyle gösterir
  - **Seçim mekanizması**: Bir uçağı seçmek için üzerine tıklayın (açık mavi vurgulanır)
  - **HEDEF KİLİTLE düğmesi** (Turuncu): Seçimi onaylar ve seçilen uçağın takibini başlatır

## Acil Durum Kontrolleri

- **Konum**: Sağ alt köşe
- **Amaç**: Kritik güvenlik fonksiyonlarına hızlı erişim
- **Düğmeler**:
  - **Kalkış Noktasına Dön** (Turuncu): İHA'ya kalkış konumuna dönmesini emreder
  - **KAMİKAZE** (Koyu Kırmızı): Yönlendirilmiş çarpma dizisini başlatır (son derece dikkatli kullanın)
  - **ACİL DURUM DURDURMA** (Parlak Kırmızı): Acil durumlar için tüm motorları hemen keser
  
  > **UYARI**: Acil Durum Durdurma işlevi, İHA'nın mevcut konumundan düşmesine neden olacaktır. Yalnızca uçuşa devam etme riski kontrolsüz bir alçalma riskinden daha yüksek olduğu aşırı acil durumlarda kullanın.

## Klavye Kısayolları

| İşlev | Kısayol |
|----------|----------|
| Kalkış Noktasına Dön | F1 |
| Acil Durum Durdurma | F12 |
| Harita/Kamera Tam Ekran Geçişi | F11 |
| Manuel Moda Geç | Ctrl+M |
| Otonom Moda Geç | Ctrl+A |

## Sorun Giderme

### Bağlantı Sorunları
- Ağ bağlantınızın sabit olduğundan emin olun
- İHA'nın açık olduğunu ve iletişim menzilinde olduğunu doğrulayın
- Ayarlarda doğru sunucu adresinin yapılandırıldığını kontrol edin

### Ekran Sorunları
- Harita veya kamera beslemesi donmuş görünüyorsa, ilgili panellerdeki yenileme düğmesine tıklayın
- Boş ekranlar için veri kaynaklarının düzgün bağlandığını doğrulayın
- Harita ve kamera beslemeleri arasındaki bölücüyü sürükleyerek bölünmüş görünümü ayarlayın

### Acil Durum Prosedürleri
1. İHA yanıt vermez hale gelirse, önce "Kalkış Noktasına Dön" işlevini deneyin
2. Kontrol tekrar kazanılamazsa, son çare olarak "ACİL DURUM DURDURMA" düğmesini kullanın
3. Acil durumlarda mümkün olduğunca İHA ile görsel teması koruyun

---

Teknik destek için, lütfen sistem yöneticinize başvurun veya İHA Yer Kontrol İstasyonu paketinizle birlikte verilen teknik belgelere bakın.