from django.db import models
from PIL import Image

# Create your models here.

'''
 Model for handling images on the app.
'''
class ImageData(models.Model):
    #
    # TODO: image field
    # DONE define the MEDIA_ROOT and MEDIA_URL in the site settings.py file.
    # DONE define the upload_to option (subdirectory of MEDIA_ROOT.
    # 3. use "image.url" to get the image. {{ object.image.url }} in a template.
    #
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    date_uploaded = models.DateField(auto_now=True)
    # type will not be used; managed by the image field (restricts to images).
    # size will not be used; managed by the image field (obecjt.image.size, calls Storage.size() method)
    def __str__(self):
        return self.image.url
    
'''
 Model for handling thumbnails
'''
class ThumbnailData(models.Model):
    #
    # TODO: thumbnail field
    # 1-3. Same as the image field above but specific for image thumbnails.
    #
    thumbnail = models.ImageField(upload_to='thumbs/%Y/%m/%d')
    image = models.ForeignKey(ImageData, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        # save the model first
        super().save()
        
        # open via PIL
        img = Image.open(self.thumbnail.path)
        
        # make thumbnail
        size = (128, 128)
        img.thumbnail(size, Image.ANTIALIAS)
        
        # save the new thumbnail image
        img.save(self.thumbnail.path)
            
    
    def __str__(self):
        return self.thumbnail.url
'''
 Model for handling tags on the app.
'''
class ImageTag(models.Model):
    tag = models.CharField(max_length=64)
    
    def __str__(self):
        return self.tag
'''
 Model for associating images with specific tags.
'''
class ImageTagAssoc(models.Model):
    image = models.ForeignKey(ImageData, on_delete=models.CASCADE)
    tag = models.ForeignKey(ImageTag, on_delete=models.CASCADE)
    
    def __str__(self):
        return '{0} >> {1}'.format(self.image, self.tag)
