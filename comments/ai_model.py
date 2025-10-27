from transformers import pipeline

toxic_classifier = pipeline("text-classification", model="unitary/toxic-bert")

def get_toxicity_score(comment: str) -> dict:
    result = toxic_classifier(comment)[0]
    return {
        "label": result["label"],
        "score": round(result["score"], 3)
    }
