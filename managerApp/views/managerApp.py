from django.shortcuts import render


#Paginas principales para la aplicacion
def home(request):
    '''TODO->Aquí se va a redirigir por la autenticación'''
    
    return render(request, 'managerApp/home.html')