import torchaudio
from speechbrain.pretrained import EncoderClassifier

model = EncoderClassifier.from_hparams(
    source="speechbrain/emotion-recognition-wav2vec2-IEMOCAP",
    savedir="pretrained_models/emotion"
)

def analyze_audio(uploaded_file):
    with open("temp.wav", "wb") as f:
        f.write(uploaded_file.read())

    signal, fs = torchaudio.load("temp.wav")
    if fs != 16000:
        signal = torchaudio.transforms.Resample(fs, 16000)(signal)

    out_prob, out_class, _ = model.classify_file("temp.wav")

    print(f"[AUDIO] Predicted Emotion: {out_class}")

    score_map = {
        "happy": 0.8,
        "angry": -1.0,
        "sad": -0.8,
        "neutral": 0.0,
    }
    return score_map.get(out_class.lower(), 0.0)




