# import requests
# from bs4 import BeautifulSoup
# import os

# # URL of the Times of India website or a specific section
# url = "https://timesofindia.indiatimes.com/"

# # Send an HTTP request to the website
# response = requests.get(url)

# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the HTML content of the page
#     soup = BeautifulSoup(response.content, 'html.parser')

#     # Find all the article links on the page
#     article_links = soup.find_all('a', class_='w_img')
    
#     for link in article_links:
#         article_url = link['href']
#         article_response = requests.get(article_url)
        
#         if article_response.status_code == 200:
#             article_soup = BeautifulSoup(article_response.content, 'html.parser')
            
#             # Find all the images in the article
#             article_images = article_soup.find_all('img')
            
#             # Create a directory to save the images for each article
#             article_title = article_soup.title.string
#             article_directory = article_title.replace(" ", "_")
            
#             if not os.path.exists(article_directory):
#                 os.makedirs(article_directory)
            
#             # Download and save the images
#             for i, img in enumerate(article_images):
#                 img_url = img['src']
#                 img_response = requests.get(img_url)
#                 if img_response.status_code == 200:
#                     img_filename = f"{article_directory}/image_{i}.jpg"
#                     with open(img_filename, 'wb') as img_file:
#                         img_file.write(img_response.content)
#                         print(f"Downloaded: {img_filename}")
# else:
#     print("Failed to retrieve the website content.")


# import requests
# from bs4 import BeautifulSoup
 
 
# url = 'https://timesofindia.indiatimes.com/"'
# reqs = requests.get(url)
# soup = BeautifulSoup(reqs.text, 'html.parser')
 
# urls = []
# for link in soup.find_all('a'):
#     print(link.get('href'))
import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

# The main URL to start scraping
url = 'https://timesofindia.indiatimes.com/'

reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

# Find all the URLs on the page
urls = []
for link in soup.find_all('a', href=True):
    urls.append(urljoin(url, link['href']))

# Create a directory for downloaded images
download_folder = 'downloaded_images'
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# Function to download images from a URL and save them in the download folder
def download_images_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        page_soup = BeautifulSoup(response.text, 'html.parser')
        images = page_soup.find_all('img')

        for i, img in enumerate(images):
            img_url = img.get('src')
            if img_url:
                img_response = requests.get(urljoin(url, img_url))
                if img_response.status_code == 200:
                    img_filename = os.path.join(download_folder, f"image_{i}.jpg")
                    with open(img_filename, 'wb') as img_file:
                        img_file.write(img_response.content)
                        print(f"Downloaded: {img_filename}")

# Loop through the URLs and download images
for url in urls:
    download_images_from_url(url)

print(f"All images have been downloaded and saved in the '{download_folder}' folder.")

