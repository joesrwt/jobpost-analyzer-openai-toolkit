import streamlit as st
from datetime import datetime

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Conversational AI for Scam Detection and Digital Awareness in Thailand",
    page_icon="👦🏻",
    layout="centered"
)
# --- HEADER: SIDE-BY-SIDE ---
col1, col2 = st.columns([1, 2.5])
with col1:
    st.image(
        "https://raw.githubusercontent.com/joesrwt/streamlit-openai/main/Image%2014-7-2568%20BE%20at%2000.10.jpeg",
        width=100
    )
with col2:
    st.markdown(
        "**น้องรู้ทัน** คือแชทบอทที่รวบรวมข้อมูลกลโกงมิจฉาชีพทางออนไลน์กว่า 1,000 บทความ "
        "อัปเดตตรงจากเว็บไซต์ **ศูนย์ต่อต้านข่าวปลอมประเทศไทย (Anti-Fake News Centre Thailand)** "
        "ซึ่งอยู่ภายใต้การกำกับดูแลของกระทรวงดิจิทัลเพื่อเศรษฐกิจและสังคม (MDES)"
    )

# --- CSS STYLE ---
st.markdown("""
<style>
.chat-container {
    display: flex;
    margin-top: 1em;
}
.chat-user {
    justify-content: flex-end;
}
.chat-assistant, .chat-reference {
    justify-content: flex-start;
}
.chat-bubble {
    padding: 1em;
    border-radius: 15px;
    max-width: 75%;
}
.chat-bubble-user {
    background-color: #2f3542;
    color: white;
    text-align: right;
    margin-right: 10px;
}
.chat-bubble-assistant {
    background-color: #f1f2f6;
    color: black;
    margin-left: 10px;
}
.chat-icon {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    object-fit: cover;
}
.chat-bubble-reference {
    background-color: #f1f2f6;
    color: black;
    padding: 1em;
    border-radius: 15px;
    margin-left: 10px;
    max-width: 85%;
    box-shadow: 1px 1px 5px rgba(0,0,0,0.1);
}
.chat-bubble-reference h4 {
    margin-top: 0;
}
.chat-meta {
    color: #57606f;
    font-size: 0.9em;
}
</style>
""", unsafe_allow_html=True)

# --- USER MESSAGE ---
st.markdown(f"""
<div class="chat-container chat-user">
    <div class="chat-bubble chat-bubble-user">
        มี SMS ส่งมาบอกว่าผมทำผิดกฎหมายจากธนาคาร แล้วให้กดลิงก์ด้วย แบบนี้ธนาคารจะส่งลิงก์มาจริงไหมครับ
    </div>
    <img src="https://cdn-icons-png.flaticon.com/512/747/747545.png" class="chat-icon" />
</div>
""", unsafe_allow_html=True)

# --- ASSISTANT MESSAGE ---
st.markdown(f"""
<div class="chat-container chat-assistant">
    <img src="https://raw.githubusercontent.com/joesrwt/streamlit-openai/main/Image%2014-7-2568%20BE%20at%2000.10.jpeg" class="chat-icon" />
    <div class="chat-bubble chat-bubble-assistant">
        รอสักครู่นะครับ... น้องรู้ทันกำลังหาข้อมูลให้อยู่ครับผม! 👦🏻🔍<br><hr>
        🔎 <strong>น้องรู้ทัน เจอแล้วครับผม!!</strong><br><br>
        <strong>👦🏻 น้องรู้ทัน</strong>:<br>
        จากข้อมูลที่ ศูนย์ต่อต้านข่าวปลอมประเทศไทยได้ให้ไว้<br>
        <strong>ธนาคารไม่มีนโยบายส่งลิงก์ผ่าน SMS ครับผม</strong><br>
        หากได้รับข้อความอ้างว่ามาจากธนาคารและให้กดลิงก์ ถือว่าเป็น <em>มิจฉาชีพ</em> แน่นอนครับผม<br><br>
        🚨 <strong>ระดับความอันตราย:</strong> 🔴 อันตรายมาก ควรหยุดทันที<br>
        🕵️‍♂️ <strong>ประเภทกลโกง:</strong> SMS Phishing<br>
        💬 <strong>คำอธิบาย:</strong> หลอกให้กดลิงก์ในข้อความ SMS เพื่อให้เปิดเผยข้อมูลส่วนตัว หรือติดตั้งแอปควบคุมเครื่อง
    </div>
</div>
""", unsafe_allow_html=True)

