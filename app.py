import streamlit as st
import whisper
import tempfile
import os

st.title("🎙️ Transcriptor Mágico")

uploaded_file = st.file_uploader("Sube tu audio/video", type=["mp3", "wav", "mp4"])

if uploaded_file:
    # Guardar temporalmente
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_path = tmp_file.name
    
    # Transcribir
    model = whisper.load_model("base")
    result = model.transcribe(tmp_path)
    
    # Mostrar resultado
    st.text_area("Transcripción:", result["text"], height=300)
    
    # Limpiar
    os.unlink(tmp_path)
