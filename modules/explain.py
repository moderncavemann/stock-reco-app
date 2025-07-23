def generate_explanation(score_text, score_image, score_audio):
    reasons = []

    if score_text > 0.2:
        reasons.append("Text sentiment is positive.")
    elif score_text < -0.2:
        reasons.append("Text sentiment is negative.")

    if score_image > 0.2:
        reasons.append("Images reflect optimism.")
    elif score_image < -0.2:
        reasons.append("Images reflect pessimism.")

    if score_audio > 0.2:
        reasons.append("Audio tone is confident.")
    elif score_audio < -0.2:
        reasons.append("Audio tone suggests concern.")

    return " ".join(reasons) or "No strong signals detected."

