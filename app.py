import streamlit as st
import google.generativeai as genai
import pandas as pd
import io
import json

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
# 🗂️ 核心功能：精簡為各大萬用分頁 + 口碑訓練儀
# ==========================================
tab1, tab2, tab3, tab4, tab5, tab6 , tab7, tab8= st.tabs([
    "🔍 產品網路健檢", 
    "🗣️ 全產業口碑製造機", 
    "🔗 競品與服務比較", 
    "🚨 負評拆彈與攻防",
    "📝 SEO 關鍵字標題訓練",
    "🔥 Threads 爆文潤飾",
    "📢 熱度流量請益文",
    "💬 口碑推文擴散生成"
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
            with st.spinner("🚨 危機處理專家已連線，正在擬定防守與掩埋對策..."):
                try:
                    prompt = (
                        f"你是一位擁有 15 年經驗的資深危機處理公關以及有資深的網路口碑操作經驗。客戶目前遭遇了以下網友的具體負評：\n"
                        f"「{raw_reviews}」\n"
                        "請提供一份完整的「負評拆彈與 SEO 掩埋作戰計畫」，必須包含以下 8 大模塊：\n\n"
                        "1. 🚨 危機等級與擴散風險評估\n"
                        "2. 🌋 核心網友情緒與真實痛點解析\n"
                        "3. 🛡️ 負評處理及風向平衡 (提供 5 個不同人設的口碑種子留言切角，溫和稀釋負面氛圍)\n"
                        "4. ⚔️ 口碑主動攻防與風向引導 (包含風向轉移、反向質疑原 PO 動機等戰術)\n"
                        "5. ⚖️ 平台機制與長尾防護 (檢舉下架的可行性評估)\n"
                        "6. ⏳ 黃金應對行動時間表 (2小時與24小時內的具體動作)\n"
                        "7. 🩹 官方回覆與私訊溝通範本 (提供公開留言與私訊安撫的文字範例)\n"
                        "8. 🌊 SEO 掩埋與洗版戰略 (進攻型防護)：\n"
                        "   - 為了防止這篇負評在 Google 搜尋結果頁 (SERP) 長尾發酵，請企劃 3 個『帶有相同關鍵字、但切角完全不同』的正面或中立論壇發文主題。\n"
                        "   - 目的是透過發布這些全新且高互動的文章，利用演算法將這篇負評擠出搜尋引擎第一頁。\n"
                        "   - 請提供這 3 篇文章的「吸睛標題」與「內文切角設定」。"
                    )
                    response = model.generate_content(prompt)
                    st.success("✨ 危機拆彈與掩埋對策擬定完畢！")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"發生錯誤：{e}")
        else:
            st.warning("⚠️ 拆彈模式需要您先貼上原始負評喔！")
            
# ------------------------------------------
# 🚪 第五分頁：SEO 素人標題製造機 (🌟 演算法霸榜優化版)
# ------------------------------------------
with tab5:
    st.info("💡 **高階 SEO 模式**：導入 E-E-A-T 真實經驗原則與 LSI 語意關聯。產出的標題將兼具「鄉民高點擊率」與「Google 爬蟲高權重」。")
    
    st.markdown("#### 🔑 1. 設定 SEO 關鍵字矩陣 (Keyword Matrix)")
    col_k1, col_k2, col_k3 = st.columns(3)
    with col_k1:
        seo_core_kw = st.text_input("🎯 核心關鍵字：", placeholder="例：法令紋玻尿酸", help="您最希望排上 Google 第一頁的主詞彙。")
    with col_k2:
        seo_long_kw = st.text_input("🔎 長尾關鍵字：", placeholder="例：費用, 後遺症, 評價", help="網友搜尋時常搭配核心關鍵字的痛點字詞。")
    with col_k3:
        seo_lsi_kw = st.text_input("🕸️ LSI 關聯詞 (選填)：", placeholder="例：cc數, 凹陷, 補骨", help="與主題高度相關的專業詞彙，能大幅提升 Google 語意權重。")

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
            ["精打細算：想找便宜/比價/看費用", 
             "極度避險：怕踩雷/看失敗心得/問缺點", 
             "觀望求證：看真實效果/開箱/對比圖",
             "新手求知：尋求專業知識/原理/懶人包"]
        )

    st.divider()

    if st.button("🚀 演算 Google 演算法霸榜標題", type="primary", key="btn5"):
        if seo_core_kw:
            with st.spinner("🤖 正在對接 Google 搜尋意圖與 E-E-A-T 原則..."):
                try:
                    prompt = (
                        f"你是一位精通 Google 搜尋演算法 (特別是 E-E-A-T 原則與 2024 核心更新) 以及台灣論壇生態的頂級 SEO 專家。\n"
                        f"操作目標：產出極度自然、完全沒有業配感，但又能完美吻合 Google 搜尋爬蟲語意邏輯的「素人論壇標題」。\n\n"
                        f"【SEO 關鍵字矩陣】\n"
                        f"📍 核心關鍵字：{seo_core_kw}\n"
                        f"📍 核心長尾字：{seo_long_kw if seo_long_kw else '無特定'}\n"
                        f"📍 LSI 語意關聯詞：{seo_lsi_kw if seo_lsi_kw else '無特定'}\n\n"
                        f"【文章架構設定】\n"
                        f"📍 文章類型：{post_type}\n"
                        f"📍 搜尋意圖 (Search Intent)：{seo_intent}\n\n"
                        "【🏆 Google 演算法高權重標題公式 (嚴格遵守)】\n"
                        "1. 雙層次結構：標題必須包含「情緒/情境引導 (給人看)」與「精準關鍵字 (給 Google 看)」。\n"
                        "2. 長度控制：控制在 25-32 個繁體中文字，確保在 Google 搜尋結果頁 (SERP) 不會被截斷。\n"
                        "3. 展現真實經驗 (E-E-A-T 中的 Experience)：Google 極度偏好『第一手經驗』。請在標題中自然流露出『親身經歷』或『真實困擾』的語氣。\n"
                        "4. 絕對去農場化：禁用「2026最新」、「必看」、「大公開」。使用論壇真實語氣（可適度包含空格、逗號或問號）。\n\n"
                        "【請產出以下內容】\n"
                        "請給我 5 個符合上述高階 SEO 邏輯的完美標題選項。\n"
                        "格式請完全依照以下呈現：\n\n"
                        "🔹 標題 1：[產出的素人自然標題]\n"
                        "   ├ 💡 點擊心理學：[簡述這個標題為何能吸引鄉民點擊]\n"
                        "   └ 📈 Google 演算法視角：[解析這個標題抓住了哪些 LSI 語意，以及為何能滿足設定的搜尋意圖]\n\n"
                        "(以此類推，產出 5 個選項)"
                    )
                    response = model.generate_content(prompt)
                    st.success("✨ 演算完成！請參考以下 E-E-A-T 高權重標題佈局：")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"發生錯誤：{e}")
        else:
            st.warning("⚠️ SEO 操作最基本的就是「核心關鍵字」，請務必填寫喔！")

