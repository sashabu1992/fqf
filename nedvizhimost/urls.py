from django.urls import path
from . import views

urlpatterns = [
    path('catalog/', views.nedvizhimost_list, {
    	'template':'nedvizhimost/nedvizhimost_list.html',
    	'category' :'',
    	'h1': 'Каталог недвижимости'
    	}, 
    	name='nedvizhimost_list'),
    path('maps/', views.nedvizhimost_list, {
    	'template':'nedvizhimost/maps_list.html',
    	'category' :'',
        'h1': 'Карта объектов'},
    	 name='maps_list'),
    path('catalog/komerch/', views.nedvizhimost_list, {
    	'template':'nedvizhimost/nedvizhimost_list.html',
    	'category' :'komerch',
    	'h1': 'Комерческая недвижимость '
    	},
    	 name='komerch_list'),
    path('catalog/kvartir/', views.nedvizhimost_list, {
    	'template':'nedvizhimost/nedvizhimost_list.html',
    	'category' :'kvartira',
    	'h1': 'Квартиры '
    	},
    	 name='kvartir_list'),
    path('catalog/zagorod/', views.nedvizhimost_list, {
    	'template':'nedvizhimost/nedvizhimost_list.html',
    	'category' :'zagorod',
    	'h1': 'Загородная недвижимость '
    	},
    	 name='zagorod_list'),
    path('catalog/garazhi/', views.nedvizhimost_list, {
    	'template':'nedvizhimost/nedvizhimost_list.html',
    	'category' :'garazh',
    	'h1': 'Гаражи '
    	},
    	 name='garazhi_list'),
    path('catalog/zemuchas/', views.nedvizhimost_list, {
    	'template':'nedvizhimost/nedvizhimost_list.html',
    	'category' :'zemuch',
    	'h1': 'Земельнае участки '
    	},
    	 name='zemuchas_list'),
    path('catalog/newstroi/', views.nedvizhimost_list, {
    	'template':'nedvizhimost/nedvizhimost_list.html',
    	'category' :'newstroi',
    	'h1': 'Новостройки '
    	},
    	 name='newstroi_list'),
    path('catalog/best/', views.best_list, {
    	'template':'nedvizhimost/best_list.html',
    	'h1': 'Лучшие предложения '
    	},
    	 name='best_list'),
    path('ajaxbest/<int:id>/', views.ajaxbest, name='ajaxbest'),
    path('catalog/<slug:slug_dom>/', views.DetailPosts, name='DetailPosts'), # new
    
    
]