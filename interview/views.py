from interview.serializers import SheduleSerializer
from rest_framework import generics
from interview.models import shedule
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

class InterviewList(generics.ListCreateAPIView):
    queryset = shedule.objects.all()
    serializer_class = SheduleSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class Getsheduledtime(APIView):
    def get(self,request):
        id = request.query_params.get("id")
        pk = request.query_params.get("pk")
        date = request.query_params.get("date")
        one = shedule.objects.filter(id=id,date=date)
        two = shedule.objects.filter(id=pk,date = date)
        listone = []
        listtwo = []
        for i in one:
            for j in range(i.starttime,i.endtime):

                listone.append((j,j+1))
        for i in two:
            for j in range(i.starttime,i.endtime):
                listtwo.append((j,j+1))
        listone = set(listone)
        slotes  = listone.intersection(listtwo)
        return Response({"available slots are ":slotes})

    