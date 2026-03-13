from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def sign_in(request):
    return render(request, "sign-in.html")
def sign_up(request):
    return render(request, "sign-up.html")
def gallery(request):
    return render(request, "gallery.html")
def testimonials(request):
    return render(request, "testimonials.html")
def team(request):
    return render(request, "team.html")
def faq(request):
    return render(request, "faq.html")
def privacy_policy(request):
    return render(request, "privacy-policy.html")
def terms_conditions(request):
    return render(request, "terms-conditions.html")
def about(request):
    return render(request, "about.html")
def donations(request):
    return render(request, "donations.html")
def donation_details(request, donation_id):
    return render(request, "donation-details.html", {"donation_id": donation_id})
def events(request):
    return render(request, "events.html")
def event_details(request, event_id):
    return render(request, "event-details.html", {"event_id": event_id})
def blog(request):
    return render(request, "blog.html")
def blog_details(request, blog_id):
    return render(request, "blog-details.html", {"blog_id": blog_id})
def contact(request):
    return render(request, "contact.html")
