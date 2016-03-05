from rest_framework import serializers

from api.models import *

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Levels
        fields = '__all__'

# class AudioSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Audios
#         fields = '__all__'

class PronuncationSerializer(serializers.BaseSerializer):
    def to_representation(self, obj):
        return {'type': obj.ptype, 'pronuncation': obj.pronuncation}

class DefinitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Definitions
        fields = ('pos', 'definition', 'language')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class SentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sentences
        fields = '__all__'

class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translations
        fields = '__all__'

class SentenceForWordSerializer(serializers.ModelSerializer):

    translation = TranslationSerializer(many=True)
    class Meta:
        model = Sentences
        fields = ('created', 'is_offical', 'sentence', 'uuid', 'translation')
        read_only_fields = ('created', 'is_offical', 'sentence', 'uuid', 'translation')

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'

class WordSerializer(serializers.ModelSerializer):
    definition = DefinitionSerializer(many=True)
    pronuncation = PronuncationSerializer(many=True)
    sentence = SentenceForWordSerializer(many=True)
    #note = NoteSerializer(many=True)
    class Meta:
        model = Words
        #fields = ('definitions',)
        fields = ('word', 'pronuncation', 'sentence', 'note', 'definition')
        read_only_fields = ('word', 'pronuncation', 'sentence', 'note', 'definition')


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Votes
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Records
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

    def update(self, instance, v_data):
        _u = Users()
        return

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registers
        fields = '__all__'

    def create(self, validated_data):
        register = Registers(**validated_data)
        register.save()
        _u = Users(register=register, daily_task=20, name="No Name")
        _u.save()
        return register

class UserListSerializer(serializers.ModelSerializer):
    #register = RegisterSerializer()
    class Meta:
        model = Users
        fields = ('uid', 'is_male', 'daily_task', 'name')