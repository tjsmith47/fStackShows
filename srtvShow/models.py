from django.db import models


#EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')

class ShowManager(models.Manager):
    def post_validator(self, postData):
        errors = {}
        title = Show.objects.filter(title=postData['title'])
        #network = Show.objects.filter(network=postData['network'])
        #today = datetime.date.today()
        #release_date = Show.objects.filter(release_date=postData['release_date'])
        if title:
            errors['unique'] = 'Show has already been registered.'
        if not len(postData['title']) >= 2:
            errors['title'] = 'Please provide title that is at least 2 characters'
        if not len(postData['network']) >= 3:
            errors['network'] = 'Please provide a network that is at least 3 characters'
        if len(postData['release_date']) == 0:
            errors['release_date'] = 'Please provide a release date'
        #if len(postData['release_date']) == 0:
            #errors['not_past'] = 'Please provide a date.'
        if len(postData['description']) > 0 and len(postData['description']) < 10:
            errors['desc_length'] = "Description must be 10 characters if provided"
        return errors
    def update_validator(self, postData):
        errors = {}
        if not len(postData['title']) >= 2:
            errors['title'] = 'Please provide a title'
        if not len(postData['network']) >= 3:
            errors['network'] = 'Please provide a network'
        if not postData['release_date']:
            errors['release_date'] = 'Please provide a release date'
        #if len(postData['release_date']) == 0:
            #errors['not_past'] = 'Please ust a date.'
        if len(postData['description']) > 0 and len(postData['description']) < 10:
            errors['desc_length'] = "Description must be 10 characters if provided"
        return errors

class Show(models.Model):
    # id = <int>
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField(null=True, blank=True)
    desc = models.TextField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
    def __repr__(self):
        return "{} ({}, {})".format(
            self.title, 
            self.network, 
            self.release_date
        )