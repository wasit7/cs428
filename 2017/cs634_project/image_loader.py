# dog http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02084071
# cat
import shutil
import requests
import uuid
import os

dog_url="http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02084071"
dog_response=requests.get(dog_url, stream=True)
dogs=dog_response.text.split()

for url in dogs:
	response = requests.get(url, stream=True)
	file_name= '{}.jpg'.format(uuid.uuid4())
	with open( os.path.join("dataset","dog", file_name), 'wb') as out_file:
	    shutil.copyfileobj(response.raw, out_file)
	del response