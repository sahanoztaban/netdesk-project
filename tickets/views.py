from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Ticket
from .forms import TicketForm
from django.contrib.auth.forms import UserCreationForm

@login_required
def home(request):

    search_query = request.GET.get('search')

    if search_query:
        tickets = Ticket.objects.filter(title__icontains=search_query)
    else:
        tickets = Ticket.objects.all()

    paginator = Paginator(tickets, 3)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    return render(request, 'tickets/home.html', {
        'page_obj': page_obj,
        'search_query': search_query
    })

@login_required
def create_ticket(request):

    if request.method == 'POST':

        form = TicketForm(request.POST)

        if form.is_valid():

            ticket = form.save(commit=False)

            ticket.created_by = request.user

            ticket.save()

            return redirect('home')

    else:

        form = TicketForm()

    return render(request, 'tickets/create_ticket.html', {
        'form': form
    })

@login_required
def edit_ticket(request, ticket_id):

    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.method == 'POST':

        form = TicketForm(request.POST, instance=ticket)

        if form.is_valid():

            form.save()

            return redirect('home')

    else:

        form = TicketForm(instance=ticket)

    return render(request, 'tickets/edit_ticket.html', {
        'form': form,
        'ticket': ticket
    })

@login_required
def delete_ticket(request, ticket_id):

    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.method == 'POST':

        ticket.delete()

        return redirect('home')

    return render(request, 'tickets/delete_ticket.html', {
        'ticket': ticket
    })

def register(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('login')

    else:

        form = UserCreationForm()

    return render(request, 'tickets/register.html', {
        'form': form
    })

@login_required
def make_admin(request):

    user = request.user

    user.is_staff = True
    user.is_superuser = True

    user.save()

    return redirect('/admin')