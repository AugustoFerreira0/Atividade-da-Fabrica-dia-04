from rest_framework import routers
from .views import TodolistViewset, PessoaViewset

router = routers.DefaultRouter()
router.register(r'todo', TodolistViewset)
router.register(r'Pessoa', PessoaViewset)
urlpatterns = router.urls
