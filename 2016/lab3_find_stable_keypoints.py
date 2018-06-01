from scipy.ndimage import filters
from PIL import Image
#from numpy import *
from pylab import *

def Gausian_response(img,sigma=1):
    """ Compute Gaussian response function
        for each pixel in a graylevel image. """
    
    # Gausian response
    img_sigma = zeros(img.shape)
    filters.gaussian_filter(img, (sigma,sigma), (0,0), img_sigma)
    
    return img_sigma
    


img = array(Image.open('img/graffiti.jpg').convert('L'))
sigma1=1
keypoints=ones(img.shape, dtype=bool)
img_sigma1=Gausian_response(img,sigma1)
for i in range(4):
    img_sigma1=Gausian_response(img,sigma1)
    sigma2=sigma1*1.414
    img_sigma2=Gausian_response(img,sigma2)
    keypoints[keypoints]=(img_sigma2[keypoints]-img_sigma1[keypoints])>25
    
    
subplot(1,2,1)
set_cmap('gray')
imshow(img)
title('original image')

subplot(1,2,2)
imshow(keypoints)
title('stable keypoints')
show()