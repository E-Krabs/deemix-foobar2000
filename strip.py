print('File name (foobar.txt):')
file = input()
with open(file) as infile, open('foobar.txt', 'w') as outfile:
    for line in infile:
        if not line.strip(): continue  # skip the empty line
        outfile.write(line)  # non-empty line. Write it to output
