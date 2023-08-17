from django.shortcuts import render, redirect
from room.models import *
from datetime import datetime, timedelta
from django.utils.dateparse import parse_date
import random
# Create your views here.

# Email Imports
from django.template import loader
from django.core.mail import EmailMultiAlternatives


def AccomodationView(request):
    rooms = RoomsModel.objects.all()
    # Get the current date and time
    current_datetime = datetime.now()
    # Get the day of the week as an integer (0 for Monday, 1 for Tuesday, and so on)
    day_of_week = current_datetime.weekday()

    # Check if the day falls on Monday to Thursday (0 to 3)
    if day_of_week <= 3:
        week_day = 'weekday'
    else:
        week_day = 'weekend'

    context = {
        "rooms": rooms,
        "week_day": week_day
    }

    return render(request, 'room/accomodations.html', context)


def CottageDetailsView(request, id):
    room = RoomsModel.objects.get(id=id)
    # Get the current date and time
    current_datetime = datetime.now()
    # Get the day of the week as an integer (0 for Monday, 1 for Tuesday, and so on)
    day_of_week = current_datetime.weekday()

    # Check if the day falls on Monday to Thursday (0 to 3)
    if day_of_week <= 3:
        week_day = 'weekday'
    else:
        week_day = 'weekend'

    context = {
        "room": room,
        "week_day": week_day
    }

    return render(request, 'room/cottageDetails.html', context)


def BookCottageView(request, id):
    room = RoomsModel.objects.get(id=id)
    # Get the current date and time
    current_datetime = datetime.now()
    # Get the day of the week as an integer (0 for Monday, 1 for Tuesday, and so on)
    day_of_week = current_datetime.weekday()

    # Check if the day falls on Monday to Thursday (0 to 3)
    if day_of_week <= 3:
        week_day = 'weekday'
    else:
        week_day = 'weekend'

    if request.method == 'POST' and 'submit_reservation' in request.POST:
        reserve_room = ReservedRoomModel()
        reserve_room.ref = random.randrange(0, 10000000)
        reserve_room.room = room
        reserve_room.firstName = request.POST.get('firstName')
        reserve_room.lastName = request.POST.get('lastName')
        reserve_room.phone = request.POST.get('phone')
        email = request.POST.get('email')
        if email:
            reserve_room.email = email

        # get check in and checkout dates from session
        booking_info = request.session.get('booking_data')
        reserve_room.check_in = booking_info.get('checkin')
        reserve_room.check_out = booking_info.get('checkout')
        reserve_room.room_total = booking_info.get('room_total')
        reserve_room.breakfast_total = booking_info.get('breakfast_total')
        reserve_room.grand_total = booking_info.get('grand_total')
        reserve_room.save()

        # save all dates with breakfast to model 1st check which group it belongs to
        food_list = request.session.get('food_dates', [])
        for i in food_list:
            input_date_string = i
            # Define the input date format
            input_date_format = "%d %a %B %Y"
            # Parse the input date string
            input_date = datetime.strptime(
                input_date_string, input_date_format).date()

            if input_date.weekday() <= 3:  # Monday to Thursday (0 to 3)
                # create reserved date model
                reserve_date = ReservedDates()
                reserve_date.ref = reserve_room.ref
                reserve_date.date = input_date
                reserve_date.room_pirce = room.room_prices.room_only
                breakfast_price = room.room_prices.room_breakfast - room.room_prices.room_only
                reserve_date.breakfast_price = breakfast_price
                reserve_date.breakfast = 'Yes'
                reserve_date.weekday = 'weekday'
                reserve_date.save()
                reserve_room.user_dates.add(reserve_date)

            else:  # Friday to Sunday (4 to 6)
                # create reserved date model
                reserve_date = ReservedDates()
                reserve_date.ref = reserve_room.ref
                reserve_date.date = input_date
                reserve_date.room_pirce = room.room_prices.room_weekend
                breakfast_price = room.room_prices.room_weeknd_breakfast - \
                    room.room_prices.room_weekend
                reserve_date.breakfast_price = breakfast_price
                reserve_date.breakfast = 'Yes'
                reserve_date.weekday = 'weekend'
                reserve_date.save()
                reserve_room.user_dates.add(reserve_date)

        # ************ send email start ******************
        print('email start')
        name = reserve_room.firstName
        email = reserve_room.email
        room_name = reserve_room.room.title
        guests = reserve_room.room.people

        template = loader.get_template('partials/email-txt.txt')
        context = {
            'name': name,
            'room_name': room_name,
            'guests': guests,
            'ref': reserve_room.ref,
            'checkIn': reserve_room.check_in,
            'checkOut': reserve_room.check_out,
            'total': reserve_room.grand_total,
            'email': email,
            'food_list': food_list
        }
        message = template.render(context)

        list = [reserve_room.email, 'sekgoeng.booking@gmail.com']
        email = EmailMultiAlternatives(
            "SEKGOENG RESERVATION CONFIRMATION", message,  # subject
            "Booking",
            bcc=list
        )

        # convert html and css inside email.txt to html
        email.content_subtype = 'html'

        email.send()
        print('email sent')
        # ************ send email end ******************

        return redirect('message')

    context = {
        "room": room,
        "week_day": week_day
    }

    return render(request, 'room/bookCottage.html', context)


