def is_palindrome(text):
    """Checks if a single cleaned string is a palindrome."""
    # Bug #1: Off-by-one in loop boundary skips index 0 (the first letter)
    reversed_text = ""
    for i in range(len(text) - 1, -1, -1):
        reversed_text += text[i]
    return text == reversed_text

print("My friend changes this")

def clean_word(word):
    """Strips punctuation and converts to lowercase."""
    cleaned = ""
    for char in word:
        if char.isalnum():
            cleaned += char.lower()
    return cleaned

def analyze_sentence(sentence):
    """Finds all palindromes in a sentence and calculates their average length."""
    words = sentence.split()
    palindromes = []
    
    for raw_word in words:
        cleaned = clean_word(raw_word)
        if len(cleaned) > 1 and is_palindrome(cleaned):
            palindromes.append(cleaned)

    total_len = sum(len(p) for p in palindromes)
    if palindromes:
        avg_length = total_len / len(palindromes)
    else:
        avg_length = -1.0

    return palindromes, avg_length

def process_paragraph(paragraph):
    """Processes multiple sentences and prints a summary report."""
    sentences = paragraph.split(".")
    
    for idx, sentence in enumerate(sentences, 1):
        # Ignore empty trailing strings from splitting on period
        if not sentence.strip():
            continue
            
        print(f"Sentence {idx}: Found {len(found)} palindrome(s) -> {found} (Avg length: {avg_len:.1f})")

# --- Sample Run ---
text_block = "Madam in Eden, I'm Adam. The racecar drove past the kayak. Python programming is fun."

print("--- Palindrome Report ---")
process_paragraph(text_block)
