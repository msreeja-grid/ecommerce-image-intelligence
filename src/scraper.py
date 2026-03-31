import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
import urllib3

# This hides that annoying SSL warning from your terminal
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def run_scraper():
    # 1. Setup absolute paths
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raw_path = os.path.join(BASE_DIR, "data", "raw")
    
    # 2. Safety Check: If 'raw' is a file, delete it so we can make it a folder
    if os.path.exists(raw_path) and not os.path.isdir(raw_path):
        os.remove(raw_path)
        
    os.makedirs(raw_path, exist_ok=True)

    url = "https://books.toscrape.com/catalogue/page-1.html"
    print(f"Downloading images to: {raw_path}")
    
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.text, "html.parser")
    products = []

    for i, item in enumerate(soup.select(".product_pod")):
        title = item.h3.a["title"]
        img_src = "https://books.toscrape.com/" + item.img["src"].replace("../", "")
        
        img_filename = f"product_{i}.jpg"
        local_path = os.path.join(raw_path, img_filename)
        
        # Download
        img_data = requests.get(img_src, verify=False).content
        with open(local_path, "wb") as f:
            f.write(img_data)
            
        products.append({"title": title, "local_path": local_path})
        print(f"Successfully saved: {img_filename}")

    df = pd.DataFrame(products)
    df.to_csv(os.path.join(BASE_DIR, "data", "metadata.csv"), index=False)
    print("\nScraper finished successfully!")

if __name__ == "__main__":
    run_scraper()