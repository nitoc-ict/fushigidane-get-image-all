import get_image
import os

coord = input("Coordinate >>")
coord = coord.split(',')
lat = float(coord[0])
long = float(coord[1])


url_1 = get_image.make_one_url(lat, long, 0)
url_2 = get_image.make_one_url(lat, long, 120)
url_3 = get_image.make_one_url(lat, long, 270)

try:
    new_dir = str(lat)+","+str(long)
    try:
        os.mkdir(new_dir)
    except OSError:
        print('already exists')
    os.chdir(new_dir)
    image_1 = get_image.download_image(url_1)
    get_image.save_image("North.png", image_1)
    image_2 = get_image.download_image(url_2)
    get_image.save_image("South.png", image_2)
    image_3 = get_image.download_image(url_3)
    get_image.save_image("West.png", image_3)

    print("done")
except Exception as err:
       print(err)