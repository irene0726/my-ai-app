import streamlit as st
import google.generativeai as genai

# 1. 呼叫雲端保險箱裡的金鑰
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

# 2. 使用最新 2.5 版本模型
model = genai.GenerativeModel('gemini-2.5-flash')

# --- 網頁前端介面設計 ---
st.set_page_config(page_title="全能口碑與聲量分析儀", page_icon="🔍")
st.title("🔍 全能口碑與危機處理分析儀")
st.markdown("一鍵切換：一般品健檢 ｜ 醫美聲量客觀分析 ｜ 負評拆彈攻防")

# 3. 三大模式選擇按鈕
mode = st.radio(
    "🎯 請選擇您需要的分析模式：",
    (
        "✅ 一般產品常規健檢 (輸入產品名)", 
        "🏥 醫美客觀聲量分析 (輸入診所/醫師名)",
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
# 🚪 第二扇門：醫美客觀聲量分析 (精準餵料升級版)
# ==========================================
elif mode == "🏥 醫美客觀聲量分析 (輸入診所/醫師名)":
    clinic_doctor_name = st.text_input("🏥 請輸入想查詢的「醫美診所」或「醫師姓名」：")
    forum_data = st.text_area("📄 追求 100% 精準：請貼上您在 PTT/Dcard 找到的「關鍵討論文章與推文」(選填，貼上後準確度極高)：", height=150)
    
    if st.button("🚀 開始醫美聲量分析"):
        if clinic_doctor_name:
            with st.spinner("👩‍⚕️ AI 正在深度掃描醫美論壇真實聲量..."):
                try:
                    # 如果有貼上資料，就啟動「鐵血防幻覺」指令
                    if forum_data:
                        prompt = (
                            f"你是一位嚴謹的醫美公關分析師。請【嚴格只根據以下我提供的論壇討論內容】，客觀分析「{clinic_doctor_name}」的評價。\n"
                            f"絕對不可瞎掰、不可使用外部記憶！若提供的資料中沒有提到某一點，請直接寫「資料未提及」。\n"
                            f"【論壇討論內容】：\n{forum_data}\n\n"
                            "請提供以下 5 大維度的分析：\n"
                            "1. 📊 整體聲量與好感度總結\n"
                            "2. 👨‍⚕️ 醫師專長與美感風格\n"
                            "3. 🏢 診所服務與推銷評價 (是否有推銷壓力)\n"
                            "4. ⚠️ 潛在風險與避雷預警 (是否有具體客訴或失敗案例)\n"
                            "5. 🎯 競品比較與受眾輪廓"
                        )
                    # 如果沒貼資料，就用原本的通用掃描
                    else:
                        prompt = (
                            f"你是一位嚴謹的醫美產業分析師。請綜合你所知的台灣醫美論壇資訊，客觀分析「{clinic_doctor_name}」的網路聲量。\n"
                            "若資訊不足，請直接回答「目前網路討論樣本數不足」，不可捏造。\n"
                            "請提供：1.整體聲量 2.醫師專長與美感 3.診所推銷評價 4.潛在風險預警 5.競品比較。"
                        )
                        
                    response = model.generate_content(prompt)
                    st.success("分析完成！以下是精準聲量報告：")
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
