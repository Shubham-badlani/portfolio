


# # app.py
# import streamlit as st
# from pathlib import Path
# import base64
# import datetime

# # ---------------- CONFIG ----------------
# PAGE_TITLE = "Shubham Badlani — Portfolio"
# PAGE_ICON = "🛠️"
# RESUME_FILENAME = "Shubham_Resume25_11_2025.pdf"

# RESUME_RUNTIME_PATH = Path("/mnt/data") / RESUME_FILENAME
# RESUME_ASSETS_PATH = Path("assets") / RESUME_FILENAME
# RESUME_PATH = RESUME_RUNTIME_PATH if RESUME_RUNTIME_PATH.exists() else RESUME_ASSETS_PATH

# # <-- use the uploaded image path you provided -->
# PROFILE_RUNTIME = Path("/mnt/data/WhatsApp Image 2024-07-06 at 16.17.23_3d1d87db.jpg")
# PROFILE_ASSETS = Path("assets") / "profile.jpg"
# PROFILE_PATH = PROFILE_RUNTIME if PROFILE_RUNTIME.exists() else (PROFILE_ASSETS if PROFILE_ASSETS.exists() else None)

# VIDEO_RUNTIME = Path("/mnt/data") / "intro.mp4"
# VIDEO_ASSETS = Path("assets") / "intro.mp4"
# VIDEO_PATH = VIDEO_RUNTIME if VIDEO_RUNTIME.exists() else (VIDEO_ASSETS if VIDEO_ASSETS.exists() else None)

# GITHUB_URL = "https://github.com/Shubham-badlani"
# LINKEDIN_URL = "https://www.linkedin.com/in/shubham-badlani-576511351/"
# EMAIL = "shubhambadlani05@gmail.com"
# PHONE = "+91 9351359006"
# LOCATION = "Pune, Maharashtra, India"

# st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")
# st.markdown(navbar_html, unsafe_allow_html=True)
# st.markdown("<div class='nav-spacer'></div>", unsafe_allow_html=True)


# # ---------------- session state defaults ----------------
# if "theme" not in st.session_state:
#     st.session_state["theme"] = "dark"
# if "lang" not in st.session_state:
#     st.session_state["lang"] = "EN"

# # ---------------- content (EN / JP polite) ----------------
# TEXT = {
#     "EN": {
#         "about_title": "About me",
#         "about": "Enthusiastic electronics engineer specializing in VLSI, FPGA, embedded systems, and AI-driven hardware solutions. Passionate about building intelligent systems by combining hardware design with ML models. Strong foundation in HDL, embedded C, CMOS circuits, and modern software tools.",
#         "skills_title": "Top Skills",
#         "education_title": "Education",
#         "education_items": [
#             ("B.E. in Electronics Engineering – VLSI Design & Technology", "KJ College of Engineering and Management Research (SPPU), Pune (2023–2027)"),
#             ("Senior Secondary (PCM)", "Central Academy, CBSE, Jodhpur — 80% (May 2023)"),
#             ("Secondary", "Central Academy, CBSE, Jodhpur — 90% (May 2021)")
#         ],
#         "experience_title": "Experience",
#         "experience_items": [
#             ("Research & Development AI Engineer Intern", "Sciemetric Technologies (TASI India) — June–Aug 2025"),
#             ("Angular Intern", "Infosys SpringBoard — Nov 2024 – Jan 2025")
#         ],
#         "projects_title": "Projects",
#         "projects_items": [
#             ("Climate Prediction (Kaggle)", "ML models predicting rainfall & temperature trends (1901–2020 dataset).", "https://www.kaggle.com/code/shubhambadlani/predicting-climate"),
#             ("CTS Leak Test - Phase Deviation Detector", "Industrial IoT leak-detection pipeline with anomaly detection & Streamlit dashboard.", ""),
#             ("Student Result Processing App", "Python + MySQL based student result processing application (2025).", ""),
#             ("AI ChatBot for Farmers", "Integrated AI & weather API with localization and text-to-speech (2024).", ""),
#             ("FPGA & HDL Mini Projects", "Verilog-based counters, FSMs, ALU using FPGA flow.", ""),
#             ("VLSI CMOS Circuits (Microwind)", "Designed basic CMOS logic using Microwind.", "")
#         ],
#         "languages_title": "Languages",
#         "contact_title": "Contact",
#         "download_resume": "Download Resume (PDF)",
#         "no_resume": "Resume not found. Place your PDF at one of these paths: " + str(RESUME_RUNTIME_PATH) + " or " + str(RESUME_ASSETS_PATH),
#         "profile_alt": "Profile image"
#     },
#     "JP": {
#         "about_title": "自己紹介",
#         "about": "私はVLSI、FPGA、組み込みシステム、およびAI駆動のハードウェアソリューションを専門とするエレクトロニクスエンジニアです。ハードウェア設計と機械学習モデルを組み合わせてインテリジェントなシステムを構築することに情熱を持っています。HDL、組み込みC、CMOS回路、および最新のソフトウェアツールに関する堅固な基盤があります。",
#         "skills_title": "主なスキル",
#         "education_title": "学歴",
#         "education_items": [
#             ("学士（電子工学） – VLSI設計・技術", "KJ College of Engineering and Management Research (SPPU), Pune（2023–2027）"),
#             ("高等学校（理系）", "Central Academy, CBSE, Jodhpur — 80%（2023年5月）"),
#             ("中学校卒業", "Central Academy, CBSE, Jodhpur — 90%（2021年5月）")
#         ],
#         "experience_title": "職務経験",
#         "experience_items": [
#             ("研究開発 AI エンジニア インターン", "Sciemetric Technologies (TASI India) — 2025年6月–8月"),
#             ("Angular インターン", "Infosys SpringBoard — 2024年11月 – 2025年1月")
#         ],
#         "projects_title": "プロジェクト",
#         "projects_items": [
#             ("気候予測（Kaggle）", "降雨および気温の傾向を予測する機械学習モデル（1901–2020 データセット）。", "https://www.kaggle.com/code/shubhambadlani/predicting-climate"),
#             ("CTS リークテスト - フェーズ偏差検出器", "異常検知とStreamlitダッシュボードを備えた産業用IoTリーク検出パイプライン。", ""),
#             ("学生成績処理アプリ", "Python + MySQL による学生成績処理アプリケーション（2025）。", ""),
#             ("農家向けAIチャットボット", "天気APIと音声合成を統合した多言語チャットボット（2024）。", ""),
#             ("FPGA / HDL ミニプロジェクト", "Verilogによるカウンタ、FSM、ALU をFPGAフローで実装。", ""),
#             ("VLSI CMOS 回路（Microwind）", "Microwindを用いた基本的なCMOS論理の設計。", "")
#         ],
#         "languages_title": "対応言語",
#         "contact_title": "お問い合わせ",
#         "download_resume": "履歴書をダウンロード（PDF）",
#         "no_resume": "履歴書が見つかりません。次のいずれかのパスにPDFを配置してください: " + str(RESUME_RUNTIME_PATH) + " または " + str(RESUME_ASSETS_PATH),
#         "profile_alt": "プロフィール画像"
#     }
# }

