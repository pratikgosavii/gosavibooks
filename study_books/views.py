from django.shortcuts import render, redirect
from home.models import books
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.






def books_study_filter(request):

    if request.method == 'POST':
        standard = request.POST.get("standard")
        pattern  = request.POST.get("pattern")
        category  = request.POST.get("category")
       
 
        #session
        request.session['standard_school']= standard
        request.session['patter_school']=pattern
        request.session['category']= category

      


    
    filter_standard=request.session['standard_school']
    filter_pattern= request.session['patter_school']
    

  
   

    posts = books.objects.filter(standard = filter_standard, pattern =  filter_pattern, category = category)
      
    
    paginator = Paginator(posts, 9)

    page = request.GET.get('page')

    


    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    

        
    return render(request, 'shop-grid.html', {'posts': posts})


def books_college_filter(request):

    if request.method == 'POST':
        standard = request.POST['class']
        course  = request.POST['patter']

        dests = books.objects.filter(standard = standard, course = course)
        
    return render(request, 'shop-grid.html', {'dests': dests})


def books_eng_filter(request):

    if request.method == 'POST':
        year = request.POST['year']
        field  = request.POST['field']

        dests = books.objects.filter(year = year, field = field)
        
    return render(request, 'shop-grid.html', {'dests': dests})


def books_medical_filter(request):

    if request.method == 'POST':
        year = request.POST['year']
        field  = request.POST['filed']

        dests = books.objects.filter(year = year, filed = field)
        
    return render(request, 'shop-grid.html', {'dests': dests})

def single_product(request, book_id):


    

    dests = books.objects.filter(id = book_id)
    return render(request, 'single-product.html', {'dests': dests})




