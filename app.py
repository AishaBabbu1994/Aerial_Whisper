import streamlit as st
import whisper
import tempfile
import os

st.title("🎙️ Transcriptor Mágico")

uploaded_file = st.file_uploader("Sube tu audio/video", type=["mp3", "wav", "mp4"])

# Carga el modelo SOLO UNA VEZ
@st.cache_resource
def load_whisper_model():
    return whisper.load_model("base")

if uploaded_file:
    # Guarda temporalmente el archivo
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_path = tmp_file.name
    
    try:
        # Transcribe
        with st.spinner("Transcribiendo... 🪄"):
            model = load_whisper_model()
            result = model.transcribe(tmp_path)
            transcription = result["text"]
        
        # Muestra resultado
        st.success("¡Listo! ✨")
        st.text_area("📝 Transcripción:", transcription, height=300)
        
        # Botón de descarga
        st.download_button(
            label="📥 Descargar como TXT",
            data=transcription,
            file_name="transcripcion.txt",
            mime="text/plain"
        )
        
    finally:
        # Limpia siempre
        os.unlink(tmp_path)
