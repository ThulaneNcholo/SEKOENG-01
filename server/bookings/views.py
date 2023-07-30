from django.shortcuts import render, redirect
from .models import BookedModel, BookingCateredModel
from room.models import *
from datetime import date, datetime, timedelta
import json
import random
from django.db.models import Q
from django.utils.dateparse import parse_date
from django.db.models import Max


# Create your views here.


def AvailabilityCheck(request, id):
    room = RoomsModel.objects.get(id=id)
    # Clear session after adding the features
    food_list = request.session.get('Food_list', [])
    total = request.session.get('total_fee')
    dates_str = request.session.get('dates')

    if food_list:
        del request.session['Food_list']
        request.session.modified = True
        request.session.save()

    if total:
        del request.session['total_fee']
        request.session.modified = True
        request.session.save()

    if dates_str:
        del request.session['dates']
        request.session.modified = True
        request.session.save()

    context = {
        "room": room
    }

    return render(request, 'bookings/availability.html', context)


def CheckRoomAvailabity(request):

    if request.method == 'POST':
        roomID = request.POST.get('roomID')
        room = RoomsModel.objects.get(id=roomID)
        checkIn = request.POST.get('checkIn')
        checkout = request.POST.get('checkOut')

        check_in_days = datetime.strptime(checkIn, '%Y-%m-%d').date()
        check_out_days = datetime.strptime(checkout, '%Y-%m-%d').date()

        num_of_days = (check_out_days - check_in_days).days
        fee = room.price
        food_fee = 0
        request.session['total_fee'] = float(fee)

        date_list = []

        room_check = BookedModel.objects.filter(
            room=room, check_in_date__lte=checkout, check_out_date__gte=checkIn)

        if room_check.exists():
            result_view = 'not available'
        else:
            result_view = 'available'
            fee = room.price * num_of_days
            request.session['total_fee'] = float(fee)
            check_in_days = datetime.strptime(checkIn, '%Y-%m-%d').date()
            check_out_days = datetime.strptime(checkout, '%Y-%m-%d').date()

            date_list = []

            current_date = check_in_days
            while current_date <= check_out_days:
                date_list.append(current_date)
                current_date += timedelta(days=1)

        dates_str = [d.isoformat() for d in date_list]
        request.session['dates'] = json.dumps(dates_str)

    context = {
        "result_view": result_view,
        "fee": fee,
        "food_fee": food_fee,
        "date_list": date_list
    }

    return render(request, 'partials/room_check.html', context)


def CatedFoodView(request, id):
    food_list = request.session.get('Food_list', [])
    if request.method == 'POST':
        confirm = request.POST.get('confirm')
        if confirm == 'None':
            option = request.POST.get('option')
            date = request.POST.get('date')
            status = request.POST.get('status')

            if status == 'add':
                if id == 1:
                    food_data = {
                        'id': id,
                        'date': date,
                        'option': 'breakfast',
                        'price': 70
                    }

                    food_list.append(food_data)
                    request.session['Food_list'] = food_list

                elif id == 2:
                    food_data = {
                        'id': id,
                        'date': date,
                        'option': 'lunch',
                        'price': 90
                    }
                    food_list.append(food_data)
                    request.session['Food_list'] = food_list
                elif id == 3:
                    food_data = {
                        'id': id,
                        'date': date,
                        'option': 'dinner',
                        'price': 120
                    }
                    food_list.append(food_data)
                    request.session['Food_list'] = food_list

            elif status == 'remove':
                if id == 1:
                    for i in range(len(food_list)):
                        if food_list[i]['date'] == date:
                            del food_list[i]
                            request.session['Food_list'] = food_list
                            break

                elif id == 2:
                    for i in range(len(food_list)):
                        if food_list[i]['date'] == date:
                            del food_list[i]
                            request.session['Food_list'] = food_list
                            break

                elif id == 3:
                    for i in range(len(food_list)):
                        if food_list[i]['date'] == date:
                            del food_list[i]
                            request.session['Food_list'] = food_list
                            break
        else:
            print('confirm')

    room_total = request.session.get('total_fee')

    food_fee = 0
    for price in food_list:
        price = price['price']
        food_fee = price + food_fee

    fee = float(room_total) + float(food_fee)

    context = {
        "food_fee": food_fee,
        "fee": fee,
        "room_total": room_total
    }

    return render(request, 'partials/fee_paid.html', context)


