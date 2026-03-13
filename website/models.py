from django.db import models


class Donation(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="donations/", blank=True, null=True)
    raised_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    donors_count = models.PositiveIntegerField(default=0)
    progress_percent = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class DonationContribution(models.Model):
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE, related_name="contributions")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.first_name} - {self.amount}"


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="events/", blank=True, null=True)
    event_date = models.DateField()
    start_time = models.CharField(max_length=50, blank=True)
    end_time = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=200, blank=True)
    organizer = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=120, default="Admin")
    excerpt = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to="blog/", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class BlogComment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.post.title}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    accepted_terms = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.subject}"


class GalleryItem(models.Model):
    MEDIA_IMAGE = "image"
    MEDIA_VIDEO = "video"
    MEDIA_CHOICES = [
        (MEDIA_IMAGE, "Image"),
        (MEDIA_VIDEO, "Video"),
    ]

    title = models.CharField(max_length=200, blank=True)
    media_type = models.CharField(max_length=10, choices=MEDIA_CHOICES, default=MEDIA_IMAGE)
    image = models.ImageField(upload_to="gallery/", blank=True, null=True)
    video_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title or f"Gallery Item #{self.id}"


class Testimonial(models.Model):
    name = models.CharField(max_length=120)
    role = models.CharField(max_length=120, blank=True)
    message = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)
    image = models.ImageField(upload_to="testimonials/", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
