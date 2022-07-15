from django.shortcuts import render, redirect
from .forms import TeamForm
from .models import TeamMember

# Create your views here.

def team_list(request): 
    context = { 'team_list': TeamMember.objects.all() }
    return render(request, 'team_members/team_list.html', context)

def team_form(request, id=0): 
    if request.method == 'GET':
        if id == 0:
            form = TeamForm()
        else:
            teammember = TeamMember.objects.get(pk=id)
            form = TeamForm(instance=teammember)
        return render(request, 'team_members/team_form.html',{ 'form': form })
    else: 
        if id == 0:
            form = TeamForm(request.POST)
        else:
            teammember = TeamMember.objects.get(pk=id)
            form = TeamForm(request.POST, instance=teammember)
        if form.is_valid():
            form.save()
        return redirect('/team/list')

def team_delete(request, id): 
    teammember = TeamMember.objects.get(pk=id)
    teammember.delete()
    return redirect('/team/list')

def showthis(request):
    count = TeamMember.objects.all().count()
    context = { 'count': count }
    return render(request, 'team_members/base.html', context)