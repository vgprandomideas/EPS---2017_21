from pathlib import Path
import streamlit as st
import sqlite3
import tempfile
from contextlib import closing
import streamlit.components.v1 as components
st.set_page_config(page_title="Tamil Nadu | Development Record",layout="wide",initial_sidebar_state="collapsed")
root=Path(__file__).parent
st.markdown("<style>.stApp{background:#f4f7f4;color:#17382e}.block-container{padding:3.5rem 1.25rem 1rem;max-width:1440px}header[data-testid='stHeader']{background:transparent}@media(max-width:640px){.block-container{padding:3.5rem .75rem 1rem} [data-testid='stDownloadButton'] button{min-height:48px;white-space:normal} [data-testid='stMarkdownContainer'] h3{font-size:1.2rem;line-height:1.35}}</style>",unsafe_allow_html=True)
pdf=root/"EPS_WhitePaper.pdf"
db=Path(tempfile.gettempdir())/"eps_whitepaper_downloads.sqlite3"
def download_count(increment=False):
    with closing(sqlite3.connect(db,timeout=10)) as conn:
        with conn:
            conn.execute("CREATE TABLE IF NOT EXISTS downloads (id INTEGER PRIMARY KEY, count INTEGER NOT NULL)")
            conn.execute("INSERT OR IGNORE INTO downloads VALUES (1,0)")
            if increment:
                conn.execute("UPDATE downloads SET count=count+1 WHERE id=1")
            return conn.execute("SELECT count FROM downloads WHERE id=1").fetchone()[0]
if pdf.exists():
    with st.container(border=True):
        st.markdown("### Development White Paper | 2017–2021")
        st.markdown("Comprehensive report on Tamil Nadu's development record.")
        st.download_button("Download White Paper (PDF)",pdf.read_bytes(),"EPS_WhitePaper.pdf","application/pdf",on_click=lambda: download_count(True),use_container_width=True)
        st.markdown("[Read White Paper online ↗](https://raw.githubusercontent.com/vgprandomideas/EPS---2017_21/main/EPS_WhitePaper.pdf)")
        st.markdown(f"**Downloads: {download_count():,}**")

    
components.html((root/"index.html").read_text(encoding="utf-8"),height=1800,scrolling=True)
