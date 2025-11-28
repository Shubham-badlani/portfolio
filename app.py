
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

    # # Language Selection
    # lang = st.radio("Language", ["EN", "JP"], index=0 if st.session_state.lang=="EN" else 1)
    # if lang != st.session_state.lang:
    #     st.session_state.lang = lang
    #     st.rerun()

    # # Theme Toggle
    # theme_icon = "☀️ Light Mode" if st.session_state.theme == "dark" else "🌙 Dark Mode"
    # if st.button(theme_icon):
    #     st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"
    #     st.rerun()

    # st.markdown("---")

    # Sidebar Navigation


    st.markdown("### **Navigation**")
    st.markdown("<a href='#about'>About Me</a>", unsafe_allow_html=True)
    st.markdown("[Skills](#skills)", unsafe_allow_html=True)
    st.markdown("[Certificates](#certificates)", unsafe_allow_html=True)

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
    st.markdown(f" **Email:** {EMAIL}")
    st.markdown(f"[ LinkedIn]({LINKEDIN})")
    st.markdown(f"[ GitHub]({GITHUB})")


# # ------------------------------ MAIN CONTENT ------------------------------
# # -------------------------- PAGE HEADER --------------------------
# # Container for name + top-right icons
# st.markdown("""
#     <div style='display:flex; justify-content:space-between; align-items:center;'>
#         <h1 style='margin:0;'>Shubham Badlani</h1>
#         <div style='display:flex; align-items:center; gap:20px;'>
# """, unsafe_allow_html=True)



# # ------------------ Resume Button ------------------
# if RESUME_PATH.exists():
#     with open(RESUME_PATH, "rb") as f:
#         resume_bytes = f.read()
#     st.download_button(
#         label="📄 Resume",
#         data=resume_bytes,
#         file_name=RESUME_FILENAME,
#         key="resume_download_top"
#     )

# ------------------------------ PAGE HEADER ------------------------------

# Create header row
col1, col2, col3 = st.columns([2.5, 1, 1])

# ------------------ LEFT: NAME ------------------
with col1:
    st.markdown(
        "<h1 style='margin:0; font-size:38px;'>Shubham Badlani</h1>",
        unsafe_allow_html=True
    )

# ------------------ MIDDLE: RESUME BUTTON ------------------
with col2:
    if RESUME_PATH.exists():
        with open(RESUME_PATH, "rb") as f:
            resume_bytes = f.read()
        st.download_button(
            label="📄 Resume",
            data=resume_bytes,
            file_name=RESUME_FILENAME,
            key="resume_download_top",
            use_container_width=True
        )

# ------------------ RIGHT: LINKEDIN & EMAIL BUTTONS ------------------
with col3:
   st.markdown("""
<a href="https://www.linkedin.com/in/shubham-badlani-576511351/" target="_blank" style="text-decoration:none;">
    <button style="
        width:100%;
        padding:8px 12px;
        font-size:15px;
        border:none;
        border-radius:6px;
        background-color:#0A66C2;
        color:white;
        cursor:pointer;">
        🔗 LinkedIn
    </button>
</a>

<br><br>

<a href="mailto:shubhambadlani05@gmail.com" style="text-decoration:none;">
    <button style="
        width:100%;
        padding:8px 12px;
        font-size:15px;
        border:none;
        border-radius:6px;
        background-color:#6B7280;
        color:white;
        cursor:pointer;">
        ✉️ Email
    </button>
</a>
""", unsafe_allow_html=True)


# ------------------ Social Icons (Clickable) ------------------


# ---------- About Section ----------
st.markdown("<a id='about'></a>", unsafe_allow_html=True)
st.markdown(f"<h1>{TEXT[st.session_state.lang]['about_title']}</h1>", unsafe_allow_html=True)
st.write(TEXT[st.session_state.lang]["about"])
st.write("---")

# Skills

st.markdown("<h2 id='skills'>Skills</h2>", unsafe_allow_html=True)
skills_groups = {
    "HDL & FPGA": [
        "Verilog", "VHDL", "RTL Design", "FPGA Flow", "Xilinx Vivado"
    ],
    "Electronics & VLSI": [
        "CMOS Design", "Control Systems", "Analog Circuits", "Digital Circuits",
        "Signal Systems", "LTSpice", "Cadence (Basic)"
    ],
    "Microcontrollers": [
        "8051", "PIC Microcontroller", "MPLAB", "Keil uVision"
    ],
    "Simulation & EDA Tools": [
        "Microwind", "Proteus", "MATLAB", "Multisim"
    ],
    "Embedded & Communication": [
        "UART", "SPI", "I2C", "TCP/IP Basics", "Arduino"
    ],
    "Programming Languages": [
        "C", "C++", "Python", "JavaScript", "TypeScript", "Verilog HDL"
    ],
    "Web & Frameworks": [
        "HTML", "CSS", "TailwindCSS", "Angular", "Flask", "Streamlit"
    ],
    "Python ML/DL Libraries": [
        "Pandas", "NumPy", "Matplotlib", "Seaborn", "Plotly", "SciPy",
        "Scikit-learn", "TensorFlow", "XGBoost", "OpenCV",
        "NLP", "Bayesian Models", "Prediction Pipelines", "Joblib"
    ],
    "Data & Visualization": [
        "Power BI", "Excel", "Kaggle Notebooks"
    ],
    "Databases": [
        "MySQL"
    ],
    "Tools & Platforms": [
        "Git", "GitHub", "Arduino IDE"
    ]
}

