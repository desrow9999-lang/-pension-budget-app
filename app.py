import streamlit as st
from datetime import datetime, date

# ページ設定
st.set_page_config(page_title="PENSION POCKET", page_icon="💳", layout="centered")

# スタイリッシュなデザインを適用するカスタムCSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&family=Noto+Sans+JP:wght@300;400;500;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Outfit', 'Noto Sans+JP', sans-serif;
    }
    
    .main-title {
        font-weight: 700;
        font-size: 2.2rem;
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    
    .sub-title {
        font-weight: 300;
        color: #666;
        font-size: 0.95rem;
        margin-bottom: 2rem;
    }
    
    .card {
        background: #ffffff;
        padding: 1.5rem;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        margin-bottom: 1.5rem;
        border: 1px solid #eaeaea;
    }
</style>
""", unsafe_allow_html=True)

# ヘッダー
st.markdown('<p class="main-title">PENSION POCKET</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">次の支給日まで、スマートに生き抜くお金の管理</p>', unsafe_allow_html=True)

# メイン画面での入力セクション
st.markdown("### 💰 今回の受給・予算設定")
with st.container():
    col_a, col_b = st.columns(2)
    with col_a:
        pension = st.number_input("2カ月の年金受給額 (円)", value=200000, step=10000)
    with col_b:
        fixed_cost = st.number_input("2カ月の固定費 (円)", value=80000, step=5000)

# 計算ロジック
total_days = 60  
passed_days = 15  # 経過日数のサンプル
remaining_days = total_days - passed_days

free_budget = pension - fixed_cost
daily_budget = free_budget / total_days if total_days > 0 else 0

# 本日の状況ダッシュボード
st.markdown("### ⚡ 本日の状況")
col1, col2 = st.columns(2)
with col1:
    st.metric(label="残り日数", value=f"{remaining_days} 日")
with col2:
    st.metric(label="1日あたりの目安", value=f"¥ {int(daily_budget):,}")

st.info("💡 今日使える目安額の範囲内に抑えることで、次の支給日まで安心して過ごせます。")

# 支出記録
st.markdown("### 🛒 支出を記録する")
with st.form("expense_form", clear_on_submit=True):
    amount = st.number_input("金額 (円)", min_value=0, step=100)
    category = st.selectbox("カテゴリ", ["食費", "医療費", "光熱・日用品", "その他"])
    submitted = st.form_submit_button("支出を追加する")
    if submitted:
        st.success(f"「{category}」に ¥{amount:,} を記録しました！")
