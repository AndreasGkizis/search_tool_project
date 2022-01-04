from rest_framework import serializers
from .models import *


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class PaperSerializer(serializers.ModelSerializer):
    year_id = serializers.SlugRelatedField(many=False, read_only=True, slug_field='year_published')  # giati many=false?
    type_id = serializers.SlugRelatedField(many=False, read_only=True, slug_field='type')
    language = serializers.SlugRelatedField(many=True, read_only=True, slug_field='language')
    tag = serializers.SlugRelatedField(many=True, read_only=True, slug_field='tag')
    material = serializers.SlugRelatedField(many=True, read_only=True, slug_field='material')

    class Meta:
        model = Paper
        fields = ['title',
                  'year_id',
                  'type_id',
                  'language',
                  'tag',
                  'material']