# # ---------------- CSS (theme aware) ----------------
# BASE_CSS = r"""
# :root {
#   --bg: #0e0e11;
#   --card: #0f1724;
#   --text: #e6eef8;
#   --muted: #9aa6c0;
#   --accent: #6366f1;
#   --glass: rgba(255,255,255,0.03);
# }
# .light {
#   --bg: #ffffff;
#   --card: #f6f7fb;
#   --text: #0b1220;
#   --muted: #6b7280;
#   --accent: #4f46e5;
#   --glass: rgba(0,0,0,0.02);
# }
# .css-root {
#   background: linear-gradient(180deg, var(--bg) 0%, var(--card) 100%);
#   color: var(--text);
#   transition: all .25s ease;
#   padding-top: 0px;
#   margin:0;
#   font-family: Inter, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
# }
# .header {
#   display:flex;
#   align-items:center;
#   gap:16px;
# }
# .logo {
#   width:64px;
#   height:64px;
#   border-radius:12px;
#   display:flex;
#   align-items:center;
#   justify-content:center;
#   font-weight:700;
#   font-size:22px;
#   background: linear-gradient(135deg, rgba(255,255,255,0.03), rgba(0,0,0,0.03));
#   border:1px solid rgba(255,255,255,0.04);
# }
# .card {
#   background: var(--glass);
#   padding: 16px;
#   border-radius: 12px;
#   border: 1px solid rgba(255,255,255,0.04);
#   box-shadow: 0 8px 22px rgba(2,6,23,0.45);
#   transition: transform .18s ease;
#   margin-bottom: 16px;
# }
# .card:hover { transform: translateY(-4px); }
# .tag {
#   display:inline-block;
#   padding:6px 10px;
#   border-radius:999px;
#   background: rgba(255,255,255,0.03);
#   font-size:13px;
#   margin:4px 4px 4px 0;
#   color: var(--text);
# }
# .small { font-size:13px; color:var(--muted); }
# .center { text-align:center; }
# .link { color:var(--accent); text-decoration:none; }
# .timeline { border-left:2px solid rgba(255,255,255,0.05); padding-left:14px; margin-left:6px; }
# """
# NAV_CSS = """
# <style>
# .navbar {
#     position: fixed;
#     top: 0;
#     left: 0;
#     right: 0;
#     height: 62px;
#     background-color: var(--card);
#     backdrop-filter: blur(6px);
#     display: flex;
#     align-items: center;
#     justify-content: space-between;
#     padding: 0px 26px;
#     border-bottom: 1px solid rgba(255,255,255,0.06);
#     z-index: 9999;
# }
# .nav-left {
#     display:flex;
#     align-items:center;
#     gap:12px;
# }
# .nav-logo {
#     font-size:18px;
#     font-weight:700;
#     color:var(--accent);
# }
# .nav-links a {
#     margin: 0 12px;
#     color: var(--accent);
#     text-decoration: none;
#     font-size:14px;
#     font-weight:500;
# }
# .nav-links a:hover { color:var(--accent); text-shadow: 0 0 10px var(--accent); }
# .nav-actions {
#     display:flex;
#     gap:10px;
#     align-items:center;
# }
# .lang-select, .theme-btn {
#     padding:6px 10px;
#     border-radius:8px;
#     border: none;
#     background: rgba(255,255,255,0.03);
#     color:var(--text);
#     font-weight:500;
# }
# .nav-spacer { height: 72px; } /* push page content below navbar */
# </style>
# """
# THEME_ICON_CSS = """
# <style>
# .theme-icon {
#     font-size: 20px;
#     cursor: pointer;
#     padding: 6px 8px;
#     border-radius: 6px;
#     background: rgba(255,255,255,0.05);
#     transition: all 0.25s ease;
# }

# .theme-icon:hover {
#     background: rgba(255,255,255,0.15);
#     transform: scale(1.08);
# }
# </style>
# """


# # ---------------- APPLY CSS + ROOT WRAPPER ----------------
# root_class = "css-root" + ("" if st.session_state["theme"] == "dark" else " light")
# st.markdown(f"<style>{BASE_CSS}</style>", unsafe_allow_html=True)
# st.markdown(THEME_ICON_CSS, unsafe_allow_html=True)
# st.markdown(f"<style>{NAV_CSS}</style>", unsafe_allow_html=True)
# st.markdown(f"<div class='{root_class}' style='padding-top:0px;'>", unsafe_allow_html=True)

# # ---------------- NAVBAR (FIXED + VISIBLE) ----------------
# navbar_html = f"""
# <div class="navbar" style="z-index: 99999 !important;">
#   <div class="nav-left">
#     <div class="nav-logo">SB</div>
#     <div class="nav-links">
#       <a href="#about">{'About' if st.session_state['lang']=='EN' else '自己紹介'}</a>
#       <a href="#skills">{'Skills' if st.session_state['lang']=='EN' else 'スキル'}</a>
#       <a href="#education">{'Education' if st.session_state['lang']=='EN' else '学歴'}</a>
#       <a href="#experience">{'Experience' if st.session_state['lang']=='EN' else '職務経験'}</a>
#       <a href="#projects">{'Projects' if st.session_state['lang']=='EN' else 'プロジェクト'}</a>
#       <a href="#contact">{'Contact' if st.session_state['lang']=='EN' else 'お問い合わせ'}</a>
#     </div>
#   </div>
#   <div class="nav-actions">
#     <!-- Streamlit widgets go below (separate container) -->
#   </div>
# </div>
# <div class="nav-spacer"></div>
# """

# st.markdown(navbar_html, unsafe_allow_html=True)

# # ---------------- Header area with widgets ----------------
# header_cols = st.columns([1.1, 2, 1.2])
# with header_cols[0]:
#     if PROFILE_PATH:
#         # show rounded profile image — width 140 (will display nicely)
#         st.image(str(PROFILE_PATH), width=140, caption=TEXT[st.session_state["lang"]]["profile_alt"])
#     else:
#         st.markdown("<div class='logo card'><div style='font-size:28px; font-weight:700; padding-top:10px;'>SB</div></div>", unsafe_allow_html=True)

# with header_cols[1]:
#     st.markdown(f"<h1 style='margin:0'>Shubham Badlani</h1>", unsafe_allow_html=True)
#     st.markdown(f"<div class='small'>Electronics Engineer (VLSI Design & Technology) • Embedded Systems • FPGA • AI & ML</div>", unsafe_allow_html=True)

