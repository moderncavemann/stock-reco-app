def generate_explanation(score_text=None, score_image=None, score_audio=None):
    explanation_parts = []

    if score_text is not None:
        explanation_parts.append(f"📝 **Text sentiment score**: {score_text:.2f}")

    if score_image is not None:
        explanation_parts.append(f"🖼️ **Image sentiment score**: {score_image:.2f}")

    if score_audio is not None:
        explanation_parts.append(f"🔊 **Audio sentiment score**: {score_audio:.2f}")

    if not explanation_parts:
        return "No explanation available."

    return "\n\n".join(explanation_parts)


