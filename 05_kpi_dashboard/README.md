# 05 - KPI Dashboard

> **"Veriyi göremezseniz, yönetemezsiniz."**

Bu modül, alt seviyedeki analitik modellerin ve veri yığınlarının "buzdağının görünen yüzü"dür. **Streamlit** kullanılarak geliştirilen bu interaktif dashboard, yöneticilerin anlık karar almasını sağlar.

## 🎯 Business Case
Üst düzey yöneticiler (C-Level) veya Bölge Müdürleri kod okumaz; grafik okur. Onların sabah kahvesini içerken şu sorulara cevap bulması gerekir:
- "Dün toplam ne kadar ciro yaptık?"
- "Hangi kategoride hedefi tutturamadık?"
- "Ortalama sepet tutarımız düşüyor mu?"

Bu dashboard, teknik karmaşıklığı soyutlayarak **Business Intelligence (BI)** katmanını oluşturur.

## 🔧 Metodoloji (Teknoloji Yığını)
- **Streamlit:** Python ile hızlı web uygulaması geliştirmek için.
- **Plotly:** İnteraktif (zoom yapılabilir, üzerine gelinebilir) grafikler için.
- **Pandas:** Arka plandaki veri manipülasyonu için.

### Gösterilen KPI'lar
1. **Toplam Ciro (Revenue):** Nakit akışı.
2. **Satış Adedi (Volume):** Operasyonel yük.
3. **Ortalama Sepet Tutarı (AOV):** Müşteri değeri.

## 🚀 Nasıl Çalıştırılır?

Bu bir web uygulamasıdır. Terminalden şu komutla başlatılır:

```bash
streamlit run 05_kpi_dashboard/dashboard_app.py
```
*Komutu çalıştırdıktan sonra tarayıcınızda otomatik olarak açılacaktır (Genellikle http://localhost:8501).*

## 📈 Özellikler
- **Sidebar Filtreleri:** İstediğiniz kategoriye veya mağazaya odaklanın.
- **Dinamik Kartlar:** Seçime göre anında güncellenen metrikler.
- **Responsive Tasarım:** Tablet veya geniş ekranda uyumlu görünüm.
