# 04 - Promotion Impact Analysis

> **"İndirim yaptık, çok sattık... Peki kâr ettik mi?"**

Bu modül, promosyonların (kampanyaların) satışlar üzerindeki **saf etkisini (incremental sales)** ölçmek için istatistiksel testler uygular.

## 🎯 Business Case
FMCG şirketleri pazarlama bütçelerinin büyük kısmını "Trade Promotion" (Ticari Pazarlama) aktivitelerine harcar. Ancak çoğu zaman şu sorular yanıtsız kalır:
- Satış artışı indirimden mi geldi, yoksa zaten mevsimsel olarak artacak mıydı?
- İndirim bittikten sonra satışlar dip yaptı mı? (Stoklama etkisi)

Bu analiz, **ROAS (Return on Ad Spend)** ve **ROI** hesaplamaları için kritik girdiyi sağlar.

## 🔧 Metodoloji (Uplift & A/B Test)
1. **Grup Karşılaştırması:** Promosyonlu günler vs Standart günler.
2. **T-Testi (Student's t-test):** İki grup arasındaki farkın istatistiksel olarak anlamlı (Significant) olup olmadığını test eder.
3. **Uplift Hesabı:** `(Promo Satış Ortalaması - Baz Satış Ortalaması) * Gün Sayısı` bize kampanyanın kazandırdığı ekstra satışı verir.

## 🚀 Nasıl Çalıştırılır?

```bash
jupyter notebook 04_promotion_impact/promotion_analysis.ipynb
```

## 📈 Beklenen Çıktılar
- Promosyonlu ve promosyonsuz dönemlerin ortalama satış grafiği.
- T-Test sonucu (P-Value yorumu).
- Kampanyanın başarı/başarısızlık kararı.
