from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView, DeleteView , CreateView
from django.urls import reverse_lazy
from .models import Article


# Create your views here.
class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Article

    template_name = 'articles/article_new.html'

    fields = ('title','body')

    def form_valid(self,form):
        """ Allows current logged in user to post article """
        form.instance.author =self.request.user
        return super().form_valid(form)

    

class ArticleListView(LoginRequiredMixin,ListView):
    model = Article


    template_name = 'articles/article_list.html'


class ArticleDetailView(LoginRequiredMixin,DetailView):
    model = Article

    template_name = 'articles/article_detail.html'


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Article

    fields = ('title','body')

    template_name = 'articles/article_edit.html'


    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user



class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Article

    template_name = 'articles/article_delete.html'

    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
