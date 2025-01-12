from transformers import pipeline

def classify_text(text):
    classifier = pipeline("text-classification")
    return classifier(text)

if __name__ == "__main__":
    text = "I love programming!"
    result = classify_text(text)
    print(result)
