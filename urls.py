
from django.contrib import admin
from django.urls import path
from .import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="index"),
    # path("",views.innerpage,name="inner-page.html"),
    # path("",views.portfolio,name="portfolio-details.html"),


]
#  path("",views.index,name="index"),
#     path("about",views.about,name="about us"),
#     path("services",views.services,name="service by  us"),
#     path("contact ",views.contact,name="contact us"),
#     # path("add",views.add,name=" adding"),
