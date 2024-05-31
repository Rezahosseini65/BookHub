from rest_framework.routers import SimpleRouter

from bookhub.apps.publishers.views import PublisherViewSet

router = SimpleRouter()
router.register('', PublisherViewSet)

urlpatterns = [

]+router.urls