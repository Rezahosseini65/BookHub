from rest_framework.routers import SimpleRouter

from bookhub.apps.translators.views import TranslatorViewSet

router = SimpleRouter()
router.register('', TranslatorViewSet)

urlpatterns = [

]+router.urls
