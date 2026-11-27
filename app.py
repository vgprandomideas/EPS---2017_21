from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(page_title="Tamil Nadu | Development Record",layout="wide",initial_sidebar_state="collapsed")
root=Path(__file__).parent
st.markdown("<style>.stApp{background:#f4f7f4;color:#17382e}.block-container{padding:1rem 1rem 0;max-width:1440px}header[data-testid='stHeader']{background:transparent}</style>",unsafe_allow_html=True)
pdf=root/"white-paper.pdf"
if pdf.exists():
    st.download_button("Download white paper",pdf.read_bytes(),"Tamil-Nadu-2017-2021.pdf","application/pdf")
components.html((root/"index.html").read_text(encoding="utf-8"),height=1800,scrolling=True)
