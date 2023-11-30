#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import pandas as pd 
from selenium.webdriver.common.by import By

import requests
import time
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException


# # Question 1 solution
# 

# In[181]:


driver=webdriver.Chrome()


# In[182]:


driver.get('https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos')


# In[183]:


#fetching all the details
videoname=[]
artist=[]
date=[]
views=[]
try:
    vid=driver.find_elements(By.XPATH,'//table[@class="wikitable sortable jquery-tablesorter"]/tbody/tr/td[2]/a')
    for i in vid:
        videoname.append(i.text)
except NoSuchElementException:
    videoname.append('-')
topname=[]
topname=videoname[:30]
try:
    art=driver.find_elements(By.XPATH,'//table[@class="wikitable sortable jquery-tablesorter"]/tbody/tr/td[3]')
    for i in art:
        artist.append(i.text)
except NoSuchElementException:
    artist.append('-')
topartist=[]
topartist=artist[:30]
try:
    dt=driver.find_elements(By.XPATH,'//table[@class="wikitable sortable jquery-tablesorter"]/tbody/tr/td[5]')
    for i in dt:
        date.append(i.text)
except NoSuchElementException:
    date.append('-')
topdata=[]
topdate=date[:30]

try:
    views=[]
    vw=driver.find_elements(By.XPATH,'//table[@class="wikitable sortable jquery-tablesorter"]/tbody/tr/td[4]')
    for i in vw:
        views.append(i.text)
except NoSuchElementException:
    views.append('-')
topviews=[]
topviews=views[:30]


# In[63]:


print(len(topname),len(topartist),len(topdate),len(topviews))


# In[64]:


df=pd.DataFrame({'video name':topname,'artists':topartist,'date':topdate,'views':topviews})
df


# # Question 2 solution

# In[69]:


driver2=webdriver.Chrome()
driver2.get('https://www.bcci.tv/')


# In[72]:


#fixture btn
btn=driver2.find_element(By.XPATH,'//*[@id="imw-international-men"]/a[2]')
btn.click()


# In[83]:


#fetching details
series=[]
place=[]
date=[]
stime=[]
try:
    s=driver2.find_elements(By.XPATH,'//*[@id="match-card"]/div[1]/div/div/h5')
    for i in s:
        series.append(i.text)
except NoSuchelementException:
    series.append('-')
try:
    p=driver2.find_elements(By.XPATH,'//*[@id="match-card"]/div[2]/div[1]/span[1]')
    for i in p:
        place.append(i.text)
except NoSuchelementException:
    place.append('-')
try:
    d=driver2.find_elements(By.XPATH,'//*[@id="match-card"]/div[1]/div/div/div[2]/div[1]')
    for i in d:
        date.append(i.text)
except NoSuchelementException:
    date.append('-')
    
try:
    t=driver2.find_elements(By.XPATH,'//div[@class="match-time no-margin ng-binding"]')
    for i in t:
        stime.append(i.text)
except NoSuchelementException:
    stime.append('-')


# In[85]:


print(len(series),len(place),len(date),len(stime))


# # question 3 solution

# In[86]:


driver=webdriver.Chrome()
driver.get('https://statisticstimes.com/')


# In[93]:


economy_btn=driver.find_element(By.XPATH,'//*[@id="top"]/div[2]/div[2]')
economy_btn.click()


# In[94]:


india_btn=driver.find_element(By.XPATH,'//*[@id="top"]/div[2]/div[2]/div/a[3]')
india_btn.click()


# In[95]:


state_wise_btn=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/ul/li[1]/a')
state_wise_btn.click()


# In[101]:


rank=[]
state=[]
GSDP1=[]
GSDP2=[]
share=[]
GDP=[]

try:
    rnk=driver.find_elements(By.XPATH,'//table[@id="table_id"]/tbody/tr/td[1]')
    for i in rnk:
        rank.append(i.text)
except NoSuchelementException:
    rank.append('-')
try:
    st=driver.find_elements(By.XPATH,'//table[@id="table_id"]/tbody/tr/td[2]')
    for i in st:
        state.append(i.text)
except NoSuchelementException:
    state.append('-')
try:
    g1=driver.find_elements(By.XPATH,'//table[@id="table_id"]/tbody/tr/td[3]')
    for i in g1:
        GSDP1.append(i.text)
except NoSuchelementException:
    GSDP1.append('-')
try:
    g2=driver.find_elements(By.XPATH,'//table[@id="table_id"]/tbody/tr/td[4]')
    for i in g2:
        GSDP2.append(i.text)
except NoSuchelementException:
    GSDP2.append('-')
try:
    sh=driver.find_elements(By.XPATH,'//table[@id="table_id"]/tbody/tr/td[5]')
    for i in sh:
        share.append(i.text)
except NoSuchelementException:
    share.append('-')
