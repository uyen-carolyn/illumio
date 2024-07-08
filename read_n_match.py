import sys


def load_words(input_file):
    """Load file and put words into a set."""
    predefined_words = set()
    with open(input_file, 'r') as file:
        for line in file:
            word = line.strip()
            if word:
                predefined_words.add(word)
    return predefined_words


def find_matches(input_file, predefined_words):
    """Find matches from file against predefined words."""
    matches = []
    with open(input_file, 'r') as file:
        for line in file:
            word = line.strip()
            if word in predefined_words:
                matches.append(word)
    return matches


def main():
    if len(sys.argv) != 3:
        print("Usage: python read_n_match.py <words_file.txt> <input_file.txt>")
        sys.exit(1)

    words_file = sys.argv[1]
    input_file = sys.argv[2]

    # Load predefined words
    predefined_words = load_words(words_file)

    # Find matches in the input file
    matches = find_matches(input_file, predefined_words)

    # Output the matches
    print(f"Found {len(matches)} Matches:")
    for match in matches:
        print(match)


if __name__ == "__main__":
    main()