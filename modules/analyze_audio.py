import torch
import torchaudio
from speechbrain.pretrained import EncoderClassifier

model = EncoderClassifier.from_hparams(
    source="speechbrain/emotion-recognition-wav2vec2-IEMOCAP",
    savedir="tmpdir"
)

def analyze_audio(uploaded_file):
    with open("temp.wav", "wb") as f:
        f.write(uploaded_file.read())

    # 加载音频
    signal, fs = torchaudio.load("temp.wav")
    if fs != 16000:
        signal = torchaudio.transforms.Resample(fs, 16000)(signal)

    # 推理
    out_prob, out_class, _ = model.classify_file("temp.wav")
    print("Predicted class:", out_class)

    # 简单映射为分数（可自定义）
    scores = {
        "angry": -1.0,
        "sad": -0.8,
        "neutral": 0.0,
        "happy": 0.8
    }
    return scores.get(out_class.lower(), 0.0)



