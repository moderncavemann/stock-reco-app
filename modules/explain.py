def generate_explanation(score_text, score_image, score_audio):
    reasons = []
    if score_text > 0.2:
        reasons.append("Textual sentiment is positive.")
    elif score_text < -0.2:
        reasons.append("Textual sentiment is negative.")
    if score_image > 0.2:
        reasons.append("Images reflect optimism.")
    if score_audio < -0.2:
        reasons.append("Audio suggests concern or negativity.")
    return " ".join(reasons) or "No strong signals detected."
