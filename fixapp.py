#!/usr/bin/env python3
import re

# Dosyayı oku
with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# İlk ve ikinci save_photo bloklarını bul
matches = re.finditer(r'@app\.route\(\'/save_photo\', methods=\[\'POST\'\]\)\s*def save_photo\(\):', content)
positions = [m.start() for m in matches]

if len(positions) < 2:
    print("İki save_photo fonksiyonu bulunamadı!")
    exit(1)

# İlk save_photo'dan başlayalım
first_save_photo_start = positions[0]

# İlk save_photo ile get_speech arasındaki bloğu kaldır
get_speech_pos = content.find("@app.route('/get_speech'", first_save_photo_start)
if get_speech_pos == -1:
    print("get_speech fonksiyonu bulunamadı!")
    exit(1)

# Yeni içerik: ilk save_photo'yu kaldır
new_content = content[:first_save_photo_start] + content[get_speech_pos:]

# Yazdır
with open('app.py.fixed', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Dosya başarıyla düzenlendi! app.py.fixed dosyasını kontrol edin.")
