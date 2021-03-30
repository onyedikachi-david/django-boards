from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import Board, Topic, Post
from .forms import NewTopicForm


# Create your views here.
def home(request):
    boards = Board.objects.all()
    return render(request, 'boards/home.html', {'boards': boards})


def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'boards/topics.html', {'board': board})


def new_topic(request, pk):
    # global form
    # myform = NewTopicForm()
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()  # TODO: get the currently logged user.
    if request.method == "POST":
        myform = NewTopicForm(request.POST)
        if myform.is_valid():
            topic = myform.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=myform.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('board_topics', pk=board.pk) # TODO: redirect to the created topic page
    else:
        myform = NewTopicForm()
    return render(request, 'boards/new_topic.html', {'board': board, 'form': myform})

