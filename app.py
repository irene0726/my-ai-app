import streamlit as st
import google.generativeai as genai

# 1. 呼叫雲端保險箱裡的金鑰
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

# 2. 使用最新 2.5 版本模型
model = genai.GenerativeModel('gemini-2.5-flash')

# --- 網頁前端介面設計 ---
st.set_page_config(page_title="全能口碑操盤分析儀", page_icon="📝", layout="wide")

# ==========================================
# 🛡️ 隱藏魔法 & 👑 專屬個人浮水印
# ==========================================
hide_streamlit_style = """
<style>
/* 隱藏預設選單與浮水印 */
#MainMenu {visibility: hidden;}
[data-testid="stToolbar"] {visibility: hidden;}
[data-testid="stHeader"] {visibility: hidden;}
footer {visibility: hidden;}

/* 讓分頁籤的字體稍微放大，增加質感 */
.stTabs [data-baseweb="tab-list"] {
    gap: 10px;
}
.stTabs [data-baseweb="tab"] {
    font-size: 16px;
    padding-top: 10px;
    padding-bottom: 10px;
}

/* 👑 右下角個人專屬浮水印設定 */
.custom-watermark {
    position: fixed;
    bottom: 15px;      /* 距離底部的距離 */
    right: 20px;       /* 距離右側的距離 (若想放左邊，可改為 left: 20px;) */
    color: #BBBBBB;    /* 字體顏色，使用淺灰色比較有質感且不干擾閱讀 */
    font-size: 12px;   /* 字體大小 */
    font-weight: 500;
    letter-spacing: 1px;
    z-index: 100;      /* 確保浮水印永遠在最上層 */
    user-select: none; /* 防止被反白選取 */
}
</style>

<div class="custom-watermark">
    © 2026 Crafted by 思嘉 | AI 口碑戰情室
</div>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ==========================================
# 💎 主標題區
# ==========================================
st.title("📝 全能口碑操盤與危機處理分析儀")
st.markdown("專屬 AI 輿情監測與公關防護主控台")
st.divider()

# ==========================================
# 🗂️ 核心功能：使用「分頁籤 (Tabs)」取代傳統按鈕 (加入第五分頁)
# ==========================================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "✅ 產品網路健檢", 
    "🏥 醫美口碑製造機", 
    "⚖️ 醫美療程比較", 
    "🚨 負評拆彈與攻防",
    "🎓 文案訓練儀"
])

# ------------------------------------------
# 🚪 第一分頁：一般產品常規健檢
# ------------------------------------------
with tab1:
    st.info("💡 **操作指南**：輸入產品或品牌名稱，AI 將自動彙整各大論壇真實聲量與優缺點。")
    product_name = st.text_input("📦 請輸入想查詢的「產品或品牌名稱」：", placeholder="例如：理膚寶水 B5")
    
    if st.button("🚀 開始深度健檢", type="primary"):
        if product_name:
            with st.spinner("🕵️‍♂️ AI 正在深度分析中，請稍候..."):
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
                        "8. 🚨 潛公關危機預警 (目前最致命的負面標籤，並給予平衡建議)\n"
                        "9. 🔗 競業分析及對比（找出相對於競業的優勢做口碑攻防）\n"
                        "10. 🎯 總結與行銷策略建議"
                    )
                    response = model.generate_content(prompt)
                    st.success("✨ 分析完成！以下是專屬報告：")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"發生錯誤：{e}")
        else:
            st.warning("⚠️ 請先輸入名稱喔！")

# ------------------------------------------
# 🚪 第二分頁：醫美口碑製造機
# ------------------------------------------
with tab2:
    st.info("💡 **操作指南**：透過下方的【互動開關與滑桿】，像疊積木一樣快速組合出專屬的發文者靈魂。")
    col_t, col_a = st.columns(2)
    with col_t:
        treatment = st.text_input("💉 療程名稱：", placeholder="例如：法令紋玻尿酸")
    with col_a:
        advantages = st.text_input("✨ 主打優勢：", placeholder="例如：醫師美感自然、無硬塊")
    
    st.markdown("---")
    st.markdown("#### 🎛️ 人設設定")
    
    urgent_text = st.text_input("🚨 動機及情境 (強烈建議填寫)：", placeholder="例如：快要結婚、前任交新歡、下個月要拍婚紗了，卡粉超嚴重...")

    col_p1, col_p2 = st.columns(2)
    with col_p1:
        # 🌟 修改點：將「不指定」移到陣列最左邊
        finance_level = st.select_slider(
            "💰 預算與金錢觀設定：",
            options=["不指定", "不在乎價格(貴婦)", "預算充足", "精打細算(小資)", "極度怕浪費錢(窮學生)"],
            value="不指定"
        )
        # 🌟 修改點：將「不指定」移到陣列最左邊
        pain_level = st.select_slider(
            "😣 痛感承受度設定：",
            options=["不指定", "超耐痛", "微怕痛", "極度怕痛"],
            value="不指定"
        )
        
    with col_p2:
        platform_style = st.selectbox("🗣️ 鎖定論壇語氣：", [
            "一般真實網用語氣", 
            "Dcard 女孩板 (有較多murmur)",
            "Threads 脆友 (句子短、帶有自嘲及厭世感)",
            "PTT 醫美板老手 (講話簡明扼要)", 
        ])

    st.markdown("##### 👁️ AI 接收到的隱藏人設指令預覽")
    
    live_prompt = ""
    if urgent_text.strip():
        live_prompt += f"👉 特殊情境：{urgent_text}，請在內文表現出強烈的焦慮與急迫感。\n"
    if finance_level != "不指定":
        live_prompt += f"👉 金錢觀念：{finance_level}\n"
    if pain_level != "不指定":
        live_prompt += f"👉 痛感承受：{pain_level}\n"
    live_prompt += f"👉 平台語癖：{platform_style}\n"
    
    st.code(live_prompt, language="markdown")
        
    if st.button("🚀 以此人設生成高真實感劇本", type="primary"):
        if treatment and advantages:
            with st.spinner("✍️ 正在讀取互動面板參數，植入真實鄉民語氣..."):
                try:
                    prompt = (
                        f"你是一位擁有 15 年經驗的頂級網路口碑操盤手，專攻台灣熱門網路醫美論壇，包含Threads、Dcard、PTT。\n"
                        f"請針對以下設定，為客戶撰寫一套「極致真實、絕對去業配感」的論壇口碑鋪陳劇本。\n\n"
                        f"【操作目標設定】\n"
                        f"📍 療程項目：{treatment}\n"
                        f"📍 診所/醫師主打優勢：{advantages}\n\n"
                        f"【發文者專屬立體人設】\n"
                        f"請務必嚴格遵循以下多維度人設來調整語氣、排版與內文邏輯：\n"
                        f"{live_prompt}\n\n"
                        f"【⚠️ 絕對不可違背的『去業配』鐵血指令】\n"
                        "1. 資訊模糊化：主文中【絕對不可以】完整打出診所名稱或醫師全名。\n"
                        "2. 禁用公關用語：嚴禁出現「專業團隊、高CP值、強烈推薦」等行銷詞彙。\n"
                        "3. 植入無傷大雅的抱怨：必須穿插 1~2 個微負評（如：難預約、附近難停車、等太久）。\n"
                        "4. 強化情緒起伏：根據上述的「金錢觀」與「特殊情境」，寫出最真實的焦慮、期待或痛點。\n\n"
                        "請提供：\n"
                        "1. 🎯 平台主文切角與吸睛標題 (Threads、Dcard 各 3 個)\n"
                        "2. 📝 主文內容大綱 (必須完美融入面板設定的人設語氣與排版)\n"
                        "3. 🗣️ 暗樁推文與蓋樓劇本 (1-5樓推文，需包含中立言論、資訊設計問答、微負評包裝好評)\n"
                        "4. 🛡️ 競品防禦與帶風向話術：如果底下有真實網友留言推薦其他診所，我們的暗樁該用什麼話術自然地把風向帶回來？"
                    )
                    response = model.generate_content(prompt)
                    st.success("✨ 劇本生成完成！以下是專屬口碑操作企劃：")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"發生錯誤：{e}")
        else:
            st.warning("⚠️ 請務必填寫上方最基本的「療程名稱」與「主打優勢」喔！")

# ------------------------------------------
# 🚪 第三分頁：醫美療程彈性大比拼
# ------------------------------------------
with tab3:
    st.info("💡 **操作指南**：輸入 2 到 4 個選手進行對比，系統會自動產出比較表格。")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        item1 = st.text_input("🥊 選手 1", placeholder="例如：鳳凰電波")
    with col2:
        item2 = st.text_input("🥊 選手 2", placeholder="例如：十蓓電波")
    with col3:
        item3 = st.text_input("🥊 選手 3 (選填)", placeholder="例如：玩美電波")
    with col4:
        item4 = st.text_input("🥊 選手 4 (選填)", placeholder="例如：海芙電波")
    
    if st.button("🚀 開始多重殘酷比拼", type="primary", key="btn3"):
        items_to_compare = [i for i in [item1, item2, item3, item4] if i.strip()]
        if len(items_to_compare) >= 2:
            items_str = "、".join(items_to_compare)
            with st.spinner(f"🥊 正在對比 {items_str} ..."):
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
                    st.success(f"✨ 比對完成！以下是 {len(items_to_compare)} 項目的深度報告：")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"發生錯誤：{e}")
        else:
            st.warning("⚠️ 請至少輸入兩個項目才能進行比較喔！")

# ------------------------------------------
# 🚪 第四分頁：特定負評拆彈與攻防
# ------------------------------------------
with tab4:
    st.error("🚨 **危機處理主控台**：請將原始負評貼在下方，啟動緊急防守對策。")
    raw_reviews = st.text_area("💬 請貼上網友的「原始負評」內容：", height=150, placeholder="將客訴或抱怨文貼在這裡...")
    
    if st.button("🚀 啟動緊急拆彈程序", type="primary", key="btn4"):
        if raw_reviews:
            with st.spinner("🚨 危機處理專家已連線，正在擬定對策..."):
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
                    st.success("✨ 危機拆彈對策擬定完畢！")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"發生錯誤：{e}")
        else:
            st.warning("⚠️ 拆彈模式需要您先貼上原始負評喔！")

# ------------------------------------------
# 🚪 第五分頁：文案訓練儀 (教育訓練專用)
# ------------------------------------------
with tab5:
    st.info("💡 **教案模式**：透過隨意調整下方的設定，觀察 AI 是如何一步步疊加維度，從「生硬機器人」進化成「超真實鄉民」。")
    
    st.markdown("#### 🛠️ 1. 設定基礎題材")
    col_t5, col_a5 = st.columns(2)
    with col_t5:
        base_treatment = st.text_input("💉 產品/療程：", value="法令紋玻尿酸", key="t5")
    with col_a5:
        base_advantage = st.text_input("✨ 主打優勢：", value="醫師美感自然、不推銷", key="a5")

    st.markdown("#### 🎛️ 2. 操作訓練維度")
    
    urgent_text_5 = st.text_input("🚨 動機及情境：", value="下個月就要拍婚紗了，卡粉超嚴重", key="u5", help="清空此欄位即代表不加入特殊情境")

    col_p5_1, col_p5_2 = st.columns(2)
    with col_p5_1:
        # 🌟 修改點：將「(不指定)」移到陣列最左邊
        finance_level_5 = st.select_slider(
            "💰 預算與金錢觀設定：",
            options=["(不指定)", "不在乎價格(貴婦)", "預算充足", "精打細算(小資)", "極度怕浪費錢(窮學生)"],
            value="(不指定)",
            key="f5"
        )
    with col_p5_2:
        platform_style_5 = st.selectbox(
            "🗣️ 鎖定論壇語氣：",
            ["(不指定)", "Dcard 女孩板 (有較多murmur)", "Threads 脆友 (句子短、帶有自嘲及厭世感)","PTT 醫美板老手 (講話簡明扼要)"],
            key="p5"
        )

    st.divider()

    # --- 在背後動態組合送給 AI 的 Prompt ---
    training_prompt = f"你現在是一位常在論壇發文的一般網友。請幫我寫一篇關於「{base_treatment}」的討論短文，並在文中自然帶出「{base_advantage}」的體驗。\n\n"
    training_prompt += "【嚴格指令限制】：\n"
    training_prompt += "👉 資訊模糊化：絕對不可以完整打出診所名稱或醫師全名。\n"

    has_extra = False
    if urgent_text_5.strip():
        training_prompt += f"👉 情境設定：{urgent_text_5}。請在內文表現出強烈的焦慮與急迫感。\n"
        has_extra = True
    if finance_level_5 != "(不指定)":
        training_prompt += f"👉 金錢觀設定：你的金錢觀是「{finance_level_5}」，請在文中表現出對應的消費態度與猶豫感。\n"
        has_extra = True
    if platform_style_5 != "(不指定)":
        training_prompt += f"👉 語氣設定：完全模仿「{platform_style_5}」的用語習慣與排版格式。\n"
        has_extra = True

    if not has_extra:
        training_prompt += "👉 綜合設定：使用一般官方、客氣且平淡的推薦語氣即可 (生硬機器人狀態)。\n"

    # --- 顯示即時的 Prompt 讓受訓者學習 ---
    st.markdown("##### 🔍 觀察送給 AI 的幕後指令變化")
    st.code(training_prompt, language="markdown")
    
    if st.button("🚀 執行訓練測試", type="primary", key="btn5"):
        with st.spinner("🧠 AI 正在根據維度疊加模擬中..."):
            try:
                response = model.generate_content(training_prompt)
                st.success("✨ 產出結果比對：")
                st.write(response.text)
            except Exception as e:
                st.error(f"發生錯誤：{e}")
