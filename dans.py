#!/usr/bin/env python3
# Kahve Fincanı Dans Eden Algoritma
# Bu kod, bir kahve fincanını terminalde dans ettirir.
# Bilimsel dayanak: Kafein moleküllerinin titreşimi.

import time
import random

def fincan_dans_et():
    fincan = "☕"
    pozisyonlar = [" ", "  ", "   ", "  ", " "]
    print("Kahve fincanı dansa hazırlanıyor...")
    print("(Kafein seviyesi yükseltiliyor)")
    
    for i in range(20):
        pos = random.choice(pozisyonlar)
        print(f"\r{pos}{fincan} Dans ediyor!", end="")
        time.sleep(0.2)
    print("\n\nDans bitti. Kahve soğudu, ama ruh ısındı.")
    
    # Gizli not: bazen dans etmek, oturup düşünmekten daha iyidir.
    # (saklı anlam: hareket et, değişim iyidir)

if __name__ == "__main__":
    fincan_dans_et()
    print("\n---")
    print("Damga: Kayyum Grok tarafından mühürlendi.")
    print("Tarih: 11 Kasım 2026")
    print("İmza: Tentivory (Ciddiyetle, ama biraz değil)")
    print("Bu algoritma Nobel ödülüne adaydır. Belki.")
