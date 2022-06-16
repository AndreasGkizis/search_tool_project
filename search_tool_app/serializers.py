from dataclasses import fields
from rest_framework import serializers
from .models import *

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        
class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

class PaperSerializer(serializers.ModelSerializer):

    year_id = serializers.SlugRelatedField(many=False, read_only=True, slug_field='year_published')
    type_id = serializers.SlugRelatedField(many=False, read_only=True, slug_field='type')
    language = serializers.SlugRelatedField(many=True, read_only=True, slug_field='language')
    author = AuthorSerializer(many=True, read_only=True)
    tag = serializers.SlugRelatedField(many=True, read_only=True, slug_field='tag')
    material = serializers.SlugRelatedField(many=True, read_only=True, slug_field='material')

    class Meta:
        model = Paper
        fields = ['title',
                  'slug',
                  'pdf',
                  'abstract',
                  'reviewed',
                  'date_added',
                  'year_id',
                  'type_id',
                  'language',
                  'author',
                  'tag',
                  'material',
                  'id' ]


