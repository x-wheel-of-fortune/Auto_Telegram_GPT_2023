import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

# Define the search query and search engine URL


def get_image(query,n):
    search_url = "https://www.bing.com/images/search?q=" + query
    # Send a GET request to the search engine URL and get the response
    response = requests.get(search_url)

    # Parse the HTML content of the response using Beautiful Soup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the image tags on the page
    img_tags = soup.find_all("img")
    #print(img_tags)
    # Extract the source URLs of the images
    img_urls = []
    for img in img_tags:
        if "data-src" in img.attrs:
            img_urls.append(img["data-src"])
    return(img_urls[1])
    # # Filter out any non-image URLs
    # img_urls = [url for url in img_urls if url.endswith(".jpg") or url.endswith(".png")]
    #
    # # Make all the URLs absolute
    # parsed_url = urlparse(search_url)
    # #img_urls = [urljoin(f"{parsed_url.scheme}://{parsed_url.netloc}", url) for url in img_urls]


    # Download the images
    # for i, url in enumerate(img_urls):
    #     response = requests.get(url)
    #     with open(f"{query}_{i}.jpg", "wb") as f:
    #         f.write(response.content)
#print(get_image("cute cats",0))