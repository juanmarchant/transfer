from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  login , logout
from .models import *
from .forms import *
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            rut = form.cleaned_data['rut']
            cliente, created = Cliente.objects.get_or_create(rut=rut)
            
            # Encuentra un chofer disponible
            chofer_disponible = Chofer.objects.filter(status=False).first()
            
            if chofer_disponible:
                # Asigna el chofer como ocupado
                chofer_disponible.status = True
                chofer_disponible.save()

                # Crea el ticket
                ticket = Ticket.objects.create(
                    status=True,
                    chofer=chofer_disponible,
                    cliente=cliente
                )
                ticket.save()
                return redirect("cliente_transfer", ticket=ticket.id)
            else:
                return HttpResponse("No hay choferes disponibles en este momento.")
    else:
        form = ClienteForm()
        
    choferes_disponibles_count = Chofer.objects.filter(status=False).filter(is_staff = False).count()
    return render(request, 'index.html', {'form': form, 'choferes': choferes_disponibles_count})



def chofer_register(request):
    if request.method == 'POST':
        form = ChoferSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('chofer_dashboard')  # Redirige a la página de inicio o a donde desees
    else:
        form = ChoferSignUpForm()
    return render(request, 'registration/chofer_register.html', {'form': form})

def delete(request, id):
    
    ticket = get_object_or_404(Ticket, id=id)   
    if request.method=='POST':
        if 'delete' in request.POST:
            ticket.delete()    
            user = request.user
            user.status = False
            user.save()
            
            return redirect('chofer_dashboard')
        
    return render(request, 'delete.html', {'ticket': ticket})  

def finalizar(request, id):
    
    ticket = get_object_or_404(Ticket, id=id)   
    if request.method=='POST':
        if 'finalizar' in request.POST:
            ticket.status = False
            user = request.user
            user.status = False
            user.save()
            ticket.save()      
            return redirect('chofer_dashboard')
        
    return render(request, 'finalizar.html', {'ticket': ticket})  

@login_required
def chofer_dashboard(request):
    tickets = Ticket.objects.filter(chofer=request.user).filter(status= True)
    return render(request, 'chofer_dashboard.html', {'tickets': tickets})

def logout(request):
    logout(request)
    return redirect('/')

def qr_cliente(request, ticket):
    ticket_obj = get_object_or_404(Ticket, id=ticket)
    return render(request, 'qr_client.html', {'ticket': ticket_obj})
