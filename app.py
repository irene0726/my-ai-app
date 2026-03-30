import streamlit as st
import google.generativeai as genai

# 1. 呼叫雲端保險箱裡的金鑰
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

# 2. 使用最新 2.5 版本模型
model = genai.GenerativeModel(
    model_name='gemini-2.5-flash',
    tools='[{"google_search": {}}]'
)

# --- 網頁前端介面設計 ---
st.set_page_config(page_title="雙模式口碑分析儀", page_icon="🔍")
st.title("🔍 雙模式產品真實口碑分析儀")
st.markdown("一鍵切換分析視角：全網聲量健檢 或是 針對特定負評進行拆彈！")

# 3. 雙模式選擇按鈕
mode = st.radio(
    "🎯 請選擇您需要的分析模式：",
    ("✅ 常規全網口碑健檢 (輸入產品名，AI 自動上網爬文)", "🚨 特定負評拆彈處理 (貼上網友原始負評，AI 幫你擬定對策)")
)

product_name = st.text_input("📦 請輸入產品、品牌或診所名稱 (必填)：")

# 4. 如果選擇「拆彈模式」，就顯示一個大型文字框讓您貼上負評
raw_reviews = ""
if mode == "🚨 特定負評拆彈處理 (貼上網友原始負評，AI 幫你擬定對策)":
    raw_reviews = st.text_area("💬 請在此貼上網友的「原始負評」或「炎上文章」內容：", height=200)

if st.button("🚀 開始深度分析"):
    if product_name:
        # 防呆機制：如果選了拆彈模式卻沒貼內文，會跳出提醒
        if mode == "🚨 特定負評拆彈處理 (貼上網友原始負評，AI 幫你擬定對策)" and not raw_reviews:
             st.warning("⚠️ 拆彈模式需要您貼上網友的原始負評喔！")
        else:
            with st.spinner("🕵️‍♂️ AI 正在深度分析中，請稍候..."):
                try:
                    if mode == "✅ 常規全網口碑健檢 (輸入產品名，AI 自動上網爬文)":
                        prompt = f"""
                        你是一位資深的消費者口碑分析師與品牌公關顧問。請運用聯網搜尋功能，深度分析台灣各大知名論壇對於以下產品的最新真實討論。

                        請過濾掉明顯的公關稿與業配文，並整理出一份專業的分析報告，包含：
                        1. 📊 網路聲量總結 (整體討論熱度與正負評比例)
                        2. ✨ 真實優點歸納 (列出 3-5 點網友最推崇的特色)
                        3. 💣 踩雷與缺點抱怨 (不修飾地列出真實痛點)
                        4. 📌 各論壇風向差異 (PTT、Dcard、Mobile01 的網友在意的點有何不同？)
                        5. 🚨 潛在公關危機預警 (揪出目前最致命的負面標籤，並給予平衡建議)
                        6. 🎭 素人發文切角建議 (提供 3 個最自然、不具業配感的論壇討論情境)
                        7. 🎯 總結與行銷策略建議

                        請幫我深度分析這個產品：{product_name}
                        """
                    
                    else: # 危機拆彈模式
                        prompt = f"""
                        你是一位資深的危機處理專家與公關顧問。客戶的產品/品牌「{product_name}」目前遭遇了以下網友的具體負評攻擊。
                        
                        以下是網友的原始負評內容：
                        「{raw_reviews}」

                        請針對上述的原始負評內容直擊核心，整理出以下 5 點「負評拆彈與回覆報告」：
                        1. 🌋 核心情緒與痛點拆解 (這位網友真正生氣、不滿的底層原因是什麼？)
                        2. 🩹 官方公關回覆建議 (請擬定一段可以直接回覆給該網友的官方留言，語氣需誠懇、能安撫情緒且不推卸責任)
                        3. 🛡️ 護航與緩頰切角建議 (如果我們要請暗樁或素人帳號在底下幫忙留言緩頰，請提供 3 個不具業配感、合理且客觀的反駁或護航觀點)
                        4. 🚨 後續延燒風險評估 (這篇負評有沒有可能引發更大規模的炎上？)
                        5. 🔄 內部服務優化建議 (根據這個負評，品牌端實際上應該做什麼改進？)
                        """
                    
                    response = model.generate_content(prompt)
                    st.success(f"分析完成！以下是為您專屬客製的報告：")
                    st.write(response.text)
                    
                except Exception as e:
                    st.error(f"發生錯誤：{e}")
    else:
        st.warning("⚠️ 請先輸入產品或品牌名稱喔！")
