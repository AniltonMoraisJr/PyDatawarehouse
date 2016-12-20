from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^login/$', views.index, name="login"),
    url(r'^administration/$', views.administration, name="administration"),
    url(r'^do_logout/$', views.do_logout, name="do_logout"),
    url(r'^fornecedores/$', views.fornecedores, name="fornecedores"),
    url(r'fornecedores/novofornecedor/$', views.new_fornecedor, name="new_fornecedor"),
    url(r'^produtos/$', views.produtos, name="produtos"),
    url(r'^produtos/novoproduto/$', views.new_produto, name="new_produto"),
]