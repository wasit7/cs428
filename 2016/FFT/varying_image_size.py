# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 17:48:17 2014

@author: Wasit
"""
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
from scipy.ndimage import zoom
ima=np.array(Image.open('../img/book.jpg').convert('L'))
imb=np.array(Image.open('../img/left01_h.jpg').convert('L'))

#frequency domain
fa=np.log(np.abs(np.fft.fftshift(np.fft.fft2(ima))))
fb=np.log(np.abs(np.fft.fftshift(np.fft.fft2(imb))))
#scaling
sa=(100./fa.shape[0],100./fa.shape[1])
sb=(100./fb.shape[0],100./fb.shape[1])
#normalized frequency domian
ga=zoom(fa,sa,order = 2)
gb=zoom(fb,sb,order = 2)

fig1=plt.figure()
plt.imshow(ga,interpolation='none')
plt.set_cmap('gray')

fig2=plt.figure()
plt.imshow(fa,interpolation='none')
plt.set_cmap('gray')

#f_FFT=2*width/wavelength