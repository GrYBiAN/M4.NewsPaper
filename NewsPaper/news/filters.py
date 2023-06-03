from django import forms
from .models import Post
from django_filters import FilterSet, DateFilter, CharFilter


class PostFilter(FilterSet):
    title = CharFilter(lookup_expr='icontains',  )

    time_create = DateFilter(widget=forms.DateInput(attrs={'type':'date'}),
                                            lookup_expr='gt')


class Meta:
    model = Post
    fields = ('post_type',)
