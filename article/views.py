from django.shortcuts import render, get_object_or_404
from article.models import Article, Mail

def home(request):
    articles = Article.objects.all()

    recent_articles = Article.objects.order_by("-id")

    if request.method == "POST":
        data = request.POST.get("mail")
        mail = Mail.objects.create(mail=data)
        mail.save()
    context = {
        "articles": articles,
        "recent_articles": recent_articles
    }
    return render(request, "index.html", context=context)


def detail(request, pk):
    article = get_object_or_404(Article, id=pk)
    context = {
        "article": article
    }
    return render(request, 'blog-single.html', context)

