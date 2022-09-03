#file_name = "malhar_time.txt"
file_name = "text"

time_list = []
with open(file_name, 'r', encoding='utf-8',  errors='ignore') as f:
    for line in f:
        time = line.split("\n")[0].split("_")[1]
        time_list.append(time)
print(len(time_list))

file_name = "text_.txt"
sentence_list = []
with open(file_name, 'r', encoding='utf-8',  errors='ignore') as f:
    for line in f:
        word = line.split("\t")[1].split("\n")[0]
        sentence_list.append(word)
print(len(sentence_list))

file_name = "G_2.xml"
wfile = open(file_name, 'w+', encoding='utf-8')
i = 0
for j in range(len(sentence_list)):
	sentence = sentence_list[j]
	time = time_list[j]
	wfile.write("<line timestamp=\""+str(time)+"\" is_valid=\"1\">"+"\n")
	word = sentence.split(" ")
	for k in range(len(word)):
		wfile.write("<word timestamp=\"\" is_valid=\"1\">"+str(word[k])+"</word>"+"\n")
	wfile.write("</line>"+"\n")

