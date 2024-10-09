from django.shortcuts import render
from contact.models import Contact

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")

        email = request.POST.get("email")

        subject = request.POST.get("subject")

        comment = request.POST.get("comment")

        obj = Contact.objects.create(name=name,
                                     email=email,
                                     subject=subject,
                                     comment=comment)
        obj.save()

    return render(request, 'contact.html')
