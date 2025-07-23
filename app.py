import streamlit as st
from modules.fetch_data import fetch_multimodal_data
from modules.fuse_scores import fuse_scores
from modules.explain import generate_explanation

st.set_page_config(page_title="Multimodal Stock Recommender")

st.title("📈 Multimodal Stock Recommendation System")

ticker = st.text_input("Enter stock symbol (e.g., TSLA, AAPL)")

if st.button("Analyze"):
    st.info("Fetching and analyzing data...")

    text_data, images, audios = fetch_multimodal_data(ticker)

    score_text = 0.0  # placeholder
    score_image = 0.0  # placeholder
    score_audio = 0.0  # placeholder

    result, final_score = fuse_scores(score_text, score_image, score_audio)
    explanation = generate_explanation(score_text, score_image, score_audio)

    st.markdown(f"### ✅ Recommendation: **{result}**")
    st.metric("Overall Score", round(final_score, 3))
    st.write("### Reasoning")
    st.write(explanation)
