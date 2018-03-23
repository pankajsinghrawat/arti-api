import urllib.request
import random

def downloader(urlpathparam):
    file_name = random.randrange(1,10000)
    full_file_name = str(file_name) + '.jpg'
    urllib.request.urlretrieve(urlpathparam, full_file_name)
    return full_file_name
