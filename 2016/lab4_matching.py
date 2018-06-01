#lab04_hog.py
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
    sigma1=4
    keypoints=ones(img.shape, dtype=bool)
    img_sigma1=Gausian_response(img,sigma1)
    for i in range(8):
        img_sigma1=Gausian_response(img,sigma1)
        sigma2=sigma1*1.414
        img_sigma2=Gausian_response(img,sigma2)
        keypoints[keypoints]=(img_sigma2[keypoints]-img_sigma1[keypoints])>14
        
    y,x = nonzero(keypoints)
    return x,y
    
def getHog(img, posx,posy):
    '''to compute histogram of gradient at pos. 
    Note that this fucntion may access out of bound pixel'''
    sigma=4
    posx=int(posx)
    posy=int(posy)
    img8=img[posx-8:posx+8,posy-8:posy+8]
    imgx = zeros(img8.shape)
    filters.gaussian_filter(img8, (sigma,sigma), (0,1), imgx)
    imgy = zeros(img8.shape)
    filters.gaussian_filter(img8, (sigma,sigma), (1,0), imgy)
    theta=arctan2(imgy,imgx)
    t=4*(theta.flatten()/pi+1)
    t=t.astype(int)
    #generate histogram
    desc = zeros(8)
    desc=bincount(t,None,8)
    #shift the max to the left
    n=desc.argmax()
    desc=concatenate((desc[n:],desc[:n]),axis=0)
    desc=desc/linalg.norm(desc)*0.99999
    return desc

subplot(1,2,1)
img = array(Image.open('img/remote1.jpg').convert('L'))
set_cmap('gray')
imshow(img)
x,y=getKeypoints(img)

for i in range(len(x)):
    
plot(x,y,'rx')
title('remote1')

subplot(1,2,2)
img = array(Image.open('img/remote2.jpg').convert('L'))
set_cmap('gray')
imshow(img)
x,y=getKeypoints(img)
plot(x,y,'rx')
title('remote2')
