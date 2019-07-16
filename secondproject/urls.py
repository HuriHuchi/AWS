from django.contrib import admin
from django.urls import path, include
import blog.views
import portfolio.views
import accounts.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # home
    path('', blog.views.home, name="home"),
    
    # blog app으로부터 url을 끌어오기
    path('blog/', include("blog.urls")),
    # portfolio app으로부터 url을 끌어오기
    path('portfolio/', include("portfolio.urls")),
    # accounts app으로부터 url을 끌어오기
    path('accounts/', include("accounts.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # 병렬적으로 더해주기