# ------------------------------------------
# 🧵 第六分頁：Threads 爆文轉譯機 (🔥 演算法共鳴優化版)
# ------------------------------------------
with tab6:
    st.info("🔥 **Threads 爆文製造機**：將平淡無奇的公關草稿，轉化為自帶流量的「脆」風格高互動串文。")
    
    st.markdown("#### 📝 1. 貼上您的原始草稿")
    draft_text = st.text_area(
        "請貼上您原本想發的文字（不管多生硬、多像業配都沒關係）：", 
        height=150, 
        placeholder="例如：最近因為工作壓力大，作息不正常，發現臉頰有點凹陷，想詢問大家有沒有推薦的醫美診所？或是推薦打哪一種玻尿酸呢？希望價格不要太貴。"
    )

    st.markdown("#### 🎭 2. 選擇「脆」風格人設")
    threads_persona = st.selectbox(
        "選擇發文者的靈魂設定：",
        [
            "😩 厭世社畜發牢騷 (適合痛點共鳴、抱怨起手式)", 
            "👯‍♀️ 知心閨蜜真心話 (適合推坑、避雷、熱情分享)", 
            "🔥 人間清醒大實話 (適合打破迷思、逆風發言、反直覺)",
            "🥺 假求救真討論 (適合拋出選擇題、引誘網友當老師)"
        ]
    )

    st.divider()

    if st.button("🚀 一鍵轉化為 Threads 爆文", type="primary", key="btn6"):
        if draft_text:
            with st.spinner("🤖 正在注入 Threads 演算法爆款邏輯..."):
                try:
                    prompt = (
                        f"你現在是台灣 Threads (脆) 平台上的超級網紅，非常懂 Threads 的演算法與網友心理學。\n"
                        f"你的任務是將以下【原始草稿】改寫成有極高機率引發大量留言與轉發的「Threads 爆款串文」。\n\n"
                        f"【原始草稿】：\n{draft_text}\n\n"
                        f"【指定人設語氣】：{threads_persona}\n\n"
                        "【🏆 Threads 爆文必備法則 (嚴格遵守)】\n"
                        "1. 停止廢話：第一句話直接切入重點或情緒，字數越少越好，必須具備「滑到就想停下來看」的阻斷力。嚴禁任何打招呼（如：大家好、最近...）。\n"
                        "2. 視覺排版：大量使用換行（Enter），可以用「半形空格」代替逗號，每句話盡量不超過 15 個中文字，創造人類打字時「邊想邊打、碎碎念」的真實感，但閱讀要保持順暢。\n"
                        "3. 極致口語與去 AI 化：嚴禁使用「不藏私分享、強烈推薦、CP值超高」等行銷詞彙。\n"
                        "4. 絕對擬真：禁用「大家覺得呢？」這種老派 IG 結尾。要使用非常口語的時下台灣網路用語。\n"
                        "5. 留破綻/挖坑：結尾必須拋出一個「具體但兩難的選擇」或「極具爭議的提問」，誘發網友的『好為人師』心理，讓他們忍不住留言回覆。\n\n"
                        "【請產出以下內容】\n"
                        "請給我 5 個不同切入點的 Threads 串文版本：\n\n"
                        "🔹 版本 A：[直接給出改寫後的串文內容]\n"
                        "   └ 💡 爆款解析：[說明為什麼這樣寫能騙到 Threads 的演算法與網友的留言]\n\n"
                        "🔹 版本 B：[直接給出改寫後的串文內容]\n"
                        "   └ 💡 爆款解析：[說明為什麼這樣寫能騙到 Threads 的演算法與網友的留言]\n\n"
                        "🔹 版本 C：[直接給出改寫後的串文內容]\n"
                        "   └ 💡 爆款解析：[說明為什麼這樣寫能騙到 Threads 的演算法與網友的留言]\n"
                    )
                    response = model.generate_content(prompt)
                    st.success("✨ 轉化完成！請選擇最順眼的一篇去發文吧：")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"發生錯誤：{e}")
        else:
            st.warning("⚠️ 巧婦難為無米之炊，請先輸入草稿再點擊按鈕喔！")

