"""
Modify django-storages to store static and media files in sub-folders in a google cloud storage bucket
"""
from abc import ABC
from storages.backends.gcloud import GoogleCloudStorage


class GoogleCloudMediaStorage(GoogleCloudStorage, ABC):
    """
    GoogleCloudStorage for Django's Media files.
    """

    def __init__(self, *args, **kwargs):
        kwargs['location'] = 'media'
        super(GoogleCloudMediaStorage, self).__init__(*args, **kwargs)


class GoogleCloudStaticStorage(GoogleCloudStorage, ABC):
    """
    GoogleCloudStorage for Django's Static files
    """

    def __init__(self, *args, **kwargs):
        kwargs['location'] = 'static'
        super(GoogleCloudStaticStorage, self).__init__(*args, **kwargs)