def ConfirmBookingView(request):

    if request.method == 'POST':
        food_list = request.session.get('Food_list', [])
        dates_str = request.session.get('dates')
        confirmation_data = request.session.get('confirmation', [])

        if dates_str:
            dates = [date.fromisoformat(d) for d in json.loads(dates_str)]
            # Perform operations with the dates list

        for i in food_list:
            food_date = datetime.strptime(i['date'], "%B %d, %Y").date()

            for data in dates:
                if food_date == data:
                    print('available')
                    if confirmation_data:
                        print('yes data')
                        for info in confirmation_data:
                            list_date = datetime.strptime(
                                info['date'], "%B %d, %Y").date()
                            if list_date == food_date:
                                print('yes date')
                            else:
                                print('no date')

                    else:
                        print('no data')
                        if i['option'] == 'breakfast':
                            print('breakfast', i['date'])
                            confirmationed = {
                                'date': i['date'],
                                'breakfast': 'Yes',
                                'lunch': 'No',
                                'dinner': 'No',
                            }
                            confirmation_data.append(confirmationed)
                            request.session['confirmation'] = confirmation_data

                            break
                        elif i['option'] == 'lunch':
                            print('lunch', i['date'])
                            confirmationed = {
                                'date': i['date'],
                                'breakfast': 'No',
                                'lunch': 'Yes',
                                'dinner': 'No',
                            }
                            confirmation_data.append(confirmationed)
                            request.session['confirmation'] = confirmation_data
                            break
                        elif i['option'] == 'dinner':
                            confirmationed = {
                                'date': i['date'],
                                'breakfast': 'No',
                                'lunch': 'No',
                                'dinner': 'Yes',
                            }
                            confirmation_data.append(confirmationed)
                            request.session['confirmation'] = confirmation_data
                            break

                    # for confirmed in confirmation_data:
                    #     if confirmed['date'] == food_date:
                    #         print('in session')
                    #     else:
                    #         print('not session')

                # else:
                #     print('not available')

            # confirmation_data = {
            #     'date': food_date,
            #     'breakfast': 'Yes',
            #     'lunch': 'Yes',
            #     'dinner' : 'Yes',
            #     "price ": i['price']
            # }

    context = {
        "dates": dates,
    }

    return render(request, 'bookings/confirm.html', context)


# *******************************  New Views ***********************************************************

def SelectDatesView(request, id):
    room = RoomsModel.objects.get(id=id)
    # Clear session after adding the features
    dates = request.session.get('user_dates', [])
    roomID = request.session.get('room_id')
    guestCount = request.session.get('guest')

    if dates:
        del request.session['user_dates']
        request.session.modified = True
        request.session.save()

    if roomID:
        del request.session['room_id']
        request.session.modified = True
        request.session.save()

    if guestCount:
        del request.session['guest']
        request.session.modified = True
        request.session.save()

    print(dates)
    print(roomID)
    print(guestCount)

    context = {
        "room": room
    }
    return render(request, 'roomBooking/selectDate.html', context)