# --- REFERENCES ---
st.markdown("### 📚 เอกสารอ้างอิงจากระบบ")

st.markdown(f"""
<div class="chat-container chat-reference">
    <img src="https://raw.githubusercontent.com/joesrwt/streamlit-openai/main/Image%2014-7-2568%20BE%20at%2000.10.jpeg" class="chat-icon" />
    <div class="chat-bubble-reference">
        <h4>📄 Document 1: เตือนภัย! มิจฯ ส่ง SMS ปลอม แอบอ้างเป็นธนาคาร</h4>
        <p>
        ปัจจุบันธนาคารเลิกส่งลิงก์ผ่านทาง SMS หากพบว่ามีลิงก์แนบส่งมาโดยอ้างว่าเป็นธนาคาร ให้รู้ไว้เลยว่าเป็นมิจฉาชีพ<br>
        ❗ จุดสังเกตที่พบบ่อย:<br>
        - อ้างเป็นเจ้าหน้าที่ธนาคาร<br>
        - หลอกให้กดลิงก์<br>
        - ให้โหลดแอปควบคุมเครื่อง<br>
        - หลอกให้โอนเงินออกจากบัญชี<br><br>
        <span class="chat-meta">
        🕵️‍♂️ หน่วยงานตรวจสอบ: สำนักงานตำรวจแห่งชาติ<br>
        📅 วันที่เผยแพร่: 25 กุมภาพันธ์ 2025<br>
        🔗 <a href="https://www.antifakenewscenter.com/?p=68521" target="_blank">อ่านบทความต้นทาง</a>
        </span>
        </p>
    </div>
</div>

<div class="chat-container chat-reference">
    <img src="https://raw.githubusercontent.com/joesrwt/streamlit-openai/main/Image%2014-7-2568%20BE%20at%2000.10.jpeg" class="chat-icon" />
    <div class="chat-bubble-reference">
        <h4>📄 Document 2: SMS น่าสงสัยหลีกให้ไกล อย่าคลิกลิงก์เด็ดขาด!</h4>
        <p>
        เตือนภัย SMS กลลวงที่อ้างตัวเป็นเจ้าหน้าที่รัฐหรือบริษัทต่าง ๆ โดยแนบลิงก์ใน SMS<br>
        📌 ตัวอย่างข้อความที่พบบ่อย:<br>
        - แจ้งเตือน! ยังไม่ชำระค่าบริการ<br>
        - แจ้งเตือน! บัญชีโดน Hack<br>
        - โปรดอัปเดตข้อมูลทางลิงก์<br><br>
        ✅ ปัจจุบันธนาคารไม่มีนโยบายส่งลิงก์ขอข้อมูลลูกค้าผ่าน SMS หรืออีเมล<br><br>
        <span class="chat-meta">
        🏛 หน่วยงานตรวจสอบ: ธนาคารแห่งประเทศไทย<br>
        📅 วันที่เผยแพร่: 20 สิงหาคม 2023<br>
        🔗 <a href="https://www.antifakenewscenter.com/?p=40494" target="_blank">อ่านบทความต้นทาง</a>
        </span>
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("---")
st.caption(f"📅 อัปเดตล่าสุด: {datetime.now().strftime('%d/%m/%Y %H:%M')} | Powered by น้องรู้ทัน AI")
