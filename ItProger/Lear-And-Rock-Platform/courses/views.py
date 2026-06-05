from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Course, Lesson, Comment
from .forms import CommentForm, CourseAddForm, LessonAddForm
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin


LessonFormSet = inlineformset_factory(Course, Lesson, form=LessonAddForm, extra=1, can_delete=True)

class HomePage(ListView):
    model = Course
    template_name = 'courses/home.html'
    context_object_name = 'courses'

class CourseDetailPage(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'

class LessonDetailPage(LoginRequiredMixin, DetailView):
    model = Lesson
    template_name = 'courses/lesson_detail.html'
    context_object_name = 'lesson'

    def get_object(self, queryset=None):
        return get_object_or_404(
            Lesson,
            slug=self.kwargs['lesson_slug'],
            course__slug=self.kwargs['slug']
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.select_related('user').all()
        context['form'] = CommentForm(initial={'user': self.request.user, 'lesson': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        post_data = request.POST.copy()
        post_data['user'] = request.user.pk
        post_data['lesson'] = self.object.pk
        
        form = CommentForm(post_data)
        if form.is_valid():
            form.save()
            return redirect('lesson_detail', slug=self.kwargs['slug'], lesson_slug=self.kwargs['lesson_slug'])
        
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)

class CourseAdd(CreateView):
    model = Course
    form_class = CourseAddForm
    template_name = 'courses/course_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['lessons'] = LessonFormSet(self.request.POST)
        else:
            context['lessons'] = LessonFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        lessons = context['lessons']
        if lessons.is_valid():
            self.object = form.save()
            lessons.instance = self.object
            lessons.save()
            return redirect('home')
        return self.render_to_response(self.get_context_data(form=form))
    
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Акаунт створено для {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'courses/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Ваш профіль оновлено!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)

    return render(request, 'courses/profile.html', {'u_form': u_form})

class CourseDeleteView(LoginRequiredMixin, DeleteView):
    model = Course
    success_url = reverse_lazy('home')
    template_name = 'courses/course_confirm_delete.html'