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
/* 隱藏預設選單與頁首頁尾 */
#MainMenu {visibility: hidden;}
[data-testid="stToolbar"] {visibility: hidden;}
[data-testid="stHeader"] {visibility: hidden;}
footer {visibility: hidden;}

/* 🔨 終極黑魔法：嘗試暴力隱藏所有 Streamlit 官方浮動按鈕 */
[data-testid="stAppDeployButton"] {display: none !important;}
[data-testid="manage-app-badge"] {display: none !important;}
[class^="viewerBadge"] {display: none !important;}
.viewerBadge_container__1QSob,
.styles_viewerBadge__1yB5_,
.viewerBadge_link__1S137,
.viewerBadge_text__1JaDK {display: none !important;}

/* 讓分頁籤的字體稍微放大，增加質感 */
.stTabs [data-baseweb="tab-list"] {
    gap: 10px;
}
.stTabs [data-baseweb="tab"] {
    font-size: 16px;
    padding-top: 10px;
    padding-bottom: 10px;
}

/* 👑 左下角個人專屬浮水印設定 */
.custom-watermark {
    position: fixed;
    bottom: 15px;      
    left: 20px;       
    color: #BBBBBB;    
    font-size: 12px;   
    font-weight: 500;
    letter-spacing: 1px;
    z-index: 100;      
    user-select: none; 
}
</style>

<div class="custom-watermark">
    © 2026 Crafted by Irene Huang | Booyah
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
# 🗂️ 核心功能：精簡為四大萬用分頁 + SEO 訓練儀
# ==========================================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "✅ 產品網路健檢", 
    "🌟 全產業口碑製造機", 
    "⚖️ 競品與服務比較", 
    "🚨 負評拆彈與攻防",
    "📈 標題與 SEO 訓練儀"
])

