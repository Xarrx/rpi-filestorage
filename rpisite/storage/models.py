from django.db import models

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
    # TODO: thumbnail field
    # 1-3. Same as the image field above but specific for image thumbnails.
    #
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    thumbnail = models.ImageField(upload_to='thumbs/%Y/%m/%d')
    date_uploaded = models.DateField(auto_now=True)
    # type will not be used; managed by the image field (restricts to images).
    # size will not be used; managed by the image field (obecjt.image.size, calls Storage.size() method)
    def __str__(self):
        return self.image.url
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