# with header_cols[2]:
#     # Language selector
#     lang_choice = st.selectbox("", options=["EN", "JP"], index=0 if st.session_state["lang"]=="EN" else 1, key="lang_select")
#     if lang_choice != st.session_state["lang"]:
#         st.session_state["lang"] = lang_choice
#         st.rerun()

#         # Minimal Theme Icon Switch (🌙 → ☀️)
#         icon = "☀️" if st.session_state["theme"] == "light" else "🌙"

#         theme_icon_html = f"""
#         <span class="theme-icon" onclick="document.getElementById('theme_toggle_btn').click()">{icon}</span>
#         """

#         st.markdown(theme_icon_html, unsafe_allow_html=True)

#         # Hidden button to trigger rerun
#         if st.button("", key="theme_toggle_btn"):
#             st.session_state["theme"] = "light" if st.session_state["theme"] == "dark" else "dark"
#             st.rerun()


#     # Resume download
#     if RESUME_PATH.exists():
#         with open(RESUME_PATH, "rb") as f:
#             pdf_bytes = f.read()
#         st.download_button(TEXT[st.session_state["lang"]]["download_resume"], data=pdf_bytes, file_name=RESUME_FILENAME)
#     else:
#         st.info(TEXT[st.session_state["lang"]]["no_resume"])

# st.write("---")

# # ---------------- content sections ----------------
# st.markdown("<div id='about'></div>", unsafe_allow_html=True)
# st.subheader(TEXT[st.session_state["lang"]]["about_title"])
# st.markdown("<div class='card'>", unsafe_allow_html=True)
# st.write(TEXT[st.session_state["lang"]]["about"])
# st.markdown("</div>", unsafe_allow_html=True)

# st.markdown("<div id='skills'></div>", unsafe_allow_html=True)
# st.subheader(TEXT[st.session_state["lang"]]["skills_title"])
# st.markdown("<div class='card'>", unsafe_allow_html=True)
# skills = ["Verilog","VHDL","RTL Design","FPGA Flow (Vivado)","CMOS Design","Control Systems","Analog & Digital Circuits","Microwind","Proteus","MATLAB","LTSpice","C","C++","Python","JavaScript","TypeScript","TailwindCSS","Angular","Streamlit","Flask"]
# st.markdown("".join([f"<span class='tag'>{s}</span>" for s in skills]), unsafe_allow_html=True)
# st.markdown("</div>", unsafe_allow_html=True)

# st.markdown("<div id='education'></div>", unsafe_allow_html=True)
# st.subheader(TEXT[st.session_state["lang"]]["education_title"])
# st.markdown("<div class='card'>", unsafe_allow_html=True)
# for title, desc in TEXT[st.session_state["lang"]]["education_items"]:
#     st.markdown(f"**{title}**  \n{desc}  \n")
# st.markdown("</div>", unsafe_allow_html=True)

# st.markdown("<div id='experience'></div>", unsafe_allow_html=True)
# st.subheader(TEXT[st.session_state["lang"]]["experience_title"])
# st.markdown("<div class='card'>", unsafe_allow_html=True)
# for role, info in TEXT[st.session_state["lang"]]["experience_items"]:
#     st.markdown(f"**{role}**  \n<span class='small'>{info}</span>  \n")
# st.markdown("</div>", unsafe_allow_html=True)

# st.markdown("<div id='projects'></div>", unsafe_allow_html=True)
# st.subheader(TEXT[st.session_state["lang"]]["projects_title"])
# st.markdown("<div class='card'>", unsafe_allow_html=True)
# for title, desc, link in TEXT[st.session_state["lang"]]["projects_items"]:
#     st.markdown(f"### {title}")
#     st.write(desc)
#     if link:
#         st.markdown(f"[Explore →]({link})")
#     st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)
# st.markdown("</div>", unsafe_allow_html=True)

# st.subheader(TEXT[st.session_state["lang"]]["languages_title"])
# st.markdown("<div class='card'>", unsafe_allow_html=True)
# if st.session_state["lang"] == "EN":
#     st.markdown("<span class='tag'>English</span> <span class='tag'>日本語 (Japanese)</span>", unsafe_allow_html=True)
# else:
#     st.markdown("<span class='tag'>English</span> <span class='tag'>日本語（日本語）</span>", unsafe_allow_html=True)
# st.markdown("</div>", unsafe_allow_html=True)

# st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
# st.subheader(TEXT[st.session_state["lang"]]["contact_title"])
# st.markdown("<div class='card'>", unsafe_allow_html=True)
# st.markdown(f"**Email:** <a class='link' href='mailto:{EMAIL}'>{EMAIL}</a><br>**Phone:** {PHONE}<br>**LinkedIn:** <a class='link' href='{LINKEDIN_URL}' target='_blank'>{LINKEDIN_URL}</a><br>**GitHub:** <a class='link' href='{GITHUB_URL}' target='_blank'>{GITHUB_URL}</a>", unsafe_allow_html=True)
# st.markdown("</div>", unsafe_allow_html=True)

# st.write("---")
# year = datetime.date.today().year
# st.markdown(f"<div class='small center'>© {year} Shubham Badlani • Built with Streamlit</div>", unsafe_allow_html=True)

# st.markdown("</div>", unsafe_allow_html=True)

# # app.py (fixed full file)
# import streamlit as st
# from pathlib import Path
# import base64
# import datetime

# # ---------------- CONFIG ----------------
# PAGE_TITLE = "Shubham Badlani — Portfolio"
# PAGE_ICON = "🛠️"
# RESUME_FILENAME = "Shubham_Resume25_11_2025.pdf"

# RESUME_RUNTIME_PATH = Path("/mnt/data") / RESUME_FILENAME
# RESUME_ASSETS_PATH = Path("assets") / RESUME_FILENAME
# RESUME_PATH = RESUME_RUNTIME_PATH if RESUME_RUNTIME_PATH.exists() else RESUME_ASSETS_PATH

# # uploaded profile image
# PROFILE_RUNTIME = Path("/mnt/data/WhatsApp Image 2024-07-06 at 16.17.23_3d1d87db.jpg")
# PROFILE_ASSETS = Path("assets") / "profile.jpg"
# PROFILE_PATH = PROFILE_RUNTIME if PROFILE_RUNTIME.exists() else (PROFILE_ASSETS if PROFILE_ASSETS.exists() else None)

# VIDEO_RUNTIME = Path("/mnt/data") / "intro.mp4"
# VIDEO_ASSETS = Path("assets") / "intro.mp4"
# VIDEO_PATH = VIDEO_RUNTIME if VIDEO_RUNTIME.exists() else (VIDEO_ASSETS if VIDEO_ASSETS.exists() else None)

