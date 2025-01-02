# Import necessary libraries
from transformers import MarianMTModel, MarianTokenizer

# Load the pre-trained MarianMT model and tokenizer
model_name = 'Helsinki-NLP/opus-mt-en-fr'  # Model for English to French translation
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

# Define the translate function
def translate(text):
    # Tokenize the input text
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    # Generate translation
    translated = model.generate(**inputs)
    # Decode the translated text
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    return translated_text

# Example usage
english_text = "Hello, how are you?"
french_text = translate(english_text)

print(f"English: {english_text}")
print(f"French: {french_text}")
