from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from django.db.models import Count
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Board, Post, Topic
from .forms import TopicForm,PostForm

# Create your views here.


def home(request):

    boards = Board.objects.all() # return all boards created in the database
    
    return render(request, 'home.html', {'boards': boards})


def board_topics(request, name):

    #board = Board.objects.get(name=name)

    board = get_object_or_404(Board, name=name)

    #return all topics in this board

    topics = board.topics.order_by('-last_updated').annotate(replies=Count('posts') - 1)

    return render(request, 'board_details.html', {'board': board, 'topics': topics})


@login_required
def topic_create(request, name):

    # This view can only be accessed by users who are login

    board = get_object_or_404(Board, name=name)
    user = request.user
    #user = User.objects.first()

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

            return redirect('topic_details', name=name, topic_pk=topic.pk) # Redirect to Topic details view

    else:

        form = TopicForm()

    return render(request, 'topic_create.html', {'form': form, 'board': board})


def topic_posts(request, name, topic_pk):

    # Retrieve the post details for a specific topic in a given board

    topic = get_object_or_404(Topic, board__name=name, pk=topic_pk)

    topic.views += 1
    topic.save()

    return render(request, 'topic_posts.html', {'topic': topic})


@login_required
def topic_reply(request, name, topic_pk):

    topic = get_object_or_404(Topic, board__name=name, pk=topic_pk)
    user = request.user

    if request.method == 'POST':

        form = PostForm(request.POST)

        if form.is_valid():

            post = form.save(commit=False)

            post.topic = topic
            post.created_by = user

            post.save()

            return redirect('topic_details', name=name, topic_pk=topic_pk)

    else:

        form = PostForm()


    return render(request,'topic_reply.html',{'form': form,'topic':topic})