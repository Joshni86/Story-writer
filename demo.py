from transformers import pipeline
classifier = pipeline("sentiment-analysis")
result = classifier("I absolutely love this")
print(result)