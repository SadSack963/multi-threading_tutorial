# Python Threading Tutorial: Run Code Concurrently Using the Threading Module
# Corey Schafer
# https://www.youtube.com/watch?v=IEEhzQoKtQU

import requests
import time
import concurrent.futures


img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]


def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'./images/{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')


def get_images_standard():
    for img_url in img_urls:
        download_image()
    # Finished in 78.10 seconds


def get_images_threaded():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_image, img_urls)
    # Finished in 80.45 seconds


if __name__ == '__main__':
    t1 = time.perf_counter()

    # Internet Speed is the limiting factor here.
    # get_images_standard()
    get_images_threaded()

    t2 = time.perf_counter()

    print(f'Finished in {round(t2-t1, 2)} seconds')
