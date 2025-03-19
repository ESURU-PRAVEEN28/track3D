from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if name and phone and email and message:
            subject = f"New Contact Form Submission from {name}"
            full_message = f"Name: {name}\nPhone: {phone}\nEmail: {email}\n\nMessage:\n{message}"

            send_mail(
                subject,
                full_message,
                'your_email@gmail.com',  # Replace with your email
                ['esurupraveen2004@gmail.com'],  # Recipient email
                fail_silently=False,
            )

            messages.success(request, "Your message has been sent successfully!")
            return render(request, "contact.html")

    return render(request, "contact.html")