def CheckRoomView(request):
    if request.method == 'POST':
        roomID = request.POST.get('roomID')
        room = RoomsModel.objects.get(id=roomID)
        checkIn = request.POST.get('checkIn')
        checkout = request.POST.get('checkOut')
        guests = request.POST.get('guests')
        uuidID = request.POST.get('uuid')
        print(uuidID)
        # save guests count to session
        request.session['guest'] = guests

        checkoutFilter = BookedModel.objects.filter(
            room=room, check_out_date=checkIn)
        if checkoutFilter:
            print('true')
        else:
            print('false')

        # Check if room is not booked yet
        bookedChecked = BookedModel.objects.filter(
            Q(check_in_date__lte=checkout, check_out_date__gte=checkIn) & ~Q(check_out_date=checkIn))
        if bookedChecked:
            # **** dates selected are already book  ****
            print('booked')

            latest_checkout = bookedChecked.latest(
                'check_out_date').check_out_date
            next_available_date = latest_checkout

            # next_available_date = checkout

            context = {
                "next_available_date": next_available_date
            }

        else:
            print('available')
            # save room id to session
            request.session['room_id'] = roomID

            # **** dates selected are available  ****
            # get all the dates from check in to checkout
            check_in_days = datetime.strptime(checkIn, '%Y-%m-%d').date()
            check_out_days = datetime.strptime(checkout, '%Y-%m-%d').date()

            date_list = []

            current_date = check_in_days
            while current_date <= check_out_days:
                date_list.append(current_date)
                current_date += timedelta(days=1)

            # create dictionary of all the dates
            booking_dates = request.session.get('user_dates', [])

            # Delete Session Data doesnt work start
            if booking_dates:
                # Assign an empty list to clear the session variable
                request.session.flush()
                request.session.save()
                print('cleaned')
            else:
                print('not cleaned')
            # Delete Session Data doesnt work end

            for dateData in date_list:
                reserved_dates = {
                    'date': str(dateData),
                    'breakfast': 'No',
                    'breakfast_fee': 0,
                    'lunch': 'No',
                    'lunch_fee': 0,
                    'dinner': 'No',
                    'dinner_fee': 0,
                    "room_fee": float(room.price)
                }

                booking_dates.append(reserved_dates)
                request.session['user_dates'] = booking_dates

            context = {
                "booking_dates": booking_dates
            }

    return render(request, 'roomPartials/checkRoom.html', context)


def BookingFeeView(request, id):
    if request.method == 'POST':
        dateSelected = request.POST.get('date')
        action = request.POST.get('status')
        guestCount = request.session.get('guest')

        # get all the dates in session storage to update food selected
        booking_dates = request.session.get('user_dates', [])
        for update_data in booking_dates:
            if update_data['date'] == dateSelected:
                if action == 'add':
                    if id == 1:
                        update_data['breakfast'] = 'Yes'
                        update_data['breakfast_fee'] = 70 * int(guestCount)
                        request.session['user_dates'] = booking_dates
                        break
                    elif id == 2:
                        update_data['lunch'] = 'Yes'
                        update_data['lunch_fee'] = 100 * int(guestCount)
                        request.session['user_dates'] = booking_dates
                        break
                    elif id == 3:
                        update_data['dinner'] = 'Yes'
                        update_data['dinner_fee'] = 120 * int(guestCount)
                        request.session['user_dates'] = booking_dates
                        break
                elif action == 'remove':
                    if id == 1:
                        update_data['breakfast'] = 'No'
                        update_data['breakfast_fee'] = 0
                        request.session['user_dates'] = booking_dates
                        break
                    elif id == 2:
                        update_data['lunch'] = 'No'
                        update_data['lunch_fee'] = 0
                        request.session['user_dates'] = booking_dates
                        break
                    elif id == 3:
                        update_data['dinner'] = 'No'
                        update_data['dinner_fee'] = 0
                        request.session['user_dates'] = booking_dates
                        break

        # *** Get Food totals plus grand food total together and room total fee ***
        breafast_total = 0
        lunch_total = 0
        dinner_total = 0
        room_total_fee = 0
        for data in booking_dates:
            breafast_total = breafast_total + data['breakfast_fee']
            lunch_total = lunch_total + data['lunch_fee']
            dinner_total = dinner_total + data['dinner_fee']
            room_total_fee = room_total_fee + data['room_fee']

        food_total = breafast_total + lunch_total + dinner_total
        grand_total = food_total + room_total_fee

        context = {
            "food_total": food_total,
            "room_total_fee": room_total_fee,
            "grand_total": grand_total
        }

    return render(request, 'roomPartials/bookingsFee.html', context)


