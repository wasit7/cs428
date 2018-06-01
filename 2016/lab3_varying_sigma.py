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


subplot(2,3,1)
set_cmap('gray')
imshow(img)
title('original image')

subplot(2,3,2)
imshow(Gausian_response(img,2)-Gausian_response(img,1))
title('G2-G1')

subplot(2,3,3)
imshow(Gausian_response(img,3)-Gausian_response(img,2))
title('G3-G2')

subplot(2,3,4)
imshow(Gausian_response(img,4)-Gausian_response(img,3))
title('G4-G3')

subplot(2,3,5)
imshow(Gausian_response(img,5)-Gausian_response(img,4))
title('G5-G4')

subplot(2,3,6)
c=0.8
imshow(Gausian_response(img,6)-Gausian_response(img,5))
title('G6-G5')
show()
