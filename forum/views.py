from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import Board, Post, Topic
from .forms import TopicForm
from django.contrib.auth.models import User

# Create your views here.


def home(request):

    boards = Board.objects.all() # return all boards created in the database
    
    return render(request, 'home.html', {'boards': boards})


def board_topics(request, name):

    #board = Board.objects.get(name=name)

    board = get_object_or_404(Board, name=name)

    #return all topics in this board

    topics = board.topics.all()

    return render(request, 'board_details.html', {'board': board, 'topics': topics})


def topic_create(request, name):

    board = get_object_or_404(Board, name=name)
    #user = request.user
    user = User.objects.first()

    if request.method == 'POST':

        form = TopicForm(request.POST)

        if form.is_valid():

            topic = form.save(commit=False)

            topic.board = board
            topic.starter = user
            topic.save()  # save the topic

            post = Post.objects.create(
                topic=topic,
                message=form.cleaned_data.get('message'),
                created_by=user
            )

            return redirect('board_details', name=name)



    else:

        form = TopicForm()

    return render(request, 'topic_create.html', {'form': form, 'board': board})
