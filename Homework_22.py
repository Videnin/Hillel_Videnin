def read_last(file_path, symbol_number):
    with open(file_path, 'r') as f:
        for line in f:
            line = line.rstrip()
            if line:
                print(line[-symbol_number:])

