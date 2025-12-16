# 06 - Price Optimization

> **"Fiyat Sanattır, Elastikiyet ise Bilim."**

Bu modül, mikroekonominin temel taşı olan **Fiyat Elastikiyetini (Price Elasticity of Demand)** hesaplayarak, kârlılığı veya ciroyu maksimize edecek optimal fiyat noktasını bulmayı hedefler.

## 🎯 Business Case
Fiyatlandırma, kârlılık üzerindeki en güçlü kaldıraçtır.
- Fiyatı %10 artırırsam satışlar %5 mi düşer (Kârlıyım), yoksa %20 mi düşer (Zarardayım)?
- Hangi ürünler "Fiyat Duyarsız" (Inelastic)? Bu ürünlere zam yapmak güvenli olabilir.
- Hangi ürünler "Fiyat Duyarlı" (Elastic)? Bu ürünlerde indirim yapmak trafiği artırır.

## 🔧 Metodoloji (Log-Log Regresyon)
Analiz için OLS (Ordinary Least Squares) Regresyon yöntemi kullanılır.
Model: `ln(Quantity) = α + β * ln(Price)`

Buradaki **β (beta)** katsayısı doğrudan elastikiyeti verir:
- **β < -1:** Elastik (Fiyat artarsa talep çok düşer).
- **-1 < β < 0:** İnelastik (Fiyat artsa da talep az düşer -> **Zam Fırsatı!**).

## 🚀 Nasıl Çalıştırılır?

```bash
jupyter notebook 06_price_optimization/price_elasticity.ipynb
```

## 📈 Beklenen Çıktılar
- Seçilen ürün için Fiyat vs Talep saçılım grafiği (Scatter Plot).
- Regresyon model özeti (R-squared, Coefficients).
- Ürünün elastikiyet sınıflandırması (Fırsat/Risk yorumu).
