def normalize_persian_text(text: str) -> str:
    arabic_chars = {
        "ي": "ی", "ك": "ک", "ؤ": "و", "ئ": "ی", "إ": "ا", "أ": "ا", "ٱ": "ا"
    }
    text = "".join(arabic_chars.get(char, char) for char in text)
    text = " ".join(text.split()) 
    return text

