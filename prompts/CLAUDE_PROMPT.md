Bu klasördeki GİB özelge MCP projesini tamamla. Önce CLAUDE.md, README.md,
docs/ROADMAP.md ve docs/DISCOVERY.md oku. Claude in Chrome erişimim yok;
tarayıcı işlemlerini yerel Playwright Chromium ile yap.

Hedef sayfa:
https://gib.gov.tr/mevzuat/arama?tur=vergi-mevzuati&ktype=99&kanun-turu=ozelge

Önce mevcut dosyaları incele ve ortamı doğrula. Kurulum gerekirse scripts/setup.sh kullan.
Keşfi scripts/discover.sh ile başlat. Gerçek DOM'u inceleyip arama gönderme,
sayfalama ve bir detay açma adımlarını ekle. Gözlenen veri isteklerini belgeleyerek
herkese açık bir dahili servis varsa doğrudan HTTP adaptörü; yoksa DOM adaptörü geliştir.
API veya seçici tahmin etme. Iskeletteki DISCOVERY_REQUIRED hatalarını gerçek uygulamayla değiştir.

search_ozelge(query,page,page_size) ve get_ozelge(document_id) araçları gerçek veriler dönsün.
Sonuçlar resmi kaynak URL'si ve UTC erişim zamanı içersin. Sayfalama gerçek siteyle eşleşsin.
Kaynakta bulunmayan alanları null döndür. Engellenme ile boş sonucu ayır.
Site erişim kurallarını incele; düşük istek hızı, önbellek, timeout ve host sınırı uygula.
Kullanıcı tarayıcı profili veya Claude Chrome eklentisi kullanma.

Birim/fixture testlerini, sınırlı canlı arama+detay kontrolünü ve gerçek stdio MCP
initialize/list_tools/call_tool testini çalıştır. Gerekli belgeleri güncelle.
Tamamlanmış gibi görünen sahte örnek veri üretme. Erişim engeli varsa gözlenen hatayı
ve tamamlanamayan aşamayı açıkça belirt. En sonda nasıl çalıştıracağımı ve doğrulanan
sonuçları Türkçe anlat. Yayınlama veya toplu veri indirme yapma.
