from rest_framework import serializers
from apps.app.models import (
    User, Genre, Cinema, Hall, Seat, Movie, Show_time, Booking
)

# Serialize app users
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# Serialize movie genres
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

# Serialize cinemas
class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'

# Serialize halls with cinema info
class HallSerializer(serializers.ModelSerializer):
    cinema = CinemaSerializer(read_only=True)
    cinema__id = serializers.PrimaryKeyRelatedField(
        queryset=Cinema.objects.all(), source='cinema', write_only=True
    )

    class Meta:
        model = Hall
        fields = ['id', 'name', 'total_seats', 'cinema', 'cinema__id']

# Serialize seats with hall info
class SeatSerializer(serializers.ModelSerializer):
    hall = HallSerializer(read_only=True)
    hall__id = serializers.PrimaryKeyRelatedField(
        queryset=Hall.objects.all(), source='hall', write_only=True
    )

    class Meta:
        model = Seat
        fields = ['id', 'row', 'number', 'hall', 'hall__id']

# Serialize movies with genres
class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, read_only=True)
    genre__id = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(), source='genre', many=True, write_only=True
    )

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration', 'language', 'rating', 'genre', 'genre__id']

# Serialize show times with movie and hall info
class ShowTimeSerializer(serializers.ModelSerializer):
    hall = HallSerializer(read_only=True)
    hall__id = serializers.PrimaryKeyRelatedField(
        queryset=Hall.objects.all(), source='hall', write_only=True
    )
    movie = MovieSerializer(read_only=True)
    movie__id = serializers.PrimaryKeyRelatedField(
        queryset=Movie.objects.all(), source='movie', write_only=True
    )

    class Meta:
        model = Show_time
        fields = ['id', 'start_time', 'end_time', 'price', 'hall', 'hall__id', 'movie', 'movie__id']

# Serialize bookings with user, show_time, and seat info
class BookingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user__id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True
    )
    show_time = ShowTimeSerializer(read_only=True)
    show_time__id = serializers.PrimaryKeyRelatedField(
        queryset=Show_time.objects.all(), source='show_time', write_only=True
    )
    seat = SeatSerializer(read_only=True)
    seat__id = serializers.PrimaryKeyRelatedField(
        queryset=Seat.objects.all(), source='seat', write_only=True
    )

    class Meta:
        model = Booking
        fields = ['id', 'booking_time', 'status', 'user', 'user__id', 'show_time', 'show_time__id', 'seat', 'seat__id']

# Serialize payments with booking info
#class PaymentSerializer(serializers.ModelSerializer):
    #booking = BookingSerializer(read_only=True)
    #booking__id = serializers.PrimaryKeyRelatedField(
      #  queryset=Booking.objects.all(), source='booking', write_only=True
    #)

    #class Meta:
      ##  model = Payment
       # fields = ['id', 'amount', 'payment_time', 'status', 'booking', 'booking__id', 'payment_method']