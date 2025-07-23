from PIL import Image
import torch
from transformers import CLIPProcessor, CLIPModel

# 加载 CLIP 模型和处理器
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# 设定标签
CANDIDATE_LABELS = ["money", "growth", "bankruptcy", "risk", "technology", "crisis", "profit", "loss"]
POSITIVE = {"money", "growth", "profit", "technology"}
NEGATIVE = {"bankruptcy", "crisis", "loss", "risk"}

def analyze_image(image: Image.Image):
    image = image.convert("RGB")
    inputs = processor(text=CANDIDATE_LABELS, images=image, return_tensors="pt", padding=True)
    
    with torch.no_grad():
        outputs = model(**inputs)

    probs = outputs.logits_per_image.softmax(dim=1).squeeze()
    label_scores = dict(zip(CANDIDATE_LABELS, probs.tolist()))

    # 打分逻辑
    score = 0
    for label, p in label_scores.items():
        if label in POSITIVE:
            score += p
        elif label in NEGATIVE:
            score -= p

    return round(score, 3)
