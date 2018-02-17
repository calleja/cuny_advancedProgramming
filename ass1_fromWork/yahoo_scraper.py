#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
class that pulls Yahoo's data via BS4

div id = "quote-header-info" class = "quote-header-section"

div class="D(ib) Mend(20px)"
(grab the text from the below class)
span class = "Trsdu(0.3s) Fw(b) Mb(-4px) D(ib)"

'span' and 'div' are the attributes
"""
from bs4 import BeautifulSoup as bs
import requests as re
import re as regex

#stock1 CPT
cpt='https://finance.yahoo.com/quote/CPT?p=CPT'
#Visa
'https://finance.yahoo.com/quote/V?p=V'
#Con Edison
'https://finance.yahoo.com/quote/ED?p=ED'


cpt_pg=re.get(cpt)
cpt_html=cpt_pg.text
cpt_soup = bs(cpt_html,'html.parser')


quote1=cpt_soup.find_all('div','data-test')

#this works
quote=cpt_soup.find_all('div',{'id':'quote-header'})

quote2=cpt_soup.find({'data-test':'quote-summary-stats'})

print(quote)
len(quote)

quote[0].find({'data-test':'quote-summary-stats'})

result_list=[]
for i in quote:
    #print(i)
    result_list.append(i.find('td',{'data-test':'ASK-value'}))
    
result_list2=[]
for i in quote:
    #print(i)
    result_list2.append(i.find('td',{'data-test':'ASK-value'}).get_text())
    result_list2.append(i.find('td',{'data-test':'BID-value'}).get_text())

len(result_list2)
result_list2[0]
result_list2[1]
print(result_list2)

for i in result_list2:
    price=regex.search(r'.*?(?: )',i)
    print(float(price.group(0)))




#similar to a list... find_all searches through all the tags in the document... my target tags are compound in nature: having a tag name and an element/attribute name: div and class; and span and class
div_list=cpt_soup.find_all('div')
#print all the children of the tag with the contents attribute... this returns a list
div_list[90].contents
#print the number of children under that tag
len(div_list[90].contents)
#children attribute iteration... like a list
[g.name for g in div_list[90].contents]
#looking for a particular tag/attribute/element called 'class' with a particular name "quote-header-section"
def has_div_class(tag):
    return tag.has_attr('class') and tag.name=='div' 

#this works
div_class=cpt_soup.find_all(has_div_class)

#search the class attribute for some text and regex.search("quote-header-section").search(class)

def class_name(class_):
    return regex.search("quote-header-section").search(class_)

quote=cpt_soup.find_all(class_='quote-header-section')
#from the above, only want span class = "Trsdu(0.3s) Fw(b) Mb(-4px) D(ib)"
quote[0]
type(quote[0]) #this is a bs4.element.tag
quote[0].find_all(class_='D(ib) Mend(20px)')
quote[0].has_attr('class')
len(quote[0])

result_list=[]
for i in quote[0]:
    #if 'Trsdu(0.3s)' in i.class_:
    if i.find_all('span',class_='Trsdu(0.3s)'):
        #select for only the element I need
        result_list.append(i.contents)
        
for i in result_list[0]:
    print(i.name)
    
[g.text for g in result_list[0]]
result_list[0].text
def has_trs_class(class_):
     #trs=regex.compile('Trsdu(0.3s)')
     return regex.search('Trsdu(0.3s)',class_)
     #return regex.compile('Trsdu(0.3s)').search(class_)
    
cpt_trs=quote[0].find_all(class_=has_trs_class)
#the string one the right side of the equal sign need not be the entire value
cpt_soup.find_all(class_='Trsdu(0.3s)')
regex.compile('Trsdu(0.3s)').search(quote[0])
        
price=cpt_soup.find_all(class_='Trsdu(0.3s) Fw(b) Mb(-4px) D(ib)')


type(g) # g is a tag... tags have a lot o attributes and methods; learn more in "Navigating the Tree" and "Searching the Tree"

#the div tag will contain other tags of which 'class' is one
g.

cpt_soup.span['class']
cpt_soup.span

#first, pull the entire page:
