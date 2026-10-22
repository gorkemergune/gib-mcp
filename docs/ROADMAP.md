# Yol haritası

1. Ortam: Python sanal ortamı, MCP SDK, Playwright Chromium. Chrome eklentisi gerekmez.
   Bitiş: kurulum ve gib_status MCP çağrısı başarılı.
2. Keşif: site erişim kuralları/robots.txt incele; ilk sayfa, bir arama, ikinci sonuç sayfası,
   bir özelge detayı ve boş sonuç örneğini kaydet. Görsel kontrol ve ağ gözlemini karşılaştır.
   Bitiş: docs/DISCOVERY.md içinde kanıtlı endpoint/body veya DOM seçicileri.
3. Adaptör: doğrulanmış kamuya açık veri isteği varsa HTTP istemcisi ekle. Yoksa Playwright
   yaşam döngüsü ve gözlenmiş DOM seçicileriyle arama/detay çıkar. Her hata için tarayıcıyı kapat.
   Bitiş: aynı sorgu ve sayfa için siteyle eşleşen gerçek kayıtlar.
4. Veri sözleşmesi: arama sonucu items=[document_id,title,date,number,authority,source_url],
   page, page_size, total (bilinmiyorsa null), has_next, fetched_at, warnings.
   Detay: aynı metadata + full_text ve varsa ek bağlantıları. Kaynakta olmayan alan null.
   Tarih ISO biçiminde; özgün tarih de korunur. Tam metin kırpılırsa açıkça belirtilir.
5. Dayanıklılık: GİB host allowlist ve yönlendirme kontrolü; 2 sn istek aralığı,
   tek eşzamanlı işlem, 10 dk önbellek, zaman aşımı ve en fazla 2 geçici hata tekrarı.
   429'da Retry-After'a uy; 403/CAPTCHA'yı açık hata olarak dön. Hata asla boş sonuç olmasın.
6. MCP: iskelet search_ozelge ve get_ozelge araçlarını gerçek adaptöre bağla.
   Filtreleri ancak keşifte doğrulanınca ekle. stdio dışında gereksiz HTTP sunucusu kurma.
7. Kabul: Türkçe sorgu, boş sonuç, sayfa sınırı, ikinci sayfa, geçersiz ID, timeout,
   403/429, metin çıkarma ve kaynak bağlantısı kontrolleri; fixture testleri ve sınırlı canlı test.
   Son olarak gerçek MCP istemcisiyle initialize → list_tools → call_tool test et.
   Bitiş: Claude /mcp bağlı; gerçek arama ve detay çağrıları kanıtlarıyla başarılı.

İlk sürüm kapsamı: özelge arama ve detay. Tüm siteyi indeksleme, OCR, veritabanı,
web arayüzü ve hukuki yorumlama sonraki sürüme bırakılır.
