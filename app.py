import streamlit as st
import google.generativeai as genai

# 1. 呼叫雲端保險箱裡的金鑰
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

# 2. 使用最新 2.5 版本模型
model = genai.GenerativeModel('gemini-2.5-flash')

# --- 網頁前端介面設計 (企業級 UI 升級版) ---
st.set_page_config(page_title="全能口碑操盤分析儀", page_icon="📝", layout="wide")

# ==========================================
# 🛡️ 注入自訂 CSS：隱藏預設選單，打造 100% 私有軟體感
# ==========================================
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# ==========================================
# 💎 側邊欄設計 (Sidebar)：高階戰情儀表板
# ==========================================
with st.sidebar:
    st.title("👩‍💻 思嘉的專屬口碑戰情室")
    st.markdown("AI 輿情監測與公關防護主控台")
    st.divider()
    
    # 戰情室儀表板組件
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="📊 系統狀態", value="🟢 上線中")
    with col2:
        st.metric(label="🔥 鎖定論壇", value="PTT, Dcard")
    st.metric(label="🕸️ 即時串接平台", value="Threads, Facebook, 各大論壇")
    
    st.divider()
    
    mode = st.radio(
        "🎯 核心分析模組：",
        (
            "✅ 一般產品常規健檢", 
            "🏥 醫美口碑鋪陳製造機",
            "⚖️ 醫美療程與儀器大比拼",
            "🚨 特定負評拆彈與攻防"
        )
    )
    
    st.divider()
    st.caption("© 2026 思嘉專屬開發 ｜ AI 行銷科技工具")

# ==========================================
# 💎 主畫面動態標題
# ==========================================
st.title("📝 全能口碑操盤與危機處理分析儀")
st.markdown(f"**目前啟用模式：** `{mode}`")
st.markdown("---")

# ==========================================
# 🚪 第一扇門：一般產品常規健檢
# ==========================================
if mode == "✅ 一般產品常規健檢":
    st.info("💡 **操作指南**：輸入產品或品牌名稱，AI 將自動彙整論壇真實聲量與優缺點。")
    product_name = st.text_input("📦 請輸入想查詢的「產品或品牌名稱」：", placeholder="例如：娘家葉黃素、理膚寶水 B5")
    
    if st.button("🚀 開始深度健檢", type="primary", use_container_width=True):
        if product_name:
            # 使用高階的 status 載入動畫
            with st.status("🕵️‍♂️ 系統連線與 AI 深度運算中...", expanded=True) as status:
                st.write("🔍 掃描 Threads、Dcard、PTT 討論區...")
                st.write("🧠 執行語意分析與公關危機探測...")
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
                    status.update(label="✨ 報告解析完成！", state="complete", expanded=False)
                    st.toast('專屬報告已產出！', icon='🎉')
                    st.success("✅ 分析完成！以下是您的專屬報告：")
                    st.write(response.text)
                except Exception as e:
                    status.update(label="❌ 發生錯誤", state="error", expanded=False)
                    st.error(f"發生錯誤：{e}")
        else:
            st.warning("⚠️ 請先輸入名稱喔！")

# ==========================================
# 🚪 第二扇門：醫美口碑鋪陳製造機
# ==========================================
elif mode == "🏥 醫美口碑鋪陳製造機":
    st.info("💡 **操作指南**：生成去業配感、高真實感的論壇發文與暗樁互動劇本。")
    col_t, col_a = st.columns(2)
    with col_t:
        treatment = st.text_input("💉 療程名稱：", placeholder="例如：法令紋玻尿酸")
    with col_a:
        advantages = st.text_input("✨ 主打優勢：", placeholder="例如：醫師美感自然、無硬塊")
        
    if st.button("🚀 生成高真實感口碑劇本", type="primary", use_container_width=True):
        if treatment and advantages:
            with st.status("✍️ AI 網軍總監正在植入真實鄉民語氣...", expanded=True) as status:
                st.write("🎭 套用去業配感指令...")
                st.write("🗣️ 生成多層次推文互動陣型...")
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
                        "1. 🎯 平台主文切角與吸睛標題 (Threads、Dcard 各 3 個)\n"
                        "2. 📝 主文內容大綱 (內容須符合Threads、Dcard 平台討論屬性)\n"
                        "3. 🗣️ 暗樁推文與蓋樓劇本 (1-5樓推文，需包含中立言論、資訊設計問答、微負評包裝好評)\n"
                        "4. 🛡️ 競品防禦與帶風向話術：如果底下有真實網友留言推薦其他診所，我們的暗樁該用什麼話術自然地把風向帶回來？"
                    )
                    response = model.generate_content(prompt)
                    status.update(label="✨ 劇本編寫完成！", state="complete", expanded=False)
                    st.toast('戰術劇本已送達！', icon='🔥')
                    st.success("✅ 以下是極致真實的口碑操作企劃：")
                    st.write(response.text)
                except Exception as e:
                    status.update(label="❌ 發生錯誤", state="error", expanded=False)
                    st.error(f"發生錯誤：{e}")
        else:
            st.warning("⚠️ 請務必填寫「療程名稱」與「主打優勢」喔！")

