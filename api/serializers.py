from rest_framework import serializers
from api.models import *

class QuartierSerializer(serializers.ModelSerializer):

    class Meta:
        model=Quartier
        fields=('id','nom_quartier','date','ville')



class VideosSerializer(serializers.ModelSerializer):

    class Meta:
        model=Videos
        fields=('id','mot_cle','Date','fichier','quartiers') 

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields = '__all__'  

class AudioSerializer(serializers.Serializer):
    audio=serializers.FileField(required=True)

              

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        depth = 1
        

    def create(self, validated_data):
        
        user = User(
            email=validated_data['email'],
            user_name=validated_data['user_name'],
            
           
            is_active = True,
            
        )
        user.set_password(validated_data['password'])
        user.save()
        return user               


        