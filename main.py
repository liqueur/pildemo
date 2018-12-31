from PIL import Image
from os import path


def get_path(filename):
    p = path.dirname(__file__)
    p = path.join(p, filename)
    return p


def convert_to_jpeg():
    # 图片格式转换，不指定格式，默认根据后缀名转换
    infile = get_path('mokuno.jpg')
    outfile = get_path('mokuno2.jpg')
    try:
        Image.open(infile).save(outfile)
    except Exception as e:
        print(e)


def create_thumbnail():
    # 创建图片略缩图
    size = (128, 128)
    infile = get_path('mokuno.jpg')
    outfile = get_path('mokuno_thumbnail.jpg')
    try:
        im = Image.open(infile)
        im.thumbnail(size)
        im.save(outfile, 'JPEG')
    except Exception as e:
        print(e)


def get_info():
    # 获取图片信息
    infile = get_path('mokuno.jpg')
    try:
        im = Image.open(infile)
        print(infile, im.format, '%dx%d' % im.size, im.mode)
    except Exception as e:
        print(e)


def copy_region():
    # 截取图片区域
    box = (100, 100, 400, 400)
    infile = get_path('mokuno.jpg')
    try:
        im = Image.open(infile)
        region = im.crop(box)
        region.show()
    except Exception as e:
        print(e)


def paste_region():
    # 粘贴图片区域
    box = (100, 100, 400, 400)
    infile = get_path('mokuno.jpg')
    try:
        im = Image.open(infile)
        region = im.crop(box)
        region = region.transpose(Image.ROTATE_180)
        im.paste(region, box)
        im.show()
    except Exception as e:
        print(e)


def paste_region_2():
    # 不同图片格式图片粘贴
    infile1 = get_path('mokuno.jpg')
    infile2 = get_path('qrcode.jpg')
    try:
        im1 = Image.open(infile1)
        im2 = Image.open(infile2)
        im2.thumbnail((128, 128))
        im1.paste(im2, (0, 0, 128, 128))
        im1.show()
    except Exception as e:
        print(e)



if __name__ == '__main__':
    # convert_to_jpeg()
    # create_thumbnail()
    # get_info()
    # copy_region()
    # paste_region()
    paste_region_2()
