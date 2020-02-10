# jsonlines validator with utf-8

import json, os, codecs

# get a list of jsonfiles in the directory this code is in
filenames = [file for file in os.listdir() if file.endswith('.json')]

# collect bad line info here
badLines = list()

# iterate through files
print('Iterating through ', len(filenames), ' files:')
for file in filenames:
    print('Reading file', file)
    with codecs.open(file, 'r', encoding='utf-8', errors='replace') as f:
        linenum = 0
        for line in f.readlines():
            linenum+=1
            try:
                json.loads(line)
            except:
                print(file, f'Line {linenum} CORRUPTED!')
                badLines.append((file, linenum))

# write a file with all the bad file info 
with codecs.open('bad_lines.txt', 'a', encoding='utf-8', errors='replace') as sf:
    for i in badLines:
        sf.write(i[0]+' line 'str(+i[1]))

print('Done!')
