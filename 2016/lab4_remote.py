from scipy.ndimage import filters
from PIL import Image
from pylab import *

def Gausian_response(img,sigma=1):
    """ Compute Gaussian response function
        for each pixel in a graylevel image. """
    
    # Gausian response
    img_sigma = zeros(img.shape)
    filters.gaussian_filter(img, (sigma,sigma), (0,0), img_sigma)
    
    return img_sigma
    
def getKeypoints(img):
    sigma1=1
    keypoints=ones(img.shape, dtype=bool)
    img_sigma1=Gausian_response(img,sigma1)
    for i in range(4):
        sigma2=sigma1*1.414
        img_sigma2=Gausian_response(img,sigma2)
        keypoints[keypoints]=(img_sigma2[keypoints]-img_sigma1[keypoints])>10
        img_sigma1=img_sigma2
        sigma1=sigma2
    y,x = nonzero(keypoints)
    return x,y
    
subplot(2,2,1)
img = array(Image.open('img/remote1.jpg').convert('L'))
set_cmap('gray')
imshow(img)
x,y=getKeypoints(img)
plot(x,y,'rx')
title('remote1')

subplot(2,2,2)
img = array(Image.open('img/remote2.jpg').convert('L'))
set_cmap('gray')
imshow(img)
x,y=getKeypoints(img)
plot(x,y,'rx')
title('remote2')

subplot(2,2,3)
img = array(Image.open('img/remote3.jpg').convert('L'))
set_cmap('gray')
imshow(img)
x,y=getKeypoints(img)
plot(x,y,'rx')
title('remote3')

show()