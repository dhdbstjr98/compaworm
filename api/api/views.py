from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from account.models import User, UserToken
from .models import Comment, Comparison
from .oauth import oauth, AuthError
import json
import requests
import uuid


# Create your views here.
class UserMeView(APIView):
    def post(self, request):
        try:
            body = json.loads(request.body)
            sns = body.get("sns", None)
            access_token = body.get("access_token", None)
            if access_token == None or sns == None:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            oauth_result = oauth(sns, access_token)
            token = str(uuid.uuid4())

            try:
                user = User.objects.get(sns_id=oauth_result["sns_id"])
            except Exception:
                user = User.objects.create(
                    sns_id=oauth_result["sns_id"],
                    name=oauth_result["name"],
                    profile=oauth_result["profile"],
                    password=str(uuid.uuid4()),
                )

            UserToken.objects.create(user=user, token=token)

            return Response(
                {"name": user.name, "profile": user.profile, "token": token},
                status=status.HTTP_200_OK,
            )
        except json.decoder.JSONDecodeError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except AuthError:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def get(self, request):
        if request.user.is_anonymous:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(
            {"name": request.user.name, "profile": request.user.profile},
            status=status.HTTP_200_OK,
        )

    def delete(self, request):
        if request.user.is_anonymous:
            return Response(status=status.HTTP_404_NOT_FOUND)

        UserToken.objects.filter(token=request.META["HTTP_AUTHORIZATION"]).delete()

        return Response(status=status.HTTP_200_OK)


class ComparisonView(APIView):
    def put(self, request, obj1, obj2):
        try:
            if request.user.is_anonymous:
                return Response(status=status.HTTP_403_FORBIDDEN)

            body = json.loads(request.body)

            is_obj1 = body.get("is_obj1", None)

            if is_obj1 == None:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            # 글자 순으로 정렬
            if obj2 < obj1:
                obj1, obj2 = obj2, obj1
                is_obj1 = not is_obj1

            try:
                Comparison.objects.get(obj1=obj1, obj2=obj2, user=request.user).delete()
            except Comparison.DoesNotExist:
                pass
            finally:
                Comparison.objects.create(
                    obj1=obj1, obj2=obj2, is_obj1=is_obj1, user=request.user
                )

            return Response(status=status.HTTP_201_CREATED)

        except json.decoder.JSONDecodeError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, obj1, obj2):
        # 글자 순으로 정렬
        if obj2 < obj1:
            obj1, obj2 = obj2, obj1

        total = Comparison.objects.filter(obj1=obj1, obj2=obj2).aggregate(
            Count("obj1")
        )["obj1__count"]
        obj1_count = Comparison.objects.filter(
            obj1=obj1, obj2=obj2, is_obj1=True
        ).aggregate(Count("obj1"))["obj1__count"]
        obj2_count = total - obj1_count

        res = {obj1: obj1_count, obj2: obj2_count}

        if not request.user.is_anonymous:
            try:
                yours = Comparison.objects.get(obj1=obj1, obj2=obj2, user=request.user)
                res["yours"] = obj1 if (yours.is_obj1) else obj2
            except Comparison.DoesNotExist:
                pass

        return Response(res, status=status.HTTP_200_OK)

    def delete(self, request, obj1, obj2):
        if request.user.is_anonymous:
            return Response(status=status.HTTP_403_FORBIDDEN)

        # 글자 순으로 정렬
        if obj2 < obj1:
            obj1, obj2 = obj2, obj1

        try:
            Comparison.objects.get(obj1=obj1, obj2=obj2, user=request.user).delete()
            return Response(status=status.HTTP_200_OK)
        except Comparison.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CommentView(APIView):
    def get(self, request, obj1, obj2):
        # 글자 순으로 정렬
        reversed = False
        if obj2 < obj1:
            obj1, obj2 = obj2, obj1
            reversed = True

        ret = []
        try:
            comments = Comment.objects.filter(obj1=obj1, obj2=obj2)
            for comment in comments:
                row = {
                    "comment": comment.comment,
                    "author": comment.author.name,
                    "created_at": comment.created_at.strftime("%Y-%m-%d %H-%M-%S"),
                    "obj": comment.obj1 if comment.is_obj1 else comment.obj2,
                }

                if reversed:
                    row["obj1"] = comment.obj2
                    row["obj2"] = comment.obj1
                else:
                    row["obj1"] = comment.obj1
                    row["obj2"] = comment.obj2

                ret.append(row)
        except Comment.DoesNotExist:
            pass

        return Response(ret, status=status.HTTP_200_OK)

    def post(self, request, obj1, obj2):
        try:
            if request.user.is_anonymous:
                return Response(status=status.HTTP_403_FORBIDDEN)

            body = json.loads(request.body)
            is_obj1 = body.get("is_obj1", None)
            comment = body.get("comment", None)

            if is_obj1 == None or comment == None:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            # 글자 순으로 정렬
            if obj2 < obj1:
                obj1, obj2 = obj2, obj1
                is_obj1 = not is_obj1

            Comment.objects.create(
                obj1=obj1,
                obj2=obj2,
                author=request.user,
                is_obj1=is_obj1,
                comment=comment,
            )

            return Response(status=status.HTTP_200_OK)
        except json.decoder.JSONDecodeError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
