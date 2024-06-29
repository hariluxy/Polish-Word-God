import os

# Load words from a text file
def load_words_from_file(word_file):
    with open(word_file, 'r', encoding='utf-8') as file:
        words = [line.strip() for line in file.readlines()]
    return words

# Save results to separate files based on POS categories
def save_results_to_files(results, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save all results to total.txt
    total_file_path = os.path.join(output_dir, "total.txt")
    with open(total_file_path, 'w', encoding='utf-8') as total_file:
        unique_results = set()
        for result in results:
            initial_word, base_form, pos = result
            if (initial_word, base_form, pos) not in unique_results:
                unique_results.add((initial_word, base_form, pos))
                total_file.write(f"{initial_word};{base_form};{pos}\n")

    categorized_results = {}
    for result in results:
        initial_word, base_form, pos = result
        if pos not in categorized_results:
            categorized_results[pos] = []
        if base_form not in categorized_results[pos]:
            categorized_results[pos].append(base_form)  # Only store the base form

    for category, items in categorized_results.items():
        file_name = "unknown.txt" if category == "unknown" else f"{category}.txt"
        file_path = os.path.join(output_dir, file_name)
        with open(file_path, 'w', encoding='utf-8') as file:
            for item in items:
                file.write(f"{item}\n")
