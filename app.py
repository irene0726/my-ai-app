import streamlit as st
import google.generativeai as genai

# 1. 貼上您的全新金鑰 (記得保留雙引號)
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

# 2. 使用最穩定支援的 flash 模型
model = genai.GenerativeModel('gemini-2.5-flash')

# --- 網頁前端介面設計 ---
st.set_page_config(page_title="產品真實口碑分析儀", page_icon="🔍")
st.title("🔍 產品真實口碑一鍵分析儀")
st.markdown("輸入任何產品名稱，AI 幫你秒速爬梳論壇真實評價！")

product_name = st.text_input("📦 請輸入想查詢的產品或服務名稱：")

if st.button("🚀 開始分析口碑"):
    if product_name:
        with st.spinner("🕵️‍♂️ AI 正在深度爬文中，請稍候..."):
            try:
                # 把分析師的規則直接寫進對話中，最不容易報錯！
                prompt = f"""
                你是一位資深的消費者口碑分析師。請深度分析台灣各大知名論壇（如 PTT、Dcard、Mobile01）對於以下產品的真實討論，過濾掉明顯的公關稿與業配文，並整理出：
                1. 📊 網路聲量總結
                2. ✨ 產品真實優點及特色歸納 (至少列出3-5點，口語化)
                3. 💣 踩雷與缺點抱怨
                4. 📝 討論這個產品的網友大概有什麼樣的困擾或需求
                5. 📌 以一般網友角度分享此產品實際使用心得（好評為主）
                6. 🔎 蒐集目前網友對與此產品的評價
                7. 📈 蒐集此產品目前在Threads上的討論狀況
                8. 💡 競品比較
                9. 🎯 總結建議

                請幫我分析這個產品：{product_name}
                """
                
                response = model.generate_content(prompt)
                st.success("分析完成！以下是為您整理的口碑報告：")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"發生錯誤：{e}")
    else:
        st.warning("⚠️ 請先輸入產品名稱喔！")
