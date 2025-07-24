def fuse_scores(text_score=None, image_score=None, audio_score=None):
    """
    融合多模态得分（文本、图像、音频），输出推荐结果和融合得分
    """
    scores = []
    weights = []

    if text_score is not None:
        scores.append(text_score)
        weights.append(0.6)

    if image_score is not None:
        scores.append(image_score)
        weights.append(0.3)

    if audio_score is not None:
        scores.append(audio_score)
        weights.append(0.1)

    if not scores:
        return "Hold", 0.0

    try:
        final_score = sum(s * w for s, w in zip(scores, weights)) / sum(weights)
    except ZeroDivisionError:
        return "Hold", 0.0

    if final_score >= 0.6:
        return "Buy", round(final_score, 3)
    elif final_score <= 0.4:
        return "Sell", round(final_score, 3)
    else:
        return "Hold", round(final_score, 3)

