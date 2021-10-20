# import the application  urls.py
from django.urls import path
# import the app application views.py file
from college import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # new colleges genarate automatic if i click in web page
    path('',views.college_names_view,name='college'),



    # total colleges display
    path('allcolleges',views.College_display_data,name='allcolleges'),

    # one of the college selcect item VIKRAMA SHIMHAPUTI UNIVERSITY
    path('VSU-college/',views.vsu_view,name='vsu'),
    # one of the college selcect item YOGI VEMUNA UNIVERSITY
    path('YVU-college/',views.yvu_view,name='yvu'),
    # one of the college selcect item VENKATESWARA UNIVERSITY
    path('SVU-college/',views.svu_view,name='svu'),
    # one of the college selcect item MUMBAI UNIVERSITY
    path('Maharasta-college/',views.mhu_view,name='mhu'),
    # one of the college selcect item DELHI UNIVERSITY
    path('Delhi-college/',views.du_view,name='du'),
  

]
urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