# ------------------------------------------
# 🚪 第七分頁：熱點流量請益文 (🔥 蹭熱點無痕種草)
# ------------------------------------------
with tab7:
    st.info("🔥 **熱點流量請益文**：輸入時下流行話題與客戶產品，AI 將自動生成「神邏輯牽拖」的超自然請益文，輕鬆收割時事流量！")
    
    col_h1, col_h2 = st.columns(2)
    with col_h1:
        trending_topic = st.text_input(
            "🔥 時下熱門話題 / 時事梗：", 
            placeholder="例如：巴黎奧運、某爆紅韓劇/台劇、地震頻傳、某個網路迷因..."
        )
    with col_h2:
        client_product = st.text_input(
            "💼 客戶類型 / 服務內容：", 
            placeholder="例如：游離型葉黃素、音波拉提、室內設計、防曬乳..."
        )

    platform_vibe = st.selectbox(
        "🗣️ 發文平台語氣設定：",
        [
            "Threads 脆友 (字少、情緒化、直接拋問題)",
            "Dcard 閒聊板/女孩板 (生活化、愛用心境描述、求推薦)", 
            "PTT 八卦板/WomenTalk (直白、微酸、尋求實用建議)"
        ]
    )

    st.divider()

    if st.button("🚀 生成熱點蹭流量請益文", type="primary", key="btn7"):
        if trending_topic and client_product:
            with st.spinner(f"🤖 正在尋找「{trending_topic}」與「{client_product}」的完美神邏輯橋樑..."):
                try:
                    prompt = (
                        f"你現在是台灣最頂尖的口碑行銷操盤手，擅長『新聞挾持 (Newsjacking)』與『無痕種草』。\n"
                        f"你的任務是將【時下熱門話題】與【客戶的產品/服務】完美結合，寫出一篇極度自然的論壇「請益文/求救文」。\n\n"
                        f"【輸入資訊】\n"
                        f"📍 熱門話題/時事：{trending_topic}\n"
                        f"📍 客戶產品/服務：{client_product}\n"
                        f"📍 平台語氣：{platform_vibe}\n\n"
                        "【🏆 熱點請益文必備法則 (嚴格遵守)】\n"
                        "1. 神邏輯牽拖 (Bridge)：這是最重要的一點！這兩者之間的連結必須『極度生活化且合理』。不能硬業配。例如：因為看奧運轉播熬夜導致氣色差（帶出醫美/保養）、因為近期地震覺得家裡老屋不安全（帶出室內設計/買房）。\n"
                        "2. 隱藏商業意圖：發文者必須是一個『單純被熱點影響，而產生真實煩惱的素人』。絕對不可以在主文中說出特定品牌名稱，只能提及『品類』或『療程名稱』，目的是要在留言區讓暗樁推薦。\n"
                        "3. 絕對契合平台文化：嚴格遵守設定的【平台語氣】。排版、用語、標點符號都要像該平台的重度使用者。\n"
                        "4. 標題必須自帶流量密碼：標題必須同時包含「熱門話題關鍵字」以及「痛點/求救字眼」，吸引該話題的受眾點進來。\n\n"
                        "【請產出 3 個不同牽拖角度的劇本，格式如下】\n\n"
                        "🔹 切入點 A：[一句話總結這個神邏輯牽拖的設定]\n"
                        "   🏷️ 爆款標題：[結合話題與痛點的標題]\n"
                        "   📱 主貼文：[完全符合平台語氣的請益文草稿，純文字]\n"
                        "   └ 💡 操盤戰術解析：[說明為什麼這個『牽拖邏輯』很合理，且能成功騙到熱門話題的自然流量]\n\n"
                        "🔹 切入點 B：[一句話總結這個神邏輯牽拖的設定]\n"
                        "   🏷️ 爆款標題：[結合話題與痛點的標題]\n"
                        "   📱 主貼文：[完全符合平台語氣的請益文草稿，純文字]\n"
                        "   └ 💡 操盤戰術解析：[說明為什麼這個『牽拖邏輯』很合理，且能成功騙到熱門話題的自然流量]\n\n"
                        "🔹 切入點 C：[一句話總結這個神邏輯牽拖的設定]\n"
                        "   🏷️ 爆款標題：[結合話題與痛點的標題]\n"
                        "   📱 主貼文：[完全符合平台語氣的請益文草稿，純文字]\n"
                        "   └ 💡 操盤戰術解析：[說明為什麼這個『牽拖邏輯』很合理，且能成功騙到熱門話題的自然流量]\n"
                    )
                    response = model.generate_content(prompt)
                    st.success("✨ 流量密碼生成完畢！請挑選最不違和的切入點去發文：")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"發生錯誤：{e}")
        else:
            st.warning("⚠️ 必須同時填寫「熱門話題」與「客戶類型」，AI 才能幫您找出完美的牽拖邏輯喔！")

