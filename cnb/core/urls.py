from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('catedre', views.catedre, name='catedre'),
    path('contact', views.contact, name='contact'),
    path('informatii', views.informatii, name='informatii'),
    path('informatii/personal_administrativ/<str:pk>', views.personal_administrativ),
    path('informatii/<str:pk>', views.template_doc),
    path('istoric', views.istoric, name='istoric'),
    path('organizarea_claselor', views.organizarea_claselor),
    path('activitati_extrascolare', views.activitati_extrascolare),
    path('proiecte', views.proiecte, name='proiecte'),
    path('consiliul_elevilor_proiecte', views.proiecte_consiliul_elevilor),
    path('incarcare_proiect', views.incarcare_proiecte),
    path('modificare_proiect', views.modificare_proiect),
    path('prelucrare_excel', views.prelucrare_excel),
    path('anunturi', views.anunturi, name='anunturi'),
    path('logopedie', views.logopedie, name='logopedie'),
    path('consiliere', views.consiliere, name='consiliere'),
    path('concursuri_de_angajare', views.concursuri),
    path('olimpici', views.olimpici, name='olimpici'),
    path('biblioteca', views.biblioteca, name='biblioteca'),
    # path('biblioteca_carti<int:pk>', views.biblioteca_carti),
    path('proiecte/<str:pk>', views.template_proiecte),
    path('activitati_extrascolare/<str:pk>', views.template_proiecte),
    path('test', views.search_bar),
    # path('test_js', views.test_js),
    path('consiliul_administrativ', views.consiliu),
    path('consiliul_elevilor', views.consiliul_elevilor),
    path('oferta_educationala', views.oferta_educationala, name='oferta educationala'),
    path('404', views.not_found),

]