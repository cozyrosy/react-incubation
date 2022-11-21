from django.shortcuts import render
from . models import Account, Application, SlotBooking
from . serializers import ApplicationSerializer, SlotBookingSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.


class BookingForm(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)
    def post(self,request):
        print('helooooooo')
        user =request.user
        print(user)
        print(request.data['full_name'])
        booking = ApplicationSerializer(data=request.data)
        data = {}
        if booking.is_valid():
            booking.save()
            print('ppppppppppppppppppppppppppppp')
            data['response']='registered'
        else:
            print(booking.errors)
            data=booking.errors
        return Response(data)    


class PendingList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        pendingg = Application.objects.filter(pending = True, approved=False, declined=False, allotted=False)
        serializer = ApplicationSerializer(pendingg, many=True)
        print(pendingg)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Approving(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    def post(self,request,id):
        try:
            booking = Application.objects.get(id=id)
            
            if booking.pending == True :
                
                booking.pending = False
                booking.approved = True
                booking.save()
                return Response(status=status.HTTP_200_OK)
        except:
            pass
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ApprovedList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        print("ffffffffffffffffffffffffffffffffff")
        booking = Application.objects.filter(approved = True)
        print(booking)
        serializer = ApplicationSerializer(booking,many=True)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Declining(APIView):
    def post(self,request,id):
        try:
            declining = Application.objects.get(id=id)
            print('mmmmmmmmmmmmmmmmmmmmmmmmmmmmmm')
            if declining.pending == True :
                print('nnnnnnnnnnnnnnnnnnnnnnnnnnnnn')
                declining.pending = False
                declining.declined = True
                declining.save()
                return Response(status=status.HTTP_200_OK)
        except:
            pass
            return Response(status=status.HTTP_400_BAD_REQUEST)



class DeclinedList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    print('innn classsssss')
    def get(self, request):
        print('innnnn getttttttttttttt')
        declineee = Application.objects.filter(declined = True)
        serializer = ApplicationSerializer(declineee, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class Slots(APIView):

    def get(self,request):
        slot = SlotBooking.objects.all()
        serializer = SlotBookingSerializer(slot, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
