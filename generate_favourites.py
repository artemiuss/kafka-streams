import random
import string
import csv
import pandas as pd

def generate_random_url():
    domain = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
    extension = random.choice(['.com', '.net', '.org','.xyz',
'.info',
'.club',
'.online',
'.site',
'.store',
'.blog',
'.tech',
'.space',
'.link',
'.click',
'.design',
'.live',
'.world',
'.news',
'.io',
'.co',
'.me',
'.tv',
'.org',
'.ua'])
    return f"https://www.{domain}{extension}"

urls = [generate_random_url() for _ in range(100000)]

df = pd.DataFrame(urls, columns=["URL"])
df.to_csv('favourites.csv', index=False)
