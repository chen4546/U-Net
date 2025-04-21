import shutil

from PIL import Image
import os

from unet import  Unet
if __name__=='__main__':
    mode = "predict_all"
    #image_dir='isic2018/test/images/'
    #save_dir='isic2018/test/images_predict/'
    image_dir='BUSI-256/images/'
    save_dir='BUSI-256/images_predict/'
    if os.path.exists(save_dir):
        shutil.rmtree(save_dir)
    os.mkdir(save_dir)
    unet=Unet()
    dir_list=os.listdir(image_dir)
    for img in dir_list:
        try:
            image = Image.open(image_dir+img)
        except:
            print('Open Error! Try again!')
            continue
        else:
            r_image = unet.detect_image(image)
            r_image.save(save_dir+img)

