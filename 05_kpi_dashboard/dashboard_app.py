import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="FMCG Executive Dashboard", layout="wide")

st.title("📊 FMCG Executive Dashboard")

# Veri Yükleme
@st.cache_data
def load_data():
    df = pd.read_csv('data/mock_sales_data.csv')
    df['date'] = pd.to_datetime(df['date'])
    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error("Veri bulunamadı. Lütfen önce `python src/utils/data_generator.py` çalıştırın.")
    st.stop()

# Sidebar Filtreleri
st.sidebar.header("Filtreler")
selected_category = st.sidebar.multiselect("Kategori Seç", df['category'].unique(), default=df['category'].unique())

df_filtered = df[df['category'].isin(selected_category)]

# KPI Kartları
col1, col2, col3 = st.columns(3)
total_revenue = (df_filtered['quantity'] * df_filtered['unit_price']).sum()
total_qty = df_filtered['quantity'].sum()
avg_price = (df_filtered['quantity'] * df_filtered['unit_price']).sum() / total_qty

col1.metric("Toplam Ciro", f"₺{total_revenue:,.0f}")
col2.metric("Satış Adedi", f"{total_qty:,.0f}")
col3.metric("Ort. Sepet Tutarı", f"₺{avg_price:.2f}")

# Grafikler
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Zaman İçinde Satışlar")
    daily_sales = df_filtered.groupby('date')['quantity'].sum().reset_index()
    fig1 = px.line(daily_sales, x='date', y='quantity', title='Günlük Satış Trendi')
    st.plotly_chart(fig1, use_container_width=True)

with col_right:
    st.subheader("Kategori Bazlı Ciro")
    df_filtered['revenue'] = df_filtered['quantity'] * df_filtered['unit_price']
    cat_sales = df_filtered.groupby('category')['revenue'].sum().reset_index()
    fig2 = px.pie(cat_sales, values='revenue', names='category', title='Kategori Dağılımı', hole=0.4)
    st.plotly_chart(fig2, use_container_width=True)

st.info("Bu dashboard `data/mock_sales_data.csv` dosyasından beslenmektedir.")
