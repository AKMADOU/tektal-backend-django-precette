from django.shortcuts import render
from rest_framework import viewsets
import os

from backend.settings import MEDIA_ROOT
# os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/local/bin/ffmpeg"
import speech_recognition as sr
import moviepy.editor as me

from api.models import *
from api.serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, permissions, status
import json
from icecream import ic
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
#from rest_framework.pagination import PageNumberPagination
  


class QuartierAPIListView(generics.CreateAPIView):
    permission_classes=()
    queryset = Quartier.objects.all()
    serializer_class = QuartierSerializer

    def get(self, request, format=None):
        items = Quartier.objects.order_by('pk')
        #paginator = PageNumberPagination()
        #result_page = paginator.paginate_queryset(items, request)
        serializer = QuartierSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = QuartierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



class QuartierAPIView(generics.CreateAPIView):
    permission_classes=(
          
    )
    queryset = Quartier.objects.all()
    serializer_class = QuartierSerializer
    def get(self, request, id, format=None):
        try:
            item = Quartier.objects.get(pk=id)
            serializer = QuartierSerializer(item)
            return Response(serializer.data)
        except Quartier.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Quartier.objects.get(pk=id)
        except Quartier.DoesNotExist:
            return Response(status=404)
        self.data = request.data.copy()      
        serializer = QuartierSerializer(item, data= self.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Quartier.objects.get(pk=id)
        except Quartier.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)        




class VideosAPIListView(generics.CreateAPIView):
    permission_classes=(

    )
    queryset = Videos.objects.all()
    serializer_class = VideosSerializer

    def get(self, request, format=None):
        items = Videos.objects.order_by('pk')
        #paginator = PageNumberPagination()
        #result_page = paginator.paginate_queryset(items, request)
        serializer = VideosSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VideosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



class VideosAPIView(generics.CreateAPIView):
    permission_classes=()
    queryset = Videos.objects.all()
    serializer_class = VideosSerializer
    def get(self, request, id, format=None):
        try:
            item = Videos.objects.get(pk=id)
            serializer = VideosSerializer(item)
            return Response(serializer.data)
        except Videos.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Videos.objects.get(pk=id)
        except Videos.DoesNotExist:
            return Response(status=404)
        self.data = request.data.copy()      
        serializer = VideosSerializer(item, data= self.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Videos.objects.get(pk=id)
        except Videos.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)   



class VideosAPIListView(generics.CreateAPIView):
    permission_classes=()
    queryset = Videos.objects.all()
    serializer_class = VideosSerializer

    def get(self, request, format=None):
        items = Videos.objects.order_by('pk')
        #paginator = PageNumberPagination()
        #result_page = paginator.paginate_queryset(items, request)
        serializer = VideosSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VideosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)






class UserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get(self, request, id, format=None):
        try:
            item = User.objects.get(pk=id)
            serializer = UserSerializer(item)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = User.objects.get(pk=id)
        except User.DoesNotExist:
            return Response(status=404)
        self.data = request.data.copy()      
        serializer = UserSerializer(item, data= self.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = User.objects.get(pk=id)
        except User.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)   



class UserAPIListView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, format=None):
        items = User.objects.order_by('pk')
        #paginator = PageNumberPagination()
        #result_page = paginator.paginate_queryset(items, request)
        serializer = UserSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)          



class VideoByMotCleAPIView(generics.RetrieveAPIView):
    permission_classes=()
    queryset = Videos.objects.all()
    serializer_class = VideosSerializer
    def get(self, request,mot_cle, format=None):
        items = Videos.objects.filter(mot_cle__icontains=mot_cle)
        #paginator = PageNumberPagination()
        #result_page = paginator.paginate_queryset(items, request)
        serializer = VideosSerializer(items, many=True)
        return Response(serializer.data)

class QuartierByMotCleAPIView(generics.RetrieveAPIView):
    permission_classes=()
    queryset = Quartier.objects.all()
    serializer_class = QuartierSerializer
    def get(self, request,nom_quartier, format=None):
        items = Quartier.objects.filter(nom_quartier__icontains=nom_quartier)
        #paginator = PageNumberPagination()
        #result_page = paginator.paginate_queryset(items, request)
        serializer = QuartierSerializer(items, many=True)
        return Response(serializer.data)  




class AudioByQuartierAPIView(generics.CreateAPIView):
    permission_classes=()
    queryset = Videos.objects.all()
    serializer_class = AudioSerializer
    def post(self, request, format=None):
        #sound="Ladjaga..mp3"
        #mp3=os.path.join(request.data["audio"].name)
        
        audio = request.FILES['audio']                 
        audio_file = default_storage.save('audios/'+audio.name,ContentFile(audio.read()))
        print(audio_file)
        # ic(audio_file)
        # url="https://tektal-api.withvolkeno.com/mediafiles/"+audio_file
        url= MEDIA_ROOT+"/"+audio_file
        print(url)

        VIDEO_FILE = url
        OUTPUT_AUDIO_FILE = " converted.wav"
        OUTPUT_TEXT_FILE = " recognized.txt"        
        try:
            video_clip = me.AudioFileClip(r"{}".format(VIDEO_FILE))
            video_clip.write_audiofile(r"{}".format(OUTPUT_AUDIO_FILE))
            recognizer =  sr.Recognizer()
            audio_clip = sr.AudioFile("{}".format(OUTPUT_AUDIO_FILE))           
            with audio_clip as source:
                audio_file = recognizer.record(source)
            print("Please wait ...")
            result = recognizer.recognize_google(audio_file,language="fr-FR")            
            with open(OUTPUT_TEXT_FILE, 'w') as file:
                file.write(result)                
                items = Videos.objects.filter(mot_cle__icontains=result)                                                       
                serializer = VideosSerializer(items, many=True)
                return Response(serializer.data)                                           
        except Exception as e:            
            return Response({"message":str(e)})           
                    





class VideosByQuartierAPIView(generics.RetrieveAPIView):
    permission_classes=()
    queryset = Videos.objects.all()
    serializer_class = VideosSerializer
    def get(self, request,id, format=None):
        items = Videos.objects.filter(quartiers=id)
        #paginator = PageNumberPagination()
        #result_page = paginator.paginate_queryset(items, request)
        serializer = VideosSerializer(items, many=True)
        return Response(serializer.data)  

class UserRegisterView(generics.CreateAPIView):
    
    permission_classes = ()
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
       
        serializer = UserRegisterSerializer(data=request.data)
       
        if not serializer.is_valid():
            return Response({
                "status": "failure",
                "message": "invalid data",
                "error": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response({
            "status": "success",
            "message": "item successfully created",
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

