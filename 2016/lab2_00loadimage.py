from PIL import Image
from pylab import *

# read image to array
im = array(Image.open('img/landscape.jpg'))
# plot the image
imshow(im)
# some points
x = [100,100,400,400]
y = [200,400,200,400]
# plot the points with red star-markers
plot(x,y,'r*')
# line plot connecting the first two points
plot(x[:2],y[:2])
# add title and show the plot
title('Plotting: "img/landscape.jpg"')
show()
gin_xy=ginput(3)
print gin_xy