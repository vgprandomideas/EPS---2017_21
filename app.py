from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(page_title="Tamil Nadu | Development Record 2017–2021",layout="wide",initial_sidebar_state="collapsed")
root=Path(__file__).parent
html=(root/"index.html").read_text(encoding="utf-8")
import re, base64
def asset(m):
    name=m.group(0)
    p=root/name
    return "data:image/png;base64,"+base64.b64encode(p.read_bytes()).decode() if p.exists() else name
# Serve available report assets through embedded data URLs.
images={str(i):"data:image/png;base64,"+base64.b64encode((root/f"page-{i}.png").read_bytes()).decode() for i in range(1,52) if (root/f"page-{i}.png").exists()}
import json
html=html.replace("</head>","<script>const reportImages="+json.dumps(images)+";</script></head>")
html=html.replace("'page-'+b.dataset.page+'.png'","(reportImages[b.dataset.page] || '')")
html=re.sub(r'page-(\d+)\.png',lambda m:images.get(m.group(1),m.group(0)),html)
if not images:
    html=html.replace("</head>","<style>article img,button[data-page]{display:none!important}</style></head>")
if (root/"white-paper.pdf").exists():
    st.download_button("Download original white paper",(root/"white-paper.pdf").read_bytes(),"white-paper.pdf","application/pdf")
else:
    st.caption("Original PDF and page illustrations are pending upload to the repository.")
    html=html.replace('href="white-paper.pdf"','href="#sources"')
components.html(html,height=1200,scrolling=True)
