import streamlit as st
import google.generativeai as genai

# 1. 呼叫雲端保險箱裡的金鑰
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

# 2. 使用最新 2.5 版本模型
model = genai.GenerativeModel('gemini-2.5-flash')

# --- 網頁前端介面設計 ---
st.set_page_config(page_title="思嘉的 AI 口碑戰情室", page_icon="✨", layout="wide")

# ==========================================
# 🛡️ 隱藏魔法 & 個人化視覺設定
# ==========================================
custom_css = """
<style>
/* 隱藏預設選單與浮水印 */
#MainMenu {visibility: hidden;}
[data-testid="stToolbar"] {visibility: hidden;}
[data-testid="stHeader"] {visibility: hidden;}
footer {visibility: hidden;}

/* 分頁籤置中、字體放大且加粗，提升現代感 */
.stTabs [data-baseweb="tab-list"] {
    gap: 24px;
    justify-content: center;
}
.stTabs [data-baseweb="tab"] {
    font-size: 18px;
    font-weight: 600;
    padding: 12px 16px;
}

/* 👑 右下角個人專屬浮水印 */
.custom-footer {
    position: fixed;
    bottom: 10px;
    right: 20px;
    color: #AAAAAA;
    font-size: 13px;
    letter-spacing: 1px;
    z-index: 100;
}
</style>
<div class="custom-footer">© 2026 Crafted by 思嘉 | PR & Word-of-Mouth AI Hub</div>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ==========================================
# 💎 專屬主標題區
# ==========================================
st.title("✨ 思嘉的 AI 口碑戰情室")
st.caption("AI-Powered Public Relations & Word-of-Mouth Marketing Hub")
st.divider()

# ==========================================
# 🗂️ 核心功能導覽列
# ==========================================
tab1, tab2, tab3, tab4 = st.tabs([
    "📦 產品全網健檢", 
    "✍️ 醫美口碑劇本", 
    "⚖️ 療程殘酷比拼", 
    "🚨 危機負評拆彈"
])

# ------------------------------------------
# 🚪 第一分頁：產品全網健檢
# ------------------------------------------
with tab1:
    with st.expander("🔍 健檢條件設定 (點擊可收合/展開)", expanded=True):
        product_name = st.text_input(
            "請輸入「產品或品牌名稱」：", 
            placeholder="例如：娘家葉黃素、理膚寶水 B5",
            help="💡 輸入想查詢的產品，AI 將自動彙整各大論壇真實聲量與優缺點。"
        )
        btn1 = st.button("🚀 執行深度健檢", type="primary", key="btn1")
    
    if btn1:
        if product_name:
            with st.spinner("🕵️‍♂️ 戰情室連線中，正在撈取全網數據..."):
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
                    st.success("✨ 分析完成！您現在可以將上方的『條件設定面板』收合，方便閱讀完整報告。")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"發生錯誤：{e}")
        else:
            st.warning("⚠️ 請先輸入名稱喔！")

# ------------------------------------------
# 🚪 第二分頁：醫美口碑劇本 (🌟 升級：手動輸入人設)
# ------------------------------------------
with tab2:
    with st.expander("✍️ 劇本參數與人設設定 (點擊可收合/展開)", expanded=True):
        col_t, col_a = st.columns(2)
        with col_t:
            treatment = st.text_input(
                "💉 療程名稱：", 
                placeholder="例如：法令紋玻尿酸",
                help="💡 準備操作的醫美療程或儀器名稱"
            )
        with col_a:
            advantages = st.text_input(
                "✨ 主打優勢：", 
                placeholder="例如：醫師美感自然、無硬塊",
                help="💡 客戶診所或醫師希望溝通的核心賣點"
            )
            
        # 👑 新增：手動輸入人設欄位
        persona = st.text_input(
            "🎭 賦予發文者靈魂 (自訂人設)：", 
            placeholder="例如：精打細算的小資女、下個月要結婚焦慮的新娘、被前男友劈腿想變美的女大生...",
            help="💡 自由輸入您想要的鄉民身分，AI 將精準模仿該身分的語氣、金錢觀與在意點來撰寫文章。"
        )
            
        btn2 = st.button("🚀 生成高真實感劇本", type="primary", key="btn2")
        
    if btn2:
        if treatment and advantages:
            # 如果沒有填寫人設，預設給予「一般真實網友」
            actual_persona = persona.strip() if persona else "一般真實網友"
            
            with st.spinner(f"✍️ 正在以「{actual_persona}」的語氣撰寫劇本..."):
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
                        "2. 📝 主文內容大綱 (必須完美融入設定的人設語氣)\n"
                        "3. 🗣️ 暗樁推文與蓋樓劇本 (1-5樓推文，需包含中立言論、資訊設計問答、微負評包裝好評)\n"
                        "4. 🛡️ 競品防禦與帶風向話術：如果底下有真實網友留言推薦其他診所，我們的暗樁該用什麼話術自然地把風向帶回來？"
                    )
                    response = model.generate_content(prompt)
                    st.success("✨ 劇本生成完成！您現在可以將上方的『參數設定面板』收合，方便閱讀完整企劃。")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"發生錯誤：{e}")
        else:
            st.warning("⚠️ 請務必填寫「療程名稱」與「主打優勢」喔！")

# ------------------------------------------
# 🚪 第三分頁：療程殘酷比拼
# ------------------------------------------
with tab3:
    with st.expander("🥊 參賽選手設定 (點擊可收合/展開)", expanded=True):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            item1 = st.text_input("🥊 選手 1", placeholder="例如：鳳凰電波")
        with col2:
            item2 = st.text_input("🥊 選手 2", placeholder="例如：十蓓電波")
        with col3:
            item3 = st.text_input("🥊 選手 3 (選填)", placeholder="例如：玩美電波")
        with col4:
            item4 = st.text_input("🥊 選手 4 (選填)", placeholder="例如：黃金電波", help="💡 可輸入 2 到 4 個選手進行對比")
        
        btn3 = st.button("🚀 開始多重殘酷比拼", type="primary", key="btn3")
        
    if btn3:
        items_to_compare = [i for i in [item1, item2, item3, item4] if i.strip()]
        if len(items_to_compare) >= 2:
            items_str = "、".join(items_to_compare)
            with st.spinner(f"🥊 正在對比 {items_str} ..."):
                try:
                    prompt = (
                        f"你是一位專業且中立的醫美分析
