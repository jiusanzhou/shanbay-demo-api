from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework import status

from api.models import *
from api.serializers import *

class Auth(object):

    def isAuthed(self, **kws):
        content = kws.get('content')
        code = kws.get('code')
        return True if Users.objects.get(content=content, code=code) else False


class LevelList(generics.ListAPIView):
    queryset = Levels.objects.all()
    serializer_class = LevelSerializer

class LevelDetail(generics.ListAPIView):
    queryset = Levels.objects.all()
    serializer_class = LevelSerializer

class WordList(APIView):

    def get(self, request, format=None, **kws):
        page = 1 if int(kws.get('page', 1))<1 else int(self.kwargs.get('page', 1))
        limit = int(kws.get('limit', 15)) if 0<int(kws.get('limit', 15))<15 else 15
        words = Words.objects.all()[limit*(page-1):limit*page]
        serializer = WordSerializer(words, many=True)
        return Response({'msg': 'success', 'data': serializer.data}, status=status.HTTP_200_OK, headers={'Access-Control-Allow-Origin': '*'})

class SentenceList(generics.ListCreateAPIView):
    queryset = Sentences.objects.all()
    serializer_class = SentenceSerializer

class SentenceDetail(generics.ListCreateAPIView):
    queryset = Sentences.objects.all()
    serializer_class = SentenceSerializer

class NoteList(generics.ListCreateAPIView):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer

class NoteDetail(generics.ListCreateAPIView):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer

class HomoList(APIView):

    def get(self, request, format=None, **kws):
        _w = kws.get('word', '')
        if _w:
            words = Words.objects.get(wid=[1,2])#Words.objects.filter(definition=Definitions.objects.filter(words=Words.objects.get(word=_w.lower()))[1])
            serializer = WordSerializer(words, many=True)
            _data = serializer.data
        else:
            _data = {}
        return Response({'msg': 'success', 'data': _data}, status=status.HTTP_200_OK)

class UserList(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserListSerializer

class UserProfile(APIView):
    """"
    This should use POST method
    """

    def get(self, request, format=None, **kws):
        _id = kws.get('uid', '')
        _auth = request.META.get('HTTP_AUTHORIZATION')
        try:
            _u = Users.objects.get(uid=_id, register=Registers.objects.get(code=_auth))

            _lid = request.query_params.get('level', _u.level_id)
            _is_male = request.query_params.get('ismale', _u.is_male)
            _daily_task = request.query_params.get('task', _u.daily_task)
            _name = request.query_params.get('name', _u.name)

            _u.level = Levels.objects.get(lid=_lid)
            _u.is_male =  _is_male
            _u.daily_task = _daily_task
            _u.name = _name
            _data = {'name': _name, 'uid': _id, 'level': _lid, 'ismale': _is_male, 'task': _daily_task}
            _u.save()
            response = Response({'msg': 'success', 'data': _data}, status=status.HTTP_200_OK)
        except:
            response = Response({'msg': 'failed'}, status=status.HTTP_404_NOT_FOUND)

        return response

    def post(self, request, format=None):
        response = Response({'msg': 'failed'}, status=status.HTTP_404_NOT_FOUND)
        print(dir(request))
        return
        try:
            u = Users.objects.get(uid=request.data.get('uid', ''))
            r = Registers.objects.get(user=u)
            if request.authorization('uid', '') == r.code:
                pass
        except:
            return response
        
        is_male = True if request.data.get('ismale', True) else False
        level_id = request.data.get('ismale', 1)
        name = request.data.get('ismale', '')
        daily_task = request.data.get('ismale', '')

class Register(generics.ListCreateAPIView):
    serializer_class = RegisterSerializer
    def get(self, request, format=None):
        register = Registers.objects.all()
        serializer = RegisterSerializer(register, many=True)
        _data = serializer.data
        response = Response({'msg': 'success', 'data': _data}, status=status.HTTP_200_OK)
        return response

class Login(APIView):
    """
    Must be fixed
    """
    def post(self, request, format=None):
        content = request.data.get('content', '')
        code = request.data.get('code', '')
        r = None
        try:
            r = Registers.objects.get(content=content, code=code)
        except:
            pass

        if r:
            try:
                u = Users.objects.get(register=r)
            except:
                pass
            if u:
                if int == type(u.level_id):
                    pass
                    #_l = Levels.objects.get(lid=u.level_id)
                    #level = {'lid': _l.lid, 'name': _l.name, 'counts': _l.counts}
                _d = {'name': u.name, 'uid': u.uid, 'level': u.level_id, 'ismale': u.is_male, 'task': u.daily_task}
                response = Response({'msg': 'success', 'data': _d}, status=status.HTTP_200_OK)
                #response.set_cookie('shanbay_token', code, 3600)
            else:
                response = Response({'msg': 'failed'}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        else:
            response = Response({'msg': 'failed'}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        return response

class LoginOut(APIView):
    def get(self, request, format=None):
        response = Response({'msg': 'logout success'})
        response.delete_cookie('shanbay_token')
        return response