# GITHUB_URL = "https://github.com/Shubham-badlani"
# LINKEDIN_URL = "https://www.linkedin.com/in/shubham-badlani-576511351/"
# EMAIL = "shubhambadlani05@gmail.com"
# PHONE = "+91 9351359006"
# LOCATION = "Pune, Maharashtra, India"

# st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")
# st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

# # Inject all CSS here (correct order)
# st.markdown(f"<style>{BASE_CSS}</style>", unsafe_allow_html=True)
# st.markdown(NAV_CSS, unsafe_allow_html=True)
# st.markdown(THEME_ICON_CSS, unsafe_allow_html=True)


# # ---------------- session state defaults ----------------
# if "theme" not in st.session_state:
#     st.session_state["theme"] = "dark"
# if "lang" not in st.session_state:
#     st.session_state["lang"] = "EN"

# # ---------------- content (EN / JP polite) ----------------
# TEXT = {
#     "EN": {
#         "about_title": "About me",
#         "about": "Enthusiastic electronics engineer specializing in VLSI, FPGA, embedded systems, and AI-driven hardware solutions. Passionate about building intelligent systems by combining hardware design with ML models. Strong foundation in HDL, embedded C, CMOS circuits, and modern software tools.",
#         "skills_title": "Top Skills",
#         "education_title": "Education",
#         "education_items": [
#             ("B.E. in Electronics Engineering – VLSI Design & Technology", "KJ College of Engineering and Management Research (SPPU), Pune (2023–2027)"),
#             ("Senior Secondary (PCM)", "Central Academy, CBSE, Jodhpur — 80% (May 2023)"),
#             ("Secondary", "Central Academy, CBSE, Jodhpur — 90% (May 2021)")
#         ],
#         "experience_title": "Experience",
#         "experience_items": [
#             ("Research & Development AI Engineer Intern", "Sciemetric Technologies (TASI India) — June–Aug 2025"),
#             ("Angular Intern", "Infosys SpringBoard — Nov 2024 – Jan 2025")
#         ],
#         "projects_title": "Projects",
#         "projects_items": [
#             ("Climate Prediction (Kaggle)", "ML models predicting rainfall & temperature trends (1901–2020 dataset).", "https://www.kaggle.com/code/shubhambadlani/predicting-climate"),
#             ("CTS Leak Test - Phase Deviation Detector", "Industrial IoT leak-detection pipeline with anomaly detection & Streamlit dashboard.", ""),
#             ("Student Result Processing App", "Python + MySQL based student result processing application (2025).", ""),
#             ("AI ChatBot for Farmers", "Integrated AI & weather API with localization and text-to-speech (2024).", ""),
#             ("FPGA & HDL Mini Projects", "Verilog-based counters, FSMs, ALU using FPGA flow.", ""),
#             ("VLSI CMOS Circuits (Microwind)", "Designed basic CMOS logic using Microwind.", "")
#         ],
#         "languages_title": "Languages",
#         "contact_title": "Contact",
#         "download_resume": "Download Resume (PDF)",
#         "no_resume": "Resume not found. Place your PDF at one of these paths: " + str(RESUME_RUNTIME_PATH) + " or " + str(RESUME_ASSETS_PATH),
#         "profile_alt": "Profile image"
#     },
#     "JP": {
#         "about_title": "自己紹介",
#         "about": "私はVLSI、FPGA、組み込みシステム、およびAI駆動のハードウェアソリューションを専門とするエレクトロニクスエンジニアです。ハードウェア設計と機械学習モデルを組み合わせてインテリジェントなシステムを構築することに情熱を持っています。HDL、組み込みC、CMOS回路、および最新のソフトウェアツールに関する堅固な基盤があります。",
#         "skills_title": "主なスキル",
#         "education_title": "学歴",
#         "education_items": [
#             ("学士（電子工学） – VLSI設計・技術", "KJ College of Engineering and Management Research (SPPU), Pune（2023–2027）"),
#             ("高等学校（理系）", "Central Academy, CBSE, Jodhpur — 80%（2023年5月）"),
#             ("中学校卒業", "Central Academy, CBSE, Jodhpur — 90%（2021年5月）")
#         ],
#         "experience_title": "職務経験",
#         "experience_items": [
#             ("研究開発 AI エンジニア インターン", "Sciemetric Technologies (TASI India) — 2025年6月–8月"),
#             ("Angular インターン", "Infosys SpringBoard — 2024年11月 – 2025年1月")
#         ],
#         "projects_title": "プロジェクト",
#         "projects_items": [
#             ("気候予測（Kaggle）", "降雨および気温の傾向を予測する機械学習モデル（1901–2020 データセット）。", "https://www.kaggle.com/code/shubhambadlani/predicting-climate"),
#             ("CTS リークテスト - フェーズ偏差検出器", "異常検知とStreamlitダッシュボードを備えた産業用IoTリーク検出パイプライン。", ""),
#             ("学生成績処理アプリ", "Python + MySQL による学生成績処理アプリケーション（2025）。", ""),
#             ("農家向けAIチャットボット", "天気APIと音声合成を統合した多言語チャットボット（2024）。", ""),
#             ("FPGA / HDL ミニプロジェクト", "Verilogによるカウンタ、FSM、ALU をFPGAフローで実装。", ""),
#             ("VLSI CMOS 回路（Microwind）", "Microwindを用いた基本的なCMOS論理の設計。", "")
#         ],
#         "languages_title": "対応言語",
#         "contact_title": "お問い合わせ",
#         "download_resume": "履歴書をダウンロード（PDF）",
#         "no_resume": "履歴書が見つかりません。次のいずれかのパスにPDFを配置してください: " + str(RESUME_RUNTIME_PATH) + " または " + str(RESUME_ASSETS_PATH),
#         "profile_alt": "プロフィール画像"
#     }
# }

