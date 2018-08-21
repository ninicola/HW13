from splinter import Browser
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import time

# Initialize browser
def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape ():
  #return data as dictory
   #mars_info={}
  #mars news url  
   url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
   #define browser
   browser=init_browser()
   browser.visit(url)
   time.sleep(5)
   #latest_news
   html = browser.html
   soup = BeautifulSoup(html, 'html.parser')
   news_all = soup.find('div', class_='content_title')
   p_all = soup.find('div', class_='article_teaser_body')
   latest_news_title = news_all.text
   latest_news_p = p_all.text
   base_news_url = 'https://mars.nasa.gov'
   latest_news = base_news_url+news_all.a['href']
   #Feature images
   url2='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
   browser.visit(url2)
   time.sleep(5)

   jpl_html=browser.html
   jpl_soup=BeautifulSoup(jpl_html,'html.parser')

   image_fea1 = jpl_soup.find('a', class_='fancybox')
  #feathured_image_url show all the feature image url in one page
  
   base_nasa_url = 'https://www.jpl.nasa.gov'
   featured_image_url = base_nasa_url+image_fea1['data-fancybox-href']
   #featured_image_url
  #print out all the feaure image url
  #featured_image_url
#    mars_info['Feature_image_url']=featured_image_url
  # Mars Weather
  # Visit the Mars Weather twitter account https://twitter.com/marswxreport?lang=en and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather report as a variable called mars_weather.
   url_weather='https://twitter.com/marswxreport?lang=en'
   browser.visit(url_weather)
   time.sleep(5)
   tweet_html=browser.html
   tweet_soup=BeautifulSoup(tweet_html,'html.parser')
   mar_weather_f=tweet_soup.find('p',class_='TweetTextSize')
   mar_weather=mar_weather_f.text
#    mars_info['mars_weather']=mar_weather
   url_t='https://space-facts.com/mars/'
   tables=pd.read_html(url_t)
   tables
   df=tables[0]
   df.columns=['Facts','Value']
   new_df=df.set_index(['Facts'])
   html_table_u=new_df.to_html()
   
  #strp unwanted newlines to clean up the table
   html_table_u = html_table_u.replace('\n', '')
   html_table_u

  #save the table directly to a file
   new_df.to_html('mars_fact.html')
#    mars_info['html_table'] = html_table_u

  # # Mars Hemispheres
  # Visit the USGS Astrogeology site https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars to obtain high resolution images for each of Mar's hemispheres.
  # You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
  # Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
  # Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

   url_mars_hemi='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
   browser.visit(url_mars_hemi)
   time.sleep(5)
  #create beautiful soup
   mars_hemi_html=browser.html
   mar_hemi_soup=BeautifulSoup(mars_hemi_html,'html.parser')
   mar_hemi_soup.find_all('div',class_='item')
  #a[0].a['href']
   dv_mar_hemi=mar_hemi_soup.find_all('div',class_='item')
  #dv_mar_hemi[0].a['href']

  #    cccc=mar_hemi_soup.find_all('h3')

  #    cccc[0].text.strip('Enhanced')



  # found the url of  high resolution img
   base_url_hei='https://astrogeology.usgs.gov'
   mar_hemi_img_src=[]
  #get the full image src based on the href
   for i in range(len(dv_mar_hemi)):
       hemi_list=base_url_hei+dv_mar_hemi[i].a['href']
       mar_hemi_img_src.append(hemi_list)
   mar_hemi_img_src
   #create a lit hh to hold the title and img utl
   hh=[]
   for i in range(len(mar_hemi_img_src)):
       dv_mar_hemi=mar_hemi_soup.find_all('h3')
       mm_url=mar_hemi_img_src[i]
       browser.visit(mm_url)
       mm_html=browser.html
       mar_mm_soup=BeautifulSoup(mm_html,'html.parser')
       cc=mar_mm_soup.find('div',class_='downloads')
       dd=cc.find('li').a['href']
       #create a dic
       row={}
       row['title']=dv_mar_hemi[i].text.strip('Enhanced')
       row['img_url']=dd
       hh.append(row)

#    store in a dictory
   mars_info={
       "news_title": latest_news_title,
       "new_p": latest_news_p,
       "la_news_url": latest_news,
       "Feature_image_url": featured_image_url,
       "mars_weather": mar_weather,
       "html_table": html_table_u,
       "Hemi_image_url": hh
   }
   
   browser.quit()
   return mars_info

