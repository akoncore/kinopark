from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import User, Genre, Cinema, Hall, Seat, Movie, Show_time, Booking

# User model
@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = ("id", "name", "email")
    search_fields = ("name", "email")

# Genre model
@admin.register(Genre)
class GenreAdmin(ModelAdmin):
    list_display = ("id", "name")

# Cinema model
@admin.register(Cinema)
class CinemaAdmin(ModelAdmin):
    list_display = ("id", "name", "city", "address","created_at")
    list_filter = ("city",)
    list_editable = ("name",)
    fieldsets = (
        (
            "Cinema Information",
            {
                "fields": (
                    "name",
                    "city",
                    "address",
                )
            }
        ),
        (
            "Date and Time Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                    "deleted_at",
                )
            }
        )
    )
    readonly_fields = (
        "created_at",
        "updated_at",
        "deleted_at",
    )
    

# Hall model
@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "cinema", "total_seats")

# Seat model
@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ("id", "hall", "row", "number")

# Movie model
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "duration", "rating")
    filter_horizontal = ("genre",)

# Show_time model
@admin.register(Show_time)
class ShowTimeAdmin(admin.ModelAdmin):
    list_display = ("id", "movie", "hall", "start_time", "end_time", "price")

# Booking model
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "show_time", "seats", "status")

# Payment model
#@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "booking", "amount", "payment_method", "status")
    