# # ---------------- CSS (theme aware) ----------------
# BASE_CSS = r"""
# :root {
#   --bg: #0e0e11;
#   --card: #0f1724;
#   --text: #e6eef8;
#   --muted: #9aa6c0;
#   --accent: #6366f1;
#   --glass: rgba(255,255,255,0.03);
# }
# .light {
#   --bg: #ffffff;
#   --card: #f6f7fb;
#   --text: #0b1220;
#   --muted: #6b7280;
#   --accent: #4f46e5;
#   --glass: rgba(0,0,0,0.02);
# }
# .css-root {
#   background: linear-gradient(180deg, var(--bg) 0%, var(--card) 100%);
#   color: var(--text);
#   transition: all .25s ease;
#   padding-top: 0px;
#   margin:0;
#   font-family: Inter, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
# }
# .header {
#   display:flex;
#   align-items:center;
#   gap:16px;
# }
# .logo {
#   width:64px;
#   height:64px;
#   border-radius:12px;
#   display:flex;
#   align-items:center;
#   justify-content:center;
#   font-weight:700;
#   font-size:22px;
#   background: linear-gradient(135deg, rgba(255,255,255,0.03), rgba(0,0,0,0.03));
#   border:1px solid rgba(255,255,255,0.04);
# }
# .card {
#   background: var(--glass);
#   padding: 16px;
#   border-radius: 12px;
#   border: 1px solid rgba(255,255,255,0.04);
#   box-shadow: 0 8px 22px rgba(2,6,23,0.45);
#   transition: transform .18s ease;
#   margin-bottom: 16px;
# }
# .card:hover { transform: translateY(-4px); }
# .tag {
#   display:inline-block;
#   padding:6px 10px;
#   border-radius:999px;
#   background: rgba(255,255,255,0.03);
#   font-size:13px;
#   margin:4px 4px 4px 0;
#   color: var(--text);
# }
# .small { font-size:13px; color:var(--muted); }
# .center { text-align:center; }
# .link { color:var(--accent); text-decoration:none; }
# .timeline { border-left:2px solid rgba(255,255,255,0.05); padding-left:14px; margin-left:6px; }
# """

# NAV_CSS = """
# <style>
# /* remove Streamlit default padding so navbar becomes visible */
# .block-container {
#     padding-top: 90px !important;   /* push whole content down */
# }

# /* NAVBAR container */
# .navbar {
#     position: fixed;
#     top: 0;
#     left: 0;
#     right: 0;
#     height: 70px;
#     background: var(--card);
#     backdrop-filter: blur(8px);
#     border-bottom: 1px solid rgba(255,255,255,0.1);
#     display: flex;
#     align-items: center;
#     justify-content: space-between;
#     padding: 0px 28px;
#     z-index: 99999 !important;
# }

# /* left side */
# .nav-left {
#     display: flex;
#     align-items: center;
#     gap: 14px;
# }

# /* logo */
# .nav-logo {
#     font-size: 20px;
#     font-weight: 700;
#     color: var(--accent);
# }

# /* links */
# .nav-links a {
#     margin: 0 12px;
#     font-size: 15px;
#     color: var(--text);
#     text-decoration: none;
#     font-weight: 500;
# }
# .nav-links a:hover {
#     color: var(--accent);
# }

# /* right side widgets container */
# .nav-actions {
#     display: flex;
#     align-items: center;
#     gap: 12px;
# }
# </style>
# """

# THEME_ICON_CSS = """
# <style>
# .theme-icon {
#     font-size: 20px;
#     cursor: pointer;
#     padding: 6px 8px;
#     border-radius: 6px;
#     background: rgba(255,255,255,0.05);
#     transition: all 0.25s ease;
# }
# .theme-icon:hover {
#     background: rgba(255,255,255,0.15);
#     transform: scale(1.08);
# }
# </style>
# """

# navbar_html = f"""
# <div class="navbar">
#   <div class="nav-left">
#     <div class="nav-logo">SB</div>

#     <div class="nav-links">
#       <a href="#about">{'About' if st.session_state['lang']=='EN' else '自己紹介'}</a>
#       <a href="#skills">{'Skills' if st.session_state['lang']=='EN' else 'スキル'}</a>
#       <a href="#education">{'Education' if st.session_state['lang']=='EN' else '学歴'}</a>
#       <a href="#experience">{'Experience' if st.session_state['lang']=='EN' else '職務経験'}</a>
#       <a href="#projects">{'Projects' if st.session_state['lang']=='EN' else 'プロジェクト'}</a>
#       <a href="#contact">{'Contact' if st.session_state['lang']=='EN' else 'お問い合わせ'}</a>
#     </div>
#   </div>

#   <div class="nav-actions" id="nav-actions"></div>
# </div>
# """

# st.markdown(navbar_html, unsafe_allow_html=True)
# # Right-side nav actions (language, theme, resume)
# nav_col1, nav_col2, nav_col3 = st.columns([1, 1, 1])

# with nav_col1:
#     lang_choice = st.selectbox("", ["EN", "JP"], index=0 if st.session_state["lang"]=="EN" else 1)
#     if lang_choice != st.session_state["lang"]:
#         st.session_state["lang"] = lang_choice
#         st.rerun()

# with nav_col2:
#     icon = "☀️" if st.session_state["theme"] == "light" else "🌙"
#     theme_icon_html = f"""
#     <span class="theme-icon" onclick="document.getElementById('theme_toggle_btn').click()">{icon}</span>
#     """
#     st.markdown(theme_icon_html, unsafe_allow_html=True)

#     if st.button("", key="theme_toggle_btn"):
#         st.session_state["theme"] = "light" if st.session_state["theme"] == "dark" else "dark"
#         st.rerun()

# with nav_col3:
#     if RESUME_PATH.exists():
#         with open(RESUME_PATH, "rb") as f:
#             pdf_bytes = f.read()
#         st.download_button(TEXT[st.session_state["lang"]]["download_resume"], data=pdf_bytes, file_name=RESUME_FILENAME)



# # ---------------- apply CSS and root ----------------
# root_class = "css-root" + ("" if st.session_state["theme"] == "dark" else " light")
# st.markdown(f"<style>{BASE_CSS}</style>", unsafe_allow_html=True)
# st.markdown(NAV_CSS, unsafe_allow_html=True)       # NAV_CSS already contains <style>
# st.markdown(THEME_ICON_CSS, unsafe_allow_html=True)
# st.markdown(f"<div class='{root_class}' style='padding-top:0px;'>", unsafe_allow_html=True)

# # ---------------- NAVBAR HTML (top) ----------------
# navbar_html = f"""
# <div class="navbar" style="z-index:99999;">
#   <div class="nav-left">
#     <div class="nav-logo">SB</div>
#     <div class="nav-links">
#       <a href="#about">{'About' if st.session_state['lang']=='EN' else '自己紹介'}</a>
#       <a href="#skills">{'Skills' if st.session_state['lang']=='EN' else 'スキル'}</a>
#       <a href="#education">{'Education' if st.session_state['lang']=='EN' else '学歴'}</a>
#       <a href="#experience">{'Experience' if st.session_state['lang']=='EN' else '職務経験'}</a>
#       <a href="#projects">{'Projects' if st.session_state['lang']=='EN' else 'プロジェクト'}</a>
#       <a href="#contact">{'Contact' if st.session_state['lang']=='EN' else 'お問い合わせ'}</a>
#     </div>
#   </div>
#   <div class="nav-actions">
#     <!-- left empty: we render widgets below (language + icon + resume) -->
#   </div>
# </div>
# <div class="nav-spacer"></div>
# """


