from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import User, Author, Quote
from django.contrib import messages
import bcrypt

# Registration and Sign in page
def index(request):
    return render(request, "quotes/index.html")

# Registration of a new user
def register(request):
    if request.method == "POST":
        User.objects.register(request)
        messages.add_message(request, messages.SUCCESS,
                             "Yaaay! You succesfully registered! Please login.")
        return redirect("/")
        
    else:
        return redirect("/")

# Signing in with existing user credentials
def login(request):
    try:
        user = User.objects.get(email=request.POST["email"])

        isValid = bcrypt.checkpw(
            request.POST["password"].encode(), user.password.encode())

        if isValid:
            print("PASSWORDS EXISTS")
            request.session["name"] = user.name
            return redirect("/quotes")
        else:
            print("PASSWORD DOES NOT MATCH")
            messages.add_message(request, messages.ERROR,
                                 "Invalid Credentials!")
            return redirect("/")
    except:
        messages.add_message(request, messages.ERROR,
                             "No user with this email was found!")
        return redirect("/")


def quotes(request):
    # this returns the first 3 objects(LIMIT 3):
    latestQuotes = Quote.objects.all().order_by("-id")[:3]

    # This returns the 4 through 10 objects:
    otherQuotes = Quote.objects.all().order_by("-id")[3:10]

    context = {
        "quotes": latestQuotes,
        "otherQuotes": latestQuotes
    }

    return render(request, "quotes/quotes.html", context)


def addQuote(request):
    authors = Author.objects.all()
    quotes = Quote.objects.all().order_by("-id")
    return render(request, "quotes/quotes.html", {"authors": authors, "quotes": quotes})


def createQuote(request):
    if len(request.POST["newAuthor"]) < 3:
        messages.add_message(request, messages.ERROR,
                             "You need to supply a proper author name!")
        return redirect("/quotes")

    # if request.POST["author"]:
    #     author = int(request.POST["author"])

    # newAuthor = ""

    if len(request.POST["newAuthor"]) > 3:
        newAuthor = Author.objects.create(
            name=request.POST["newAuthor"]
        )
        author = newAuthor.id
        
        print("author")

    quote = Quote.objects.create(
        text=request.POST["quote"],
        author_id=author,
        uploaded_by_id=(User.objects.get(name=request.session["name"])).id
    )
    return redirect("/quotes")


def showQuote(request, id):
    quote = Quote.objects.get(id=id)
    # reviews = Review.objects.filter(book_id=id)

    context = {
        "quote": quote
    }
    return render(request, "quotes/showQuote.html", context)


def myaccount(request, id):
    user = (User.objects.get(name=request.session["name"])).id,

    context = {
        "user": user
    }
    return redirect(request, "quotes/manageUser.html ", context)


def showUser(request, id):
    pass