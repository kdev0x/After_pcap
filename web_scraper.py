# importing packages
from requests_html import HTMLSession
import numpy as np
session = HTMLSession()
# get url
url = input('Please enter url: ')
r = session.get(url)

r.html.render(sleep = 1)

articles = r.html.find('article')
# function to scrape the article
def get_article_info():
    newslist = []

    for item in articles:
        
        newsitem = item.find('h3' , first = True)
        news_article = {

        "title": newsitem.text,
        "link" : newsitem.absolute_link
            }
        newslist.append(news_article)
    
        
    print(newslist)
    return newslist
# calliung the function and saving the output to csv file 
try:
    article = get_article_info()
    article_output = np.array(article)
    article_output.to_csv('save_data.csv')

    
    session.close()

# checking Expectaions
except Exception as e:
    print(e)
