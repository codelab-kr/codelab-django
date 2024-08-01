# from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, ListView  # , CreateView

from services.edu.apps.courses.models import Course

from .forms import CourseEnrollForm  # , StudentRegistrationForm

# class StudentRegistrationView(CreateView):
#     template_name = 'students/student/registration.html'
#     form_class = StudentRegistrationForm
#     success_url = reverse_lazy('student_course_list')

#     def form_valid(self, form):
#         result = super().form_valid(form)
#         cd = form.cleaned_data
#         user = authenticate(username=cd['username'], password=cd['password1'])
#         login(self.request, user)
#         return result


class StudentEnrollCourseView(LoginRequiredMixin, FormView):
    course = None
    form_class = CourseEnrollForm

    def form_valid(self, form):
        self.course = form.cleaned_data['course']
        self.course.students.add(self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('student_course_detail', args=[self.course.id])  # type: ignore


class StudentCourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'students/course/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in=[self.request.user])


class StudentCourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = 'students/course/detail.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in=[self.request.user])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.get_object()
        if 'module_id' in self.kwargs:
            context['module'] = course.modules.get(id=self.kwargs['module_id'])  # type: ignore
        else:
            context['module'] = course.modules.all()[0]  # type: ignore
        return context
