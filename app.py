import streamlit as st
import whisper

st.title("🎙️ Transcriptor Mágico")

uploaded_file = st.file_uploader("Sube tu audio/video", type=["mp3", "wav", "mp4"])

if uploaded_file:
    model = whisper.load_model("base")
    result = model.transcribe(uploaded_file.name)
    st.text_area("Transcripción:", result["text"])