# ------------------------------------------
# 🚪 第一分頁：一般產品常規健檢
# ------------------------------------------
with tab1:
    st.info("💡 **操作指南**：輸入產品或品牌名稱，AI 將自動彙整各大論壇真實聲量與優缺點。")
    product_name = st.text_input("📦 請輸入想查詢的「品牌或產品名稱」：", placeholder="例如：理膚寶水 B5、娘家大紅麴、某某室內設計...")
    
    if st.button("🚀 開始深度健檢", type="primary"):
        if product_name:
            with st.spinner("🕵️‍♂️ AI 正在深度分析中，請稍候..."):
                try:
                    prompt = (
                        f"你是一位資深的消費者口碑分析師。請深度分析台灣各大熱門論壇(包含Threads、Dcard、PTT、Mobile01等等)對於「{product_name}」的最新真實討論。\n"
                        "過濾掉業配文，並提供包含以下 10 點的報告：\n"
                        "1. 📊 網路聲量總結 (整體討論熱度與正負評比例)\n"
                        "2. 📈 近三個月網路論壇討論聲量及狀況\n"
                        "3. ✨ 真實優點歸納 (口語化列出 3-5 點網友高討論的特色)\n"
                        "4. 💣 踩雷與缺點抱怨 (不修飾口語化列出真實痛點)\n"
                        "5. 📝 以一般網友口吻分享此產品使用心得\n"
                        "6. 🗣️ 素人發文切角建議 (提供 5 個最自然、不具業配感的論壇討論情境)\n"
                        "7. 📌 此產品於各論壇討論風向差異 (Threads、Dcard、PTT、Mobile01等論壇網友在意的點有何不同？)\n"
                        "8. 🚨 潛在公關危機預警 (目前最致命的負面標籤，並給予平衡建議)\n"
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
# 🚪 第二分頁：全產業口碑製造機
# ------------------------------------------
with tab2:
    st.info("💡 **操作指南**：設定產業與人設條件，下列方框會即時顯示「AI 詠唱指令」。")
    
    col_ind, col_t, col_a = st.columns([1.5, 2, 2])
    with col_ind:
        industry = st.selectbox("🏢 產業類別：", ["醫美", "保健食品",  "牙科", "眼科", "美容美體", "醫療器材", "室內設計", "月子中心","美妝保養"])
    with col_t:
        treatment = st.text_input("📦 產品/服務名稱：", placeholder="例如：海芙音波、葉黃素、新屋裝潢...")
    with col_a:
        advantages = st.text_input("✨ 主打優勢：", placeholder="例如：無推銷、成分天然、設計師好溝通...")
    
    st.markdown("---")
    st.markdown("#### 🎛️ 素人發文者靈魂設定")
    
    urgent_text = st.text_input("🚨 發文動機及情境 (強烈建議填寫)：", placeholder="例如：下個月要拍婚紗、長輩健檢報告紅字、剛買新房預算只有一百萬...")

    col_p1, col_p2 = st.columns(2)
    with col_p1:
        finance_level = st.select_slider(
            "💰 預算與金錢觀設定：",
            options=["不指定", "不在乎價格(只求最好)", "預算充足", "精打細算(重視CP值)", "預算極度緊繃"],
            value="不指定"
        )
        concern_type = st.selectbox("⚠️ 消費者最大顧慮 (痛點)：", [
            "不指定", 
            "怕沒效果/浪費錢 (保健品/保養品/醫美)",
            "怕被當盤子/隱藏追加費用 (裝潢/醫美/月子中心)",
            "怕服務人員態度差/強迫推銷",
            "怕成分不安全/有副作用",
            "怕痛/怕恢復期長 (醫美專用)"
        ])
        
    with col_p2:
        platform_style = st.selectbox("🗣️ 鎖定論壇語氣：", [
            "不指定 (一般真實網友語氣)", 
            "Dcard 閒聊/女孩板 (多內心戲、求打醒、常用空格排版)",
            "Threads 脆友 (句子短、不愛標點、帶有自嘲與厭世感)",
            "PTT 鄉民老手 (講話直接、重視專業數據或CP值)", 
            "Mobile01 / FB社團 (圖文並茂詳細開箱、婆媽群聚落)"
        ])

    st.markdown("##### 🧠 幕後 AI 詠唱指令預覽")
    
    live_prompt = f"👉 目標產業：【{industry}】\n"
    if urgent_text.strip():
        live_prompt += f"👉 特殊情境：{urgent_text}，請在內文中表現出強烈的焦慮或迫切需求。\n"
    if finance_level != "不指定":
        live_prompt += f"👉 金錢觀念：身為「{finance_level}」的消費者，請表現出對應的消費態度。\n"
    if concern_type != "不指定":
        live_prompt += f"👉 核心顧慮：極度擔心「{concern_type}」，請在文中不斷詢問網友意見或表達擔憂。\n"
    if platform_style != "不指定":
        live_prompt += f"👉 平台語癖：完全模仿「{platform_style}」的用語習慣。\n"
    
    st.code(live_prompt, language="markdown")
        
    if st.button("🚀 生成全方位口碑劇本", type="primary"):
        if treatment and advantages:
            with st.spinner("✍️ 正在融合產業知識與鄉民人設..."):
                try:
                    prompt = (
                        f"你是一位擁有 15 年經驗的頂級網路口碑操盤手，專攻台灣熱門網路論壇 (Threads、Dcard、PTT、Mobile01等)。\n"
                        f"請針對以下設定，為客戶撰寫一套「極致真實、絕對去業配感」的論壇口碑鋪陳劇本。\n\n"
                        f"【操作目標設定】\n"
                        f"📍 所屬產業：{industry}\n"
                        f"📍 產品/服務項目：{treatment}\n"
                        f"📍 主打優勢：{advantages}\n\n"
                        f"【發文者專屬立體人設】\n"
                        f"請務必嚴格遵循以下多維度人設來調整語氣、排版與內文邏輯：\n"
                        f"{live_prompt}\n\n"
                        f"【⚠️ 絕對不可違背的『去業配』鐵血指令】\n"
                        "1. 資訊模糊化：主文中【絕對不可以】完整打出品牌全名、診所名稱或設計公司全名。\n"
                        "2. 禁用公關用語：嚴禁出現「專業團隊、業界第一、強烈推薦」等行銷詞彙。\n"
                        "3. 植入無傷大雅的抱怨：必須穿插 1~2 個微負評（如：難預約、客服回覆慢、包裝難拆、附近難停車）。\n"
                        "4. 強化情緒起伏：根據設定的「金錢觀」與「核心顧慮」，寫出最真實的擔憂與期待。\n\n"
                        "請提供：\n"
                        "1. 🎯 平台主文切角與吸睛標題 (提供適合該產業論壇的 3 個標題)\n"
                        "2. 📝 主文內容大綱 (必須完美融入面板設定的人設語氣)\n"
                        "3. 🗣️ 暗樁推文與蓋樓劇本 (1-5樓推文，需包含中立觀望、真實提問、微負評包裝好評)\n"
                        "4. 🛡️ 競品防禦與帶風向話術：如果底下有真實網友留言推薦其他競品，我們的暗樁該用什麼話術自然地把風向帶回來？"
                    )
                    response = model.generate_content(prompt)
                    st.success("✨ 劇本生成完成！以下是專屬口碑操作企劃：")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"發生錯誤：{e}")
        else:
            st.warning("⚠️ 請務必填寫上方最基本的「產品/服務名稱」與「主打優勢」喔！")

