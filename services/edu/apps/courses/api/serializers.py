from rest_framework import serializers

from services.edu.apps.courses.models import Content, Course, Module, Subject


class ModuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Module
        fields = ('order', 'title', 'course')


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ('id', 'title', 'slug')


class CourseSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'title', 'slug', 'subject', 'overview', 'created', 'owner', 'modules')


class ItemRelatedField(serializers.RelatedField):

    def to_representation(self, value):
        return value.render() if hasattr(value, 'render') else None


class ContentSerializer(serializers.Serializer):
    item = ItemRelatedField(read_only=True)

    class Meta:
        model = Content
        fields = ['order', 'item']


class ModuleWithContentSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True, read_only=True)

    class Meta:
        model = Module
        fields = ('order', 'title', 'description', 'contents')


class CourseWithContentSerializer(serializers.ModelSerializer):
    modules = ModuleWithContentSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'subject', 'title', 'slug', 'overview', 'created', 'owner', 'modules')