# # ---------------- Header area with widgets (placed AFTER navbar so they appear in header row) ----------------
# header_cols = st.columns([1.1, 2, 1.2])
# with header_cols[0]:
#     if PROFILE_PATH:
#         st.image(str(PROFILE_PATH), width=140, caption=TEXT[st.session_state["lang"]]["profile_alt"])
#     else:
#         st.markdown("<div class='logo card'><div style='font-size:28px; font-weight:700; padding-top:10px;'>SB</div></div>", unsafe_allow_html=True)

# with header_cols[1]:
#     st.markdown(f"<h1 style='margin:0'>Shubham Badlani</h1>", unsafe_allow_html=True)
#     st.markdown(f"<div class='small'>Electronics Engineer (VLSI Design & Technology) • Embedded Systems • FPGA • AI & ML</div>", unsafe_allow_html=True)

# with header_cols[2]:
#     # Language selector (always shown)
#     lang_choice = st.selectbox("", options=["EN", "JP"], index=0 if st.session_state["lang"] == "EN" else 1, key="lang_select")
#     if lang_choice != st.session_state["lang"]:
#         st.session_state["lang"] = lang_choice
#         st.rerun()

#     # Theme icon (always shown)
#     icon = "☀️" if st.session_state["theme"] == "light" else "🌙"
#     theme_icon_html = f"""<span class="theme-icon" onclick="document.getElementById('theme_toggle_btn').click()">{icon}</span>"""
#     st.markdown(theme_icon_html, unsafe_allow_html=True)

#     # hidden button triggers theme change (and rerun)
#     if st.button("", key="theme_toggle_btn"):
#         st.session_state["theme"] = "light" if st.session_state["theme"] == "dark" else "dark"
#         st.rerun()

#     # Resume download
#     if RESUME_PATH.exists():
#         with open(RESUME_PATH, "rb") as f:
#             pdf_bytes = f.read()
#         st.download_button(TEXT[st.session_state["lang"]]["download_resume"], data=pdf_bytes, file_name=RESUME_FILENAME)
#     else:
#         st.info(TEXT[st.session_state["lang"]]["no_resume"])

# st.write("---")

# # ---------------- content sections ----------------
# st.markdown("<div id='about'></div>", unsafe_allow_html=True)
# st.subheader(TEXT[st.session_state["lang"]]["about_title"])
# st.markdown("<div class='card'>", unsafe_allow_html=True)
# st.write(TEXT[st.session_state["lang"]]["about"])
# st.markdown("</div>", unsafe_allow_html=True)

# st.markdown("<div id='skills'></div>", unsafe_allow_html=True)
# st.subheader(TEXT[st.session_state["lang"]]["skills_title"])
# st.markdown("<div class='card'>", unsafe_allow_html=True)
# skills = ["Verilog","VHDL","RTL Design","FPGA Flow (Vivado)","CMOS Design","Control Systems","Analog & Digital Circuits","Microwind","Proteus","MATLAB","LTSpice","C","C++","Python","JavaScript","TypeScript","TailwindCSS","Angular","Streamlit","Flask"]
# st.markdown("".join([f"<span class='tag'>{s}</span>" for s in skills]), unsafe_allow_html=True)
# st.markdown("</div>", unsafe_allow_html=True)

# st.markdown("<div id='education'></div>", unsafe_allow_html=True)
# st.subheader(TEXT[st.session_state["lang"]]["education_title"])
# st.markdown("<div class='card'>", unsafe_allow_html=True)
# for title, desc in TEXT[st.session_state["lang"]]["education_items"]:
#     st.markdown(f"**{title}**  \n{desc}  \n")
# st.markdown("</div>", unsafe_allow_html=True)

# st.markdown("<div id='experience'></div>", unsafe_allow_html=True)
# st.subheader(TEXT[st.session_state["lang"]]["experience_title"])
# st.markdown("<div class='card'>", unsafe_allow_html=True)
# for role, info in TEXT[st.session_state["lang"]]["experience_items"]:
#     st.markdown(f"**{role}**  \n<span class='small'>{info}</span>  \n")
# st.markdown("</div>", unsafe_allow_html=True)

# st.markdown("<div id='projects'></div>", unsafe_allow_html=True)
# st.subheader(TEXT[st.session_state["lang"]]["projects_title"])
# st.markdown("<div class='card'>", unsafe_allow_html=True)
# for title, desc, link in TEXT[st.session_state["lang"]]["projects_items"]:
#     st.markdown(f"### {title}")
#     st.write(desc)
#     if link:
#         st.markdown(f"[Explore →]({link})")
#     st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)
# st.markdown("</div>", unsafe_allow_html=True)

# st.subheader(TEXT[st.session_state["lang"]]["languages_title"])
# st.markdown("<div class='card'>", unsafe_allow_html=True)
# if st.session_state["lang"] == "EN":
#     st.markdown("<span class='tag'>English</span> <span class='tag'>日本語 (Japanese)</span>", unsafe_allow_html=True)
# else:
#     st.markdown("<span class='tag'>English</span> <span class='tag'>日本語（日本語）</span>", unsafe_allow_html=True)
# st.markdown("</div>", unsafe_allow_html=True)

# st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
# st.subheader(TEXT[st.session_state["lang"]]["contact_title"])
# st.markdown("<div class='card'>", unsafe_allow_html=True)
# st.markdown(f"**Email:** <a class='link' href='mailto:{EMAIL}'>{EMAIL}</a><br>**Phone:** {PHONE}<br>**LinkedIn:** <a class='link' href='{LINKEDIN_URL}' target='_blank'>{LINKEDIN_URL}</a><br>**GitHub:** <a class='link' href='{GITHUB_URL}' target='_blank'>{GITHUB_URL}</a>", unsafe_allow_html=True)
# st.markdown("</div>", unsafe_allow_html=True)

# st.write("---")
# year = datetime.date.today().year
# st.markdown(f"<div class='small center'>© {year} Shubham Badlani • Built with Streamlit</div>", unsafe_allow_html=True)

# st.markdown("</div>", unsafe_allow_html=True)

# import streamlit as st
# from pathlib import Path
# import datetime

# # -------------------------------- CONFIG --------------------------------
# PAGE_TITLE = "Shubham Badlani — Portfolio"
# PAGE_ICON = "🛠️"
# st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

# RESUME_FILENAME = "Shubham_Resume25_11_2025.pdf"

# # Resume
# RESUME_RUNTIME = Path("/mnt/data") / RESUME_FILENAME
# RESUME_ASSETS = Path("assets") / RESUME_FILENAME
# RESUME_PATH = RESUME_RUNTIME if RESUME_RUNTIME.exists() else RESUME_ASSETS

# # Profile Image
# PROFILE_RUNTIME = Path("/mnt/data/WhatsApp Image 2024-07-06 at 16.17.23_3d1d87db.jpg")
# PROFILE_ASSETS = Path("assets/profile.jpg")
# PROFILE_PATH = PROFILE_RUNTIME if PROFILE_RUNTIME.exists() else (PROFILE_ASSETS if PROFILE_ASSETS.exists() else None)

