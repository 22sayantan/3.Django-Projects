from django.shortcuts import render,redirect
from django.db import connection
from .models import Item,Category, Unit, Product, Purchase

def index(request):
    mymodels = Item.objects.all()
    return render(request, 'retailApp/index.html', {'mymodels': mymodels})

def user(request):
    
    # code for delete specific row from table:::
    if request.method == 'POST':
        del_id = request.POST.get('delete_id')
        if del_id:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM users WHERE id = %s",[del_id])
                cursor.execute("set @var := 0; update users set id = @var := (@var +1)")

    with connection.cursor() as cursor:
        cursor.execute("SELECT id,name,email FROM users")
        rows = cursor.fetchall()

    return render(request, 'retailApp/users.html',{'rows': rows})

def NewUser(request):
    if request.method == 'GET' and 'user_name' in request.GET and 'user_email' in request.GET:
        new_user_name = request.GET['user_name']
        new_user_email = request.GET['user_email']
        print(new_user_name,new_user_email)
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO users (name,email) values(%s,%s)",[new_user_name,new_user_email])
            cursor.execute("set @var := 0; update users set id = @var := (@var +1)")
    return render(request, 'retailApp/newUser.html')



# ---------------------------- inventory management ---------------------------------

def inventory(request):
    with connection.cursor() as cursor:
      cursor.execute('SELECT * from product')
      items = cursor.fetchall()

      # add item to database::::
      if request.method == 'GET':
        print()
    return render(request,'retailApp/Inventory.html',{'items':items})


def product_list(request):
  products = Product.objects.all().order_by('name')
  return render(request, 'inventory/product_list.html', {'products': products})

def product_detail(request):
  if request.method == 'GET':
        return render(request, 'retailApp/productDetail.html')

def purchase_create(request, product_id):
  if request.method == 'POST':
    # Process purchase form data and save a new Purchase object
    return redirect('product_detail', product_id)
  else:
    product = Product.objects.get(pk=product_id)
    return render(request, 'inventory/purchase_create.html', {'product': product})

# ----------------------------------------test section ----------------------------------
def test(request):
  return render(request,'retailApp/test.html')

# ----------------------------------------expense section ----------------------------------
def expense(request):
  return render(request,'retailApp/expense.html')

# ----------------------------------------jobs section ----------------------------------
def jobs(request):
  return render(request,'retailApp/jobs.html')

# ----------------------------------------library section ----------------------------------
def library(request):
  return render(request,'retailApp/library.html')

# ----------------------------------------image section ----------------------------------
def image(request):
  return render(request,'retailApp/image.html')

# ----------------------------------------docs section ----------------------------------
def docs(request):
  return render(request,'retailApp/docs.html')

# ----------------------------------------scrapper section ----------------------------------
def scrapper(request):
  return render(request,'retailApp/scrapper.html')

# ----------------------------------------analytics section ----------------------------------
def analytics(request):
  return render(request,'retailApp/analytics.html')

# ----------------------------------------booking section ----------------------------------
def booking(request):
  return render(request,'retailApp/booking.html')

# ----------------------------------------booking section ----------------------------------
def books(request):
  return render(request,'retailApp/books.html')


