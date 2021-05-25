from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from account.models import User, UserToken
from .oauth import oauth, AuthError
import json
import requests
import uuid


# Create your views here.
class UserMe(APIView):
    def post(self, request):
        try:
            body = json.loads(request.body)
            sns = body.get('sns', None)
            access_token = body.get('access_token', None)
            if access_token == None or sns == None:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            oauth_result = oauth(sns, access_token)
            token = str(uuid.uuid4())

            try:
                user = User.objects.get(sns_id=oauth_result['sns_id'])
            except Exception:
                user = User.objects.create(sns_id=oauth_result['sns_id'],
                                           name=oauth_result['name'],
                                           profile=oauth_result['profile'],
                                           password=str(uuid.uuid4()))

            UserToken.objects.create(user=user, token=token)

            return Response(
                {
                    "name": user.name,
                    "profile": user.profile,
                    "token": token
                },
                status=status.HTTP_200_OK)
        except json.decoder.JSONDecodeError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except AuthError:
            return Response(status=status.HTTP_401_UNAUTHORIZED)