from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,DetailView
from .models import TuitionPost,Area
from .forms import TuitionForm


# Create your views here.
class Home(TemplateView):
    template_name = 'base.html'


class TuitionPostCreateView(CreateView):
    model = TuitionPost
    form_class = TuitionForm
    template_name = 'tuition/creteview.html'
    success_url = '/'

    # def form_valid(self, form):
    #     form = TuitionForm(self.request.POST)


class TuitionListView(ListView):
    model = TuitionPost
    template_name = 'tuition/listview.html'


class TuitionDetailView(DetailView):
    model = TuitionPost
    template_name = 'tuition/detailview.html'


def load_cities(request):
    district_id = request.GET.get('district_id')
    areas = Area.objects.filter(district_id=district_id).all()
    return render(request, 'tuition/city_dropdown_list_options.html', {'cities': areas})

