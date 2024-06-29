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
        for result in results:
            total_file.write(f"{result[0]};{result[1]};{result[2]}\n")

    categorized_results = {}
    for result in results:
        category = result[2]
        if category not in categorized_results:
            categorized_results[category] = []
        categorized_results[category].append(result[1])  # Only store the base form

    for category, items in categorized_results.items():
        file_name = "unknown.txt" if category == "unknown" else f"{category}.txt"
        file_path = os.path.join(output_dir, file_name)
        with open(file_path, 'w', encoding='utf-8') as file:
            for item in items:
                file.write(f"{item}\n")
