import numpy as np
import pandas as pd
import httplib2
from bs4 import BeautifulSoup
import urllib.request
#from tqdm import tqdm
import os


folders = os.listdir('links/')
for i in folders:
    cnt = 0
    img_url_strs = []
    img_url = pd.read_csv('links/'+i)
    img_url_str = img_url.applymap(str)
    for index in range(img_url.shape[0]):
        # 发现链接只能是str类型，list不可以
        img = urllib.request.urlopen(img_url_str.iloc[index, 0]).read()
        with open("files/{}/{}.jpg".format(i[0:-4], i[0:-4] + '_' + str(cnt)), "wb") as out:
            print("download folders:{},index:{},length:{},link:{}".format(i[0:-4], index,
                                                                      img_url.shape[0],
                                                                      img_url_str.iloc[index, 0]))
            out.write(img)
        cnt += 1

print("finished!!!")