# 第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

from os.path import abspath;

path = abspath(__file__ + '/../../../asserts/filtered_words.txt')

filterd_words = set();

with open(path, mode='r', encoding='utf-8') as fObj:
    # TODO 优化大文件读取性能
    for line in fObj:
        filterd_words.add(line.strip())


print("请输入词语进行检测 如要退出请输入Exit")



while(True):
    word = input("请输入一个词语 并回车: ")
    if (word == 'Exit'):
        break
    if (word in filterd_words):
        print("Freedom")
    else:
        print("Human Rights")