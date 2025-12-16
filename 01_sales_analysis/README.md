# 01 - Sales Analysis & EDA

> **"Ölçemediğini yönetemezsin."**

Bu modül, ham FMCG transactional verisini anlamlı iş içgörülerine dönüştürmenin ilk adımıdır. Veri setini tanır, temizler ve temel performans metriklerini (KPI) görselleştiririz.

## 🎯 Business Case
Bir FMCG şirketi için en temel sorular şunlardır:
- **Trend:** Satışlarımız artıyor mu azalıyor mu?
- **Seasonality:** Haftasonları veya bayramlarda satışlar ne kadar artıyor?
- **Pareto Prensibi:** Ciromuzun %80'ini ürünlerin hangi %20'si oluşturuyor?

Bu analiz, şirketin "fotoğrafını çekmek" gibidir. Stratejik kararlar (ürün delist etme, bölge odaklama) bu fotoğrafa bakılarak alınır.

## 📊 Veri Yapısı
Bu modül `data/mock_sales_data.csv` dosyasını kullanır:
- `date`: Satış tarihi
- `store_id`: Mağaza kimliği
- `product_id`: Ürün kimliği
- `category`: Ürün kategorisi (Beverages, Snacks vb.)
- `quantity`: Satılan adet
- `unit_price`: Birim satış fiyatı
- `is_promo`: O an indirimde miydi? (True/False)

## 🔧 Metodoloji
1. **Data Loading & Cleaning:** Tarih formatlarının düzeltilmesi, eksik veri kontrolü.
2. **Feature Engineering:** `Revenue` (Ciro) kolonunun oluşturulması (`quantity * unit_price`).
3. **Time Series Decomposition:** Günlük, haftalık ve aylık satış trendlerinin çizdirilmesi.
4. **Category Analysis:** Kategori bazlı ciro dağılımının (Pie/Bar chart) analizi.

## 🚀 Nasıl Çalıştırılır?

Jupyter Notebook ortamında adım adım analiz için:

```bash
# Ana dizinde olduğunuzdan emin olun
jupyter notebook 01_sales_analysis/sales_eda.ipynb
```

## 📈 Beklenen Çıktılar
- Günlük ciro trend grafiği.
- Kategorilerin cirodaki payını gösteren pasta grafik.
- Haftanın en yoğun gününü gösteren analiz.
