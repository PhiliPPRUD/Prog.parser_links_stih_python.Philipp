import requests
from bs4 import BeautifulSoup

f = open("output.txt", "w")

resp_a = requests.get("https://stihibase.ru/author/")
alltext_a = resp_a.text

soup = BeautifulSoup(alltext_a, "html.parser")
kol_a = 0
mas_links_a_a = soup.find_all("a")

mas_links_a = []
for links_a1 in mas_links_a_a:
    links_a = links_a1.get("href")
    if "/author/" in links_a and links_a.count("/") == 4 and links_a not in mas_links_a:
        kol_a += 1
        mas_links_a.append(links_a)
        #print(kol_a, links_a)

        resp_s = requests.get("https://stihibase.ru" + links_a)
        alltext_s = resp_s.text

        soup = BeautifulSoup(alltext_s, "html.parser")

        kol_s = 0
        mas_links_s_a = soup.find_all("a")
        
        for links_s1 in mas_links_s_a:
            links_s = links_s1.get("href")
            if links_s.count("/") == 5:
                kol_s += 1
                #print(kol_s, links_s)
                f.write(links_s + "\n")
f.close()
f = open("output.txt", "r")
mas = f.readlines()
print(len(mas))
