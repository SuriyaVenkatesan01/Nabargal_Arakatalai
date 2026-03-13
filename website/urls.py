from django.urls import path, include
from . import views


urlpatterns = [
    
    path("", views.home, name="home"),
    path("Sign-In/", views.sign_in, name="sign_in"),
    path("Sign-Up/", views.sign_up, name="sign_up"),
    path("gallery/", views.gallery, name="gallery"),
    path("testimonials/", views.testimonials, name="testimonials"),
    path("team/", views.team, name="team"),
    path("faq/", views.faq, name="faq"),
    path("privacy-policy/", views.privacy_policy, name="privacy_policy"),
    path("terms-conditions/", views.terms_conditions, name="terms_conditions"),
    path("about/", views.about, name="about"),
    path("donations/", views.donations, name="donations"),
    path("donation-details/<int:donation_id>/", views.donation_details, name="donation_details"),
    path("events/", views.events, name="events"),
    path("event-details/<int:event_id>/", views.event_details, name="event_details"),
    path("blog/", views.blog, name="blog"),
    path("blog-details/<int:blog_id>/", views.blog_details, name="blog_details"),
    path("contact/", views.contact, name="contact"),
    
    ]