def DetailsConfirmView(request):
    if request.method == 'POST':
        booking_dates = request.session.get('user_dates', [])
        # *** Get Food totals plus grand food total together and room total fee ***
        breakfast_total = 0
        lunch_total = 0
        dinner_total = 0
        room_total_fee = 0
        for data in booking_dates:
            breakfast_total = breakfast_total + data['breakfast_fee']
            lunch_total = lunch_total + data['lunch_fee']
            dinner_total = dinner_total + data['dinner_fee']
            room_total_fee = room_total_fee + data['room_fee']

        food_total = breakfast_total + lunch_total + dinner_total
        grand_total = food_total + room_total_fee

        context = {
            "booking_dates": booking_dates,
            "food_total": food_total,
            "room_total_fee": room_total_fee,
            "grand_total": grand_total
        }
    return render(request, 'roomPartials/confirmBooking.html', context)


def UserDetailsView(request):
    if request.method == 'POST':
        referance = random.randrange(0, 10000000)
        booking_dates = request.session.get('user_dates', [])
        # *** Get Food totals plus grand food total together and room total fee ***
        breakfast_total = 0
        lunch_total = 0
        dinner_total = 0
        room_total_fee = 0
        for data in booking_dates:
            breakfast_total = breakfast_total + data['breakfast_fee']
            lunch_total = lunch_total + data['lunch_fee']
            dinner_total = dinner_total + data['dinner_fee']
            room_total_fee = room_total_fee + data['room_fee']

        food_total = breakfast_total + lunch_total + dinner_total
        grand_total = food_total + room_total_fee

        context = {
            "referance": referance,
            "grand_total": grand_total
        }

    return render(request, 'roomPartials/userDetails.html', context)


def CompleteBookingView(request):
    if request.method == 'POST':
        # get room id from session
        roomID = request.session.get('room_id')
        room = RoomsModel.objects.get(id=roomID)

        # get check-in date and check-out date only
        booking_dates = request.session.get('user_dates', [])
        first_date = min(booking_dates, key=lambda x: x['date'])
        last_date = max(booking_dates, key=lambda x: x['date'])
        check_in = first_date['date']
        check_out = last_date['date']

        # check if room still available
        bookedChecked = BookedModel.objects.filter(
            room=room, check_in_date__lte=check_out, check_out_date__gte=check_in)

        if bookedChecked:
            # **** dates selected are already book  ****
            print('booked')
        else:
            # get all total
            breakfast_total = 0
            lunch_total = 0
            dinner_total = 0
            room_total_fee = 0
            for data in booking_dates:
                breakfast_total = breakfast_total + data['breakfast_fee']
                lunch_total = lunch_total + data['lunch_fee']
                dinner_total = dinner_total + data['dinner_fee']
                room_total_fee = room_total_fee + data['room_fee']

            food_total = breakfast_total + lunch_total + dinner_total
            grand_total = food_total + room_total_fee

            # get generated ref
            referance = request.POST.get('referance')

            # save data to booked model
            save_booking = BookedModel()
            save_booking.room = room
            save_booking.ref = referance
            save_booking.firstName = request.POST.get('firstName')
            save_booking.lastName = request.POST.get('lastName')
            save_booking.phone = request.POST.get('phone')
            save_booking.email = request.POST.get('email')
            save_booking.check_in_date = check_in
            save_booking.check_out_date = check_out
            save_booking.food_total = food_total
            save_booking.room_total = room_total_fee
            save_booking.grand_total = grand_total
            save_booking.save()

            # add catered model and save to the booked model room
            for data in booking_dates:
                add_catered = BookingCateredModel()
                add_catered.ref = referance
                add_catered.date = data['date']
                add_catered.breakfast = data['breakfast']
                add_catered.lunch = data['lunch']
                add_catered.dinner = data['dinner']
                add_catered.save()
                catedModel = BookingCateredModel.objects.get(id=add_catered.id)
                save_booking.catered.add(catedModel)

    return render(request, 'roomPartials/complete.html')


