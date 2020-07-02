from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from banks.models import Branch, Bank
from banks.api.serializers import BranchSerializer


class ifscAPIView(APIView):
    permission_classes = [
        AllowAny,
    ]

    def get(self, request, *args, **kwargs):
        try:
            if request.GET.get('ifsc', ''):
                ifsc = request.GET.get('ifsc', '')
                branch = Branch.objects.get(ifsc=ifsc)
                serializer = BranchSerializer(branch)
                return Response(serializer.data)
            elif request.GET.get('bank', '') and request.GET.get('city', ''):
                bank_name = request.GET.get('bank', '')
                city = request.GET.get('city', '')
                bank = Bank.objects.get(name=bank_name)
                branch = Branch.objects.filter(bank_id=bank, city=city)
                serializer = BranchSerializer(branch, many=True)
                return Response(serializer.data)
            return Response("Either provide the ifsc or the bank and city in the query parameters!")

        except Exception as e:
            print(e)
            return Response(f'{e}')
