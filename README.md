# web-scraping-challenge

 ### Mission to Mars
In this project, I built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

### Scraping
For my initial scraping, I used Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

### NASA Mars News

1. Scraped the NASA Mars News Site and collected the latest News Title and Paragraph Text.
2. Assigned text to variables to reference later.

### JPL Mars Space Images - Featured Image

1. Pulled the url for JPL Featured Space Image.
2. Used splinter to navigate the site and found the image url for the current Featured Mars Image.
3. Assigned the url string to a variable called featured_image_url.

### Mars Facts

1. Visited the Mars Facts webpage
2. Used Pandas to scrape the table covering facts about the Mars including Diameter, Mass, etc.
3. Used Pandas to convert the data to a HTML table string.

### Mars Hemispheres

1. Visited the USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres.
2. Saved the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. 
3. Created a Python dictionary to store the data using the keys img_url and title.
4. Appended the dictionary with the image url string and the hemisphere title to a list. This list contains one dictionary for each hemisphere.

### MongoDB and Flask Application
1. Using MongoDB with Flask template, I created a new HTML page that displays all of the information that was scraped from the URLs above.
2. Converted my Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute my scraping code from above and return one Python dictionary containing all of the scraped data.
3. Created a route called /scrape that imported my scrape_mars.py script and called the scrape function.
4. Stored the return value in Mongo as a Python dictionary.
5. Created a root route / that queried Mongo database and passed the mars data into an HTML template to display the data.
6. Created a template HTML file (index.html) that used the mars data dictionary to display all of the data in the appropriate HTML elements. 
