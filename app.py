import streamlit as st
import whisper
import tempfile
import os

st.title("🎙️ Transcriptor Mágico")

uploaded_file = st.file_uploader("Sube tu audio/video", type=["mp3", "wav", "mp4"])

@st.cache_resource
def load_whisper_model():
    return whisper.load_model("tiny")  # ¡tiny para pruebas rápidas!

if uploaded_file:
    # ✨ CIERRA el archivo temporal ANTES de usarlo (clave mágica)
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_path = tmp_file.name
    
    try:
        with st.spinner(f"Transcribiendo {uploaded_file.name}... 🌙✨ (espera ~{uploaded_file.size//100000} segundos)"):
            model = load_whisper_model()
            result = model.transcribe(tmp_path)
            transcription = result["text"]
        
        st.success("¡Listo! ✨")
        st.text_area("📝 Transcripción:", transcription, height=300)
        
        st.download_button(
            "📥 Descargar TXT",
            transcription,
            "transcripcion.txt",
            "text/plain"
        )
    finally:
        os.unlink(tmp_path)
