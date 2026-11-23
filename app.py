"""الموقع الرئيسي — شغّله بالأمر:  streamlit run app.py"""
import pandas as pd
import streamlit as st
from PIL import Image

from config import AUTHOR_NAME_AR, AUTHOR_NAME_EN, LINKS, LOW_CONFIDENCE_THRESHOLD
from disease_info import DISEASES
from model_utils import model_files_exist, predict_image
from translations import TEXTS

st.set_page_config(page_title="Brain Tumor MRI Classifier", page_icon="🧠", layout="centered")

# ---------------- اللغة والتنقل ----------------
lang_choice = st.sidebar.radio("🌐 اللغة / Language", ["العربية", "English"], horizontal=True)
lang = "ar" if lang_choice == "العربية" else "en"
t = TEXTS[lang]

page = st.sidebar.radio(
    t["nav"], ["home", "about"], format_func=lambda k: t["nav_" + k], key="page"
)
st.sidebar.warning(t["disclaimer"])

# ---------------- الشكل (CSS) ----------------
rtl_css = """
.block-container, [data-testid="stSidebarUserContent"] { direction: rtl; text-align: right; }
""" if lang == "ar" else ""

st.markdown(
    f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap');
html, body, .stApp, .stMarkdown, button, label, p, h1, h2, h3, h4 {{ font-family: 'Cairo', sans-serif; }}
{rtl_css}
.author-card {{
    margin-top: 2.5rem; padding: 1.2rem 1rem; border-radius: 16px; text-align: center;
    background: linear-gradient(135deg, #6C4DF6 0%, #3B82F6 100%); color: #fff;
}}
.author-card .name {{ font-size: 1.2rem; font-weight: 700; margin: .2rem 0 .8rem; }}
.author-card a {{
    display: inline-block; margin: .2rem .3rem; padding: .35rem .9rem; border-radius: 999px;
    background: rgba(255,255,255,.18); color: #fff !important; text-decoration: none; font-weight: 600;
}}
.author-card a:hover {{ background: rgba(255,255,255,.32); }}
.result-box {{
    padding: 1rem 1.2rem; border-radius: 14px; border: 1px solid rgba(108,77,246,.35);
    background: rgba(108,77,246,.08); margin-bottom: 1rem;
}}
.result-box .label {{ font-size: .9rem; opacity: .75; }}
.result-box .value {{ font-size: 1.5rem; font-weight: 700; }}
</style>
""",
    unsafe_allow_html=True,
)


def author_card():
    name = AUTHOR_NAME_AR if lang == "ar" else AUTHOR_NAME_EN
    links = "".join(
        f'<a href="{url}" target="_blank" rel="noopener noreferrer">{label}</a>'
        for label, url in LINKS.items()
        if url
    )
    st.markdown(
        f"""
<div class="author-card">
  <div>{t['built_by']}</div>
  <div class="name">{name}</div>
  <div>{t['follow_me']}</div>
  <div>{links}</div>
</div>
""",
        unsafe_allow_html=True,
    )


def bullets(items):
    return "\n".join(f"- {i}" for i in items)


# ---------------- صفحة التحليل ----------------
def home_page():
    st.title(t["app_title"])
    st.write(t["app_subtitle"])
    st.info(t["tips"])

    if not model_files_exist():
        st.error(t["model_missing"])
        return

    uploaded = st.file_uploader(t["upload_label"], type=["jpg", "jpeg", "png"], help=t["upload_help"])
    if uploaded is None:
        return

    image = Image.open(uploaded)
    st.image(image, caption=t["uploaded_image"], width=360)

    if not st.button(t["analyze_btn"], type="primary"):
        return

    with st.spinner(t["analyzing"]):
        top, conf, probs = predict_image(image)

    info = DISEASES.get(top, {}).get(lang, {"name": top, "what": "", "symptoms": [], "treatment": ""})

    st.subheader(t["result_title"])
    st.markdown(
        f"""
<div class="result-box">
  <div class="label">{t['predicted_disease']}</div>
  <div class="value">{info['name']}</div>
  <div class="label" style="margin-top:.6rem">{t['confidence']}: {conf * 100:.1f}%</div>
</div>
""",
        unsafe_allow_html=True,
    )
    st.progress(min(max(conf, 0.0), 1.0))

    if conf < LOW_CONFIDENCE_THRESHOLD:
        st.warning(t["low_conf"])

    df = pd.DataFrame(
        {t["confidence"] + " (%)": [round(p * 100, 1) for p in probs.values()]},
        index=[DISEASES.get(k, {}).get(lang, {}).get("name", k) for k in probs],
    )
    st.markdown(f"**{t['probs_title']}**")
    st.bar_chart(df)

    st.subheader(t["about_disease"])
    if info.get("what"):
        st.markdown(f"**{t['what_is']}**\n\n{info['what']}")
    if info.get("symptoms"):
        st.markdown(f"**{t['symptoms']}**\n\n{bullets(info['symptoms'])}")
    if info.get("treatment"):
        st.markdown(f"**{t['treatment']}**\n\n{info['treatment']}")
    if info.get("note"):
        st.info(f"**{t['note']}:** {info['note']}")

    st.warning(t["disclaimer"])


# ---------------- صفحة عن المشروع ----------------
def about_page():
    st.title(t["about_title"])
    st.write(t["about_intro"])
    st.subheader(t["about_how_title"])
    st.markdown("\n".join(f"{i}. {s}" for i, s in enumerate(t["about_how"], 1)))
    st.subheader(t["about_data_title"])
    st.write(t["about_data"])
    st.subheader(t["about_model_title"])
    st.write(t["about_model"])
    st.subheader(t["about_limits_title"])
    st.markdown(bullets(t["about_limits"]))
    st.warning(t["disclaimer"])


if page == "home":
    home_page()
else:
    about_page()

author_card()