try:
    gd=driver.find_elements(By.XPATH,'//table[@id="table_id"]/tbody/tr/td[6]')
    for i in gd:
        GDP.append(i.text)
except NoSuchelementException:
    GDP.append('-')


# In[102]:


print(len(rank),len(state),len(GSDP1),len(GSDP2),len(share),len(GDP))


# In[106]:


df=pd.DataFrame({'Rank':rank,'GSDP 18-19':GSDP2,'GSDP 19-20':GSDP1,'SHARE':share,'GDP':GDP})
df


# # question 4 solution

# In[114]:


driver=webdriver.Chrome()
driver.get('https://github.com/')


# In[115]:


btn1=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/header/div/div[2]/div/nav/ul/li[3]/button')
btn1.click()
trending_btn=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/header/div/div[2]/div/nav/ul/li[3]/div/div[3]/ul/li[2]/a')
trending_btn.click()


# In[127]:


title=[]
desc=[] 
count=[]
language=[]

try:
    t=driver.find_elements(By.XPATH,'//h2[@class="h3 lh-condensed"]')
    for i in t:
        title.append(i.text)
except NoSuchelementException:
    title.append('-')
try:
    d=driver.find_elements(By.XPATH,'//article[@class="Box-row"]/p')
    for i in d:
        desc.append(i.text)
except NoSuchelementException:
    desc.append('-')
try:
    c=driver.find_elements(By.XPATH,'//a[@class="Link Link--muted d-inline-block mr-3"][2]')
    for i in c:
        count.append(i.text)
except NoSuchelementException:
    count.append('-')
try:
    l=driver.find_elements(By.XPATH,'//div[@class="f6 color-fg-muted mt-2"]/span/span[2]')
    for i in c:
        language.append(i.text)
except NoSuchelementException:
    language.append('-')


# In[128]:


print(len(title),len(desc),len(count),len(language))


# # Question 5 solution

# In[175]:


driver=webdriver.Chrome()
driver.get('https://www.billboard.com/')


# In[ ]:


ham_btn=driver.find_element(By.XPATH,'//*[@id="main-wrapper"]/header/div/div[2]/div/div/div[1]/div[1]/button')
ham_btn.click()


# In[ ]:


topsongs_btn=driver.find_element(By.XPATH,'//*[@id="main-wrapper"]/div[9]/div/div/div/ul/li[1]/ul/li[2]/a')
topsongs_btn.click()


# In[ ]:


# fetching all information
sname=[]
artist=[]
lweek=[]
pweek=[]
wb=[]

try:
    songs=driver.find_elements(By.XPATH,'//ul[@class="lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max"]/li/h3')
    for i in songs:
        sname.append(i.text)
except NoSuchElementException:
    sname.append('-')

try:
    art=driver.find_elements(By.XPATH,'//li[@class="lrv-u-width-100p"]/ul/li[1]/span')
    for i in art:
        artist.append(i.text)
except NoSuchElementException:
    artist.append('-')
try:
    week1=driver.find_elements(By.XPATH,'//li[@class="lrv-u-width-100p"]/ul/li[4]/span')
    for i in week1:
        lweek.append(i.text)
except NoSuchElementException:
    lweek.append('-')
try:
    week2=driver.find_elements(By.XPATH,'//li[@class="lrv-u-width-100p"]/ul/li[5]/span')
    for i in week2:
        pweek.append(i.text)
except NoSuchElementException:
    pweek.append('-')
try:
    w=driver.find_elements(By.XPATH,'//li[@class="lrv-u-width-100p"]/ul/li[6]/span')
    for i in w:
        wb.append(i.text)
except NoSuchElementException:
    wb.append('-')


# In[ ]:


print(len(sname),len(artist),len(lweek),len(pweek),len(wb))


# In[143]:


df=pd.DataFrame({'SONG NAME':sname,'ARTIST':artist,'LAST WEEK':lweek,'PEEK RANK':pweek,'WEEKS ON BOARD':wb})
df


# # Question no 6 solution

# In[147]:


driver=webdriver.Chrome()
driver.get(' https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare')


# In[148]:


#fetching all the details
bookname=[]
author=[]
vsold=[]
publisher=[]
genre=[]

try:
    book=driver.find_elements(By.XPATH,'//table[@class="in-article sortable"]/tbody/tr/td[2]')
    for i in book:
        bookname.append(i.text)
except NoSuchElementException:
    bookname.append('-')

try:
    ath=driver.find_elements(By.XPATH,'//table[@class="in-article sortable"]/tbody/tr/td[3]')
    for i in ath:
        author.append(i.text)
except NoSuchElementException:
    author.append('-')
try:
    sold=driver.find_elements(By.XPATH,'//table[@class="in-article sortable"]/tbody/tr/td[4]')
    for i in sold:
        vsold.append(i.text)
except NoSuchElementException:
    vsold.append('-')
try:
    pub=driver.find_elements(By.XPATH,'//table[@class="in-article sortable"]/tbody/tr/td[5]')
    for i in pub:
        publisher.append(i.text)
