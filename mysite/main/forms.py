from django import forms
from .models import Generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from haystack.forms import SearchForm



class Generic_Form(forms.ModelForm):
    
    class Meta:
        model = Generic
        # fields = [field.name for field in Schema._meta.get_fields()]
        # fields.remove("schema_name")
        # fields.remove("generic")

        fields = [field.name for field in Generic._meta.get_fields()]
        fields.remove("created_at")
        fields.remove("last_updated")


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    
    model = User
    fields = ("username",
              "first_name",
              "last_name",
              "email",
              "password1",
              "password2")
    
    field_order = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]
    
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user


class AutocompleteSearchForm(SearchForm): # Haystack SearchForm

    def search(self):
        query = self.cleaned_data["q"]
        
        if not self.is_valid():
            return self.no_query_found()
        if not query:
            return self.no_query_found() 
        
        # sqs = self.searchqueryset.filter(content=query) # Gets results from all indexed fields in all models BUT no partial text search. Full words, which behaves more like EdgeNgramField(?) NB: "content" is a special field in haystack to reference all fields/models in index.
        sqs = self.searchqueryset.filter(content=query).models(Generic) # as above but only specific model passed. Stemming is implemented by default so should be able to search for "train" to return trains.

        if self.load_all:
            sqs = sqs.load_all()

        return sqs


