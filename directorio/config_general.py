from  ads.models import Category

def datos_globales(request):
    categories = Category.objects.order_by('id')
    dict = {
        'SITE_URL': 'http://ejemplo.com',
        'SITE_NAME': 'Mi Sitio de Ejemplo',
        'SITE_AUTHOR': 'Hector Costa',
        'categories': categories
    }
    return dict