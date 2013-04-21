from rottentomatoes import RT
import json



r = RT('c6nttc6uvr4pr6ewr996p6yt').search('Toy Story 3')
w = r[0]
critics = w['critics_consensus']
synopsis = w['synopsis']
word_list = critics + synopsis

print word_list




file = open('RT.txt', 'w')
file.write(str(r))
file.close()




