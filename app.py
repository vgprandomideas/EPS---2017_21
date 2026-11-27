from pathlib import Path
import streamlit as st
import sqlite3
import tempfile
from contextlib import closing
import streamlit.components.v1 as components
st.set_page_config(page_title="Tamil Nadu | Development Record",layout="wide",initial_sidebar_state="collapsed")
root=Path(__file__).parent
st.markdown("""<style>
.stApp{background:#f4f7f4;color:#17382e}
.block-container{padding:3.5rem 1.25rem 1rem;max-width:1440px}
header[data-testid='stHeader']{background:#f4f7f4}
[data-testid='stVerticalBlockBorderWrapper']{background:#fff;border:1px solid #d6e2d9!important;border-radius:14px!important}
[data-testid='stMarkdownContainer'] h3{color:#17382e!important;font-size:1.35rem;line-height:1.3}
[data-testid='stMarkdownContainer'] p{color:#344c40!important}
[data-testid='stMarkdownContainer'] a{color:#176044!important;font-weight:600;text-decoration:underline}
[data-testid='stDownloadButton'] button{background:#18563f!important;border:1px solid #18563f!important;color:#fff!important;border-radius:8px!important;min-height:48px;white-space:normal;font-weight:600}
[data-testid='stDownloadButton'] button *{color:#fff!important}
[data-testid='stDownloadButton'] button:hover{background:#103c2d!important}
@media(max-width:640px){.block-container{padding:3.25rem .75rem 1rem}[data-testid='stMarkdownContainer'] h3{font-size:1.15rem}}
</style>""",unsafe_allow_html=True)
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
        st.markdown("### Development White Paper")
        st.markdown("Tamil Nadu · 2017–2021")
        st.download_button("Download White Paper (PDF)",pdf.read_bytes(),"EPS_WhitePaper.pdf","application/pdf",on_click=lambda: download_count(True),use_container_width=True)
        st.markdown("[Read PDF online ↗](https://raw.githubusercontent.com/vgprandomideas/EPS---2017_21/main/EPS_WhitePaper.pdf)")
        st.markdown(f"**Downloads: {download_count():,}**")

    
components.html((root/"index.html").read_text(encoding="utf-8"),height=1800,scrolling=True)
