from django.shortcuts import render,get_object_or_404
from .models import *
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from django.shortcuts import redirect
from .forms import *

def main(request):
    idea_list = IdeaPost.objects.all()
    return render(request, 'forum/main.html', {'idea_list': idea_list})


def idea_detail(request, pk):
    idea = get_object_or_404(IdeaPost, pk=pk)
    return render(request, 'forum/idea_detail.html', {'idea': idea})

def new_idea(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid:
            idea = form.save(commit = False)
            idea.author = "Jason Kam"
            idea.save()
            return redirect('forum.views.main')
    else:
        form = IdeaForm()
    return render(request, 'forum/new_idea.html', {'form':form})



def comment_add(request, pk):

    idea = get_object_or_404(IdeaPost, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.author = "Temporary Bro"
            comment.idea_post = idea
            comment.save()
            return redirect('forum.views.idea_detail', pk = idea.pk)
    else:
        form = CommentForm()
    return render(request, 'forum/new_comment.html', {'form': form, 'idea':idea})




# def new_idea(request):
#   if request.method == 'POST':
#       # Loading user inputs into form object
#       form = IdeaForm(request.POST)
#       if form.is_valid():
#           idea = form.save(commit = False)
#           idea.author = request.user
#           idea.save()
#           return redirect('forum.views.idea_detail', pk=idea.pk)
#   else:
#       form = IdeaForm()
#   return render(request, "forum/new_idea.html", {'form':form})

# def idea_detail(request, pk):
#   idea = get_object_or_404(Idea, pk=pk)
#   return render(request, "forum/idea_detail.html", {'idea':idea})



