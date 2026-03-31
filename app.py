import streamlit as st
import google.generativeai as genai

# 1. 呼叫雲端保險箱裡的金鑰
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

# 2. 使用最新 2.5 版本模型
model = genai.GenerativeModel('gemini-2.5-flash')

# --- 網頁前端介面設計 ---
st.set_page_config(page_title="全能口碑操盤分析儀", page_icon="📝", layout="wide")
st.title("📝 全能口碑操盤與危機處理分析儀")
st.markdown("一鍵切換：一般產品健檢 ｜ 醫美口碑製造機 ｜ 特定負評拆彈 ｜ **[新增] 醫美療程大比拼**")

# 3. 四大模式選擇按鈕
mode = st.radio(
    "🎯 請選擇您需要的分析模式：",
    (
        "✅ 一般產品常規健檢 (輸入產品或品牌名)", 
        "🏥 醫美口碑鋪陳製造機 (輸入療程與優勢，生成極致真實劇本)",
        "🚨 特定負評拆彈與攻防 (貼上原始客訴或負評)",
        "⚖️ 醫美療程與儀器殘酷大比拼 (輸入兩種療程，產出專業比較)"
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
# 🚪 第二扇門：醫美口碑鋪陳製造機
# ==========================================
elif mode == "🏥 醫美口碑鋪陳製造機 (輸入療程與優勢，生成極致真實劇本)":
    st.markdown("💡 **操作提示**：AI 將嚴格執行「資訊模糊化」與「微負評植入」，確保產出 100% 像真實鄉民的發文。")
    col1, col2 = st.columns(2)
    with col1:
        treatment = st.text_input("💉 準備操作的「療程名稱」(例如：法令紋玻尿酸、電音波)：")
    with col2:
        advantages = st.text_input("✨ 客戶的主打優勢」(例如：融合度好無硬塊、不強迫推銷)：")
        
    if st.button("🚀 生成高真實感口碑劇本"):
        if treatment and advantages:
            with st.spinner("✍️ AI 網軍總監正在植入真實鄉民語氣..."):
                try:
                    prompt = (
                        f"你是一位擁有 15 年經驗的頂級網路口碑操盤手，專攻台灣醫美論壇。\n"
                        f"請針對以下設定，為客戶撰寫一套「極致真實、絕對去業配感」的論壇口碑鋪陳劇本。\n\n"
                        f"【操作目標設定】\n"
                        f"📍 療程項目：{treatment}\n"
                        f"📍 診所/醫師主打優勢：{advantages}\n\n"
                        f"【⚠️ 絕對不可違背的『去業配』鐵血指令】\n"
                        "1. 資訊模糊化：主文中【絕對不可以】完整打出診所名稱或醫師全名。\n"
                        "2. 禁用公關用語：嚴禁出現「專業團隊、高CP值、強烈推薦」等行銷詞彙。\n"
                        "3. 植入無傷大雅的抱怨：必須穿插 1~2 個微負評（如：難預約、附近難停車、等太久）。\n"
                        "4. 強化情緒起伏：寫出術前爬文的焦慮、怕痛、怕失敗等底層情緒。\n\n"
                        "請提供：\n"
                        "1. 🎯 平台主文切角與吸睛標題 (Dcard、PTT 各 2 個)\n"
                        "2. 📝 主文內容大綱 (具備素人碎碎念真實感)\n"
                        "3. 🗣️ 暗樁推文與蓋樓劇本 (1-5樓，需包含求私訊、微負評包裝大好評)\n"
                        "4. 🛡️ 競品防禦與帶風向話術"
                    )
                    response = model.generate_content(prompt)
                    st.success("劇本生成完成！以下是極致真實的口碑操作企劃：")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"發生錯誤：{e}")
        else:
            st.warning("⚠️ 請務必填寫「療程名稱」與「主打優勢」喔！")

# ==========================================
# 🚪 第三扇門：特定負評拆彈與攻防
# ==========================================
elif mode == "🚨 特定負評拆彈與攻防 (貼上原始客訴或負評)": 
    raw_reviews = st.text_area("💬 請在此貼上網友的「原始負評」或「客訴文章」內容：", height=200)
    
    if st.button("🚀 開始負評拆彈"):
        if raw_reviews:
            with st.spinner("🚨 AI 危機處理專家正在擬定對策，請稍候..."):
                try:
                    prompt = (
                        f"你是一位資深危機處理專家。客戶目前遭遇了以下具體負評：\n"
                        f"「{raw_reviews}」\n"
                        "請提供包含：1.危機等級與擴散風險 2.核心情緒與真實痛點 3.黃金應對行動時間表 4.官方回覆與私訊溝通範本 5.素人防守腳本 6.主動攻防與風向引導作戰 的拆彈計畫。"
                    )
                    response = model.generate_content(prompt)
                    st.success("分析完成！以下是危機拆彈對策：")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"發生錯誤：{e}")
        else:
            st.warning("⚠️ 拆彈模式需要您先貼上原始負評喔！")

# ==========================================
# 🚪 第四扇門：醫美療程與儀器殘酷大比拼 (🌟 全新功能 🌟)
# ==========================================
else:
    st.markdown("💡 **操作提示**：輸入兩種想比較的療程或儀器，AI 會幫您整理出最適合論壇操作的殘酷對比。")
    col1, col2 = st.columns(2)
    with col1:
        item_a = st.text_input("🥊 選手 A (例如：鳳凰電波、童顏針)：")
    with col2:
        item_b = st.text_input("🥊 選手 B (例如：十蓓電波、洢蓮絲)：")
        
    if st.button("🚀 開始殘酷大比拼"):
        if item_a and item_b:
            with st.spinner("🥊 AI 正在深度比對兩者的優劣勢與論壇真實評價..."):
                try:
                    prompt = (
                        f"你是一位極度專業且中立的醫美分析師，同時深諳台灣 PTT、Dcard 醫美板的討論風向。\n"
                        f"請幫我深度比較「{item_a}」與「{item_b}」這兩種醫美療程/儀器，並產出一份可直接用於行銷企劃或論壇帶風向的【殘酷大比拼報告】。\n\n"
                        "請務必包含以下 6 大模塊，並善用 Markdown 表格呈現對比數據：\n"
                        "1. 🔬 核心原理與最大差異 (用白話文解釋兩者到底差在哪？)\n"
                        "2. 📊 殘酷對比表 (必須使用表格呈現：價格區間、維持時間、痛感評估、修復期長短、副作用風險)\n"
                        "3. 🎯 適合對象與避雷指南 (誰適合選 A？誰必須選 B？哪些體質絕對不要碰？)\n"
                        "4. 🗣️ 論壇真實風向與痛點 (網友對 A 最常抱怨什麼？對 B 最常抱怨什麼？是否有結節硬塊、燙傷等常見黑歷史？)\n"
                        "5. ⚔️ 口碑行銷切入點 (如果我們客戶的主打是 A，該如何設計論壇文章來合法且自然地『踩 B 捧 A』？提供 2 個發文切角)\n"
                        "6. 💡 總結句 (一句話精闢總結兩者的定位差異)"
                    )
                    response = model.generate_content(prompt)
                    st.success(f"比對完成！以下是【{item_a} vs {item_b}】的深度報告：")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"發生錯誤：{e}")
        else:
            st.warning("⚠️ 請務必將「選手 A」與「選手 B」都填寫完整喔！")
