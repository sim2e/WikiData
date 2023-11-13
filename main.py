import wikipediaapi
import pandas as pd
import numpy as np
import csv
from queue import Queue

wiki_en = wikipediaapi.Wikipedia('SoftwareEntireDesign_wiki', 'en')


page_py_en = wiki_en.page("Computational_complexity_theory")
print("Computational_complexity_theory" + " Page - Exists: %s" % page_py_en.exists())
# print(page_py_en.backlinks)

f = open("iter0/Computational_complexity_theory",'w+')
f.write(page_py_en.text)
f.close()

links = page_py_en.links
queue = Queue()
for title in sorted(links.keys()):
    queue.put(title)

# 해싱 셋 활용해서 중복 조사, 연결 할 때 설정 조정, 큐에 얼마나 남았는지 디버그 로그 출력 해야합니다.
next_queue = Queue()
iter = 1
visitedPage = [];
while(iter < 3):
    while(not queue.empty()):
        title = queue.get()
        print("Left Links: %s" % queue.qsize())
        if (title not in visitedPage):
            page_py_en = wiki_en.page(title)
            print(title + " Page - Exists: %s" % page_py_en.exists())
            if (page_py_en.exists()):
                visitedPage.append(title)

                if "/" not in title:
                    f = open("iter" + str(iter) + "/" + title,'w+')
                    f.write(page_py_en.text)
                    f.close()

                links = page_py_en.links
                for title in sorted(links.keys()):
                    next_queue.put(title)
    queue = next_queue
    iter = iter + 1

f = open("visitedPage",'w+')
f.write("\n".join(visitedPage))
f.close()
