from ssl import ALERT_DESCRIPTION_ACCESS_DENIED
from tkinter.messagebox import YES
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, render, HttpResponse
from django.urls import reverse
from django.contrib.auth import logout
from .forms import AmenitiesForm
from .models import amenitie, pg_owner, pg_amenities
from .models import student
from .models import adm
from django.core.files.storage import FileSystemStorage
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def add(request, name):

    own = pg_owner.objects.get(name=name)
    pg_amenity = pg_amenities.objects.filter(pg_id__name=own.name)

    return render(request, 'add.html', {'owner': own, 'pg_amenities': pg_amenity})


def book(request, pg_id):
    if (request.method == 'POST'):
        stud = student()
        stud.name = request.POST['name']
        stud.email = request.POST['email']
        stud.contact = request.POST['contact']
        stud.duration = request.POST['duration']
        stud.sharing = request.POST['sharing']
        stud.purpose = request.POST['purpose']
        stud.pg_id = pg_owner.objects.get(id=pg_id)
        stud.save()
        return redirect(reverse("home"))
    else:

        return render(request, 'book.html', {'pg_id': pg_id, })
    # return render(request, 'book.html')


def booking_details(request):
    user = student.objects.all()
    return render(request, 'booking_details.html', {'user': user})


def booking_details_pg(request, pg_id):
    user = student.objects.filter(pg_id=pg_id)
    return render(request, 'booking_details.html', {'user': user})


def admdash(request):
    return render(request, 'admdash.html')


def cities(request):
    own = pg_owner.objects.all()
    cities_list = []
    for i in own:
        if i.city not in cities_list:
            cities_list.append(i.city)
    return render(request, 'cities.html', {'owner': own, 'cities_list': cities_list})


def pg_by_cities(request, city):
    own_ = pg_owner.objects.all()
    own = pg_owner.objects.filter(city=city)
    cities_list = []
    for i in own_:
        if i.city not in cities_list:
            cities_list.append(i.city)
    return render(request, 'cities.html', {'owner': own, 'cities_list': cities_list})


def login(request):
    if (request.method == 'POST'):
        role = request.POST['role']
        name = request.POST['name']
        password = request.POST['password']
        if (role == 'Admin'):
            # checklog = adm.objects.get(name=name, password=password)
            if (name == 'admin' and password == 'user123'):
                return redirect('admdash')
            else:
                messages.warning(request,'Enter correct details..!')
                return render(request, 'login.html')
        elif (role == 'PgOwner'):
            try:
                checklog = pg_owner.objects.get(name=name, password=password)

                if (checklog):
                    return redirect('add', name)
                else:
                    messages.warning(request,'Enter correct details..!')
                    return render(request, 'login.html')
            except:
                messages.warning(request,'Enter correct details..!')
                pass        

        else:
            return render(request, 'login.html')

    return render(request, 'login.html')


def Ownerdetailtable(request):
    # own = pg_owner.objects.all()
    own = pg_owner.objects.prefetch_related('pg_amenities_set').all()
    pgs_id = pg_owner.objects.only('id')
    print(pgs_id)
    ids_list = []
    for i in pgs_id:
        ids_list.append(i.id)
    print(ids_list)
    amenities = pg_amenities.objects.filter(pg_id__in=ids_list)
    return render(request, 'Ownerdetailtable.html', {'owner': own, 'amenities': amenities})


class ManageAmenities:
    def amenities_create(request):  
        # if request.user.is_authenticated:
        if request.method == "POST":
            form = AmenitiesForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()
                return redirect(reverse("amenity_list"))
            else:
                print("Invalid Form")
        else:
            form = amenitie()
        return render(request, "amenities_form.html", {"form": form, })
        # else:
        #     return redirect("login")

    def amenities_list(request):
        # if request.user.is_authenticated:
        amenities = amenitie.objects.all().order_by('-id')
        context = {
            "amenities": amenities,
        }

        return render(request, "amenities_list.html", context)
        # else:
        #     return redirect("login")

    def amenities_update(request, id):
        # if request.user.is_authenticated:
        gift_obj = get_object_or_404(amenitie, pk=id)
        if request.method == 'POST':
            #form = CoinForm(instance=task_obj, data=request.POST)
            form = AmenitiesForm(
                request.POST, request.FILES, instance=gift_obj,)
            if form.is_valid():
                form.save()
                return redirect(reverse("gift_details", args=[id, ]))
        else:
            form = AmenitiesForm(instance=gift_obj)

        return render(request, "amenities_form.html", {"form": form, "object": gift_obj})
        # else:
        #     return redirect("login")

    def amenities_delete(request, id):
        # if request.user.is_authenticated:
        gift_obj = get_object_or_404(amenitie, id=id)
        gift_obj.delete()
        return redirect(reverse("amenity_list"))
        # else:
        #     return redirect("login")


def pginfo(request, id):
    own = pg_owner.objects.get(id=id)
    pg_amenity = pg_amenities.objects.filter(pg_id=own.id)

    return render(request, 'pginfo.html', {'owner': own, 'pg_amenities': pg_amenity})


def pgOwner(request):
    if request.method == 'POST':
        own = pg_owner()
        fs = FileSystemStorage()
        own.name = request.POST['name']
        own.pgname = request.POST['pgname']
        own.address = request.POST['address']
        own.city = request.POST['city']
        own.fees = request.POST['fees']
        own.email = request.POST['email']
        own.contact = request.POST['contact']
        # own.amenities = request.POST['amenities']
        # own.front_view=request.POST['front_view']
        front_view_file = request.FILES['front_view']
        amenities = request.POST.getlist('check[]')
        print(amenities)

        print(front_view_file)
        print(type(front_view_file))
        print(f"image/{front_view_file.name}", front_view_file.file)
        # print(type(f"image/{front_view_file.name}"+front_view_file.file))
        own.front_view = fs.save(
            f"image/{front_view_file.name}", front_view_file.file)

        any_view_file = request.FILES['any_view']
        own.any_view = fs.save(
            f"image/{any_view_file.name}", any_view_file.file)

        bed_room_file = request.FILES['bed_room']
        own.bed_room = fs.save(
            f"image/{bed_room_file.name}", bed_room_file.file)
        own.password = request.POST['password']
        own.save()
        user = pg_owner.objects.filter(contact=own.contact)[:1]
        f_user = pg_owner.objects.get(id=user[0].id)
        print(user)
        for i in amenities:
            print(i)
            pg_amenities_obj = pg_amenities()
            pg_amenities_obj.pg_id = f_user
            pg_amenities_obj.amenitie = amenitie.objects.get(id=i)
            pg_amenities_obj.save()
        return render(request, 'home.html')

    else:
        amenities = amenitie.objects.all().order_by('-id')
        context = {
            "amenities": amenities,
        }

        return render(request, "pgOwner.html", context)


def userdetailtable(request):
    user = student.objects.all()
    return render(request, 'userdetailtable.html', {'user': user})


def deleteowner(request, id):
    own = pg_owner.objects.get(id=id)
    own.delete()
    return redirect('Ownerdetailtable')


def deletestudent(request, id):
    own = student.objects.get(id=id)
    own.delete()
    return redirect('userdetailtable')


def logout(request):
    logout(request)
