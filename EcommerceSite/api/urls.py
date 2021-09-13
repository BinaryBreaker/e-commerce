from  .views import BlogPostRudView , CatgoryData
from django.conf.urls import url
from django.urls import path


urlpatterns = [
    url(r'^(?P<id>\d+)/$', BlogPostRudView.as_view(), name='post-rud'),
    path("cat/<int:id>", CatgoryData.as_view(), name="CatgoryData"),

]
