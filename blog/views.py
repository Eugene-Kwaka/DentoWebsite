from django.shortcuts import render, get_object_or_404, redirect, reverse
from blog.models import Category, Post
#from dentist.models import Patient
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Q
from blog.forms import CommentForm, PostForm, CategoryForm
from .decorators import allowed_users


def search(request):
    post_list = Post.objects.all()
    query = request.GET.get('q')
    if query:
        post_list = post_list.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    context = {
        'post_list': post_list,
    }
    return render(request, 'search_results.html', context)

@allowed_users(allowed_roles=['admin'])
def categories(request):
    categories = Category.objects.all()
    context = {
        'categories':categories,
    }
    return render(request, 'category.html', context)


@allowed_users(allowed_roles=['admin'])
def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
        else:
            form = CategoryForm()
    context ={
        'form':form,
    }
    return render(request, 'add_category.html', context)

@allowed_users(allowed_roles=['admin'])
def update_category(request, pk):
    category = Category.objects.get(id=pk)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
        else:
            form = CategoryForm()
    context ={
        'form':form,
    }
    return render(request, 'update_category.html', context)

@allowed_users(allowed_roles=['admin'])
def delete_category(request, pk):
    category = Category.objects.get(id=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('categories')
    context = {
        'category': category,
    }
    return render(request, 'delete_category.html', context)



def get_category_count():
    queryset = Post.objects.values(
        'categories__title').annotate(Count('categories__title'))
    return queryset


# This view handles the blog page that shows all the posts have been posted.
def blog(request):
    category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[0:3]
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_post_list = paginator.page(page)
    except PageNotAnInteger:
        paginated_post_list = paginator.page(1)
    except EmptyPage:
        paginated_post_list = paginator.page(paginator.num_pages)

    context = {
        'post_list': paginated_post_list,
        'page_request_var': page_request_var,
        'most_recent': most_recent,
        'category_count': category_count,
    }

    return render(request, 'blog.html', context)

# Logic for a specific post


def post(request, id):
    category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[0:3]
    post = get_object_or_404(Post, id=id)

    # logic for the CommentForm
    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse('post-detail', kwargs={
                'id': post.id
            }))

    context = {
        'category_count': category_count,
        'most_recent': most_recent,
        'post': post,
        'form': form,
    }
    return render(request, 'blog-details.html', context)


@allowed_users(allowed_roles=['admin'])
def post_create(request):
    title = 'Create'
    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('post-detail', kwargs={
                'id': form.instance.id
            }))
    context = {
        'form': form,
        'title': title,
    }
    return render(request, 'post_create.html', context)


@allowed_users(allowed_roles=['admin'])
def post_update(request, id):
    title = 'Update'
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('post-detail', kwargs={
                'id': form.instance.id
            }))
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'post_create.html', context)


@allowed_users(allowed_roles=['admin'])
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    context = {
        'post': post,
    }
    return render(request, 'post_delete.html', context)
