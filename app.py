import streamlit as st
import google.generativeai as genai

# 1. 呼叫雲端保險箱裡的金鑰
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

# 2. 使用最新 2.5 版本模型 (純文字分析，最穩定版本)
model = genai.GenerativeModel('gemini-2.5-flash')

# --- 網頁前端介面設計 ---
st.set_page_config(page_title="全能口碑操盤分析儀", page_icon="🔍")
st.title("🔍 全能口碑與危機處理分析儀")
st.markdown("一鍵切換：一般品健檢 ｜ 醫美專屬網軍操盤 ｜ 負評拆彈攻防")

# 3. 三大模式選擇按鈕 (精準對應下方三扇門)
mode = st.radio(
    "🎯 請選擇您需要的分析模式：",
    (
        "✅ 一般產品常規健檢 (輸入產品名)", 
        "🏥 醫美專屬口碑雷達 (輸入診所/醫師名)",
        "🚨 特定負評拆彈與攻防 (貼上原始負評)"
    )
)

st.divider()

# ==========================================
# 🚪 第一扇門：一般產品常規健檢
# ==========================================
if mode == "✅ 一般產品常規健檢 (輸入產品名)":
    product_name = st.text_input("📦 請輸入想查詢的「產品或品牌名稱」：")
    
    if st.button("🚀 開始產品健檢"):
        if product_name:
            with st.spinner("🕵️‍♂️ AI 正在深度分析中，請稍候..."):
                try:
                    prompt = f"""
                    你是一位資深的消費者口碑分析師。請深度分析台灣各大論壇對於「{product_name}」的最新真實討論。
                    過濾掉業配文，並提供包含以下 7 點的報告：
                    1. 📊 網路聲量總結 (討論熱度與正負評比例)
                    2. ✨ 真實優點歸納 (3-5 點網友最推崇的特色)
                    3. 💣 踩雷與缺點抱怨 (不修飾的真實痛點)
                    4. 📌 各論壇風向差異 (PTT、Dcard 等平台的在意點差異)
                    5. 🚨 潛在公關危機預警 (最致命的負面標籤與平衡建議)
                    6. 🎭 素人發文切角建議 (3 個最自然的論壇討論情境)
                    7. 🎯 總結與行銷策略建議
                    """
                    response = model.generate_content(prompt)
                    st.success("分析完成！以下是常規口碑報告：")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"發生錯誤：{e}")
        else:
            st.warning("⚠️ 請先輸入產品或品牌名稱喔！")

# ==========================================
# 🚪 第二扇門：醫美專屬口碑雷達 (網軍操盤大腦)
# ==========================================
elif mode == "🏥 醫美專屬口碑雷達 (輸入診所/醫師名)":
    clinic_doctor_name = st.text_input("🏥 請輸入想查詢的「醫美診所」或「醫師姓名」：")
    
    if st.button("🚀 開始醫美口碑操盤分析"):
        if clinic_doctor_name:
            with st.spinner("👩‍⚕️ AI 正在為您生成網軍操盤劇本，請稍候..."):
                try:
                    prompt = f"""
                    你是一位專精於台灣醫美產業的資深口碑操盤手與公關顧問。請針對「{clinic_doctor_name}」在台灣醫美論壇 (尤其是 PTT Facelift 板、Dcard 醫美板、Threads) 的真實討論進行深度剖析。

                    請務必過濾掉明顯的診所業配、公關文與假帳號推文，並提供一份極具實戰價值的「醫美專屬口碑深度雷達報告」，包含以下 10 大模塊：
                    1. 📊 網路聲量總結 (整體討論熱度與正負評比例)
                    2. 📈 近三個月網路論壇討論聲量及狀況
                    3. ✨ 真實優點歸納 (口語化列出 3-5 點網友高討論的特色)
                    4. 💣 踩雷與缺點抱怨 (不修飾口語化列出真實痛點)
                    5. ‼️ 網友醫美失敗負評
                    6. 📝 以一般網友口吻分享此醫美心得
                    7. 🗣️ 素人發文切角建議 (提供 5 個最自然、不具業配感的論壇討論情境)
                    8. 📌 於各論壇討論風向差異 (Threads、PTT、Dcard、Mobile01 的網友在意的點有何不同？)
                    9. 🚨 潛在公關危機預警 (目前最致命的負面標籤，並給予平衡建議)
                    10. 🔗 競業分析及對比（找出相對於競業的優勢做口碑攻防）
                    11. 🎯 總結與行銷策略建議

                    """
                    response = model.generate_content(prompt)
                    st.success("分析完成！以下是醫美專屬操盤企劃：")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"發生錯誤：{e}")
        else:
            st.warning("⚠️ 請先輸入診所或醫師名稱喔！")

# ==========================================
# 🚪 第三扇門：特定負評拆彈與攻防
# ==========================================
else: 
    raw_reviews = st.text_area("💬 請在此貼上網友的「原始負評」或「客訴文章」內容：", height=200)
    
    if st.button("🚀 開始負評拆彈"):
        if raw_reviews:
            with st.spinner("🚨 AI 危機處理專家正在擬定對策，請稍候..."):
                try:
                    prompt = f"""
                    你是一位擁有 15 年經驗的資深危機處理專家。客戶目前遭遇了以下網友的具體負評：
                    「{raw_reviews}」

                    請提供「負評拆彈作戰計畫」，包含：
                    1. 🚨 危機等級與擴散風險 (炎上指數)
                    2. 🌋 核心情緒與真實痛點 (底層不滿原因)
                    3. ⏳ 黃金應對行動時間表 (2小時與24小時內的動作)
                    4. 🩹 官方回覆與私訊溝通範本 (公開留言與私訊安撫文字)
                    5. 🛡️ 素人防守腳本 (3 個不同人設的暗樁留言切角)
                    6. ⚔️ 主動攻防與風向引導作戰 (風向轉移、反向質疑原 PO 動機)
                    """
                    response = model.generate_content(prompt)
                    st.success("分析完成！以下是危機拆彈對策：")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"發生錯誤：{e}")
        else:
            st.warning("⚠️ 拆彈模式需要您先貼上原始負評喔！")
