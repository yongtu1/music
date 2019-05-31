from django.shortcuts import render, redirect
from .models import Board, Comment
from models import Board

# Create your views here.
def index(request):
    boards = Board.objects.all()[::-1]#.order_by('-id')
    return render(request, 'boards/index.html/',{'boards':boards})

def new(request):
    if request.method == 'POST' :
        title = request.POST.get('title')
        content = request.POST.get('content')
        file=request.FILES.get('file')
        board = Board(title=title, content=content, file=file)
        board.save()
        return redirect('boards:detail', board.pk)
    else:
        return render(request, 'boards/new.html')
        
def detail(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    comments=board.comment_set.all()
    return render(request, 'boards/detail.html/',{'board':board, 'comments':comments})

def edit(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    if request.method=='POST':
        board.title=request.POST.get('title')
        board.content=request.POST.get('content')
        board.image=request.FILES.get('image')
        board.save()
        return redirect('boards:detail', board.pk)
    else:
        return render(request, 'boards/edit.html', {'board' :board})

def delete(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    if request.method=='POST':
        board.delete()
        return redirect('boards:index')
    else :
        return redirect('boards:detail',board.pk)
        
def comments_create(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    if request.method == 'POST':
        comment = Comment()
        comment.board = board
        comment.content = request.POST.get('content')
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