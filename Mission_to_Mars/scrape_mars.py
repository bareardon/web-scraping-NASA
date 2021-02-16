#!/usr/bin/env python
# coding: utf-8

# Import dependenices: BeautifulSoup, Pandas and Splinter 

from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd 
import time
import requests


# Set executable path and initialize Chrome Browser
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# Vist the NASA Mars News Site
url = "https://mars.nasa.gov/news/"
browser.visit(url)
time.sleep(2)


# HTML object
html = browser.html

# Pasrse HTML with BeautifulSoup 
news_soup = BeautifulSoup(html, 'html.parser')

# Retrieve all elements that contain the news title 
news = news_soup.find_all('div', class_="list_text")

# Retrieve the latest news
latest_news = news[0]

# Use Beautiful Soup's find() method to navigate and retrieve attributes
news_title = latest_news.find('div', class_="content_title").text
news_p = latest_news.find('div', class_="article_teaser_body").text

# Print information
print('-----------')
print(news_title)
print(news_p)


# Visit the JPL Featured Space Image
featured_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
browser.visit(featured_url)


# HTML object
image_html = browser.html

# Pasrse HTML with BeautifulSoup 
image_soup = BeautifulSoup(image_html, 'html.parser')


# image_tag=soup.find('img', class_='headerimage')
# partial_url=image_tag.get('src')

# Retrieve the featured image url
image_url = (image_soup.find('img', class_='headerimage fade-in').get('src'))

# Create the website URL link to take you directly to the featured image
featured_image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/'+ image_url

# Display the full image url
print(featured_image_url)
                                         

# Visit the Mars Facts webpage
facts_url = 'https://space-facts.com/mars/'


# Scrape the table containing facts about the planet including Diameter, Mass, etc.
tables = pd.read_html(facts_url)
tables



# Determine data type of table
type(tables)



# Slice the original dataframe using normal indexing 
facts_df = tables[0]
facts_df.columns= ['Description', 'Mass']
facts_df.head()



# Set the index to the `Fact` column
facts_df.set_index('Description', inplace=True)
facts_df


# Convert the facts dataframe to HTML
html_table = facts_df.to_html()
html_table



# Strip unwanted newlines to clean up the table
html_table.replace('\n', '')




# Set executable path and initialize Chrome Browser
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the USGS Astrogeology site
astro_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(astro_url)



# HTML object
html = browser.html

# Pasrse HTML with BeautifulSoup 
astro_soup = BeautifulSoup(html, 'html.parser')


# Create list for the hemisphere images urls 
hemisphere_image_urls = []
count = 0
mars_hemisphere_url = 'https://astrogeology.usgs.gov/'
hemisphere_location = astro_soup.find_all('div', class_='item')

# Obtain high resolution images for each of Mar's hemispheres
for results in hemisphere_location:
    mars = results.find('h3').text
    browser.links.find_by_partial_text(mars).click()
    time.sleep(1)
    
    html = browser.html
    astro_soup = BeautifulSoup(html, 'html.parser')
    partial_image = astro_soup.find('img', class_='wide-image')['src']
    
    img_url = mars_hemisphere_url + partial_image
    
    # Create dictionary lists
    hemisphere_image_urls.append({
        'title': mars,
        'img_url': img_url
    })
    
    count = count + 1
    
    if len(hemisphere_location)>count:
        browser.back()
        time.sleep(1)
        
    else:
        break 
        
    
hemisphere_image_urls




browser.quit()