# Display skills as stylish tags
for group, items in skills_groups.items():
    st.markdown(f"### {group}")
    st.markdown(
        "".join(
            [
                f"<span style='padding:6px 12px; margin:4px; background:#ddd; "
                f"border-radius:10px; display:inline-block;'>{item}</span>"
                for item in items
            ]
        ),
        unsafe_allow_html=True
    )
    st.write("")
    
st.write("---")

# Certificates
st.markdown("<h2 id='certificates'>Certificates</h2>", unsafe_allow_html=True)

certificates = [
    "📜 Fundamentals in C – E&ICT Academy IIT Kanpur (2023)",
    "📜 AI Fundamentals with Capstone Project – IBM SkillsBuild (Jun 2024 – Aug 2024)",
    "📜 Cyber Security Fundamentals – IBM SkillsBuild (2024)",
    "🏅 Excellence in DSA (Rank 1000) – UnStop (2024)",
    "📜 C Programming (2024)",
    "📜 HTML, CSS, JS, Tailwind, Angular – Infosys Springboard (2024)",
    "🧑‍🏫 Campus Ambassador – Acmegrade (2024)",
    "💼 Web Development Intern – MyDailyWork.com (2024)",
    "📜 Analog Electronics – Udemy (2025)",
    "🎓 Internship Completion (Angular) – Infosys Springboard (2025)",
    "🎓 Internship Completion (R&D AI) – Sciemetric Technologies India PvtLtd (TASI India) (2025)",
    "🎓 Internship Completion (AI Azure) – Microsoft Edunet (AICTE) (2025)",
    "🌱 Internship Completion (Green Skills in AI) – Edunet (AICTE) (2025)"
]

for c in certificates:
    st.markdown(f"- {c}")

st.write("---")

# Education
st.markdown("<h2 id='education'>Education</h2>", unsafe_allow_html=True)

st.markdown("""
### 🎓 B.E. Electronics Engineering — VLSI Design & Technology  
**KJ College of Engineering & Management Research (SPPU), Pune**  
*2023 – 2027*

### 🏫 Senior Secondary (PCM) — CBSE  
**Central Academy, Jodhpur**  
*2023 — 80%*

### 🏫 Secondary (10th) — CBSE  
**Central Academy, Jodhpur**  
*2021 — 90%*
""")

st.write("---")



# Experience
st.markdown("<h2 id='experience'>Experience</h2>", unsafe_allow_html=True)

st.markdown("""
### **Research & Development AI Engineer Intern — Sciemetric Technologies (TASI India)**  
**Jun 2025 – Aug 2025**  
- Developed anomaly detection & Bayesian change-point models for industrial pressure cycles  
- Automated leak-test evaluation using ML pipelines  
- Built a Streamlit dashboard for real-time visualization and prediction  
""")

st.markdown("""
### **Angular Intern — Infosys Springboard**  
**Nov 2024 – Jan 2025**  
- Built responsive components & UI screens using Angular  
- Worked with TypeScript, services, modules, templating  
- Created small applications with routing, forms & API integration  
""")

st.write("---")


# Projects
st.markdown("<h2 id='projects'>Projects</h2>", unsafe_allow_html=True)

st.markdown("""
### **Climate Prediction – Machine Learning (Kaggle)**
- Built ML models to predict rainfall & temperature trends (1901–2020 IMD dataset)  
- Tools: Pandas, NumPy, Scikit-learn, Matplotlib  
[Kaggle Notebook](https://www.kaggle.com/code/shubhambadlani/predicting-climate)
""")

st.markdown("""
### **CTS Leak Test – Phase Deviation Detector**
- Developed anomaly detection models (Isolation Forest + Bayesian CPD)  
- Built Streamlit dashboard for real-time industrial test-cycle analysis  
- Used in predicting leak deviations across PRF, PFN, SDP, DPD phases  
""")

st.markdown("""
### **Student Result Processing System**
- Python + MySQL based application for managing student records & generating results  
- Automated grading logic with clean UI  
""")

st.markdown("""
### **AI ChatBot for Farmers**
- Integrated weather API + AI model for agriculture guidance  
- Supports Hindi/English and text-to-speech  
""")

st.markdown("""
### **FPGA Mini Projects (Verilog HDL)**
- Built counters, FSMs, ALU, and small digital modules on FPGA  
- Tools: Verilog, Vivado  
""")

st.write("---")


# Languages
st.markdown("<h2 id='languages'>Languages</h2>", unsafe_allow_html=True)
st.write("- English  ")
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
                st.success(" Message sent! Thank you.")
            else:
                st.error(" Failed to send message — try again later.")

with col2:
    st.subheader("My Contact Details")
    st.write(f" Email: {EMAIL}")
    st.write(f" Phone: {PHONE}")
    st.write(f"[ LinkedIn]({LINKEDIN})")
    st.write(f"[ GitHub]({GITHUB})")
