import streamlit as st
from datetime import datetime, date

# ページ設定
st.set_page_config(page_title="PENSION POCKET", page_icon="💳", layout="centered")

# スタイリッシュなデザイン
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
</style>
""", unsafe_allow_html=True)

# ヘッダー
st.markdown('<p class="main-title">PENSION POCKET</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">次の支給日まで、スマートに生き抜くお金の管理</p>', unsafe_allow_html=True)

# セッション状態の初期化（支出の記録用）
if 'expenses' not in st.session_state:
    st.session_state.expenses = []

# 設定セクション
st.markdown("### 💰 今回の受給・予算設定")
col_a, col_b = st.columns(2)
with col_a:
    pension = st.number_input("2カ月の年金受給額 (円)", value=200000, step=10000, key="pension_in")
with col_b:
    fixed_cost = st.number_input("2カ月の固定費 (円)", value=80000, step=5000, key="fixed_in")

# 計算ロジック
total_days = 60  
passed_days = 15  # 経過日数サンプル
remaining_days = total_days - passed_days

# 支出の合計を計算
total_spent = sum(item['amount'] for item in st.session_state.expenses)
free_budget = pension - fixed_cost - total_spent
daily_budget = free_budget / remaining_days if remaining_days > 0 else 0

# 本日の状況ダッシュボード
st.markdown("### ⚡ 本日の状況")
col1, col2 = st.columns(2)
with col1:
    st.metric(label="残り日数", value=f"{remaining_days} 日")
with col2:
    st.metric(label="1日あたりの目安", value=f"¥ {int(daily_budget):,}")

st.info("💡 今日使える目安額の範囲内に抑えることで、次の支給日まで安心して過ごせます。")

# 支出記録フォーム
st.markdown("### 🛒 支出を記録する")
with st.form("expense_form", clear_on_submit=True):
    amount = st.number_input("金額 (円)", min_value=0, step=100)
    category = st.selectbox("カテゴリ", ["食費", "医療費", "光熱・日用品", "その他"])
    submitted = st.form_submit_button("支出を追加する")
    if submitted and amount > 0:
        st.session_state.expenses.append({"category": category, "amount": amount})
        st.success(f"「{category}」に ¥{amount:,} を追加しました！")
        st.rerun()

# 記録した支出の一覧表示
if st.session_state.expenses:
    st.markdown("### 📝 最近の支出履歴")
    for idx, exp in enumerate(reversed(st.session_state.expenses)):
        st.write(f"- **{exp['category']}**: ¥{exp['amount']:,}")
