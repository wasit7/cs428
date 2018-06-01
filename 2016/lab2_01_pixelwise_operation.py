from PIL import Image
#from numpy import *
from pylab import *
im = array(Image.open('img/landscape.jpg').convert('L'))
im2 = 255 - im #invert image
im3 = (100.0/255) * im + 100 #clamp to interval 100...200
im4 = 255.0 * (im/255.0)**2 #squared
subplot(2, 2, 1)
set_cmap('gray')
imshow(im)
show()
title('Plotting: "im"')

subplot(2, 2, 2)
imshow(im2)
show()
title('Plotting: "255 - im"')

subplot(2, 2, 3)
imshow(im3)
show()
title('Plotting: "(100.0/255) * im + 100"')

subplot(2, 2, 4)
imshow(im4)
show()
title('Plotting: "255.0 * (im/255.0)**2"')