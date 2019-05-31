from django.shortcuts import render, redirect, get_object_or_404
from .models import Board, Comment
from django.db.models import Count

# Create your views here.
def index(request):
    boards = Board.objects.annotate(count=Count('like_users')).order_by('-count')
    # boards = Board.objects.all().order_by('-like_users')
    return render(request, 'boards/index.html/',{'boards':boards})
    
def search(request, board_num):

    board = Board.objects.all().filter(board_num = board_num).annotate(count=Count('like_users')).order_by('-count')
    return render(request, 'boards/index.html', {'boards' : board})
    
def new(request):
    if request.method == 'POST' :
        board_num=int(request.POST.get('board_num'))
        title = request.POST.get('title')
        content = request.POST.get('content')
        file=request.FILES.get('file')
        board = Board(title=title, content=content, file=file, user=request.user, board_num=board_num)
        board.save()
        return redirect('boards:detail', board.pk)
    else:
        return render(request, 'boards/new.html')

def detail(request, board_pk):
    board=get_object_or_404(Board, pk=board_pk)
    comments=board.comment_set.all()
    return render(request, 'boards/detail.html/',{'board':board, 'comments':comments})

def edit(request, board_pk):
    board=get_object_or_404(Board, pk=board_pk)
    if board.user == request.user:
        if request.method=='POST':
            board.title=request.POST.get('title')
            board.board_num=request.POST.get('board_num')
            board.content=request.POST.get('content')
            board.file=request.FILES.get('file')
            board.save()
            return redirect('boards:detail', board.pk)
        else:
            return render(request, 'boards/edit.html', {'board' :board})
    else : 
        return redirect('boards:detail', board.pk)

def delete(request, board_pk):
    board=get_object_or_404(Board, pk=board_pk)
    if board.user == request.user:
        if request.method=='POST':
            board.delete()
            return redirect('boards:index')
        else :
            return redirect('boards:detail',board.pk)
    else : 
        return redirect('boards:detail', board.pk)
        
def comments_create(request, board_pk):
    board=get_object_or_404(Board, pk=board_pk)
    if request.method == 'POST':
        comment = Comment()
        comment.board = board
        comment.content = request.POST.get('content')
        comment.user = request.user
        comment.save()
        return redirect('boards:detail', board.pk)
    else :
        return redirect('boards:detail', board.pk)
        
def comment_delete(request, board_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('boards:detail', board_pk)
    else :
        return redirect('boards:detail', board_pk)
        
def like(request, board_pk):
    board=get_object_or_404(Board, pk=board_pk)
    user=request.user
    
    if board.like_users.filter(pk=user.pk).exists():
        board.like_users.remove(user)
    else:
        board.like_users.add(user)
    return redirect('boards:detail', board_pk)

    