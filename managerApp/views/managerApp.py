from . import *


#Paginas principales para la aplicacion
def home(request):    
    return render(request, 'managerApp/home.html')