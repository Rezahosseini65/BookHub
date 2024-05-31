from rest_framework.routers import SimpleRouter

from bookhub.apps.authors.views import AuthorViewSet

router = SimpleRouter()
router.register('', AuthorViewSet)

urlpatterns = [

]+router.urls
