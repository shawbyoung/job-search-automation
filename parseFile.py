def firstParse(filename):
    with open('./unparsed/'+ filename + '.txt') as in_f:
        lines =  in_f.readlines()

    newlines = []
    flag = False

    for i in range(len(lines)):
        if flag:
            #hardcoding formatting
            lines[i] = lines[i].replace('\n','')
            lines[i] = lines[i].replace('<br>','')
            lines[i] = lines[i].replace('<\br>','')
            lines[i] = lines[i].replace('<p>','')
            lines[i] = lines[i].replace('<\p>','')
            lines[i] = lines[i].replace('&amp;','')
            newlines.append(lines[i])
            flag = False
        if lines[i] == '\n':
            flag = True

    with open( './parsed/' + filename + '.txt', 'w') as out_f:
        for line in newlines:
            out_f.write(f"{line}\n")

    print(filename, ' Parsed')