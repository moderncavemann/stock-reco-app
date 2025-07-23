def fuse_scores(score_text, score_image, score_audio,
                  w_text=0.5, w_image=0.3, w_audio=0.2):
    final_score = (w_text * score_text +
                   w_image * score_image +
                   w_audio * score_audio)
    if final_score > 0.3:
        return "BUY ✅", final_score
    elif final_score < -0.3:
        return "SELL ❌", final_score
    else:
        return "HOLD 🤔", final_score
