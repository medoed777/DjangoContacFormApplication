from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from blogs.models import Blogs


class BlogCreateView(CreateView):
    model = Blogs
    template_name = 'blogs/blog_create.html'
    fields = ['head', 'content', 'image']
    success_url = reverse_lazy("blogs:blogs_list")

class BlogsListView(ListView):
    model = Blogs
    template_name = 'blogs/blogs_list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blogs.objects.filter(is_active=True)


class BlogUpdateView(UpdateView):
    model = Blogs
    template_name = 'blogs/blog_update.html'
    fields = ['head', 'content', 'image']

    def get_success_url(self):
        return reverse('blogs:blog_detail', kwargs={'pk': self.object.pk})


class BlogDeleteView(DeleteView):
    model = Blogs
    template_name = 'blogs/blog_delete.html'
    success_url = reverse_lazy("blogs:blogs_list")


class BlogDetailView(DetailView):
    model = Blogs
    template_name = "blogs/blog_detail.html"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views += 1
        obj.save()
        return obj
