from django.shortcuts import render
from django.views import generic
from django.db.models import Sum

from classes.models import Session
from .forms import DateForm

# Create your views here.
class PaymentList(generic.ListView):
    model = Session
    queryset = Session.objects.filter(paid_time__isnull=False)
    template_name = "payment_list.html"
    context_object_name = "sessions"

    def get_context_data(self, **kwargs):
        form = DateForm()
        context = super().get_context_data(**kwargs)
        context["form"] = form
        context["total_price"] = (
            self.get_queryset().aggregate(total=Sum("price"))["total"] or 0
        )
        return context

    def get(self, request, *args, **kwargs):
        form = DateForm(request.GET)
        if form.is_valid():
            start = form.cleaned_data.get("start_date")
            end = form.cleaned_data.get("end_date")
            print(start, end)
        return super().get(request, *args, **kwargs)
    
