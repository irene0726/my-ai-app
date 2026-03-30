import streamlit as st
import google.generativeai as genai

# 1. 呼叫雲端保險箱裡的金鑰
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

# 2. 使用最新 2.5 版本模型，並開啟「Google 聯網搜尋」功能
model = genai.GenerativeModel(
    model_name='gemini-2.5-flash',
    tools='google_search_retrieval'
)

# --- 網頁前端介面設計 ---
st.set_page_config(page_title="雙模式口碑分析儀", page_icon="🔍")
st.title("🔍 雙模式產品真實口碑分析儀")
st.markdown("一鍵切換分析視角，從日常健檢到危機處理，全方位掌握論壇風向！")

product_name = st.text_input("📦 請輸入想查詢的產品或品牌名稱：")

# 3. 雙模式選擇按鈕 (精華就在這裡！)
mode = st.radio(
    "🎯 請選擇您需要的分析模式：",
    ("✅ 常規口碑健檢 (適合一般產品、新品上市)", "🚨 公關危機處理 (適合負評滿天飛、炎上中的產品)")
)

if st.button("🚀 開始深度分析"):
    if product_name:
        with st.spinner("🕵️‍♂️ AI 正在全網深度爬文中，請稍候..."):
            try:
                # 4. 根據選擇的模式，自動切換 AI 的大腦 (Prompt)
                if mode == "✅ 常規口碑健檢 (適合一般產品、新品上市)":
                    prompt = f"""
                    你是一位資深的消費者口碑分析師與品牌公關顧問。請運用聯網搜尋功能，深度分析台灣各大知名論壇（如 PTT、Dcard、Mobile01）對於以下產品的最新真實討論。

                    請過濾掉明顯的公關稿與業配文，並整理出一份專業的分析報告，必須包含以下 7 點：
                    1. 📊 網路聲量總結 (整體討論熱度與正負評比例)
                    2. ✨ 真實優點歸納 (列出 3-5 點網友最推崇的特色)
                    3. 💣 踩雷與缺點抱怨 (不修飾地列出真實痛點)
                    4. 📌 各論壇風向差異 (PTT、Dcard、Mobile01 的網友在意的點有何不同？)
                    5. 🚨 潛在公關危機預警 (揪出目前最致命的負面標籤，並給予平衡建議)
                    6. 🎭 素人發文切角建議 (提供 3 個最自然、不具業配感的論壇討論情境)
                    7. 🎯 總結與行銷策略建議

                    請幫我深度分析這個產品：{product_name}
                    """
                
                else: # 如果選的是危機處理模式
                    prompt = f"""
                    你是一位資深的消費者口碑分析師與危機處理專家。請運用聯網搜尋功能，深度分析台灣各大論壇對於以下產品的「負面評價與炎上事件」。

                    請直擊核心，整理出以下 5 點危機處理報告：
                    1. 🌋 炎上核心點與情緒拆解 (分析網友真正生氣的點，是單純失望、憤怒抵制還是跟風嘲笑？)
                    2. 🛡️ 尋找「僅存的護航點」 (在滿滿負評中，找出仍給予好評或幫忙緩頰的微弱聲音與觀點)
                    3. 📉 負評擴散地圖與重災區 (指出負評最密集的論壇，並分析各平台酸民攻擊的切入點差異)
                    4. 🩹 品牌即刻止血建議 (給予能安撫核心情緒的具體第一步止血動作建議)
                    5. 🔄 逆轉風向的長尾操作切角 (設計 3 個「示弱、誠懇或反向操作」的素人發文切角，幫助未來洗白)

                    請幫我深度分析這個產品/品牌的危機：{product_name}
                    """
                
                # 呼叫 AI 產出結果
                response = model.generate_content(prompt)
                st.success(f"分析完成！以下是為您專屬客製的【{mode[:6]}】報告：")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"發生錯誤：{e}")
    else:
        st.warning("⚠️ 請先輸入產品名稱喔！")
