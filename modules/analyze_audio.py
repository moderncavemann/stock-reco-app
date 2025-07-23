import torch
import torchaudio
from transformers import Wav2Vec2ForSequenceClassification, Wav2Vec2Processor

model_name = "ehcalabres/wav2vec2-lg-xlsr-en-speech-emotion-recognition"
model = Wav2Vec2ForSequenceClassification.from_pretrained(model_name)
processor = Wav2Vec2Processor.from_pretrained(model_name)

# 情绪标签 → 金融情绪打分
EMOTION_SCORE = {
    "angry": -1.0, "sad": -0.8, "fearful": -0.6, "disgust": -0.5,
    "neutral": 0.0, "happy": 0.8, "surprised": 0.4, "calm": 0.3
}

def analyze_audio(uploaded_file):
    waveform, sample_rate = torchaudio.load(uploaded_file)
    
    # 转为 mono + 16kHz
    if sample_rate != 16000:
        waveform = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)(waveform)
    if waveform.shape[0] > 1:
        waveform = waveform.mean(dim=0, keepdim=True)

    input_values = processor(waveform.squeeze(), sampling_rate=16000, return_tensors="pt").input_values

    with torch.no_grad():
        logits = model(input_values).logits

    predicted_id = torch.argmax(logits, dim=-1).item()
    label = model.config.id2label[predicted_id]
    return EMOTION_SCORE.get(label.lower(), 0.0)


