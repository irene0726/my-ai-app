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
# 🗂️ 核心功能：使用「分頁籤 (Tabs)」取代傳統按鈕
# ==========================================
tab1, tab2, tab3, tab4 = st.tabs([
    "✅ 一般產品常規健檢", 
    "🏥 醫美口碑鋪陳製造機", 
    "⚖️ 醫美療程彈性大比拼", 
    "🚨 特定負評拆彈與攻防"
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
                        "6. 🗣️ 素人發文切角建議 (提供 5 個最自然、不具業配感的論壇討論情境)\n"
                        "7. 📌 此產品於各論壇討論風向差異 (Threads、Dcard、PTT 的網友在意的點有何不同？)\n"
                        "8. 🚨 潛在公關危機預警 (目前最致命的負面標籤，並給予平衡建議)\n"
                        "9. 🔗 競業分析及對比（找出相對於競業的優勢做口碑攻防）\n"
                        "10. 🎯 總結與行銷策略建議"
                    )
                    response = model.generate_content(prompt)
                    st.success("✨ 分析完成！以下是專屬報告：")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"發生錯誤：{e}")
        else:
            st.warning("⚠️ 請先輸入名稱喔！")

# ------------------------------------------
# 🚪 第二分頁：醫美口碑鋪陳製造機 (🌟 升級：手動輸入人設)
# ------------------------------------------
with tab2:
    st.info("💡 **操作指南**：生成去業配感、高真實感的論壇發文與暗樁互動劇本。您可自由賦予發文者靈魂。")
    col_t, col_a = st.columns(2)
    with col_t:
        treatment = st.text_input("💉 療程名稱：", placeholder="例如：法令紋玻尿酸")
    with col_a:
        advantages = st.text_input("✨ 主打優勢：", placeholder="例如：醫師美感自然、無硬塊")
        
    # 👑 新增：手動打字輸入人設
    persona = st.text_input(
        "🎭 賦予發文者靈魂 (自訂人設)：", 
        placeholder="例如：準備下個月結婚、瘋狂容貌焦慮的新娘...",
        help="💡 自由輸入您想要的鄉民身分，AI 將精準模仿該身分的語氣、金錢觀與在意點來撰寫文章。"
    )
        
    if st.button("🚀 生成高真實感口碑劇本", type="primary"):
        if treatment and advantages:
            # 如果使用者趕時間沒填寫人設，系統自動補上預設值，避免報錯
            actual_persona = persona.strip() if persona else "一般真實網友"
            
            with st.spinner(f"✍️ 正在以「{actual_persona}」的語氣植入真實鄉民語氣..."):
                try:
                    prompt = (
                        f"你是一位擁有 15 年經驗的頂級網路口碑操盤手，專攻台灣醫美論壇。\n"
                        f"請針對以下設定，為客戶撰寫一套「極致真實、絕對去業配感」的論壇口碑鋪陳劇本。\n\n"
                        f"【操作目標設定】\n"
                        f"📍 療程項目：{treatment}\n"
                        f"📍 診所/醫師主打優勢：{advantages}\n"
                        f"📍 發文者專屬人設：{actual_persona}\n\n"
                        f"【⚠️ 絕對不可違背的『去業配』鐵血指令】\n"
                        "1. 資訊模糊化：主文中【絕對不可以】完整打出診所名稱或醫師全名。\n"
                        "2. 禁用公關用語：嚴禁出現「專業團隊、高CP值、強烈推薦」等行銷詞彙。\n"
                        "3. 植入無傷大雅的抱怨：必須穿插 1~2 個微負評（如：難預約、附近難停車、等太久）。\n"
                        f"4. 強化情緒起伏與人設：劇本與推文必須完美符合「{actual_persona}」這個身分會有的語氣、金錢考量或痛點。\n\n"
                        "請提供：\n"
                        "1. 🎯 平台主文切角與吸睛標題 (Threads、Dcard 各 3 個)\n"
                        "2. 📝 主文內容大綱 (內容須符合Threads、Dcard 平台討論屬性，並完美融入設定的人設語氣)\n"
                        "3. 🗣️ 暗樁推文與蓋樓劇本 (1-5樓推文，需包含中立言論、資訊設計問答、微負評包裝好評)\n"
                        "4. 🛡️ 競品防禦與帶風向話術：如果底下有真實網友留言推薦其他診所，我們的暗樁該用什麼話術自然地把風向帶回來？"
                    )
                    response = model.generate_content(prompt)
                    st.success("✨ 劇本生成完成！以下是口碑操作企劃：")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"發生錯誤：{e}")
        else:
            st.warning("⚠️ 請務必填寫「療程名稱」與「主打優勢」喔！")

# ------------------------------------------
# 🚪 第三分頁：醫美療程彈性大比拼
# ------------------------------------------
with tab3:
    st.info("💡 **操作指南**
