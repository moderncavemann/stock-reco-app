from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# 加载 FinBERT 模型
tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")

def analyze_text(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=-1)

    # FinBERT 的类别顺序：[negative, neutral, positive]
    score = probs[0][2] - probs[0][0]  # positive - negative
    return score.item()

