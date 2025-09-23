from django.shortcuts import render
from django.views import generic
from django.db.models import Sum

from classes.models import Session
from .forms import DateForm

# Create your views here.
class PaymentList(generic.ListView):
    model = Session
    template_name = "payment_list.html"
    context_object_name = "sessions"

    def get_queryset(self):
        queryset = Session.objects.filter(paid_time__isnull=False)
        self.form = DateForm(self.request.GET)
        if self.form.is_valid():
            start = self.form.cleaned_data.get("start_date")
            end = self.form.cleaned_data.get("end_date")
            if start:
                queryset = queryset.filter(date__gte=start)
            if end:
                queryset = queryset.filter(date__lte=end)
        return queryset

    def get_context_data(self, **kwargs):
        form = DateForm()
        context = super().get_context_data(**kwargs)
        context["form"] = form
        context["total_price"] = (
            self.get_queryset().aggregate(total=Sum("price"))["total"] or 0
        )
        return context

