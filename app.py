import streamlit as st
from PIL import Image
import requests
from io import BytesIO
from modules.fetch_data import fetch_multimodal_data
from modules.analyze_text import analyze_text
from modules.analyze_image import analyze_image
from modules.fuse_scores import fuse_scores
from modules.explain import generate_explanation

st.set_page_config(page_title="📊 Multimodal Stock Recommender")
st.title("📈 Multimodal Stock Recommendation System")

ticker = st.text_input("Enter stock symbol (e.g., TSLA, AAPL)")

if st.button("Analyze"):
    st.info("Fetching and analyzing data...")

    texts, images, _ = fetch_multimodal_data(ticker)

    score_text = analyze_text(texts[0]) if texts else 0.0
    score_image = (
        analyze_image(Image.open(BytesIO(requests.get(images[0]).content)))
        if images else 0.0
    )

    result, final_score = fuse_scores(score_text, score_image)
    explanation = generate_explanation(score_text, score_image)

    st.markdown(f"### ✅ Recommendation: **{result}**")
    st.metric("Overall Score", round(final_score, 3))
    st.write("### Reasoning")
    st.write(explanation)


