# 03 - Demand Forecasting (Talep Tahmini)

> **"Geleceği tahmin edemezsin, ama planlayabilirsin."**

Bu modül, geçmiş satış verilerini kullanarak gelecekteki talebi öngörmek için Facebook'un **Prophet** kütüphanesini kullanır.

## 🎯 Business Case
FMCG'de stok yönetimi bıçak sırtıdır:
- **Az Stok:** Yok satma (Out-of-Stock) -> Ciro kaybı ve müşteri memnuniyetsizliği.
- **Fazla Stok:** Depo maliyeti ve SKT (Son Kullanma Tarihi) riski -> İmha maliyeti.

Doğru talep tahmini, bu iki risk arasındaki mükemmel dengeyi (Optimal Stock Level) bulmayı sağlar.

## 🔧 Metodoloji
**Facebook Prophet** algoritması seçilmiştir çünkü:
1. **Mevsimsellik:** Haftalık (Hafta sonu artışı) ve Yıllık (Yaz/Kış) döngüleri otomatik algılar.
2. **Kayıp Veri:** Eksik günlerde bile çalışabilir.
3. **Trend Değişimi:** Kampanya dönemlerindeki ani sıçramaları (Changepoints) öğrenebilir.

## 🚀 Nasıl Çalıştırılır?

```bash
jupyter notebook 03_demand_forecasting/forecasting.ipynb
```

## 📈 Beklenen Çıktılar
- Önümüzdeki 30 günün günlük satış tahmini.
- Tahmin güven aralıkları (Lower/Upper Bound).
- Trend ve Mevsimsellik bileşenlerinin (Seasonality Components) ayrıştırılmış grafikleri.
