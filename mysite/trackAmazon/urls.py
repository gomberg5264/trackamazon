from django.conf.urls import url
# from .views import *
from .controllers.index import *
from .controllers.login import *
from .controllers.register import *
from .controllers.contact import *

urlpatterns = [
    url(r'^$', index_req, name="index"),
    url(r'^login$', login, name="login"),
    url(r'^register$', register, name="register"),
    url(r'^contact$', contact, name="contact")
]