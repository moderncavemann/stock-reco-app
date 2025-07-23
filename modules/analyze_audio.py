import torch
import torchaudio
from transformers import AutoModelForAudioClassification, AutoProcessor

model_name = "superb/wav2vec2-base-superb-er"
model = AutoModelForAudioClassification.from_pretrained(model_name)
processor = AutoProcessor.from_pretrained(model_name)

# label 映射（示例，可按你需求调整评分逻辑）
EMOTION_SCORE = {
    "angry": -1.0, "sad": -0.8, "fearful": -0.6, "disgust": -0.5,
    "neutral": 0.0, "happy": 0.8, "surprised": 0.4, "calm": 0.3
}

def analyze_audio(uploaded_file):
    waveform, sample_rate = torchaudio.load(uploaded_file)

    # 确保 mono 且 16kHz
    if sample_rate != 16000:
        resample = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)
        waveform = resample(waveform)
    if waveform.shape[0] > 1:
        waveform = waveform.mean(dim=0, keepdim=True)

    inputs = processor(waveform.squeeze(), sampling_rate=16000, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    predicted_label = model.config.id2label[outputs.logits.argmax(-1).item()]
    return EMOTION_SCORE.get(predicted_label.lower(), 0.0)



