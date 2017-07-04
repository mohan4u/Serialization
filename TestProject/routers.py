from rest_framework import routers
import testapp.views as testviews

router = routers.DefaultRouter()


router.register(r'users', testviews.SignUpViewSet)