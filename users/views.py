from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserSerializer



# Create your views here.
class AuthAPIView(APIView):
    def post(self, request):
        email = request.data.get("email")
        is_exist_user = User.objects.filter(email=email).exists()
        # 아직 회원가입 안 된 유저일 때
        if not is_exist_user:
            serializer = UserSerializer(data=request.data)
            # jwt 토큰 접근
            if serializer.is_valid():
                user = serializer.save()

                # jwt 토큰 접근
                token = TokenObtainPairSerializer.get_token(user)
                refresh_token = str(token)
                access_token = str(token.access_token)
                res = Response(
                    {
                        "user": serializer.data,
                        "message": "register successs",
                        "token": {
                            "access": access_token,
                            "refresh": refresh_token,
                        },
                    },
                    status=status.HTTP_200_OK,
                )

                # jwt 토큰 => 쿠키에 저장
                res.set_cookie("access", access_token)
                res.set_cookie("refresh", refresh_token)
                return res
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        else:  #로그인시 토큰 발급
            user = User.objects.get(email=email)
            serializer = UserSerializer(user)

            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": serializer.data,
                    "message": "login successs",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )

            # jwt 토큰 => 쿠키에 저장
            res.set_cookie("access", access_token, httponly=True)
            res.set_cookie("refresh", refresh_token, httponly=True)
            return res

    # 로그아웃
    def delete(self, request):
        # 쿠키에 저장된 토큰 삭제 => 로그아웃 처리
        response = Response({
            "message": "Logout success"
        }, status=status.HTTP_202_ACCEPTED)
        response.delete_cookie("access")
        response.delete_cookie("refresh")
        return response
