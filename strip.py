import os

print('Type File Name (foobar.txt):')
file = input()
path = os.getcwd()
name = path+'/'+file
#print(name)
with open(name) as infile, open('strip.txt', 'w') as outfile:
    for line in infile:
        if not line.strip(): continue  # skip the empty line
        outfile.write(line.replace('"', '').replace(' - ', '/').replace('.flac', ''))  # non-empty line. Write it to output
