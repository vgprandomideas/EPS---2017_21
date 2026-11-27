from pathlib import Path
import streamlit as st
import sqlite3
import tempfile
from contextlib import closing
import streamlit.components.v1 as components
st.set_page_config(page_title="Tamil Nadu | Development Record",layout="wide",initial_sidebar_state="collapsed")
root=Path(__file__).parent
st.markdown("<style>.stApp{background:#f4f7f4;color:#17382e}.block-container{padding:1rem 1rem 0;max-width:1440px}header[data-testid='stHeader']{background:transparent}</style>",unsafe_allow_html=True)
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
    left,right=st.columns([3,1])
    with left:
        st.download_button("Download white paper (PDF)",pdf.read_bytes(),"EPS_WhitePaper.pdf","application/pdf",on_click=lambda: download_count(True),use_container_width=True)
    with right:
        st.metric("Website downloads",download_count())
    st.caption("Counts download button clicks on this running website instance; direct PDF links are not counted.")
components.html((root/"index.html").read_text(encoding="utf-8"),height=1800,scrolling=True)
