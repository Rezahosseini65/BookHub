from rest_framework.routers import SimpleRouter

from bookhub.apps.books.views import CategoryViewSet, BookViewSet

router = SimpleRouter()
router.register('categories', CategoryViewSet)
router.register('books', BookViewSet)

urlpatterns = [

]+router.urls
