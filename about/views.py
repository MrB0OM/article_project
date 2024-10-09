from django.shortcuts import render
from about.models import Feedback

def about(request):
    feedback = Feedback.objects.all()
    context = {
        "feedbacks": feedback
    }
    return render(request, 'about.html', context=context)