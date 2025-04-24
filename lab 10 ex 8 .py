with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        words = line.split()
        new_line = ' '.join(word for word in words if word.lower() not in ['a', 'the'])
        outfile.write(new_line + "\n")
