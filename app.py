import streamlit as st
import google.generativeai as genai

# 1. 呼叫雲端保險箱裡的金鑰
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

# 2. 使用最新 2.5 版本模型
model = genai.GenerativeModel('gemini-2.5-flash')

# --- 網頁前端介面設計 ---
st.set_page_config(page_title="雙模式口碑分析儀", page_icon="🔍")
st.title("🔍 雙模式產品真實口碑分析儀")
st.markdown("一鍵切換分析視角：全網聲量健檢 或是 針對特定負評進行拆彈與攻防！")

# 3. 雙模式選擇按鈕
mode = st.radio(
    "🎯 請選擇您需要的分析模式：",
    ("✅ 常規全網口碑健檢 (輸入產品名，AI 自動上網爬文)", "🚨 特定負評拆彈與攻防 (貼上網友原始負評，AI 幫你擬定對策)")
)

st.divider()

# ==========================================
# 路線 A：常規全網口碑健檢
# ==========================================
if mode == "✅ 常規全網口碑健檢 (輸入產品名，AI 自動上網爬文)":
    product_name = st.text_input("📦 請輸入想查詢的「產品、品牌名稱」：")
    
    if st.button("🚀 開始口碑健檢"):
        if product_name:
            with st.spinner("🕵️‍♂️ AI 正在深度分析中，請稍候..."):
                try:
                    prompt = f"""
                    你是一位資深的消費者網路口碑分析師與品牌公關顧問。請深度分析台灣各大知名論壇（包含Threads、Dcard、PTT、Mobile01）對於以下產品的最新真實討論。

                    請過濾掉明顯的公關稿與業配文，並整理出一份專業的分析報告，包含：
                    1. 📊 網路聲量總結 (整體討論熱度與正負評比例)
                    2. 📈 近三個月網路論壇討論聲量及狀況
                    3. ✨ 真實優點歸納 (口語化列出 3-5 點網友高討論的特色)
                    4. 💣 踩雷與缺點抱怨 (不修飾口語化列出真實痛點)
                    5. 📝 以一般網友口吻分享此產品使用心得
                    6. 🗣️ 素人發文切角建議 (提供 3 個最自然、不具業配感的論壇討論情境)
                    7. 📌 此產品於各論壇討論風向差異 (Threads、PTT、Dcard、Mobile01 的網友在意的點有何不同？)
                    8. 🚨 潛在公關危機預警 (目前最致命的負面標籤，並給予平衡建議)
                    9. 🔗 競業分析及對比（找出相對於競業的優勢做口碑攻防）
                    10. 🎯 總結與行銷策略建議

                    請幫我深度分析這個產品：{product_name}
                    """
                    response = model.generate_content(prompt)
                    st.success("分析完成！以下是為您專屬客製的報告：")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"發生錯誤：{e}")
        else:
            st.warning("⚠️ 健檢模式需要您先輸入產品或品牌名稱喔！")

# ==========================================
# 路線 B：特定負評拆彈與攻防處理
# ==========================================
else: 
    raw_reviews = st.text_area("💬 請在此貼上網友的「原始負評」或「客訴文章」內容：", height=200)
    
    if st.button("🚀 開始負評拆彈與攻防"):
        if raw_reviews:
            with st.spinner("🚨 AI 危機處理專家正在擬定對策，請稍候..."):
                try:
                    prompt = f"""
                    你是一位擁有 15 年經驗的資深網路口碑操作專家與論壇風向操盤手。客戶的產品目前在論壇上遭遇了以下網友的具體負評攻擊。
                    
                    以下是網友的原始負評內容：
                    「{raw_reviews}」

                    請針對這篇負評，提供一份極具實戰價值的「負評拆彈與口碑攻防作戰計畫」，必須包含以下 7 大模塊：
                    
                    1. 🚨 危機等級與擴散風險
                    2. 🌋 網友情緒與真實痛點
                    3. 🛡️ 負評處理及風向平衡 (口碑防護與緩頰)
                    4. ⚔️ 口碑主動攻防與風向引導作戰 (網軍實戰操盤)
                    5. ⚖️ 平台機制與長尾防護
                    6. ⏳ 黃金應對行動時間表
                    7. 🩹 官方回覆與私訊溝通範本
                    """
                    response = model.generate_content(prompt)
                    st.success("分析完成！以下是為您擬定的危機處理對策：")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"發生錯誤：{e}")
        else:
            st.warning("⚠️ 拆彈模式需要您先貼上網友的原始負評喔！")
