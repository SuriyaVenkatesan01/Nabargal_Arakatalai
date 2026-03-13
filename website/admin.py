from django.contrib import admin

from .models import Donation, DonationContribution, Event, BlogPost, BlogComment, ContactMessage, GalleryItem, Testimonial


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "raised_amount", "goal_amount", "donors_count", "is_active")
    list_filter = ("category", "is_active")
    search_fields = ("title", "category", "description")


@admin.register(DonationContribution)
class DonationContributionAdmin(admin.ModelAdmin):
    list_display = ("donation", "first_name", "email", "amount", "created_at")
    list_filter = ("donation", "created_at")
    search_fields = ("first_name", "last_name", "email")


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "event_date", "location", "is_active")
    list_filter = ("event_date", "is_active")
    search_fields = ("title", "description", "location", "organizer")


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "author_name", "created_at", "is_active")
    list_filter = ("created_at", "is_active")
    search_fields = ("title", "excerpt", "content", "author_name")


@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ("post", "name", "email", "created_at", "is_approved")
    list_filter = ("created_at", "is_approved")
    search_fields = ("name", "email", "message", "post__title")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name", "email", "subject", "message")


@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ("title", "media_type", "is_active", "created_at")
    list_filter = ("media_type", "is_active")
    search_fields = ("title", "video_url")


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "rating", "is_active", "created_at")
    list_filter = ("rating", "is_active")
    search_fields = ("name", "role", "message")

# Register your models here.
