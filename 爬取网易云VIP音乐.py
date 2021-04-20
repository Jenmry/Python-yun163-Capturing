#!usr/bin/python
# -*- coding = utf-8 -*-
"""
@author: Jenmry
@time: 2021/3/18
@tool: Pycharm2020.3
"""
from urllib.parse import quote
import requests
import random
import json

User_Agent_list = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
    'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB7.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.33 Safari/534.3 SE 2.X MetaSr 1.0',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E) QQBrowser/6.9.11079.201',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)'
]
headers = {
    'cookie': 'kg_mid=6762a790f22d97d93e44e5807cbbc924; kg_dfid=2SoVtz3x77dH16qdc53GLKZE; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1614760346,1615902258,1615906322,1615992629; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1615992636',
    'User-Agent': random.choice(User_Agent_list),
    'referer': 'https://www.kugou.com/song/'
}
print('****************************')
print('本程序将为您免费下载网易云全网音乐')
print('****************************')
musicName = input('请输入歌曲名字或歌手名字：')
encodName = quote(musicName)
url1 = 'http://music.163.com/api/search/get/web?csrf_token=hlpretag=&hlposttag=&s={}&type=1&offset=0&total=true&limit=20'.format(encodName)
response1 = requests.get(url1, headers)
dict1 = json.loads(response1.text)
songName = []
idNumber = []
singerName = []
lists = dict1['result']['songs']
for i in range(len(lists)):
    singerName.append(lists[i]['artists'][0]['name'])
    songName.append(lists[i]['name'])
    idNumber.append(lists[i]['id'])
    print(f'【{i + 1}】-------------->{songName[i]}--{singerName[i]}')
# print(len(singerName), singerName)
# print(len(songName), songName)
# print(len(idName), idName)
# print(idNumber)
path = input('请输入你要保存的路径：')
print("""下载单首歌曲请输入 1
下载多首歌曲请输入 2""")
choice = int(input('请输入：'))
if choice == 1:
    songNumber = int(input('请输入你要下载的歌曲的序号：'))
    play_url = f'http://music.163.com/song/media/outer/url?id={idNumber[songNumber - 1]}.mp3'
    # print(play_url)
    response2 = requests.get(play_url, headers=headers)
    # print(response2.content)
    with open(f'{path}//{songName[songNumber - 1]}-{singerName[songNumber - 1]}.mp3', 'wb') as f:
        print(f'{songName[songNumber - 1]}-{singerName[songNumber - 1]}正在下载中......................')
        # sleep(2)
        f.write(response2.content)
        f.close()
if choice == 2:
    pageNumber = int(input('请输入你要下载到第几首：'))
    for i in range(pageNumber):
        play_url = f'http://music.163.com/song/media/outer/url?id={idNumber[i]}'
        response2 = requests.get(play_url, headers=headers)
        with open(f'{path}//{songName[i]}-{singerName[i]}.mp3', 'wb') as f:
            print(f'{songName[i]}-{singerName[i]}正在下载中..........................')
            f.write(response2.content)
            f.close()
print('歌曲下载完成')
