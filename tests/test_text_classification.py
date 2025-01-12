from examples.text_classification import classify_text

def test_classify_text():
    text = "I love programming!"

    result = classify_text(text)

    # Check if the result is a list
    assert result[0]["label"] in ["POSITIVE", "NEGATIVE"]
