def fuse_scores(text_score=None, image_score=None, audio_score=None):
    """
    融合各模态得分，可根据需要设定权重。
    如果某个模态为空，则只融合有效模态。
    """

    scores = []
    weights = []

    if text_score is not None:
        scores.append(text_score)
        weights.append(0.6)  # 文本权重

    if image_score is not None:
        scores.append(image_score)
        weights.append(0.3)  # 图片权重

    if audio_score is not None:
        scores.append(audio_score)
        weights.append(0.1)  # 音频权重

    if not scores:
        return 0.0

    # 加权平均
    weighted_sum = sum(s * w for s, w in zip(scores, weights))
    total_weight = sum(weights)

    return round(weighted_sum / total_weight, 3)
