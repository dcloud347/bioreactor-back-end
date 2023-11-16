from rest_framework.routers import SimpleRouter
from .views import DesiredValuesViewSet, RecordViewSet

router = SimpleRouter()
router.register('desired-values', DesiredValuesViewSet)
router.register('record', RecordViewSet)
urlpatterns = router.urls