# # Social links
# GITHUB = "https://github.com/Shubham-badlani"
# LINKEDIN = "https://www.linkedin.com/in/shubham-badlani-576511351/"
# EMAIL = "shubhambadlani05@gmail.com"
# PHONE = "+91 9351359006"

# # -------------------------------- SESSION --------------------------------
# if "theme" not in st.session_state:
#     st.session_state.theme = "dark"

# if "lang" not in st.session_state:
#     st.session_state.lang = "EN"


# # -------------------------------- TEXT --------------------------------
# TEXT = {
#     "EN": {
#         "about_title": "About Me",
#         "about": "Electronics Engineer specializing in VLSI, FPGA, Embedded Systems & AI-driven hardware.",
#         "skills_title": "Top Skills",
#         "education_title": "Education",
#         "experience_title": "Experience",
#         "projects_title": "Projects",
#         "languages_title": "Languages",
#         "contact_title": "Contact",
#         "resume": "Download Resume",
#     },
#     "JP": {
#         "about_title": "自己紹介",
#         "about": "VLSI、FPGA、組込みシステム、AIハードウェアに特化したエレクトロニクスエンジニア。",
#         "skills_title": "主なスキル",
#         "education_title": "学歴",
#         "experience_title": "職務経験",
#         "projects_title": "プロジェクト",
#         "languages_title": "対応言語",
#         "contact_title": "お問い合わせ",
#         "resume": "履歴書をダウンロード",
#     }
# }


# # -------------------------------- SIDEBAR --------------------------------
# with st.sidebar:
#     st.markdown("## **Shubham Badlani**")

#     if PROFILE_PATH:
#         st.image(str(PROFILE_PATH), width=180, caption="")

#     # Language Switch
#     lang = st.radio("Language", ["EN", "JP"], index=0 if st.session_state.lang=="EN" else 1)
#     if lang != st.session_state.lang:
#         st.session_state.lang = lang
#         st.rerun()

#     # Theme toggle
#     theme_icon = "☀️ Light Mode" if st.session_state.theme == "light" else "🌙 Dark Mode"
#     if st.button(theme_icon):
#         st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"
#         st.rerun()

#     # Navigation menu
#     st.markdown("---")
#     st.markdown("### **Navigation**")
#     st.markdown("[About](#about)")
#     st.markdown("[Skills](#skills)")
#     st.markdown("[Education](#education)")
#     st.markdown("[Experience](#experience)")
#     st.markdown("[Projects](#projects)")
#     st.markdown("[Contact](#contact)")

#     st.markdown("---")

#     # Resume download
#     if RESUME_PATH.exists():
#         with open(RESUME_PATH, "rb") as f:
#             st.download_button(TEXT[st.session_state.lang]["resume"], f, file_name=RESUME_FILENAME)

#     # Social
#     st.markdown("---")
#     st.markdown("### Connect")
#     st.markdown(f"📧 **Email:** {EMAIL}")
#     st.markdown(f"[🔗 LinkedIn]({LINKEDIN})")
#     st.markdown(f"[💻 GitHub]({GITHUB})")


# # -------------------------------- PAGE CONTENT --------------------------------

# st.markdown(f"# {TEXT[st.session_state.lang]['about_title']}")
# st.write(TEXT[st.session_state.lang]["about"])
# st.write("---")

# # Skills
# st.markdown("<div id='skills'></div>", unsafe_allow_html=True)
# st.subheader(TEXT[st.session_state.lang]["skills_title"])
# skills = ["Verilog","VHDL","RTL","FPGA","Embedded C","Python","JavaScript","Proteus","Microwind"]
# st.markdown("".join([f"<span style='padding:6px 12px; margin:4px; background:#eee; border-radius:10px; display:inline-block;'>{s}</span>" for s in skills]), unsafe_allow_html=True)
# st.write("---")

# # Education
# st.markdown("<div id='education'></div>", unsafe_allow_html=True)
# st.subheader(TEXT[st.session_state.lang]["education_title"])
# st.write("""
# - **B.E. Electronics (VLSI)** — SPPU (2023–2027)  
# - **PCM Senior Secondary** — CBSE (80%)  
# - **Secondary** — CBSE (90%)
# """)
# st.write("---")

# # Experience
# st.markdown("<div id='experience'></div>", unsafe_allow_html=True)
# st.subheader(TEXT[st.session_state.lang]["experience_title"])
# st.write("""
# - **R&D AI Engineer Intern — Sciemetric (TASI India)** (2025)  
# - **Angular Intern — Infosys Springboard** (2024–2025)  
# """)
# st.write("---")

# # Projects
# st.markdown("<div id='projects'></div>", unsafe_allow_html=True)
# st.subheader(TEXT[st.session_state.lang]["projects_title"])
# st.write("""
# - Climate Prediction (Kaggle)  
# - CTS Leak Test - Deviation Detector  
# - Student Result App  
# - Farmer AI ChatBot  
# - FPGA Mini Projects  
# """)
# st.write("---")

# # Contact
# st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
# st.subheader(TEXT[st.session_state.lang]["contact_title"])
# st.write(f"""
# 📧 **Email:** {EMAIL}  
# 📞 **Phone:** {PHONE}  
# 🔗 **LinkedIn:** {LINKEDIN}  
# 💻 **GitHub:** {GITHUB}  
# """)

# st.write("---")
# st.write(f"© {datetime.date.today().year} — Built by Shubham Badlani")


import streamlit as st
from pathlib import Path
import datetime
from base64 import b64encode

# -------------------------------- CONFIG --------------------------------
PAGE_TITLE = "Shubham Badlani — Portfolio"
PAGE_ICON = "🛠️"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

RESUME_FILENAME = "Shubham_Resume25_11_2025.pdf"

# Resume Path
RESUME_RUNTIME = Path("/mnt/data") / RESUME_FILENAME
RESUME_ASSETS = Path("assets") / RESUME_FILENAME
RESUME_PATH = RESUME_RUNTIME if RESUME_RUNTIME.exists() else RESUME_ASSETS

# Profile Image
PROFILE_RUNTIME = Path("/mnt/data/WhatsApp Image 2024-07-06 at 16.17.23_3d1d87db.jpg")
PROFILE_ASSETS = Path("assets/profile.jpg")
PROFILE_PATH = PROFILE_RUNTIME if PROFILE_RUNTIME.exists() else (PROFILE_ASSETS if PROFILE_ASSETS.exists() else None)

# Social links
GITHUB = "https://github.com/Shubham-badlani"
LINKEDIN = "https://www.linkedin.com/in/shubham-badlani-576511351/"
EMAIL = "shubhambadlani05@gmail.com"
PHONE = "+91 9351359006"

