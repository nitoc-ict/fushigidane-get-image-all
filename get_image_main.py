import get_image
import os

def get_image_main(coord):
    #  coord = input("Coordinate >>")
    coord = coord.split(',')
    lat = float(coord[0])
    long = float(coord[1])


    url_1 = get_image.make_one_url(lat, long, 0)
    url_2 = get_image.make_one_url(lat, long, 120)
    url_3 = get_image.make_one_url(lat, long, 270)

    if os.path.basename(os.getcwd()) != 'image_point':
        os.chdir('..')
    else:
        os.chdir('image_point')


    new_dir = str(lat)+","+str(long)
    try:
        os.mkdir(new_dir)
    except OSError:
        print('already exists')
        os.chdir(new_dir)

    image_1 = get_image.download_image(url_1)
    get_image.save_image("1.png", image_1)
    image_2 = get_image.download_image(url_2)
    get_image.save_image("2.png", image_2)
    image_3 = get_image.download_image(url_3)
    get_image.save_image("3.png", image_3)
    print("done")
