import jieba
import os

jieba.load_userdict('./mydict.txt') #載入自定義詞典

path ='./res2'
file_list = os.listdir(path)
#print(file_list)

all_article_string = ''
for each_article in file_list:
    article_path = path + '/'+ each_article
    with open (article_path, 'r', encoding='utf-8') as f:
        tmp_article_string = f.read().split('\n')[1:] #不要作者資訊(split後為一行一行的)
    for article_line in tmp_article_string:
        all_article_string += article_line + '\n'

print(all_article_string)

#計算每個詞出現幾次

s_list = jieba.cut(all_article_string) 
word_count = {}
for i in s_list:
    if i in word_count:
        word_count[i] += 1
    else:
        word_count[i] = 1

#創建停用字詞然後匯入    
stopword_path ='./stopword.txt'
stopword_list =[]
with open (stopword_path, 'r', encoding='utf-8') as f:
    for i in f.readlines():
       stopword_list.append(i.replace('\n',''))

word_list = [(k,word_count[k]) for k in word_count if len(k) >1 and k not in stopword_list]


word_list.sort(key = lambda x :x[1],reverse = True)
#用lambda指定排序依據，每一個元組視為x，針對x[1]進行降冪排序
print(word_list)