def BreakfastView(request, id):

    if request.method == 'POST':
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')

        if checkout:
            room = RoomsModel.objects.get(id=id)
            breakfastPirce = room.breakfast_price - room.price
            # Get all the dates from check-in to check-out
            check_in_date = parse_date(checkin)
            check_out_date = parse_date(checkout)
            date_list = [
                check_in_date + timedelta(days=i) for i in range((check_out_date - check_in_date).days + 1)]

            # Initialize lists to store the days in different categories
            weekdays = []
            weekday_breakfast = room.room_prices.room_breakfast - room.room_prices.room_only

            weekends = []
            weekend_breakfast = room.room_prices.room_weeknd_breakfast - \
                room.room_prices.room_weekend

            # Iterate through the date range between check-in and check-out dates
            current_date = check_in_date
            while current_date <= check_out_date:
                if current_date.weekday() <= 3:  # Monday to Thursday (0 to 3)
                    weekdays.append(current_date.strftime('%d %a %B %Y'))
                else:  # Friday to Sunday (4 to 6)
                    weekends.append(current_date.strftime('%d %a %B %Y'))

                # Increment the current date by one day
                current_date += timedelta(days=1)

            context = {
                "room": room,
                "weekday_breakfast": weekday_breakfast,
                "weekend_breakfast": weekend_breakfast,
                "date_list": date_list,
                "weekdays": weekdays,
                "weekends": weekends
            }

            return render(request, 'partials/breakfastPartial.html', context)

    return render(request, 'partials/breakfastPartial.html')


def CottageInfoView(request, id):
    if request.method == 'POST':
        room = RoomsModel.objects.get(id=id)
        weekday_breakfast = room.room_prices.room_breakfast - room.room_prices.room_only
        weekend_breakfast = room.room_prices.room_weeknd_breakfast - \
            room.room_prices.room_weekend
        selected_dates = request.POST.getlist('breakfast_value')

        # ******* check which days belong to which category for room prices *********
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        # Get all the dates from check-in to check-out
        check_in_date = parse_date(checkin)
        check_out_date = parse_date(checkout)

        # separate the prices
        weekday_price = 0
        weekend_price = 0

        # Iterate through the date range between check-in and check-out dates
        current_date = check_in_date
        while current_date <= check_out_date:
            if current_date.weekday() <= 3:  # Monday to Thursday (0 to 3)
                weekday_price = room.room_prices.room_only + weekday_price
            else:  # Friday to Sunday (4 to 6)
                weekend_price = room.room_prices.room_weekend + weekend_price

            # Increment the current date by one day
            current_date += timedelta(days=1)

        # ******* check which days belong to which category for breakfast prices *********
        weekdays = []
        weekends = []
        weekday_breakfast_total = 0
        weekend_breakfast_total = 0

        for i in selected_dates:
            input_date_string = i
            # Define the input date format
            input_date_format = "%d %a %B %Y"
            # Parse the input date string
            input_date = datetime.strptime(
                input_date_string, input_date_format).date()

            if input_date.weekday() <= 3:  # Monday to Thursday (0 to 3)
                weekdays.append(current_date.strftime('%Y-%m-%d'))
                weekday_breakfast_total = weekday_breakfast_total + weekday_breakfast
            else:  # Friday to Sunday (4 to 6)
                weekends.append(current_date.strftime('%Y-%m-%d'))
                weekend_breakfast_total = weekend_breakfast_total + weekend_breakfast

        total = 0
        sub_total = weekday_price + weekend_price
        breakfast_total = weekday_breakfast_total + weekend_breakfast_total
        total = total + sub_total + breakfast_total

        booking_details = {
            'room_total': float(sub_total),
            'breakfast_total': float(breakfast_total),
            'grand_total': float(total),
            'checkin': checkin,
            'checkout': checkout
        }

        # Save the dictionary in the session
        request.session['booking_data'] = booking_details
        request.session['food_dates'] = selected_dates

        context = {
            "total": total
        }

    return render(request, 'partials/cottageInfo.html', context)


def MessageView(request):
    return render(request, 'room/message.html')
