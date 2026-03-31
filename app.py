import streamlit as st
import google.generativeai as genai

# 1. 呼叫雲端保險箱裡的金鑰
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

# 2. 使用最新 2.5 版本模型
model = genai.GenerativeModel('gemini-2.5-flash')

# --- 網頁前端介面設計 ---
st.set_page_config(page_title="全能口碑操盤分析儀", page_icon="📝")
st.title("📝 全能口碑操盤與危機處理分析儀")
st.markdown("一鍵切換：一般產品全網健檢 ｜ 醫美口碑鋪陳製造機 ｜ 特定負評拆彈與攻防")

# 3. 三大模式選擇按鈕
mode = st.radio(
    "🎯 請選擇您需要的分析模式：",
    (
        "✅ 一般產品常規健檢 (輸入產品或品牌名)", 
        "🏥 醫美口碑鋪陳製造機 (輸入療程與優勢，生成網軍劇本)",
        "🚨 特定負評拆彈與攻防 (貼上原始客訴或負評)"
    )
)

st.divider()

# ==========================================
# 🚪 第一扇門：一般產品常規健檢
# ==========================================
if mode == "✅ 一般產品常規健檢 (輸入產品或品牌名)":
    product_name = st.text_input("📦 請輸入想查詢的「產品或品牌名稱」：")
    
    if st.button("🚀 開始產品健檢"):
        if product_name:
            with st.spinner("🕵️‍♂️ AI 正在深度分析中，請稍候..."):
                try:
                    prompt = (
                        f"你是一位資深的消費者口碑分析師。請深度分析台灣各大論壇對於「{product_name}」的最新真實討論。\n"
                        "過濾掉業配文，並提供包含以下 7 點的報告：\n"
                        "1. 📊 網路聲量總結 (討論熱度與正負評比例)\n"
                        "2. ✨ 真實優點歸納 (3-5 點網友最推崇的特色)\n"
                        "3. 💣 踩雷與缺點抱怨 (不修飾的真實痛點)\n"
                        "4. 📌 各論壇風向差異 (PTT、Dcard 等平台的在意點差異)\n"
                        "5. 🚨 潛在公關危機預警 (最致命的負面標籤與平衡建議)\n"
                        "6. 🎭 素人發文切角建議 (3 個最自然的論壇討論情境)\n"
                        "7. 🎯 總結與行銷策略建議"
                    )
                    response = model.generate_content(prompt)
                    st.success("分析完成！以下是常規口碑報告：")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"發生錯誤：{e}")
        else:
            st.warning("⚠️ 請先輸入產品或品牌名稱喔！")

# ==========================================
# 🚪 第二扇門：醫美口碑鋪陳製造機 (🌟 全新口碑編劇大腦 🌟)
# ==========================================
elif mode == "🏥 醫美口碑鋪陳製造機 (輸入療程與優勢，生成網軍劇本)":
    st.markdown("💡 **操作提示**：讓 AI 幫您產出高真實感、去業配感的論壇發文與暗樁互動劇本。")
    col1, col2 = st.columns(2)
    with col1:
        treatment = st.text_input("💉 準備操作的「療程名稱」(例如：電音波、玻尿酸)：")
    with col2:
        advantages = st.text_input("✨ 客戶診所/醫師的「主打優勢」(例如：不推銷、無硬塊)：")
        
    if st.button("🚀 生成論壇口碑劇本"):
        if treatment and advantages:
            with st.spinner("✍️ AI 網軍總監正在撰寫論壇發文與推文劇本..."):
                try:
                    prompt = (
                        f"你是一位擁有 15 年經驗的頂級網路口碑操盤手，專攻台灣熱門醫美論壇（如 Threads、Dcard 醫美板、PTT Facelift等）。\n"
                        f"請針對以下設定，為客戶撰寫一套「高真實感、去業配感」的論壇口碑鋪陳劇本。\n\n"
                        f"【操作目標設定】\n"
                        f"📍 療程項目：{treatment}\n"
                        f"📍 診所/醫師主打優勢：{advantages}\n\n"
                        "請提供以下 4 大實戰口碑劇本：\n"
                        "1. 🎯 各平台主文切角與吸睛標題：請分別針對 Threads、Dcard 各提供 3 個不同人設的標題與切入點 (例如：請益文、修復期焦慮文、多間諮詢比較文)。\n"
                        "2. 📝 主文內容大綱：挑選其中一個最具潛力的標題，撰寫一段具有「素人真實感」的內文大綱，務必適度加入一些無傷大雅的猶豫或微抱怨，以降低業配感。\n"
                        "3. 🗣️ 暗樁推文與蓋樓劇本：設計主文底下 1 到 5 樓的推文或設計問答，必須包含「中立言論」、「微負評包裝大好評」等真實互動。\n"
                        "4. 🛡️ 競品防禦與帶風向話術：如果底下有真實網友留言推薦其他診所，我們的暗樁該用什麼話術自然地把風向帶回來？"
                    )
                    response = model.generate_content(prompt)
                    st.success("劇本生成完成！以下是您的專屬口碑操作企劃：")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"發生錯誤：{e}")
        else:
            st.warning("⚠️ 請務必填寫「療程名稱」與「主打優勢」喔！")

# ==========================================
# 🚪 第三扇門：特定負評拆彈與攻防
# ==========================================
else: 
    raw_reviews = st.text_area("💬 請在此貼上網友的「原始負評」或「客訴文章」內容：", height=200)
    
    if st.button("🚀 開始負評拆彈"):
        if raw_reviews:
            with st.spinner("🚨 AI 危機處理專家正在擬定對策，請稍候..."):
                try:
                    prompt = (
                        f"你是一位擁有 15 年經驗的資深危機處理專家。客戶目前遭遇了以下網友的具體負評：\n"
                        f"「{raw_reviews}」\n"
                        "請提供「負評拆彈作戰計畫」，包含：\n"
                        "1. 🚨 危機等級與擴散風險 (炎上指數)\n"
                        "2. 🌋 核心情緒與真實痛點 (底層不滿原因)\n"
                        "3. ⏳ 黃金應對行動時間表 (2小時與24小時內的動作)\n"
                        "4. 🩹 官方回覆與私訊溝通範本 (公開留言與私訊安撫文字)\n"
                        "5. 🛡️ 素人防守腳本 (3 個不同人設的暗樁留言切角)\n"
                        "6. ⚔️ 主動攻防與風向引導作戰 (風向轉移、反向質疑原 PO 動機)"
                    )
                    response = model.generate_content(prompt)
                    st.success("分析完成！以下是危機拆彈對策：")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"發生錯誤：{e}")
        else:
            st.warning("⚠️ 拆彈模式需要您先貼上原始負評喔！")
