import requests
import time
from bs4 import BeautifulSoup

def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return "ERROR"

def get_content(url):
    # analysis tieba web file
    comments = []   #initialize a list to save post
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    liTags = soup.find_all('li', attrs={'class': ' j_thread_list clearfix'})
    for li in liTags:
        comment = {}
        try:
            comment['title'] = li.find('a', attrs={'class': 'j_th_tit '}).text.strip()
            comment['link'] = "http://tieba.baidu.com/" + li.find('a', attrs={'class': 'j_th_tit '})['href']
            comment['name'] = li.find('span', attrs={'class': 'tb_icon_author '}).text.strip()
            comment['time'] = li.find('span', attrs={'class': 'pull-right is_show_create_time'}).text.strip()
            comment['replyNum'] = li.find('span', attrs={'class': 'threadlist_rep_num center_text'}).text.strip()
            comments.append(comment)

        except:
            print("there is a mistake")
    return comments

def Out2File(dict):
    with open('TTBT.txt', 'a+') as f:
        for comment in dict:
            f.write('title: {}\t link:{}\t author:{}\t time:{}\t reply:{}\n'.format(
                comment['title'],comment['link'],comment['name'],comment['time'],comment['replyNum']
            ))
        print("current page crawled done")

def main(base_url,deep):
    url_list=[]
    for i in range(0,deep):
        url_list.append(base_url + '&pn='+str(50*i))
    print('all web page has download local, starting filte')

    for url in url_list:
        content = get_content(url)
        Out2File(content)
    print('all info has saved done')

base_url = 'https://tieba.baidu.com/f?kw=%E8%A5%BF%E9%83%A8%E4%B8%96%E7%95%8C&ie=utf-8&pn=50'
deep = 1

if __name__=='__main__':
    main(base_url, deep)