# *******************************  NEW BOOKING VIEWS ***********************************************************
def BookRoomDateView(request, id):
    room = RoomsModel.objects.get(id=id)
    print('room')

    context = {
        "room": room
    }

    return render(request, 'BookRoom/book_date.html', context)

# Room check availability results view partial


def RoomResultsview(request):
    if request.method == 'POST':
        roomID = request.POST.get('roomID')
        room = RoomsModel.objects.get(id=roomID)
        checkIn = request.POST.get('checkIn')
        checkout = request.POST.get('checkOut')
        guests = request.POST.get('guests')
        uuidID = request.POST.get('uuid')
        print(guests)

        # Check if room is not booked yet
        bookedChecked = BookedModel.objects.filter(
            Q(room=room, check_in_date__lte=checkout, check_out_date__gte=checkIn, status='Complete') & ~Q(check_out_date=checkIn))

        if bookedChecked:
            # print('booked')
            max_checkout_date = bookedChecked.aggregate(Max('check_out_date'))[
                'check_out_date__max']
            next_available_date = max_checkout_date

            context = {
                "available_date": next_available_date
            }

        else:
            uuidCheck = BookedModel.objects.filter(
                Q(uuid=uuidID, status='Cart')).exists()

            # check if uuid is in cart
            if uuidCheck:
                userCart = BookedModel.objects.get(
                    Q(uuid=uuidID, status='Cart'))
                userCart.check_in_date = checkIn
                userCart.check_out_date = checkout
                userCart.guests = guests
                userCart.save()

                # Remove existing food dates
                userCart.catered.all().delete()

                # Get all the dates from check-in to check-out
                check_in_date = parse_date(checkIn)
                check_out_date = parse_date(checkout)
                date_list = [
                    check_in_date + timedelta(days=i) for i in range((check_out_date - check_in_date).days + 1)]

                # Create and associate new BookingCateredModel instances
                catered_models = [BookingCateredModel(
                    ref=uuidID, date=date) for date in date_list]
                BookingCateredModel.objects.bulk_create(catered_models)
                userCart.catered.add(*catered_models)

                context = {
                    "foodDates": userCart,

                }

            else:
                roomCart = BookedModel()
                roomCart.uuid = uuidID
                roomCart.ref = uuidID
                roomCart.room = room
                roomCart.check_in_date = checkIn
                roomCart.check_out_date = checkout
                roomCart.guests = guests
                roomCart.status = 'Cart'
                roomCart.save()

                # Get all the dates from check-in to check-out
                check_in_date = parse_date(checkIn)
                check_out_date = parse_date(checkout)
                date_list = [
                    check_in_date + timedelta(days=i) for i in range((check_out_date - check_in_date).days + 1)]

                # Create and associate new BookingCateredModel instances
                catered_models = [BookingCateredModel(
                    ref=uuidID, date=date) for date in date_list]
                BookingCateredModel.objects.bulk_create(catered_models)
                roomCart.catered.add(*catered_models)

                foodDates = BookedModel.objects.get(id=roomCart.id)

                context = {
                    "foodDates": foodDates
                }

    return render(request, 'BookRoomPartials/room_results.html', context)


