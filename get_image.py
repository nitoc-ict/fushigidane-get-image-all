import requests
import os
from time import sleep

def get_image(coord):
    #  coord = coord.split(',')
    lat = float(coord[0])
    long = float(coord[1])


    url_1 = make_one_url(lat, long, 0)
    url_2 = make_one_url(lat, long, 120)
    url_3 = make_one_url(lat, long, 270)

    if os.path.basename(os.getcwd()) == 'fushigidane-get-image-all':
        os.chdir('image_point')
    elif os.path.basename(os.getcwd()) != 'image_point':
        os.chdir('..')

    new_dir = str(lat) + "," + str(long)
    try:
        os.mkdir(new_dir)
    except OSError:
        print('already exists')

    os.chdir(new_dir)

    image_1 = download_image(url_1)
    save_image("1.png", image_1)
    image_2 = download_image(url_2)
    save_image("2.png", image_2)
    image_3 = download_image(url_3)
    save_image("3.png", image_3)
    print("done")


def make_one_url(lon, lat, heading):
    api_key = 'AIzaSyAJr9KY6uPnhArf4sI2USTB55NH61Ih1Eg'
    url_str = r"https://maps.googleapis.com/maps/api/streetview?size=500x300&fov=120"
    url_str += r"&location=" + str(lon) + r"," + str(lat)
    url_str += r"&heading=" + str(heading)
    # 以下のオプションをつけたほうが望ましいと考えられる
    url_str += r"&key=" + str(api_key)
    return url_str


# 画像をダウンロードする
# 指定したURLの画像データを返す関数
def download_image(url, timeout=30):
    try:
        response = requests.get(url, allow_redirects=False, timeout=timeout)
    except requests.exceptions.ConnectTimeout:
        print('タイムアウトしました')
        sleep(5)

    if response.status_code != 200:
        e = Exception(response.status_code)
        raise e

    content_type = response.headers["content-type"]
    if 'image' not in content_type:
        e = Exception("Content-Type: " + content_type)
        raise e

    return response.content


# 画像を保存する関数
def save_image(filename, image):
    with open(filename, "wb") as fout:
        fout.write(image)
