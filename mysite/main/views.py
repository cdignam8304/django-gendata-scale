from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Contact
from .models import Generic, Schema
# from .forms import Contact_Form
from .forms import Generic_Form
# from django.forms import formset_factory
from django.forms.models import modelformset_factory
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from haystack.views import search_view_factory
from haystack.generic_views import SearchView
from haystack.forms import SearchForm


# Create your views here.

def homepage(request):
    context = {}
    title = "Dashboard"
    schemas = Schema.objects.all()
    context["title"] = title
    context["schemas"] = schemas
    return render(request=request,
                  template_name="main/homepage.html",
                  context=context)


# NO PAGINATION - NOT CURRENTLY USED AS PAGINATION IS WORKING BELOW
@login_required(login_url="/login/")
def generic_update(request, schema):
    context = {}
    title = f"Edit {schema}"
    context["title"] = title
    context["schema"] = schema
    
    # Code to get list of fields for an instance of Schema:
    generic_fields = []
    specific_fields = []
    fieldnames = [field.name for field in Schema._meta.get_fields()]
    fieldnames.remove("schema_description")
    fieldnames.remove("generic")
    for field in fieldnames: 
        fname = getattr(Schema.objects.all().filter(schema_name__exact=schema)[0], field) 
        if fname != "INACTIVE": 
            generic_fields.append(field)
            specific_fields.append(fname)
    context["generic_fields"] = generic_fields
    context["specific_fields"] = specific_fields
    
    GenericFormset = modelformset_factory(model=Generic, form=Generic_Form, extra=1)
    formset = GenericFormset(request.POST or None, queryset=Generic.objects.filter(schema_name__schema_name=schema))
    if formset.is_valid():
        instances = formset.save(commit=False)
        
        for instance in instances:
            instance.save()
        
        messages.success(request, f"Records updated")
        return redirect(f"/generic_update/{schema}/")
    else:
        if request.POST: # So don't get error when first load page (GET request)
            messages.error(request, formset.errors)
    
    context["formset"] = formset
    
    return render(request, "main/generic_update.html", context)
    

# WITH PAGINATION 
@login_required(login_url="/login/")
def generic_update_paginate(request, schema):
    context = {}
    title = f"Edit {schema}s"
    context["title"] = title
    context["schema"] = schema
    
    # Code to get list of fields for an instance of Schema:
    generic_fields = []
    specific_fields = []
    fieldnames = [field.name for field in Schema._meta.get_fields()]
    fieldnames.remove("schema_description")
    fieldnames.remove("generic")
    for field in fieldnames: 
        fname = getattr(Schema.objects.all().filter(schema_name__exact=schema)[0], field) 
        if fname != "INACTIVE": 
            generic_fields.append(field)
            specific_fields.append(fname)
    context["generic_fields"] = generic_fields
    context["specific_fields"] = specific_fields
    
    GenericFormset = modelformset_factory(model=Generic, form=Generic_Form, extra=0)
    
    if request.method == "POST":    
        formset = GenericFormset(request.POST)
        if formset.is_valid():
            instances = formset.save(commit=False)
            
            for instance in instances:
                instance.save()
            
            messages.success(request, f"Records updated")
            return redirect(f"/generic_update/{schema}/")
        else:
            if request.POST: # So don't get error when first load page (GET request)
                messages.error(request, formset.errors)
                
    else:
        query = Generic.objects.filter(schema_name__schema_name=schema)
        num_forms_per_page = 8 # for pagination
        paginator = Paginator(query, num_forms_per_page) # show 10 forms per page
        page = request.GET.get("page")
        try:
            objects = paginator.page(page)
        except PageNotAnInteger:
            objects = paginator.page(1)
        except EmptyPage:
            objects = paginator.page(paginator.num_pages)
        page_query = query.filter(id__in=[object.id for object in objects])
        formset = GenericFormset(queryset=page_query)
        
        context["formset"] = formset
        context["objects"] = objects
        
        # return render(request, "main/generic_update_paginate.html", context)
        return render(request, "main/generic_update_paginate_materialize.html", context)


def register(request):
    context = {}
    title = "Register"
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid(): # check the form filled out correctly
            user = form.save() # commit the new user record to the database
            username = form.cleaned_data.get("username")
            messages.success(request, f"New Account Created: {username}")
            login(request=request, user=user) # so new user doesn't have to login again afer registering
            messages.info(request, f"You are now logged in as: {username}")
            return redirect("main:homepage") # arg using the variable names created in urls.py in main
        else:
            # Implement a short-term error handling solution:
            for msg in form.error_messages: # form.error_messages is a dict
                # print(form.error_messages[msg]) # prints errors to console
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = NewUserForm
    context["title"] = title
    context["form"] = form
    
    return render(request=request, # This handles the default GET request
                  template_name="main/register.html",
                  context=context)


def logout_request(request):
    
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")


def login_request(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request=request,
                                  data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username,
                                password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as: {username}")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    
    # Context
    context = {}
    form = AuthenticationForm()
    title = "Login"
    context["form"] = form
    context["title"] = title
    return render(request=request,
                  template_name="main/login.html",
                  context=context)
    

@login_required(login_url="/login/")
def get_user_profile(request, username):
    
    if request.user.is_authenticated:
        user = User.objects.get(username=username)
        return render(request, "main/user_profile.html", {"user":user})
    else:
        messages.error(request, "You must be logged in to view the account page!")
        return redirect("main:homepage")


class BasicSearchView(SearchView):
    form = SearchForm()
    template_name = "main/generic_update_paginate_materialize.html"
    
