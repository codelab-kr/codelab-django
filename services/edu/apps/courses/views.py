from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import Course


def course_list(request):
    return render(request, 'courses/course/list.html')


class OwnerMixin:

    def get_queryset(self):
        qs = super().get_queryset()  # type: ignore
        return qs.filter(owner=self.request.user)  # type: ignore


class OwnerEditMixin:

    def form_valid(self, form):
        form.instance.owner = self.request.user  # type: ignore
        return super().form_valid(form)  # type: ignore


class OwnerCourseMixin(OwnerMixin, LoginRequiredMixin, PermissionRequiredMixin):
    model = Course
    fields = ['subject', 'title', 'slug', 'overview']
    success_url = reverse_lazy('course:manage_list')  # type: ignore


class OwnerCourseEditMixin(OwnerCourseMixin, OwnerEditMixin):
    template_name = 'courses/manage/course/form.html'  # type: ignore


class ManageCourseListView(OwnerCourseMixin, ListView):
    template_name = 'courses/manage/course/list.html'  # type: ignore
    permission_required = 'courses.view_course'


class CourseCreateView(OwnerCourseEditMixin, CreateView):
    permission_required = 'courses.add_course'


class CourseUpdateView(OwnerCourseEditMixin, UpdateView):
    permission_required = 'courses.change_course'


class CourseDeleteView(OwnerCourseMixin, DeleteView):
    template_name = 'courses/manage/course/delete.html'  # type: ignore
    permission_required = 'courses.delete_course'
