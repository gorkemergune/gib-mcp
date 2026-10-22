# İlk inceleme — 22 Ekim 2026
Hedef: https://gib.gov.tr/mevzuat/arama?tur=vergi-mevzuati&ktype=99&kanun-turu=ozelge

Doğrulanan: HTTP ile HTML alındı; Next.js /_next/static/chunks ve arama sayfası JS paketi var.
İlk HTML içinde özelge sonuçlarını doğrulayamadık. Bu, sitede dahili veri servisi olmadığı anlamına gelmez.
Henüz doğrulanmayan: arama endpoint'i, method/body, filtre adları, toplam sonuç, sayfalama,
detay URL/ID şeması, PDF ekleri, boş sonuç ve yüklenme durumlarının işaretleri.

Keşif betiği temiz Chromium oturumuyla ilk sayfanın HTML/metin/ekran görüntüsünü,
form kontrollerini ve fetch/XHR URL+durumlarını artifacts/ altına yazar.
İlk açılışı kaydeder; arama düğmesine basmaz. Sonraki geliştirmede gerçek kontrolleri incele,
bir sorgu gönder, sayfa değiştir ve detay aç; her adımın ağ isteğini karşılaştır.
Başlangıçta istek görülmemesi API yok anlamına gelmez. JSON body/parametre analizi ayrıca gerekir.
Artifacts içindeki URL ve metinler paylaşılmadan önce incelenmeli; git'e eklenmemeli.

## Codex yeniden kontrolü — 22 Ekim 2026
Desktop klasörü bu Codex oturumundan okunabiliyor ve yazılabiliyor. Diğer terminal
uygulamasının macOS izin durumu buradan belirlenemez; klasör taşıma zorunluluğu doğrulanmadı.
Playwright sandbox içinde MachPort Permission denied hatası verdi; izinli çalıştırmada açıldı.
İlk tarayıcı keşfi HTTP 200 döndürdü; body metni, form kontrolleri ve XHR listesi boştu.
Bu çıktı başarılı veri keşfi sayılmaz. İstek hatası ve JS hata kayıtları eklendi;
boş kontrol listesi artık incomplete ve çıkış kodu 2 üretir.
Gerçek stdio MCP initialize/list_tools/gib_status ve aramanın açık hata vermesi kontrolü geçti.
Bu, canlı özelge aramasının çalıştığı anlamına gelmez.
setup.sh artık editable yerine normal paket kurulumu yapar; yalnız headless Chromium
indirir. Böylece .pth bağımlılığı ve gereksiz tam tarayıcı indirmesi azaltıldı; önceki
lock hatasının kesin çözüldüğü henüz test edilmedi.

### İçerik bekleme düzeltmesinden sonraki sonuç
İkinci keşifte form ve metin yüklendi; request_failures ve script_errors boş.
Arama alanı DOM'da input#searchText (name=searchText) olarak görüldü.
Başlangıçta özelge sekmesi ve tarih filtreleri var; sonuç tablosunda 0 yazıyor.
Arama gönderilmediği için bu değer doğrulanmış bir sorgunun boş sonucu değildir.
Gözlenen POST isteği:
https://gib.gov.tr/api/gibportal/mevzuat/kanun/filterList?page=0&size=1000&sortFieldName=priority&sortType=ASC
Bu kanun listesini yükleyen istektir; özelge arama endpoint'i olarak kullanılmamalı.
Sonraki adım: searchText'e sorgu girip formu gönderirken ağ body/yanıtlarını incelemek.