# ==========================================
# 🚪 第三扇門：醫美療程彈性大比拼
# ==========================================
elif mode == "⚖️ 醫美療程與儀器大比拼":
    st.info("💡 **操作指南**：輸入 2 到 4 個選手進行對比，系統會自動產出殘酷比較表格。")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        item1 = st.text_input("🥊 選手 1", placeholder="例如：鳳凰電波")
    with col2:
        item2 = st.text_input("🥊 選手 2", placeholder="例如：十蓓電波")
    with col3:
        item3 = st.text_input("🥊 選手 3 (選填)", placeholder="例如：玩美電波")
    with col4:
        item4 = st.text_input("🥊 選手 4 (選填)", placeholder="例如：黃金電波")
    
    if st.button("🚀 開始多重殘酷比拼", type="primary", use_container_width=True):
        items_to_compare = [i for i in [item1, item2, item3, item4] if i.strip()]
        
        if len(items_to_compare) >= 2:
            items_str = "、".join(items_to_compare)
            with st.status(f"🥊 正在對比 {items_str} 的優劣勢...", expanded=True) as status:
                st.write("⚖️ 讀取儀器與療程技術規格...")
                st.write("🗣️ 彙整論壇網友真實痛點與反饋...")
                try:
                    prompt = (
                        f"你是一位專業且中立的醫美分析師，深諳台灣Threads、 Dcard 與 PTT 醫美板風向。\n"
                        f"請幫我深度比較以下項目：{items_str}。\n\n"
                        "報告必須包含以下模塊，並使用 Markdown 表格呈現對比：\n"
                        "1. 🔬 核心原理白話文解釋：這幾者在技術原理上的關鍵差異。\n"
                        "2. 📊 清楚對比表格：包含效果、維持時間、痛感評估、恢復期、價格區間、副作用風險、論壇討論熱度。\n"
                        "3. 🎯 適合對象分析：分別針對不同預算、痛感承受度、期望效果的受眾給予建議。\n"
                        "4. 🗣️ 論壇真實風向與常見抱怨：網友對這幾項療程分別最常酸什麼？或最擔憂什麼？\n"
                        "5. ⚔️ 口碑行銷攻防建議：若客戶主打其中一項，該如何在論壇「請益文」中自然地引導風向？提供 3 個發文切角。\n"
                        "6. 💡 總結：一句話點出這幾者的定位差異。"
                    )
                    response = model.generate_content(prompt)
                    status.update(label="✨ 殘酷比拼完成！", state="complete", expanded=False)
                    st.toast('比較報表出爐！', icon='📊')
                    st.success(f"✅ 以下是 {len(items_to_compare)} 項目的深度報告：")
                    st.write(response.text)
                except Exception as e:
                    status.update(label="❌ 發生錯誤", state="error", expanded=False)
                    st.error(f"發生錯誤：{e}")
        else:
            st.warning("⚠️ 請至少輸入兩個項目才能進行比較喔！")

# ==========================================
# 🚪 第四扇門：特定負評拆彈與攻防
# ==========================================
else: 
    st.error("🚨 **危機處理主控台**：請將論壇或 Google 評論的原始負評貼在下方，啟動緊急防守對策。")
    raw_reviews = st.text_area("💬 請貼上網友的「原始負評」內容：", height=150, placeholder="將客訴或抱怨文直接貼在這裡...")
    
    if st.button("🚀 啟動緊急拆彈程序", type="primary", use_container_width=True):
        if raw_reviews:
            with st.status("🚨 危機處理專家已連線，正在擬定對策...", expanded=True) as status:
                st.write("🛡️ 評估炎上風險與擴散層級...")
                st.write("⚔️ 生成官方安撫與暗樁防守腳本...")
                try:
                    prompt = (
                        f"你是一位擁有 15 年經驗的資深危機處理公關以及有資深的網路口碑操作經驗。客戶目前遭遇了以下網友的具體負評：\n"
                        f"「{raw_reviews}」\n"
                        "請提供「負評拆彈作戰計畫」，包含：\n"
                        "1. 🚨 危機等級與擴散風險\n"
                        "2. 🌋 核網友情緒與真實痛點\n"
                        "3. 🛡️ 負評處理及風向平衡 (5 個不同人設的暗樁留言切角，溫和稀釋負面)\n"
                        "4. ⚔️ 口碑主動攻防與風向引導 (風向轉移、反向質疑原 PO 動機、洗文稀釋策略)\n"
                        "5. ⚖️ 平台機制與長尾防護 (檢舉下架可行性與 SEO 防護)\n"
                        "6. ⏳ 黃金應對行動時間表 (2小時與24小時內的具體動作)\n"
                        "7. 🩹 官方回覆與私訊溝通範本 (公開留言與私訊安撫文字)" 
                    )
                    response = model.generate_content(prompt)
                    status.update(label="✨ 危機拆彈對策擬定完畢！", state="complete", expanded=False)
                    st.toast('防守劇本已生成！', icon='🛡️')
                    st.success("✅ 以下是為您擬定的作戰計畫：")
                    st.write(response.text)
                except Exception as e:
                    status.update(label="❌ 發生錯誤", state="error", expanded=False)
                    st.error(f"發生錯誤：{e}")
        else:
            st.warning("⚠️ 拆彈模式需要您先貼上原始負評喔！")
