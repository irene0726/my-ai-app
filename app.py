import streamlit as st
import google.generativeai as genai

# 1. 呼叫雲端保險箱裡的金鑰
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

# 2. 使用最新 2.5 版本模型
model = genai.GenerativeModel('gemini-2.5-flash')

# --- 網頁前端介面設計 ---
st.set_page_config(page_title="全能口碑操盤分析儀", page_icon="📝", layout="wide")

# ==========================================
# 🛡️ 隱藏魔法：移除所有 Streamlit 標籤、按鈕與浮水印，打造純淨版面
# ==========================================
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
[data-testid="stToolbar"] {visibility: hidden;}
[data-testid="stHeader"] {visibility: hidden;}
footer {visibility: hidden;}
/* 讓分頁籤的字體稍微放大，增加質感 */
.stTabs [data-baseweb="tab-list"] {
    gap: 10px;
}
.stTabs [data-baseweb="tab"] {
    font-size: 16px;
    padding-top: 10px;
    padding-bottom: 10px;
}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ==========================================
# 💎 主標題區
# ==========================================
st.title("📝 全能口碑操盤與危機處理分析儀")
st.markdown("專屬 AI 輿情監測與公關防護主控台")
st.divider()

# ==========================================
# 🗂️ 核心功能：使用「分頁籤 (Tabs)」取代傳統按鈕 (加入第五分頁)
# ==========================================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "✅ 一般產品常規健檢", 
    "🏥 醫美口碑鋪陳製造機", 
    "⚖️ 醫美療程彈性大比拼", 
    "🚨 特定負評拆彈與攻防",
    "🎓 語氣訓練儀"
])

# ------------------------------------------
# 🚪 第一分頁：一般產品常規健檢
# ------------------------------------------
with tab1:
    st.info("💡 **操作指南**：輸入產品或品牌名稱，AI 將自動彙整各大論壇真實聲量與優缺點。")
    product_name = st.text_input("📦 請輸入想查詢的「產品或品牌名稱」：", placeholder="例如：理膚寶水 B5")
    
    if st.button("🚀 開始深度健檢", type="primary"):
        if product_name:
            with st.spinner("🕵️‍♂️ AI 正在深度分析中，請稍候..."):
                try:
                    prompt = (
                        f"你是一位資深的消費者口碑分析師。請深度分析台灣各大論壇對於「{product_name}」的最新真實討論。\n"
                        "過濾掉業配文，並提供包含以下 10 點的報告：\n"
                        "1. 📊 網路聲量總結 (整體討論熱度與正負評比例)\n"
                        "2. 📈 近三個月網路論壇討論聲量及狀況\n"
                        "3. ✨ 真實優點歸納 (口語化列出 3-5 點網友高討論的特色)\n"
                        "4. 💣 踩雷與缺點抱怨 (不修飾口語化列出真實痛點)\n"
                        "5. 📝 以一般網友口吻分享此產品使用心得\n"
                        "6. 🗣️ 素人發文切角建議 (提供 5 個最
