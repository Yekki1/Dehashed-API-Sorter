import sys

def insert_newline_before_sequence(input_file, output_file, sequence):
    try:
        with open(input_file, 'r') as infile:
            content = infile.read()
            modified_content = content.replace(sequence, '\n' + sequence)

        with open(output_file, 'w') as outfile:
            outfile.write(modified_content)

        print(f"New line inserted before '{sequence}'. Output saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file_path> <output_file_path>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    character_sequence = ",{"

    insert_newline_before_sequence(input_file_path, output_file_path, character_sequence)
