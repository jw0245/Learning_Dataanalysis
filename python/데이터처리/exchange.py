#!/usr/bin/env python
# coding: utf-8

# In[2]:


# '''
# 환율정보
# - 새로운 파일 생성
# - 달라, 엔화 추출해서 DB에 저장
# - DB명 : aidb
# - 테이블명 : exchange
# 	컬럼명 : dollar, yen (varchar)
# '''


# In[3]:


import urllib.request as req
from bs4 import BeautifulSoup


# In[5]:


res = req.urlopen('https://finance.naver.com/marketindex/')
soup = BeautifulSoup(res, 'html.parser')
dollar = soup.select_one('#exchangeList > li > a.head.usd > div > span.value')
yen = soup.select_one('#exchangeList > li > a.head.jpy > div > span.value')
#dollar.string,yen.string


# In[6]:


import pymysql


# In[13]:


# float으로 형변환
dollar_float = float(dollar.string.replace(',',''))
yen_float = float(yen.string.replace(',',''))
#dollar_float, yen_float


# In[15]:


conn = pymysql.connect(host='localhost', user='aiuser', password='ai1234', 
                       db='aidb', charset='utf8')
cur = conn.cursor()
sql = "insert into exchange (dollar, yen, getdate) values ({}, {}, now())".format(dollar_float, yen_float)
cur.execute(sql)
conn.commit()


# In[ ]:




