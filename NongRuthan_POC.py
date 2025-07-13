import streamlit as st
from datetime import datetime

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Conversational AI for Scam Detection and Digital Awareness in Thailand",
    page_icon="👦🏻",
    layout="centered"
)

# --- SIDE-BY-SIDE: Logo and Title ---
col1, col2 = st.columns([1, 2.5])  # ปรับอัตราส่วนคอลัมน์ตามความเหมาะสม

with col1:
    st.image(
        "https://raw.githubusercontent.com/joesrwt/streamlit-openai/main/Image%2014-7-2568%20BE%20at%2000.10.jpeg",
        width=120
    )

with col2:
    st.markdown(
        "**น้องรู้ทัน** คือแชทบอทที่รวบรวมข้อมูลกลโกงมิจฉาชีพทางออนไลน์กว่า 1,000 บทความ "
        "อัปเดตตรงจากเว็บไซต์ **ศูนย์ต่อต้านข่าวปลอมประเทศไทย (Anti-Fake News Centre Thailand)** ซึ่งอยู่ภายใต้การกำกับดูแลของ \nกระทรวงดิจิทัลเพื่อเศรษฐกิจและสังคม (MDES)"
    )

# --- CUSTOM CSS ---
st.markdown("""
<style>
.chat-bubble-user {
    background-color: #2f3542;
    color: white;
    padding: 1em;
    border-radius: 15px;
    margin-left: 20%;
    margin-right: 0;
    margin-top: 1em;
    text-align: right;
}
.chat-bubble-assistant {
    background-color: #f1f2f6;
    color: black;
    padding: 1em;
    border-radius: 15px;
    margin-right: 20%;
    margin-left: 0;
    margin-top: 1em;
}
.reference-box {
    background-color: #dfe4ea;
    padding: 0.8em;
    border-radius: 10px;
    margin-top: 0.5em;
}
</style>
""", unsafe_allow_html=True)

# --- SIMULATED USER MESSAGE ---
st.markdown(f"""
<div class="chat-bubble-user">
    มี SMS ส่งมาบอกว่าผมทำผิดกฎหมายจากธนาคาร แล้วให้กดลิงก์ด้วย แบบนี้ธนาคารจะส่งลิงก์มาจริงไหมครับ
</div>
""", unsafe_allow_html=True)

# --- SIMULATED ASSISTANT MESSAGE ---
st.markdown(f"""
<div class="chat-bubble-assistant">
รอสักครู่นะครับ... น้องรู้ทันกำลังหาข้อมูลให้อยู่ครับผม! 👦🏻🔍  
<hr>
🔎 <strong>น้องรู้ทัน เจอแล้วครับผม!!</strong><br><br>

<strong>👦🏻 น้องรู้ทัน</strong>:  
จากข้อมูลที่ ศูนย์ต่อต้านข่าวปลอมประเทศไทยได้ให้ไว้  
<strong>ธนาคารไม่มีนโยบายส่งลิงก์ผ่าน SMS ครับผม</strong>  
หากได้รับข้อความอ้างว่ามาจากธนาคารและให้กดลิงก์ ถือว่าเป็น <em>มิจฉาชีพ</em> แน่นอนครับผม<br><br>

🚨 <strong>ระดับความอันตราย:</strong> 🔴 อันตรายมาก ควรหยุดทันที<br>
🕵️‍♂️ <strong>ประเภทกลโกง:</strong> SMS Phishing<br>
💬 <strong>คำอธิบาย:</strong> หลอกให้กดลิงก์ในข้อความ SMS เพื่อให้เปิดเผยข้อมูลส่วนตัว หรือติดตั้งแอปควบคุมเครื่อง
</div>
""", unsafe_allow_html=True)

# --- REFERENCES ---
st.markdown(f"""
<div class="reference-box">
<b>Document 1:</b><br>
> ธนาคารไม่มีนโยบายส่งลิงก์ผ่านทาง SMS หากพบว่ามีลิงก์แนบมาโดยอ้างว่าเป็นธนาคาร ให้รู้ไว้เลยว่าเป็นมิจฉาชีพ  
> ❗ อ้างเป็นเจ้าหน้าที่ / หลอกให้โหลดแอปควบคุมเครื่อง / โอนเงิน  
📅 25 ก.พ. 2025  
🔗 <a href="https://www.antifakenewscenter.com/?p=68521" target="_blank">ลิงก์บทความ</a>  
🕵️‍♂️ หน่วยงานตรวจสอบ: สำนักงานตำรวจแห่งชาติ
</div>

<div class="reference-box">
<b>Document 2:</b><br>
> เตือนภัย! SMS ปลอมจากมิจฉาชีพ อ้างชื่อธนาคาร/บริษัทต่าง ๆ แล้วแนบลิงก์  
> ❗ ระวังข้อความแจ้งเตือนปลอม เช่น “บัญชีโดน Hack” หรือ “ปรับปรุงระบบ”  
📅 20 ส.ค. 2023  
🔗 <a href="https://www.antifakenewscenter.com/?p=40494" target="_blank">ลิงก์บทความ</a>  
🏛 หน่วยงานตรวจสอบ: ธนาคารแห่งประเทศไทย
</div>
""", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("---")
st.caption(f"📅 อัปเดตล่าสุด: {datetime.now().strftime('%d/%m/%Y %H:%M')} | Powered by น้องรู้ทัน AI")
