def fuse_scores(text_score=None, image_score=None):
    """
    融合文本与图片模态得分，输出推荐结果和融合得分
    """
    scores = []
    weights = []

    if text_score is not None:
        scores.append(text_score)
        weights.append(0.7)

    if image_score is not None:
        scores.append(image_score)
        weights.append(0.3)

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

