import morfeusz2
import re

# Map detailed POS tags to major categories
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

# Clean the base form by removing extra morphological attributes
def clean_base_form(base_form):
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
        classification = analysis[2][3]  # Get classification list
        results.append((base_form, major_pos, pos, classification))
    return results

# Analyze words and ensure unique results, excluding specific types
def analyze_words(words):
    unique_results = set()
    results = []
    
    excluded_classifications = ["nazwa_geograficzna", "imię", "nazwisko", "nazwa_organizacji"]
    
    for word in words:
        analyses = get_base_forms_morfeusz(word)
        for base_form, major_pos, full_pos, classification in analyses:
            # Check if the word has any of the excluded classifications
            if any(tag in classification for tag in excluded_classifications):
                continue  # Skip this word
            
            if (base_form, major_pos) not in unique_results:
                unique_results.add((base_form, major_pos))
                print(f"Initial word: {word}, Base Form: {base_form}, POS: {major_pos}, Full POS: {full_pos}, Classification: {classification}")
                results.append([word.lower(), base_form, major_pos])
    
    return results
