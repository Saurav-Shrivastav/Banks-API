from rest_framework.serializers import ModelSerializer, CharField

from  banks.models import Branch


class BranchSerializer(ModelSerializer):
    bank = CharField(source='bank_id.name', read_only=True)

    class Meta:
        model = Branch
        fields = [
            'ifsc',
            'bank',
            'branch',
            'address',
            'city',
            'district',
            'state',
        ]