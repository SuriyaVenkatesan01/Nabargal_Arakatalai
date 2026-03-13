from decimal import Decimal, InvalidOperation

from django.db import transaction
from django.shortcuts import get_object_or_404, render

from .models import Donation, DonationContribution, Event, BlogPost, BlogComment, ContactMessage, GalleryItem, Testimonial

def home(request):
    return render(request, "home.html")

def sign_in(request):
    return render(request, "sign-in.html")
def sign_up(request):
    return render(request, "sign-up.html")
def gallery(request):
    items = GalleryItem.objects.filter(is_active=True).order_by("-created_at")
    return render(request, "gallery.html", {"items": items})
def testimonials(request):
    testimonials_qs = Testimonial.objects.filter(is_active=True).order_by("-created_at")
    return render(request, "testimonials.html", {"testimonials": testimonials_qs})
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
    donations_qs = Donation.objects.filter(is_active=True).order_by("-created_at")
    return render(request, "donations.html", {"donations": donations_qs})
def donation_details(request, donation_id):
    donation = get_object_or_404(Donation, id=donation_id, is_active=True)
    success = False
    errors = []

    if request.method == "POST":
        first_name = request.POST.get("first_name", "").strip()
        last_name = request.POST.get("last_name", "").strip()
        email = request.POST.get("email", "").strip()
        phone_number = request.POST.get("phone_number", "").strip()
        amount_raw = request.POST.get("amount", "").strip()

        if not first_name:
            errors.append("First name is required.")
        if not email:
            errors.append("Email is required.")

        amount = None
        try:
            amount = Decimal(amount_raw)
            if amount <= 0:
                errors.append("Amount must be greater than 0.")
        except (InvalidOperation, TypeError):
            errors.append("Amount is invalid.")

        if not errors:
            with transaction.atomic():
                DonationContribution.objects.create(
                    donation=donation,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone_number=phone_number,
                    amount=amount,
                )

                donation.raised_amount = (donation.raised_amount or Decimal("0")) + amount
                donation.donors_count = (donation.donors_count or 0) + 1
                if donation.goal_amount and donation.goal_amount > 0:
                    progress = int((donation.raised_amount / donation.goal_amount) * 100)
                    donation.progress_percent = min(100, progress)
                else:
                    donation.progress_percent = 0
                donation.save(update_fields=["raised_amount", "donors_count", "progress_percent"])
                success = True

    return render(
        request,
        "donation-details.html",
        {"donation": donation, "success": success, "errors": errors},
    )
def events(request):
    events_qs = Event.objects.filter(is_active=True).order_by("event_date")
    return render(request, "events.html", {"events": events_qs})
def event_details(request, event_id):
    event = get_object_or_404(Event, id=event_id, is_active=True)
    return render(request, "event-details.html", {"event": event})
def blog(request):
    posts = BlogPost.objects.filter(is_active=True).order_by("-created_at")
    return render(request, "blog.html", {"posts": posts})
def blog_details(request, blog_id):
    post = get_object_or_404(BlogPost, id=blog_id, is_active=True)
    success = False
    errors = []

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()

        if not name:
            errors.append("Name is required.")
        if not email:
            errors.append("Email is required.")
        if not message:
            errors.append("Comment is required.")

        if not errors:
            BlogComment.objects.create(
                post=post,
                name=name,
                email=email,
                message=message,
            )
            success = True

    comments = post.comments.filter(is_approved=True).order_by("-created_at")

    return render(
        request,
        "blog-details.html",
        {"post": post, "comments": comments, "success": success, "errors": errors},
    )
def contact(request):
    success = False
    errors = []

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone_number = request.POST.get("phone_number", "").strip()
        subject = request.POST.get("subject", "").strip()
        message = request.POST.get("message", "").strip()
        accepted_terms = request.POST.get("gridCheck") is not None

        if not name:
            errors.append("Name is required.")
        if not email:
            errors.append("Email is required.")
        if not subject:
            errors.append("Subject is required.")
        if not message:
            errors.append("Message is required.")
        if not accepted_terms:
            errors.append("Please accept terms and privacy policy.")

        if not errors:
            ContactMessage.objects.create(
                name=name,
                email=email,
                phone_number=phone_number,
                subject=subject,
                message=message,
                accepted_terms=accepted_terms,
            )
            success = True

    return render(request, "contact.html", {"success": success, "errors": errors})
