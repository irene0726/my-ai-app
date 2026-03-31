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
st.markdown("一鍵切換：一般產品健檢 ｜ 醫美口碑製造機 ｜ 醫美療程大比拼 ｜ **特定負評拆彈**")

# 3. 四大模式選擇按鈕 (順序已重新排列)
mode = st.radio(
    "🎯 請選擇您需要的分析模式：",
    (
        "✅ 一般產品常規健檢 (輸入產品或品牌名)", 
        "🏥 醫美口碑鋪陳製造機 (輸入療程與優勢，生成極致真實劇本)",
        "⚖️ 醫美療程與儀器大比拼 (支援 2-4 種項目同時比較)",
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
                        "過濾掉業配文，並提供包含聲量總結、優缺點歸納、論壇風向差異、潛在危機預警、素人發文切角及行銷建議的報告。"
                    )
                    response = model.generate_content(prompt)
                    st.success("分析完成！")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"發生錯誤：{e}")
        else:
            st.warning("⚠️ 請先輸入名稱喔！")

# ==========================================
# 🚪 第二扇門：醫美口碑鋪陳製造機
# ==========================================
elif mode == "🏥 醫美口碑鋪陳製造機 (輸入療程與優勢，生成極致真實劇本)":
    st.markdown("💡 **操作提示**：生成去業配感、高真實感的論壇發文與暗樁互動劇本。")
    col_t, col_a = st.columns(2)
    with col_t:
        treatment = st.text_input("💉 療程名稱 (例如：法令紋玻尿酸)：")
    with col_a:
        advantages = st.text_input("✨ 主打優勢 (例如：醫師美感自然、無硬塊)：")
        
    if st.button("🚀 生成高真實感口碑劇本"):
        if treatment and advantages:
            with st.spinner("✍️ 正在植入真實鄉民語氣..."):
                try:
                    prompt = (
                        f"你是一位頂級口碑操盤手，專攻台灣醫美論壇。請針對「{treatment}」及其優勢「{advantages}」撰寫口碑劇本。\n"
                        "必須嚴格執行去業配指令：資訊模糊化、植入微負評、強化術前焦慮、禁用行銷詞彙。\n"
                        "提供：1.平台主文切角(Dcard/PTT) 2.素人碎碎念大綱 3.暗樁蓋樓劇本(含求私訊) 4.競品防禦話術。"
                    )
                    response = model.generate_content(prompt)
                    st.success("劇本生成完成！")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"發生錯誤：{e}")
        else:
            st.warning("⚠️ 請務必填寫完整喔！")

# ==========================================
# 🚪 第三扇門：醫美療程彈性大比拼 (順序已往前移)
# ==========================================
elif mode == "⚖️ 醫美療程與儀器大比拼 (支援 2-4 種項目同時比較)":
    st.markdown("💡 **操作提示**：請至少輸入兩個項目。您可以輸入 2 個、3 個或 4 個選手進行對比。")
    
    # 建立四個並排的輸入框
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        item1 = st.text_input("🥊 選手 1", placeholder="例如：鳳凰電波")
    with col2:
        item2 = st.text_input("🥊 選手 2", placeholder="例如：十蓓電波")
    with col3:
        item3 = st.text_input("🥊 選手 3 (選填)", placeholder="例如：玩美電波")
    with col4:
        item4 = st.text_input("🥊 選手 4 (選填)", placeholder="例如：黃金電波")
    
    if st.button("🚀 開始多重殘酷比拼"):
        # 過濾出有填寫內容的項目
        items_to_compare = [i for i in [item1, item2, item3, item4] if i.strip()]
        
        if len(items_to_compare) >= 2:
            items_str = "、".join(items_to_compare)
            with st.spinner(f"🥊 正在對比 {items_str} ..."):
                try:
                    prompt = (
                        f"你是一位專業且中立的醫美分析師，深諳台灣 Dcard 與 PTT 醫美板風向。\n"
                        f"請幫我深度比較以下項目：{items_str}。\n\n"
                        "報告必須包含以下模塊，並使用 Markdown 表格呈現對比：\n"
                        "1. 🔬 核心原理白話文解釋：這幾者在技術原理上的關鍵差異。\n"
                        "2. 📊 殘酷對比表格：包含價格區間、維持時間、痛感評估、修復期、副作用風險、論壇討論熱度。\n"
                        "3. 🎯 適合對象分析：分別針對不同預算、痛感承受度、期望效果的受眾給予建議。\n"
                        "4. 🗣️ 論壇真實風向與常見抱怨：網友對這幾項療程分別最常酸什麼？或最擔憂什麼？\n"
                        "5. ⚔️ 口碑行銷攻防建議：若客戶主打其中一項，該如何在論壇「請益文」中自然地引導風向？提供 2 個發文切角。\n"
                        "6. 💡 總結：一句話點出這幾者的定位差異。"
                    )
                    response = model.generate_content(prompt)
                    st.success(f"比對完成！以下是 {len(items_to_compare)} 項目的深度報告：")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"發生錯誤：{e}")
        else:
            st.warning("⚠️ 請至少輸入兩個項目才能進行比較喔！")

# ==========================================
# 🚪 第四扇門：特定負評拆彈與攻防 (順序已移至壓軸)
# ==========================================
else: 
    raw_reviews = st.text_area("💬 請在此貼上網友的「原始負評」內容：", height=200)
    
    if st.button("🚀 開始負評拆彈"):
        if raw_reviews:
            with st.spinner("🚨 正在擬定拆彈對策..."):
                try:
                    prompt = (
                        f"你是一位資深危機處理專家。針對負評內容：「{raw_reviews}」，提供包含危機等級、情緒拆解、行動時間表、官方及私訊範本、素人防守腳本及風向引導的拆彈計畫。"
                    )
                    response = model.generate_content(prompt)
                    st.success("拆彈對策擬定完成！")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"發生錯誤：{e}")
        else:
            st.warning("⚠️ 請先貼上負評內容喔！")
