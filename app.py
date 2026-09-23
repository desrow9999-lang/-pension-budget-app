import streamlit as st
from datetime import datetime, date

st.set_page_config(page_title="年金サイクルの家計簿", page_icon="📅")

st.title("📅 年金サイクルの家計簿")
st.caption("次の支給日まで安心して暮らすためのお金管理アプリ")

# サイドバー：設定
st.sidebar.header("受給・予算設定")
pension = st.sidebar.number_input("2カ月の年金受給額（合計）", value=200000, step=10000)
fixed_cost = st.sidebar.number_input("2カ月の固定費（家賃・光熱費など）", value=80000, step=5000)

# 本日の状況
st.subheader("💡 今日の状況")

# 簡易的に60日サイクルとして計算
total_days = 60
passed_days = 15  # 経過日数サンプル
remaining_days = total_days - passed_days

free_budget = pension - fixed_cost
daily_budget = free_budget / total_days if total_days > 0 else 0

col1, col2 = st.columns(2)
col1.metric("残り日数", f"{remaining_days} 日")
col2.metric("1日あたりの目安", f"約 {int(daily_budget):,} 円")

st.info("💡 今日使っていい金額を守れば、次の支給日まで赤字になりません！")

# 支出入力フォーム
st.subheader("🛒 支出を記録する")
with st.form("expense_form"):
    amount = st.number_input("金額", min_value=0, step=100)
    category = st.selectbox("カテゴリ", ["食費", "医療費", "光熱・日用品", "その他"])
    submitted = st.form_submit_button("追加する")
    if submitted:
        st.success(f"{category}に {amount:,} 円追加しました！")