# -------------------------------- SESSION --------------------------------
if "theme" not in st.session_state:
    st.session_state.theme = "dark"

if "lang" not in st.session_state:
    st.session_state.lang = "EN"

# Load profile image as base64
if PROFILE_PATH and PROFILE_PATH.exists():
    with open(PROFILE_PATH, "rb") as f:
        profile_b64 = b64encode(f.read()).decode()
else:
    profile_b64 = None


# -------------------------------- TEXT --------------------------------
TEXT = {
    "EN": {
        "about_title": "About Me",
        "about": "Electronics Engineer specializing in VLSI, FPGA, Embedded Systems & AI-driven hardware.",
        "skills_title": "Top Skills",
        "education_title": "Education",
        "experience_title": "Experience",
        "projects_title": "Projects",
        "languages_title": "Languages",
        "contact_title": "Contact",
        "resume": "Download Resume",
        "contact_form": "Contact Form"
    },
    "JP": {
        "about_title": "自己紹介",
        "about": "VLSI、FPGA、組込みシステム、AIハードウェアに特化したエレクトロニクスエンジニア。",
        "skills_title": "主なスキル",
        "education_title": "学歴",
        "experience_title": "職務経験",
        "projects_title": "プロジェクト",
        "languages_title": "対応言語",
        "contact_title": "お問い合わせ",
        "resume": "履歴書をダウンロード",
        "contact_form": "お問い合わせフォーム"
    }
}

# -------------------------------- SIDEBAR --------------------------------
with st.sidebar:

    # Small circular logo + name side-by-side
    if profile_b64:
        st.markdown(
            f"""
            <div style="display:flex; align-items:center; gap:10px;">
                <img src="data:image/png;base64,{profile_b64}"
                style="width:60px; height:60px; border-radius:50%; object-fit:cover;">
                <div style="font-size:20px; font-weight:700;">Shubham Badlani</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown("### **Shubham Badlani**")

    st.markdown("---")

    # Language Selection
    lang = st.radio("Language", ["EN", "JP"], index=0 if st.session_state.lang=="EN" else 1)
    if lang != st.session_state.lang:
        st.session_state.lang = lang
        st.rerun()

    # Theme Toggle
    theme_icon = "☀️ Light Mode" if st.session_state.theme == "dark" else "🌙 Dark Mode"
    if st.button(theme_icon):
        st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"
        st.rerun()

    st.markdown("---")

    # Sidebar Navigation
    st.markdown("### **Navigation**")
    st.markdown("[About](#about)", unsafe_allow_html=True)
    st.markdown("[Skills](#skills)", unsafe_allow_html=True)
    st.markdown("[Education](#education)", unsafe_allow_html=True)
    st.markdown("[Experience](#experience)", unsafe_allow_html=True)
    st.markdown("[Projects](#projects)", unsafe_allow_html=True)
    st.markdown("[Languages](#languages)", unsafe_allow_html=True)
    st.markdown("[Contact](#contact)", unsafe_allow_html=True)

    st.markdown("---")

    # Resume Download
    if RESUME_PATH.exists():
        with open(RESUME_PATH, "rb") as f:
            st.download_button(TEXT[st.session_state.lang]["resume"], f, file_name=RESUME_FILENAME)

    st.markdown("---")

    # Social Links
    st.markdown("### Connect")
    st.markdown(f"📧 **Email:** {EMAIL}")
    st.markdown(f"[🔗 LinkedIn]({LINKEDIN})")
    st.markdown(f"[💻 GitHub]({GITHUB})")


# ------------------------------ MAIN CONTENT ------------------------------

st.markdown(f"<h1 id='about'>{TEXT[st.session_state.lang]['about_title']}</h1>", unsafe_allow_html=True)
st.write(TEXT[st.session_state.lang]["about"])
st.write("---")

# Skills
st.markdown("<h2 id='skills'>Skills</h2>", unsafe_allow_html=True)
skills = ["Verilog","VHDL","RTL","FPGA","Embedded C","Python","JavaScript","Proteus","Microwind"]
st.markdown("".join([f"<span style='padding:6px 12px; margin:4px; background:#ddd; border-radius:10px; display:inline-block;'>{s}</span>" for s in skills]), unsafe_allow_html=True)
st.write("---")

# Education
st.markdown("<h2 id='education'>Education</h2>", unsafe_allow_html=True)
st.write("""
- **B.E. Electronics (VLSI)** — SPPU (2023–2027)  
- **PCM Senior Secondary** — CBSE (80%)  
- **Secondary** — CBSE (90%)
""")
st.write("---")

# Experience
st.markdown("<h2 id='experience'>Experience</h2>", unsafe_allow_html=True)
st.write("""
- **R&D AI Engineer Intern — Sciemetric (TASI India)** (2025)  
- **Angular Intern — Infosys Springboard** (2024–2025)  
""")
st.write("---")

# Projects
st.markdown("<h2 id='projects'>Projects</h2>", unsafe_allow_html=True)
st.write("""
- Climate Prediction (Kaggle)  
- CTS Leak Test - Deviation Detector  
- Student Result App  
- Farmer AI ChatBot  
- FPGA Mini Projects  
""")
st.write("---")

# Languages
st.markdown("<h2 id='languages'>Languages</h2>", unsafe_allow_html=True)
st.write("- English  \n- Japanese")
st.write("---")


# ------------------------------ CONTACT SECTION ------------------------------

import requests

GSHEET_URL = "https://script.google.com/macros/s/AKfycbyPBvUSulGui8c2FtLjpYOo-LvsW3FMZTKlXJQQtV17AfuRnZ8M_JILOXylSCogeuwY/exec"

st.markdown("<h2 id='contact'>Contact</h2>", unsafe_allow_html=True)

col1, col2 = st.columns([1.4, 1])

with col1:
    st.subheader("Send me a Message")
    name = st.text_input("Your Name")
    email_in = st.text_input("Your Email")
    subject = st.text_input("Subject")
    message = st.text_area("Message")

    if st.button("Send Message"):
        if not name or not email_in or not message:
            st.error("Please fill in all required fields.")
        else:
            payload = {
                "name": name,
                "email": email_in,
                "subject": subject,
                "message": message
            }
            response = requests.post(GSHEET_URL, json=payload)
            if response.status_code == 200:
                st.success("✅ Message sent! Thank you.")
            else:
                st.error("❌ Failed to send message — try again later.")

with col2:
    st.subheader("My Contact Details")
    st.write(f"📧 Email: {EMAIL}")
    st.write(f"📞 Phone: {PHONE}")
    st.write(f"[🔗 LinkedIn]({LINKEDIN})")
    st.write(f"[💻 GitHub]({GITHUB})")
