def process_file(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            data = infile.readlines()

        processed_data = [line.strip().upper() for line in data]  # Example processing: convert to uppercase

        with open(output_file, 'w') as outfile:
            for line in processed_data:
                outfile.write(line + '\n')

        print(f"Processed data written to {output_file}")
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
process_file('input.txt', 'output.txt')
