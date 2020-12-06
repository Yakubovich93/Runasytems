from rest_framework import serializers
from .models import Categories


class FilterCategorySerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecuriveSerializer(serializers.Serializer):

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CategoriesSerializer(serializers.ModelSerializer):

    children = RecuriveSerializer(many=True, read_only=True)

    class Meta:
        list_serializer_class = FilterCategorySerializer
        model = Categories
        fields = ('name', 'children')
