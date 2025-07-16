import streamlit as st
from utils.meal_plan import generate_meal_plan
from utils.explain import explain_choice
from utils.voice_input import transcribe_audio
from utils.image_food_detect import detect_food_items
from PIL import Image

st.set_page_config(page_title="🥗 Smartest AI Nutrition Assistant", layout="centered")
st.title("🥗 Smartest AI Nutrition Assistant")

mode = st.radio("Choose Input Mode", ["Text", "Voice", "Image"])

if mode == "Text":
    user_input = st.text_area("Enter your health goals, preferences, allergies, etc.", "I want a high-protein meal plan, I do gym 5x/week")

elif mode == "Voice":
    audio_file = st.file_uploader("Upload a voice file (WAV/MP3)", type=["wav", "mp3"])
    if audio_file:
        user_input = transcribe_audio(audio_file)
        st.success(f"Transcribed: {user_input}")

elif mode == "Image":
    img_file = st.file_uploader("Upload a food or grocery image", type=["png", "jpg", "jpeg"])
    if img_file:
        image = Image.open(img_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)
        user_input = detect_food_items(image)
        st.success(f"Detected food items: {user_input}")

if st.button("Generate Meal Plan"):
    if not user_input:
        st.warning("Please provide input.")
    else:
        with st.spinner("Thinking like a nutritionist..."):
            plan = generate_meal_plan(user_input)
            st.subheader("🍽️ Personalized Meal Plan")
            for meal in plan:
                st.markdown(f"**{meal['meal']}**: {meal['description']}")
                if st.toggle(f"Why this meal?", key=meal['meal']):
                    st.info(explain_choice(meal, user_input))
