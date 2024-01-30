from django.shortcuts import render, get_object_or_404, redirect
from .models import Topic, Category, User
from .forms import TopicForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages



def home(request):
    topics_list = Topic.objects.all().order_by('-published_at')  

    # Filter topics based on the selected category
    category_name = request.GET.get('category')
    if category_name:
        topics_list = topics_list.filter(categories__name__iexact=category_name)

    featured_topics = Topic.objects.filter(is_featured=True).order_by('-published_at')[:3]
    paginator = Paginator(topics_list, 5) 

    page = request.GET.get('page')
    try:
        topics = paginator.page(page)
    except PageNotAnInteger:
        topics = paginator.page(1)
    except EmptyPage:
        topics = paginator.page(paginator.num_pages)

    context = {
        'topics': topics,
        'categories': Category.objects.all(),
        'authors': User.objects.all(),
        'featured_topics': featured_topics,
        'exclude_wysiwyg': True, 
    }
    return render(request, 'home.html', context)


def topic_list(request):
    topics = Topic.objects.all().order_by('-published_at')  

    category_name = request.GET.get('category')
    if category_name:
        topics = topics.filter(categories__name__iexact=category_name)

    context = {
        'topics': topics,
        'categories': Category.objects.all(),
        'authors': User.objects.all(),
        'exclude_wysiwyg': True
    }
    return render(request, 'topic_list.html', context)

def topic_detail(request, pk):
    topic = get_object_or_404(Topic, id=pk)

    # Handle comment form submission
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # Save the comment associated with the current topic
            comment = comment_form.save(commit=False)
            comment.topic = topic
            comment.author = request.user
            comment.save()
            messages.success(request, 'Comment added successfully!')
            return redirect('topic_detail', pk=pk)

    else:
        comment_form = CommentForm()

    # Fetch existing comments for the current topic
    comments = topic.comments.all()

    context = {
        'topic': topic,
        'comment_form': comment_form,
        'comments': comments,
        'exclude_wysiwyg': True, 
    }
    return render(request, 'topic_detail.html', context)



@login_required(login_url='login')
def topic_create(request):
    if request.method == 'POST':
        form = TopicForm(request.POST, request.FILES)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.author = request.user
            topic.save()
            return redirect('home')  
    else:
        form = TopicForm()

    return render(request, 'topic_form.html', {'form': form})


@login_required
def topic_update(request, pk):
    topic = get_object_or_404(Topic, pk=pk, author=request.user)  # Ensure the topic belongs to the current user

    if request.method == 'POST':
        form = TopicForm(request.POST, request.FILES, instance=topic)  # Include request.FILES for file uploads
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TopicForm(instance=topic)

    return render(request, 'topic_form.html', {'form': form})


# @login_required
# def topic_update(request, pk):
#     topic = get_object_or_404(Topic, pk=pk)

#     if request.user != topic.author:
#         messages.error(request, "You don't have permission to update this post.")
#         return redirect('home')

#     if request.method == 'POST':
#         form = TopicForm(request.POST, instance=topic)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your post has been updated!')
#             return redirect('topic-detail', pk=topic.pk)
#         print(form)
#     else:
#         form = TopicForm(instance=topic)
    

#     return render(request, 'topic_detail.html', {'form': form})




def topic_delete(request, pk):
    topic = get_object_or_404(Topic, pk=pk)

    if request.method == 'POST':
        # Handle the POST request to delete the topic
        topic.delete()
        return redirect('topics_list')  # Redirect to the topic list after deletion

    return render(request, 'topic_delete.html', {'topic': topic})




# def blog_post(request, pk):
