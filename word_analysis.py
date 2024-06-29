import morfeusz2
import re

# Function to map detailed POS tags to major categories
def map_pos_to_category(pos):
    if any(tag in pos for tag in ["subst"]):
        return "noun"
    if any(tag in pos for tag in ["adj"]):
        return "adjective"
    if any(tag in pos for tag in ["ppron", "siebie"]):
        return "pronoun"
    if any(tag in pos for tag in ["num"]):
        return "numeral"
    if any(tag in pos for tag in ["fin", "bedzie", "praet", "impt", "imps", "inf", "pcon", "pant", "pact", "ppas", "aglt", "ger"]):
        return "verb"
    if any(tag in pos for tag in ["adv"]):
        return "adverb"
    if any(tag in pos for tag in ["prep"]):
        return "preposition"
    if any(tag in pos for tag in ["conj", "comp"]):
        return "conjunction"
    return "unknown"

# Function to clean the base form by removing extra morphological attributes
def clean_base_form(base_form):
    # Remove extra attributes (anything after a colon or tilde)
    clean_form = re.split(r'[:~]', base_form)[0]
    return clean_form.lower()

# Use Morfeusz 2 to get all base forms and their parts of speech
def get_base_forms_morfeusz(word):
    morf = morfeusz2.Morfeusz()
    analyses = morf.analyse(word.lower())
    results = []
    for analysis in analyses:
        base_form = analysis[2][1]
        base_form = clean_base_form(base_form)
        pos = analysis[2][2]
        major_pos = map_pos_to_category(pos)
        results.append((base_form, major_pos))
    return results

# Analyze words
def analyze_words(words):
    results = []
    for word in words:
        # Get all base forms and major POS using Morfeusz 2
        analyses = get_base_forms_morfeusz(word)
        for base_form, pos in analyses:
            print(f"Initial word: {word}, Base Form: {base_form}, POS: {pos}")  # Debugging output
            results.append([word.lower(), base_form, pos])
    return results
