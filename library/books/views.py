from django.shortcuts import render
from books.models import Book
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    context={'name':'arun','age':'27'}
    return render(request,'home.html',context)

@login_required
def add_book(request):
    if request.method == "POST":
        t = request.POST.get('t', '')  # Safely get title
        au = request.POST.get('a', '')  # Safely get author
        p = request.POST.get('pa', 0)  # Safely get pages, default to 0 if not provided
        pri = request.POST.get('pr', 0)  # Safely get price, default to 0 if not provided
        lang = request.POST.get('l', '')  # Safely get language

        # Convert the pages and price fields to integers, use 0 as default if the field is empty
        try:
            p = int(p) if p else 0  # Ensure that pages is an integer
        except ValueError:
            p = 0  # In case the conversion fails, set pages to 0

        try:
            pri = int(pri) if pri else 0  # Ensure that price is an integer
        except ValueError:
            pri = 0  # In case the conversion fails, set price to 0

        # Handle file uploads
        cover = request.FILES.get('i', None)
        pdf = request.FILES.get('d', None)  # Get PDF file, None if not provided


        b = Book.objects.create(
            title=t,
            author=au,
            pages=p,
            price=pri,
            language=lang,
            cover=cover,  # Assign the uploaded cover image
            pdf=pdf  # Assign the uploaded PDF
        )

        b.save()  # Save the new book instance

        return view_book(request)  # Redirect to view_book after adding

    return render(request, 'add_book.html')




@login_required
def view_book(request):
    k=Book.objects.all()       #reads all records from the table named book
    return render(request,'view_book.html',{'book':k})

@login_required
def detail(request,i):
    k=Book.objects.get(id=i)
    return render(request,'detail.html',{'book':k})
@login_required
def edit(request,s):
    k=Book.objects.get(id=s)
    if (request.method=="POST"):
        k.title=request.POST['t']
        k.author = request.POST['a']
        k.pages = request.POST['pa']
        k.price = request.POST['pr']
        k.language = request.POST['l']
        if(request.FILES['i']==None):
            k.save()
        else:
            k.cover=request.FILES['i']

        if (request.FILES.get('d') == None):
            k.save()
        else:
            k.pdf = request.FILES.get('d')
        k.save()
        return view_book(request)


    return render(request,'edit.html',{'book':k})
@login_required
def delete(request,p):
    k=Book.objects.get(id=p)
    k.delete()
    return view_book(request)
from django.db.models import Q
def search(request):
    k=None
    if(request.method=="POST"):
        query=request.POST['q']
        print(query)
        if query:
            k=Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
            print(k)
    return render(request,'search.html',{'book':k})
