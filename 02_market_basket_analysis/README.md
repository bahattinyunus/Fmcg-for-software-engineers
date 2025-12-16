# 02 - Market Basket Analysis (Sepet Analizi)

> **"Cola alan Cips de alır... ama ya Bebek Bezi alan Bira da alıyorsa?"**

Bu modül, perakendeciliğin en klasik ve en güçlü veri madenciliği uygulamasını, **Association Rule Learning** yöntemini kullanarak uygular.

## 🎯 Business Case
Müşterilerin alışveriş alışkanlıklarını çözmek, çapraz satış (Cross-sell) fırsatları yaratır.
- **Raf Dizilimi:** Birlikte alınan ürünleri yan yana koymak.
- **Bundle Önerisi:** "Bu ikisini alana %10 indirim" kampanyası kurgulamak.
- **E-Ticaret Önerisi:** "Bunu alanlar şunu da aldı" widget'ı.

## 🔧 Metodoloji (Apriori Algoritması)
Analiz için `mlxtend` kütüphanesi kullanılır.

1. **Transaction Matrix:** Veri, `Sepet ID` x `Ürün` formatına (Binary Matrix) çevrilir.
2. **Frequent Itemsets:** Belirli bir eşik değerinin (Support) üzerinde görülen ürün ikilileri bulunur.
3. **Rule Generation:** Lift ve Confidence değerlerine göre kurallar çıkarılır.

### Temel Metrikler
- **Support:** X ve Y'nin birlikte görülme sıklığı.
- **Confidence:** X alındığında Y'nin alınma olasılığı.
- **Lift:** X'in satışı Y'nin satışını ne kadar artırıyor? (Lift > 1 ise pozitif ilişki).

## 🚀 Nasıl Çalıştırılır?

```bash
jupyter notebook 02_market_basket_analysis/market_basket.ipynb
```

## 📈 Örnek Senaryo
*Çıktı:* `Rule: {Bread} -> {Milk}, Lift: 1.5`
*Yorum:* Ekmek alanların süt alma ihtimali, normalden 1.5 kat daha fazla. O zaman ekmek reyonunun yanına süt dolabı koyalım veya kahvaltı paketi yapalım.
