import torch
import torchaudio
from speechbrain.pretrained import SpeakerRecognition

# 下载模型（第一次加载会缓存）
emotion_model = torch.hub.load('speechbrain/emotion-recognition-wav2vec2-IEMOCAP', 'custom')

# 手动映射情绪分数
EMOTION_SCORE = {
    "angry": -0.9, "sad": -0.6, "fearful": -0.4, "disgust": -0.3,
    "neutral": 0.0, "happy": 0.7, "surprise": 0.4, "calm": 0.3
}

def analyze_audio(uploaded_file):
    # 保存上传音频为临时文件（Streamlit 需要这样）
    with open("temp.wav", "wb") as f:
        f.write(uploaded_file.read())

    signal, fs = torchaudio.load("temp.wav")
    if fs != 16000:
        signal = torchaudio.transforms.Resample(fs, 16000)(signal)

    prediction = emotion_model.classify_file("temp.wav")
    label = prediction[3]  # e.g. "happy"

    return EMOTION_SCORE.get(label.lower(), 0.0)