# ------------------------------------------
# 🚪 第三分頁：競品與服務比較
# ------------------------------------------
with tab3:
    st.info("💡 **操作指南**：輸入 2 到 4 個選手(產品/服務/醫美儀器皆可)進行對比，系統會自動產出比較表格。")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        item1 = st.text_input("🥊 選手 1", placeholder="例如：娘家大紅麴")
    with col2:
        item2 = st.text_input("🥊 選手 2", placeholder="例如：大研生醫納豆紅麴")
    with col3:
        item3 = st.text_input("🥊 選手 3 (選填)", placeholder="例如：老協珍...")
    with col4:
        item4 = st.text_input("🥊 選手 4 (選填)", placeholder="例如：其他競品...")
    
    if st.button("🚀 開始多重殘酷比拼", type="primary", key="btn3"):
        items_to_compare = [i for i in [item1, item2, item3, item4] if i.strip()]
        if len(items_to_compare) >= 2:
            items_str = "、".join(items_to_compare)
            with st.spinner(f"🥊 正在為您跨界對比 {items_str} ..."):
                try:
                    prompt = (
                        f"你是一位專業且中立的資深產業分析師，深諳台灣各大網路論壇(Threads、Dcard、PTT、Mobile01)的真實風向。\n"
                        f"請幫我深度比較以下項目：{items_str}。\n\n"
                        "報告必須包含以下模塊，並使用 Markdown 表格呈現對比：\n"
                        "1. 🔬 核心差異白話文解釋：這幾者在成分、技術或服務本質上的關鍵差異。\n"
                        "2. 📊 清楚對比表格：請依據該產品/服務的特性，列出最重要的比較維度(例如：價格區間、主要特色、潛在缺點、適合受眾、論壇討論熱度等)。\n"
                        "3. 🎯 適合對象分析：分別針對不同預算、不同痛點的受眾給予購買或選擇建議。\n"
                        "4. 🗣️ 論壇真實風向與常見抱怨：網友對這幾項選擇分別最常酸什麼？或最擔憂什麼？\n"
                        "5. ⚔️ 口碑行銷攻防建議：若客戶主打其中一項，該如何在論壇「請益文」中自然地引導風向？提供 3 個發文切角。\n"
                        "6. 💡 總結：一句話點出這幾者的定位差異。"
                    )
                    response = model.generate_content(prompt)
                    st.success(f"✨ 比對完成！以下是 {len(items_to_compare)} 項目的深度分析報告：")
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
    raw_reviews = st.text_area("💬 請貼上網友的「原始負評」內容：", height=150, placeholder="將各產業的客訴或抱怨文貼在這裡...")
    
    if st.button("🚀 啟動緊急拆彈程序", type="primary", key="btn4"):
        if raw_reviews:
            with st.spinner("🚨 危機處理專家已連線，正在擬定對策..."):
                try:
                    prompt = (
                        f"你是一位擁有 15 年經驗的資深危機處理公關以及有資深的網路口碑操作經驗。客戶目前遭遇了以下網友的具體負評：\n"
                        f"「{raw_reviews}」\n"
                        "請提供「負評拆彈作戰計畫」，包含：\n"
                        "1. 🚨 危機等級與擴散風險\n"
                        "2. 🌋 核心網友情緒與真實痛點\n"
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
# 🚪 第五分頁：SEO 素人標題製造機 (🌟 真實提問/分享無痕版)
# ------------------------------------------
with tab5:
    st.info("💡 **操作指南**：輸入關鍵字並選擇「請益」或「分享」，系統會自動將 SEO 關鍵字『無痕』融入最自然的素人標題中，讓文章具備高點擊率且不著痕跡！")
    
    st.markdown("#### 🔑 1. 設定 SEO 關鍵字佈局")
    col_k1, col_k2 = st.columns(2)
    with col_k1:
        seo_core_kw = st.text_input("🎯 核心關鍵字 (Target Keyword)：", placeholder="例如：法令紋玻尿酸、室內設計推薦...", help="您最希望排上 Google 第一頁的主詞彙。")
    with col_k2:
        seo_long_kw = st.text_input("🔎 長尾關鍵字 (Long-tail Keywords)：", placeholder="例如：費用, 後遺症, 評價...", help="網友搜尋時常搭配核心關鍵字的字詞，請用逗號分隔。")

    st.markdown("#### 🗣️ 2. 設定文章類型與意圖")
    col_i1, col_i2 = st.columns(2)
    with col_i1:
        post_type = st.selectbox(
            "📝 文章類型 (影響標題結構)：",
            ["🙋‍♀️ 請益/求救文 (以自然提問、求推薦、擔憂為主)", 
             "✨ 真實分享文 (以素人真實心得、避雷、心得為主)"]
        )
    with col_i2:
        seo_intent = st.selectbox(
            "🧠 網友搜尋這些字的意圖是？",
            ["想找便宜/比價/看費用", 
             "怕踩雷/看失敗心得/問缺點", 
             "看真實效果/開箱/對比圖",
             "單純收集名單/求推薦"]
        )

    st.divider()

    if st.button("🚀 產出無業配感 SEO 標題", type="primary", key="btn5"):
        if seo_core_kw:
            with st.spinner("🤖 正在演算最自然的素人標題與搜尋邏輯..."):
                try:
                    prompt = (
                        f"你是一位精通 Google 搜尋演算法與台灣論壇(Dcard、PTT、Mobile01)生態的資深素人口碑操盤手。\n"
                        f"操作目標：產出極度自然、完全沒有業配感，但又能完美吻合 Google 搜尋爬蟲胃口的「素人論壇標題」。\n\n"
                        f"【操作條件】\n"
                        f"📍 核心關鍵字：{seo_core_kw}\n"
                        f"📍 附屬長尾字：{seo_long_kw if seo_long_kw else '無特定'}\n"
                        f"📍 文章類型：{post_type}\n"
                        f"📍 搜尋意圖：{seo_intent}\n\n"
                        "【⚠️ 絕對不可違背的『去農場化』鐵血指令】\n"
                        "1. 嚴禁農場標題：絕對不可出現「2026最新」、「必看」、「大公開」、「驚呆了」等吸睛字眼。\n"
                        "2. 嚴禁濫用符號：不要在標題使用過多 【】、🔥、✨ 等圖案，請模仿一般網友用手機快速打字的隨性習慣，頂多使用單純的空格、逗號或問號。\n"
                        "3. 隱藏操作痕跡：如果選擇「請益文」，標題必須是真的像在發問（例如：XXX費用大概多少？有後遺症嗎？求推薦）；如果是「分享文」，語氣要平淡甚至帶點微抱怨（例如：終於去做了XXX，分享一下真實心得）。\n"
                        "4. 關鍵字自然融入：將核心與長尾字順暢地安插在標題中，絕不能像硬塞字詞的廣告文。\n\n"
                        "【請產出以下內容】\n"
                        "我「只需要」標題與搜尋邏輯分析。請給我 5 個最完美的標題選項。\n"
                        "格式請完全依照以下呈現：\n\n"
                        "🔹 標題 1：[產出的素人自然標題]\n"
                        "   └ 📈 SEO與搜尋邏輯分析：[簡述為何這個標題能被 Google 收錄，且網友看不出是刻意操作]\n\n"
                        "(以此類推，產出 5 個選項)"
                    )
                    response = model.generate_content(prompt)
                    st.success("✨ 演算完成！請參考以下最自然的 SEO 標題佈局：")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"發生錯誤：{e}")
        else:
            st.warning("⚠️ SEO 操作最基本的就是「核心關鍵字」，請務必填寫喔！")
