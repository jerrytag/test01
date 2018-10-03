import urllib.request
import random


def downloader(image_url):
    file_name = random.randrange(1,10000)
    full_file_name = str(file_name) + '.jpg'
    urllib.request.urlretrieve(image_url,full_file_name)

url = 'https://www.metalgearinformer.com/wp-content/uploads/2018/07/Metal-Gear-Survive-The-Encounter-2014-2.jpg'
url = 'https://www.metalgearinformer.com/wp-content/uploads/2018/07/Metal-Gear-Survive-The-Encounter-2014-3.jpg'
downloader(url)