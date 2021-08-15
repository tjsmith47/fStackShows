from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show

#localhost:8000/shows
def index(request):
    context = {
        'all_shows' : Show.objects.all(),
    }
    return render(request, 'index.html', context)

#localhost:8000/shows/new
def new(request):
    return render(request, 'new.html')

#localhost:8000/shows/create
def create(request):
    errors = Show.objects.post_validator(request.POST)
    # if errors are present:
    if len(errors) > 0:
        for value in errors.values():
            messages.error(request, value)
        return redirect(f'/shows/new')
    else:
        show = Show.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['release_date'],
            desc=request.POST['description']
        )
        show_id = show.id
        print(f'CREATE: {request.POST}')
        return redirect(f'/shows/{show_id}')

#localhost:8000/shows/<show_id>
def display(request, show_id):
    show = Show.objects.get(id=show_id)
    context = {
        'show' : show,
    }
    return render(request, 'show.html', context)

#localhost:8000/shows/<show_id>/edit
def edit(request, show_id):
    context = {
        'show' : Show.objects.get(id=show_id),
    }
    return render(request, 'edit.html', context)

#localhost:8000/shows/<show_id>/update
def update(request, show_id):
    errors = Show.objects.update_validator(request.POST)
    # if errors are present:
    if len(errors) > 0:
        for value in errors.values():
            messages.error(request, value)
        return redirect(f'/shows/{show_id}/edit')
    else:
        updated_show = Show.objects.get(id=show_id)
        updated_show.title = request.POST['title']
        updated_show.network = request.POST['network']
        updated_show.release_date = request.POST['release_date']
        updated_show.desc = request.POST['description']
        updated_show.save()
        return redirect(f'/shows/{show_id}')

#localhost:8000/shows/<show_id>/destroy
def destroy(request, show_id):
    delete_show = Show.objects.get(id=show_id)
    delete_show.delete()
    return redirect('/shows')

#localhost:8000/reset
def reset(request):
    request.session.flush()
    empty_db = Show.objects.all()
    empty_db.delete()
    return redirect('/shows')