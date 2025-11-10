import streamlit as st
from ollama import chat
from PIL import Image
import io

# Set page configuration
st.set_page_config(
    page_title="Paveikslėlio Aprašymas",
    page_icon="🖼️",
    layout="centered"
)

# Custom CSS for red background
st.markdown("""
    <style>
    .stApp {
        background-color: #8B0000;
    }
    </style>
    """, unsafe_allow_html=True)

# Application title
st.title("🖼️ Paveikslėlio Aprašymas su AI")
st.markdown("Įkelkite paveikslėlį ir dirbtinis intelektas apibūdins jo turinį.")

# File uploader for images
uploaded_file = st.file_uploader(
    "Pasirinkite paveikslėlį",
    type=["jpg", "jpeg", "png", "bmp", "gif"],
    accept_multiple_files=False,
    help="Įkelkite paveikslėlį JPG, PNG, BMP arba GIF formatu"
)

if uploaded_file is not None:
    # Display the uploaded image
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Įkeltas paveikslėlis")
        image = Image.open(uploaded_file)
        st.image(image, use_container_width=True)
    
    with col2:
        st.subheader("AI Aprašymas")
        
        # Text input for user question
        user_question = st.text_input(
            "Jūsų klausimas apie paveikslėlį",
            value="Aprašyk šį paveikslėlį detaliai lietuvių kalba. Pasakyk ką matai paveikslėlyje.",
            help="Įveskite klausimą, kurį norite užduoti apie paveikslėlį"
        )
        
        # Button to analyze the image
        if st.button("Analizuoti paveikslėlį", type="primary"):
            with st.spinner("Analizuojama..."):
                try:
                    # Convert image to bytes
                    img_byte_arr = io.BytesIO()
                    image.save(img_byte_arr, format=image.format or 'PNG')
                    img_bytes = img_byte_arr.getvalue()
                    
                    # Call Ollama with the image
                    response = chat(
                        model='gemma3:4b',
                        messages=[{
                            'role': 'user',
                            'content': user_question,
                            'images': [img_bytes]
                        }]
                    )
                    
                    # Display the response
                    st.success("Analizė baigta!")
                    st.write(response.message.content)
                    
                except Exception as e:
                    st.error(f"Įvyko klaida: {str(e)}")
                    st.info("Įsitikinkite, kad Ollama serveris veikia ir modelis 'gemma3:4b' yra parsisiųstas.")
else:
    st.info("👆 Įkelkite paveikslėlį, kad pradėtumėte analizę.")

# Footer with instructions
with st.expander("ℹ️ Kaip naudotis"):
    st.markdown("""
    **Instrukcijos:**
    1. Įkelkite paveikslėlį naudodami viršuje esantį įkėlimo lauką
    2. Paspauskite mygtuką "Analizuoti paveikslėlį"
    3. Palaukite kol AI apibūdins paveikslėlio turinį
    
    **Reikalavimai:**
    - Ollama serveris turi būti paleistas
    - Modelis 'gemma3:4b' turi būti parsisiųstas
    - Palaikomi formatai: JPG, PNG, BMP, GIF
    """)
