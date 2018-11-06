from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
from django.db.models import Q
from django.urls import reverse_lazy

from hospital.models import Info
from hospital.forms import InfoSearchForm, UploadFileForm
from mini.views import LoginRequiredMixin

# Create your views here.
class InfoLV(ListView):
    model = Info
    template_name = 'hospital/info_all.html'
    context_object_name = 'infos'

    paginate_by = 5

class InfoDV(DetailView):
    model = Info

class SearchFormView(FormView):
    form_clas = InfoSearchForm
    template_name = 'hospital/info_search.html'
    
    def form_vaild(self, form):
        schWord = '%s' % self.request.post['search_word']

        info_list = Info.objects.filter(Q(name__icontains=schWord) |
                Q(description__icontains=schWord) | Q(content__icontains=schWord)).distinct()

        context = {}
        context['form'] = form
        context['search_keyword'] = schWord
        context['search_list'] = info_list

class InfoCreateView(LoginRequiredMixin, CreateView):
    models = Info
    fields = ['name', 'pid', 'description','content' ]
    initial = {'pid': 'auto-filling-by-title'}
    success_url = reverse_lazy('hospital:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(InfoCreateView,self).form_valid(form)

class upload_file():
    pass