def RoomPriceView(request, id):
    if request.method == 'POST':
        cartID = request.POST.get('cartID')
        status = request.POST.get('status')
        date_selected = request.POST.get('date')
        selected_date = datetime.strptime(date_selected, "%B %d, %Y").date()
        formatted_date = selected_date.strftime("%Y-%m-%d")

        bookingProfile = BookedModel.objects.get(id=cartID)
        userDate = bookingProfile.catered.get(date=formatted_date)
        guests = bookingProfile.guests

        if status == 'add':
            if id == 1:
                userDate.breakfast = 'Yes'
                breakfast = 70
                userDate.breakfastFee = guests * breakfast

            elif id == 2:
                userDate.lunch = 'Yes'
                lunch = 100
                userDate.lunchFee = guests * lunch
            elif id == 3:
                userDate.dinner = 'Yes'
                dinner = 120
                userDate.dinnerFee = guests * dinner

        elif status == 'remove':
            if id == 1:
                userDate.breakfast = ''
                userDate.breakfastFee = 0

            elif id == 2:
                userDate.lunch = ''
                userDate.lunchFee = 0
            elif id == 3:
                userDate.dinner = ''
                userDate.dinnerFee = 0

        userDate.save()

        # ****** room total fee *******
        daysCount = bookingProfile.catered.count()
        roomFee = bookingProfile.room.price
        roomTotal = daysCount * roomFee

        # ****** Food total fee *******
        food_prices = bookingProfile.catered.all()
        breakFast_fee = 0
        lunch_fee = 0
        dinner_fee = 0

        for price in food_prices:
            if price.breakfastFee:
                breakFast_fee = breakFast_fee + price.breakfastFee

            if price.lunchFee:
                lunch_fee = lunch_fee + price.lunchFee

            if price.dinnerFee:
                dinner_fee = dinner_fee + price.dinnerFee

        foodTotal = breakFast_fee + lunch_fee + dinner_fee

        context = {
            "roomTotal": roomTotal,
            "foodTotal": foodTotal,
            "bookingProfile": bookingProfile
        }

    return render(request, 'BookRoomPartials/roomPrice.html', context)


def RoomConfirmationDetailsView(request):
    if request.method == 'POST':
        uuid = request.POST.get('uuid')
        bookingProfile = BookedModel.objects.get(uuid=uuid)
        userDates = bookingProfile.catered.all()

        # ****** room total fee *******
        daysCount = bookingProfile.catered.count()
        roomFee = bookingProfile.room.price
        roomTotal = daysCount * roomFee

        # ****** Food total fee *******
        food_prices = bookingProfile.catered.all()
        breakFast_fee = 0
        lunch_fee = 0
        dinner_fee = 0

        for price in food_prices:
            if price.breakfastFee:
                breakFast_fee = breakFast_fee + price.breakfastFee

            if price.lunchFee:
                lunch_fee = lunch_fee + price.lunchFee

            if price.dinnerFee:
                dinner_fee = dinner_fee + price.dinnerFee

        foodTotal = breakFast_fee + lunch_fee + dinner_fee
        grandtotal = roomTotal + foodTotal

        context = {
            "userDetails": bookingProfile,
            "userDates": userDates,
            "roomTotal": roomTotal,
            "foodTotal": foodTotal,
            "grandtotal": grandtotal
        }

    return render(request, 'BookRoomPartials/roomConfirmation.html', context)


def UserInformationView(request):
    if request.method == 'POST':
        grand_total = request.POST.get('grand_total')
        referance = random.randrange(0, 10000000)

        context = {
            "grand_total": grand_total,
            "referance": referance
        }

    return render(request, 'BookRoomPartials/user_information.html', context)


def BookingCompletionView(request):
    # bookingProfile.firstName = request.POST.get('firstName')
    # bookingProfile.lastName = request.POST.get('lastName')
    # bookingProfile.phone = request.POST.get('phone')
    # bookingProfile.email = request.POST.get('email')
    return render(request, 'BookRoomPartials/completeBooking.html')
