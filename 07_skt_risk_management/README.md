# 07 - SKT Risk Management (Raf Ömrü Analizi)

> **"Çürüyen domates değil, parandır."**

Bu modül, FMCG'nin kanayan yarası olan **Fire (Waste/Shrinkage)** problemini minimize etmek için veri odaklı bir yaklaşım sunar. Son Kullanma Tarihi (SKT) yaklaşan ürünler için "Dinamik İndirim" stratejileri geliştirir.

## 🎯 Business Case
Perakendede brüt kâr marjları düşüktür (%3-%5). Bir ürünün çöpe atılması, o üründen edilecek kârı değil, ürünün **tüm maliyetini** zarara yazar.
Bu yüzden amaç:
1. Ürün SKT'si bitmeden satılabilsin.
2. Ama gereksiz yere çok erken indirim yapılmasın (Kâr kaybı olmasın).

## 🔧 Metodoloji (Risk Scoring)
1. **RSL (Remaining Shelf Life) Hesabı:** `SKT - Bugün` formülüyle kaç gün ömrü kaldığı bulunur.
2. **Bucket Analizi:** Ürünler risk gruplarına ayrılır (Örn: Kritik 7 gün, Normal 30 gün).
3. **Satış Hızı Korelasyonu:** Kalan gün sayısı azaldıkça satış hızı düşüyor mu? (Müşteri taze ürün mü seçiyor?)

### Karar Matriksi Örneği
| RSL (Kalan Gün) | Satış Hızı | Aksiyon |
|-----------------|------------|---------|
| > 30 Gün | Normal | Tam Fiyat |
| 15-30 Gün | Düşük | Bundle Kampanya |
| 7-14 Gün | Çok Düşük | %25 İndirim |
| < 7 Gün | Kritik | %50 İndirim (Elden Çıkar) |

## 🚀 Nasıl Çalıştırılır?

```bash
jupyter notebook 07_skt_risk_management/skt_risk.ipynb
```

## 📈 Beklenen Çıktılar
- Satılan ürünlerin RSL dağılım histogramı.
- Risk gruplarına göre ortalama satış fiyatı analizi.
- İndirim yapılması gereken ürünlerin listesi (Action List).
