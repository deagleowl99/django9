from .models import Article
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login

def archive(request):
    return render(request, 'article.html', {"posts":Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'archive.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404
		
		
		
def check(name):
	try:
		article=Article.objects.get(title=name);
		if name==article.title:
			return True
		else:
			return False
			
	except Article.DoesNotExist:
		return False
			
def create_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            # обработать данные формы, если метод POST
            form = {
                'text': request.POST["text"], 'title': request.POST["title"]
            }
            # в словаре form будет храниться информация, введенная пользователем
            if(check(form['title'])):
                form['errors']='Не уникальное имя'
                return render(request, 'create_post.html', {'form': form})
            else:
                if form["text"] and form["title"]:
                    # еслиполязаполненыбезошибок
                    Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                    article_id = Article.objects.latest('id').pk
                    return redirect('get_article', article_id)
                    # перейти на страницу поста
                else:
                    # если введенные данные некорректны
                    form['errors'] = u"У вас имеются пустые поля!"
                    return render(request, 'create_post.html', {'form': form})
        else:
            # просто вернуть страницу с формой, если метод GET
            return render(request, 'create_post.html', {})
    else:
        raise Http404



def create_user(request):
    if request.method == "POST":
        form = {
            'login': request.POST["login"],
            'mail': request.POST["mail"],
            'password': request.POST["password"]
        }
        if form["login"] and form["mail"] and form["password"]:
            try:
                User.objects.get(username = form["login"])
                form['errors'] = u"Не уникальное имя пользователя!"
                return render(request, 'create_user.html', {'form': form})
            except User.DoesNotExist:
                User.objects.create_user(form["login"], form["mail"], form["password"])
                return redirect('archive')
        else:
            form['errors'] = u"У вас имеются пустые поля!"
            return render(request, 'create_user.html', {'form': form})
    else:
        return render(request, 'create_user.html', {})

def login_user(request):
    if request.method == "POST":
        form = {
            'login': request.POST["login"],
            'password': request.POST["password"]
        }
        if form["login"] and form["password"]:
            user = authenticate(username=form["login"], password=form["password"])
            if user == None:
                form['errors'] = u"Неверный логин или пароль"
                return render(request, 'login_user.html', {'form': form})
            else:
                login(request, user) 
                return redirect('archive')
        else:
            form['errors'] = u"У вас имеются пустые поля!"
            return render(request, 'login_user.html', {'form': form})
    else:
        return render(request, 'login_user.html', {})
    
def test(request):
        form = {'text': request.method}
        return render(request, 'test.html', {'form': form})	