except NoSuchElementException:
    publisher.append('-')
try:
    gen=driver.find_elements(By.XPATH,'//table[@class="in-article sortable"]/tbody/tr/td[6]')
    for i in gen:
        genre.append(i.text)
except NoSuchElementException:
    genre.append('-')


# In[149]:


print(len(bookname),len(author),len(vsold),len(publisher),len(genre))


# In[155]:


df=pd.DataFrame({'BOOK NAME':bookname,'AUTHOR':author,'VOLUME SOLD':vsold,'PUBLISHER':publisher,'GENRE':genre})
df


# 
# # Question 7 solution

# In[156]:


driver=webdriver.Chrome()
driver.get('https://www.imdb.com/list/ls095964455/')


# In[162]:


#fetching all the details
Name=[] 
Year=[] 
Genre=[] 
Runtime=[] 
Ratings=[] 
Votes=[]

try:
    name=driver.find_elements(By.XPATH,'//div[@class="lister-item-content"]/h3/a')
    for i in name:
        Name.append(i.text)
except NoSuchElementException:
    Name.append('-')

try:
    year=driver.find_elements(By.XPATH,'//div[@class="lister-item-content"]/h3/span[2]')
    for i in year:
        Year.append(i.text)
except NoSuchElementException:
    Year.append('-')
try:
    genre=driver.find_elements(By.XPATH,'//div[@class="lister-item-content"]/p/span[5]')
    for i in genre:
        Genre.append(i.text)
except NoSuchElementException:
    Genre.append('-')
try:
    runtime=driver.find_elements(By.XPATH,'//div[@class="lister-item-content"]/p/span[3]')
    for i in runtime:
        Runtime.append(i.text)
except NoSuchElementException:
    Runtime.append('-')
try:
    rating=driver.find_elements(By.XPATH,'//div[@class="ipl-rating-widget"]/div/span[2]')
    for i in rating:
        Ratings.append(i.text)
except NoSuchElementException:
    Ratings.append('-')
try:
    votes=driver.find_elements(By.XPATH,'//div[@class="lister-item-content"]/p[4]/span[2]')
    for i in votes:
        Votes.append(i.text)
except NoSuchElementException:
    Votes.append('-')


# In[165]:


df=pd.DataFrame({'Name':Name,'YEAR':Year,'GENRE':Genre,'RUNTIME':Runtime,'RATINGS':Ratings,'VOTES':Votes})
df


# # Question 8 Solution

# In[169]:


driver=webdriver.Chrome()
driver.get('https://archive.ics.uci.edu/')


# In[170]:


#fetching dataser button
dataset_btn=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/main/div/div[1]/div/div/div/a[1]')
dataset_btn.click()


# In[174]:


#fetching all the details
Dataset=[] 
Datatype=[]
Task=[] 
Attribtype=[] 
instances=[]
attribute=[]
Year=[]

try:
    data=driver.find_elements(By.XPATH,'//div[@class="relative col-span-8 sm:col-span-7"]/h2/a')
    for i in data:
        Dataset.append(i.text)
except NoSuchElementException:
    Dataset.append('-')

try:
    type=driver.find_elements(By.XPATH,'//div[@class="relative col-span-8 sm:col-span-7"]/p')
    for i in type:
        Datatype.append(i.text)
except NoSuchElementException:
    Datatype.append('-')
try:
    tsk=driver.find_elements(By.XPATH,'//div[@class="my-2 hidden gap-4 md:grid grid-cols-12"]/div[1]/span[1]')
    for i in tsk:
        Task.append(i.text)
except NoSuchElementException:
    Task.append('-')
try:
    attrib=driver.find_elements(By.XPATH,'//div[@class="col-span-3 flex items-center gap-2"][2]/span')
    for i in attrib:
        Attribtype.append(i.text)
except NoSuchElementException:
    Attribtype.append('-')
try:
    ins=driver.find_elements(By.XPATH,'//div[@class="col-span-3 flex items-center gap-2"][3]/span')
    for i in ins:
        instances.append(i.text)
except NoSuchElementException:
    instances.append('-')
try:
    att=driver.find_elements(By.XPATH,'//div[@class="col-span-3 flex items-center gap-2"][4]/span')
    for i in att:
        attribute.append(i.text)
except NoSuchElementException:
    attribute.append('-')
try:
    yr=driver.find_elements(By.XPATH,'//table[@class="col-span-full my-2 table sm:col-start-2"]/tbody/tr/td[3]')
    for i in yr:
        Year.append(i.text)
except NoSuchElementException:
    Year.append('-')


# In[179]:


df=pd.DataFrame({'DATA SET':Dataset,'TYPE':Datatype,'TASK':Task,'ATTRIBUTE TYPE':Attribtype,'INSTANCES':instances,'ATTRIBUTE':attribute})
df


# In[ ]:




