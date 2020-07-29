from django.shortcuts import render,  HttpResponseRedirect, reverse
from .models import cart, wishlist
from home.models import books

# Create your views here.



def user_cart_addproduct(request):

    if request.method == 'POST':

        bookid = request.POST['bookid']


 
    producte = books.objects.get(id = bookid)

    obj = cart.objects.create(product_id = producte, buyer = request.user)

    obj.save()
     
   

    dests = cart.objects.filter(buyer = request.user)

    subtotal = 0
    for dest in dests:

        subtotal = subtotal + int(dest.product_id.price)

    context= {

            'dests' : dests,
            'totalprice' : subtotal
        }
    
   
   

    return render(request, 'cart.html', context)



def user_cart(request):

    dests = cart.objects.filter(buyer = request.user)

    context= {

            'dests' : dests,
            
        }

    return render(request, 'cart.html', context)




def user_wishlist_addproduct(request, bookid):

   
    producte = books.objects.get(id = bookid)

    obj = wishlist.objects.create(product_id = producte, buyer = request.user)

    obj.save()
    
    return HttpResponseRedirect(reverse('index'))



def user_wishlist(request):

    dests = wishlist.objects.filter(buyer = request.user)

    context= {

            'dests' : dests
            
        }

    return render(request, 'wishlist.html', context)


    
def checkout(request):

    dests = cart.objects.filter(buyer = request.user)

    context= {

            'dests' : dests,
            
        }

    return render(request, 'checkout.html', context)


