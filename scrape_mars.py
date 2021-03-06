#import dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
import os
import pandas as pd
import time
from selenium import webdriver

def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless = False)

def scrape():
    browser = init_browser()
    mars_facts_data = {}

    url = "https://mars.nasa.gov/news/"
    browser.visit(url) 
    time.sleep(2)

    html = browser.html
    soup = bs(html,"html.parser")

    #scrapping latest news about Mars from NASA
    news_title = soup.find("div",class_="content_title").text
    news_paragraph = soup.find("div", class_="article_teaser_body").text
    mars_facts_data['news_title'] = news_title
    mars_facts_data['news_paragraph'] = news_paragraph
    
    #Mars Featured Image
    url_image = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url_image)
    time.sleep(2)

    from urllib.parse import urlsplit
    base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(url_image))
    
    xpath = "//*[@id=\"page\"]/section[3]/div/ul/li[1]/a/div/div[2]/img"

    #Use splinter to click on the mars featured image
    #to bring the full resolution image
    results = browser.find_by_xpath(xpath)
    img = results[0]
    img.click()
    time.sleep(2)
    
    #image url 
    html_image = browser.html
    soup = bs(html_image, "html.parser")
    img_url = soup.find("img", class_="fancybox-image")["src"]
    featured_img_url = base_url + img_url
    mars_facts_data["featured_image"] = featured_img_url
    
    #Mars Weather

    #Mars weather's latest tweet from the website
    mars_weather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(mars_weather_url)
    mars_weather_html = browser.html
    mars_weather_soup = bs(mars_weather_html, 'html.parser')

    tweets = mars_weather_soup.find('ol', class_='stream-items')
    mars_weather = tweets.find('p', class_="tweet-text").text
    mars_facts_data["mars_weather"] = mars_weather

    #Mars Facts

    mars_facts_url = "https://space-facts.com/mars/"
    time.sleep(2)
    table = pd.read_html(mars_facts_url)
    table[0]

    df_mars_facts = table[0]
    df_mars_facts.columns = ["Parameter", "Values"]
    clean_table = df_mars_facts.set_index(["Parameter"])
    mars_html_table = df_mars_facts.to_html()
    mars_html_table = mars_html_table.replace("\n", "")
    mars_facts_data["mars_facts_table"] = mars_html_table

    #Mars Hemisperes

    mars_hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(mars_hemispheres_url)

    #base url
    hemisphere_base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(mars_hemispheres_url))
    hemisphere_img_urls = []
    hemisphere_img_urls

    #Cerberus Hemisphere
    hemisphere_img_urls = []
    results = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[1]/a/img").click()
    time.sleep(2)
    cerberus_open_click = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
    time.sleep(1)
    cerberus_image = browser.html
    soup = bs(cerberus_image, "html.parser")
    cerberus_url = soup.find("img", class_="wide-image")["src"]
    cerberus_img_url = hemisphere_base_url + cerberus_url
    #print(cerberus_img_url)
    cerberus_title = soup.find("h2",class_="title").text
    #print(cerberus_title)
    back_button = browser.find_by_xpath("//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").click()
    cerberus = {"image title":cerberus_title, "image url": cerberus_img_url}
    hemisphere_img_urls.append(cerberus)

    #Schiaparelli Hemisphere
    results1 = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[2]/a/img").click()
    time.sleep(2)
    schiaparelli_open_click = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
    time.sleep(1)
    schiaparelli_image = browser.html
    soup = bs(schiaparelli_image, "html.parser")
    schiaparelli_url = soup.find("img", class_="wide-image")["src"]
    schiaparelli_img_url = hemisphere_base_url + schiaparelli_url
    #print(schiaparelli_img_url)
    schiaparelli_title = soup.find("h2",class_="title").text
    #print(schiaparelli_title)
    back_button = browser.find_by_xpath("//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").click()
    schiaparelli = {"image title":schiaparelli_title, "image url": schiaparelli_img_url}
    hemisphere_img_urls.append(schiaparelli)

    #Syrtis Major Hemisphere
    results1 = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[3]/a/img").click()
    time.sleep(2)
    syrtis_major_open_click = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
    time.sleep(1)
    syrtis_major_image = browser.html
    soup = bs(syrtis_major_image, "html.parser")
    syrtis_major_url = soup.find("img", class_="wide-image")["src"]
    syrtis_major_img_url = hemisphere_base_url + syrtis_major_url
    #print(syrtis_major_img_url)
    syrtis_major_title = soup.find("h2",class_="title").text
    #print(syrtis_major_title)
    back_button = browser.find_by_xpath("//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").click()
    syrtis_major = {"image title":syrtis_major_title, "image url": syrtis_major_img_url}
    hemisphere_img_urls.append(syrtis_major)

    #Valles Marineris Hemisphere
    results1 = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[4]/a/img").click()
    time.sleep(2)
    valles_marineris_open_click = browser.find_by_xpath( "//*[@id='wide-image-toggle']").click()
    time.sleep(1)
    valles_marineris_image = browser.html
    soup = bs(valles_marineris_image, "html.parser")
    valles_marineris_url = soup.find("img", class_="wide-image")["src"]
    valles_marineris_img_url = hemisphere_base_url + syrtis_major_url
    #print(valles_marineris_img_url)
    valles_marineris_title = soup.find("h2",class_="title").text
    #print(valles_marineris_title)
    back_button = browser.find_by_xpath("//*[@id='splashy']/div[1]/div[1]/div[3]/section/a").click()
    valles_marineris = {"image title":valles_marineris_title, "image url": valles_marineris_img_url}
    hemisphere_img_urls.append(valles_marineris)

    mars_facts_data["hemisphere_img_url"] = hemisphere_img_urls

    return mars_facts_data