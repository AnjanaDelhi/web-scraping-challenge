# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import time 

executable_path = {"executable_path": "chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)

# Defining function scrape that will load all the data scraped
def scrape():
    browser = browser()
    mars_news = {}

    nasa = "https://mars.nasa.gov/news/"
    browser.visit(nasa)
    time.sleep(2)

    html = browser.html
    soup = bs(html,"html.parser")

    # scrapping latest news about mars from nasa
    news_title = soup.find("div",class_="content_title").text
    news_paragraph = soup.find("div", class_="article_teaser_body").text
    mars_facts_data['news_title'] = news_title
    mars_facts_data['news_paragraph'] = news_paragraph 

     # Mars Facts

    url_facts = "https://space-facts.com/mars/"
    time.sleep(2)
    table = pd.read_html(url_facts)
    table[0]

    mars_df = table[0]
    mars_df.columns = ["Variable", "Values"]
    mars_html = mars_df.to_html()
    mars_html = mars_html.replace("\n", "")
    mars_facts_data["mars_facts_table"] = mars_html

    # Mars Hemispheres
    hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemispheres_url)

    
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    hemisphere_image_urls = []

    products = soup.find("div", class_ = "result-list" )
    hemispheres = products.find_all("div", class_="item")

    for hemisphere in hemispheres:
        title = hemisphere.find("h3").text
        title = title.replace("Enhanced", "")
        end_link = hemisphere.find("a")["href"]
        image_link = "https://astrogeology.usgs.gov/" + end_link    
        browser.visit(image_link)
        html = browser.html
        soup=BeautifulSoup(html, "html.parser")
        downloads = soup.find("div", class_="downloads")
        image_url = downloads.find("a")["href"]
        hemisphere_image_urls.append({"title": title, "img_url": image_url})
    mars_facts_data["hemisphere_img_url"] = hemisphere_img_urls

    return mars_facts_data
