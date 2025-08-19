import streamlit as st
from preprocesser import custom_preprocessor
import pickle

# Load all your models
models = {
    "Model-1 (86%)": pickle.load(open("lr_pipe.pkl", "rb")),
    "Model-2 (Overfit Model 96%)": pickle.load(open("grid.pkl", "rb")),
    "Model-3 (May Be Overfit 94%)": pickle.load(open("sentiment_pipeline.pkl", "rb"))
}

# Page configuration
st.set_page_config(page_title="Sentiment Analysis App", page_icon="😊", layout="centered")

# Title
st.title("😊 NLP-Based Sentiment & Emotion Analysis with ML")
st.write("Analyze the sentiment of your text using different ML models.")

# Model selection
selected_model_name = st.selectbox("Choose a model:", list(models.keys()))
current_model = models[selected_model_name]
st.markdown(f"**Selected Model:** {selected_model_name}")

st.markdown("💡 Tip: Longer sentences may give more accurate predictions.")
st.markdown("💡 Guide: This Model Is Build Using ML-NLP, So It Is Not 100% Accurate In Predictions.")
# User input
user_input = st.text_area("✍️ Enter your text here:", height=150)

# Analyze button
if st.button("Analyze Sentiment"):
    if user_input.strip():
        prediction = current_model.predict([user_input])[0]

        # Colored emotion display
        emotion = prediction.lower()

        if emotion == "joy":
            st.success(f"😊 Emotion Detected: {prediction.title()}")
        elif emotion == "love":
            st.success(f"❤️ Emotion Detected: {prediction.title()}")
        elif emotion == "surprise":
            st.info(f"😲 Emotion Detected: {prediction.title()}")
        elif emotion == "sadness":
            st.error(f"😢 Emotion Detected: {prediction.title()}")
        elif emotion == "anger":
            st.error(f"😡 Emotion Detected: {prediction.title()}")
        elif emotion == "fear":
            st.warning(f"😨 Emotion Detected: {prediction.title()}")
        else:
            st.info(f"ℹ️ Emotion Detected: {prediction.title()}")
    else:
        st.warning("⚠️ Please enter some text to analyze.")


# Sample sentences for testing
st.markdown("---")
st.subheader("💡 Try Sample Sentences")

sample_sentences = [
    "I just got promoted at work, and I can’t stop smiling; all my hard work finally paid off!",
    "My best friend surprised me with tickets to my favorite concert — I couldn’t believe it!",
    "I’ve been feeling lonely lately and missing the people I love the most.",
    "My partner left me a heartfelt note, and it made me feel so loved and appreciated.",
    "The sudden loud noise in the night made me jump and my heart race in fear.",
    "I can’t believe someone lied to me and betrayed my trust — I’m so angry!",
    "Seeing the breathtaking sunrise over the mountains filled me with awe and happiness.",
    "The unexpected gift left me completely surprised and grateful."
]

selected_sample = st.selectbox("Choose a sample sentence to test:", sample_sentences)

st.text_area("📋 Copy your sample sentence here:", value=selected_sample, height=80, disabled=True)