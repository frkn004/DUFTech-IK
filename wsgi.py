#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
DufTech AI Mülakat Sistemi - WSGI Başlatma Dosyası
www.aimulakat.duftech.com.tr

Bu dosya, Gunicorn veya diğer WSGI sunucuları tarafından
uygulamayı üretim ortamında başlatmak için kullanılır.
"""

import os
import logging
from app import app, start_file_watcher

# Dosya izleme sistemi
observer = None

if __name__ == "__main__":
    # Ana uygulama düz Python ile çalıştırıldığında
    logging.basicConfig(level=logging.INFO)
    print("\n=== DUF Tech Mülakat Sistemi Başlatılıyor (WSGI) ===")

    # Dosya izleme sistemini başlat
    observer = start_file_watcher()
    
    try:
        # Domain ve port bilgilerini al
        DOMAIN_NAME = os.getenv('DOMAIN_NAME', 'www.aimulakat.duftech.com.tr')
        PORT = int(os.getenv('PORT', 5000))
        
        print(f"\n[*] Web sunucusu başlatılıyor (Domain: {DOMAIN_NAME}, Port: {PORT})...")
        app.run(host='0.0.0.0', port=PORT)
    except Exception as e:
        print(f"\n[!] Program başlatılamadı: {str(e)}")
    finally:
        if observer:
            observer.stop()
            observer.join()
else:
    # WSGI sunucusu tarafından import edildiğinde
    # Dosya izleme sistemini başlat 
    observer = start_file_watcher()

# WSGI sunucusu için uygulama referansı
application = app 