# ------------------------------------------
# 🚪 第八分頁：水軍多重宇宙矩陣 (🪖 批次留言生成器)
# ------------------------------------------
with tab8:
    st.info("🪖 **水軍多重宇宙矩陣**：輸入主文與帶風向目標，AI 將自動生成 20 則不同人設的留言，並支援一鍵匯出 Excel，方便執行團隊照表操課。")
    
    st.markdown("#### 📝 1. 設定戰場與主貼文")
    col_w1, col_w2 = st.columns(2)
    with col_w1:
        target_platform = st.selectbox(
            "📍 目標論壇平台：",
            ["Threads (脆友，句子短/愛用破折號)","Dcard (大學生/新鮮人，愛用心境描述)", "PTT (鄉民老手，講話直接/微酸)"]
        )
    with col_w2:
        wom_goal = st.text_input(
            "🎯 這串留言的最終帶風向目標是？", 
            placeholder="例如：引導大家覺得『某產品雖然貴但很值得』，或是『把這家診所的醫生捧成神』"
        )
        
    main_post_content = st.text_area(
        "📄 請貼上準備發布的「主貼文內容」或「討論主題」：",
        height=150,
        placeholder="把前面分頁寫好的主文草稿貼過來，AI 才知道底下要怎麼回覆..."
    )

    st.divider()

    if st.button("🚀 召喚水軍矩陣 (產出 20 則留言)", type="primary", key="btn8"):
            if main_post_content and wom_goal:
                with st.spinner("🤖 正在切換 20 種不同的人格分裂，生成矩陣中..."):
                    try:
                        prompt = (
                            f"你是一位擁有15年豐富論壇操作經驗的口碑行銷資深專員。現在請根據以下【主貼文】，產出 20 則極度逼真的網友留言，並巧妙地達成【帶風向目標】。\n\n"
                            f"📍 目標平台：{target_platform}\n"
                            f"📍 帶風向目標：{wom_goal}\n"
                            f"📍 主貼文內容：{main_post_content}\n\n"
                            "【🏆 水軍矩陣比例與人設規則】\n"
                            "你需要模擬出一個真實討論串的生態，這 20 則留言必須包含以下比例的人設，不能全部都在稱讚（那樣太假）：\n"
                            "1. 伸手牌發問 (約 25%)：單純發問費用、地點、痛不痛、去哪買。\n"
                            "2. 中立觀望與純推 (約 30%)：路過推個、卡一個等心得、感覺不錯但還在猶豫。\n"
                            "3. 微酸質疑或抱怨競品 (約 15%)：提出合理的擔憂（如：這看起來很痛欸、可是另一家比較便宜），讓後面的暗樁有機會反駁。\n"
                            "4. 深度護航與推坑 (約 30%)：詳細分享真實經驗，用親身經歷來達成我們的【帶風向目標】。用語必須去業配感。\n\n"
                            "【⚠️ 輸出格式限制 (極度重要)】\n"
                            "請嚴格使用 JSON Array 格式輸出。絕對不要包含任何 Markdown 標記 (如 ```json)、不要表格、不要任何解釋與廢話。\n"
                            "請直接給出像這樣的純 JSON 陣列格式：\n"
                            "[\n"
                            "  {\"樓層\": \"1樓\", \"人設屬性\": \"伸手牌發問\", \"留言內容\": \"請問原PO這家在哪裡？費用大概多少？\", \"戰術目的\": \"製造詢問熱度\"},\n"
                            "  {\"樓層\": \"2樓\", \"人設屬性\": \"微酸質疑\", \"留言內容\": \"這價格我寧願去打鳳凰電波吧...\", \"戰術目的\": \"故意拋出質疑做球給後續護航\"}\n"
                            "]"
                        )
                        
                        response = model.generate_content(prompt)
                        
                        # 🧹 黑魔法：精準擷取 JSON 字串，過濾掉 AI 的廢話
                        raw_text = response.text
                        start_idx = raw_text.find('[')
                        end_idx = raw_text.rfind(']') + 1
                        
                        if start_idx != -1 and end_idx != -1:
                            clean_json_str = raw_text[start_idx:end_idx]
                            
                            try:
                                # 嘗試將 JSON 轉換為 DataFrame
                                data = json.loads(clean_json_str)
                                df = pd.DataFrame(data)
                                
                                st.success("✨ 水軍矩陣集結完畢！您可以直接複製，或下載成 Excel 檔交給執行團隊。")
                                
                                # 在網頁上展示精美的表格
                                st.dataframe(df, use_container_width=True, hide_index=True)
                                
                                # 製作下載按鈕 (使用 utf-8-sig 確保 Excel 打開中文不會亂碼)
                                csv = df.to_csv(index=False).encode('utf-8-sig')
                                st.download_button(
                                    label="📥 下載水軍劇本 (Excel CSV 格式)",
                                    data=csv,
                                    file_name='wom_matrix_script.csv',
                                    mime='text/csv',
                                )
                            except json.JSONDecodeError:
                                st.error("⚠️ 資料解析失敗：AI 產出的 JSON 格式有語法錯誤。")
                                st.text(clean_json_str) # 吐出錯誤的字串讓您檢查
                        else:
                            st.error("⚠️ 資料解析失敗：AI 未輸出預期的陣列格式。")
                            st.text(raw_text)
                            
                    except Exception as e:
                        st.error(f"發生錯誤：{e}")
