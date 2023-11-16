from rest_framework import serializers
from .models import Record, DesiredValues, nameChoices


class ChoiceField(serializers.ChoiceField):

    def to_representation(self, value):
        return self.choices[value]

    def to_internal_value(self, data):
        result = None
        for k, v in self.choices.items():
            if data == str(v):
                return int(k)
        if not result:
            raise serializers.ValidationError('数据不在选项中')
        return result


class RecordSerializer(serializers.ModelSerializer):
    name = ChoiceField(choices=nameChoices.choices)
    time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)

    class Meta:
        model = Record
        fields = ['name', 'value', 'time']


class DesiredValuesSerializer(serializers.ModelSerializer):
    name = ChoiceField(choices=nameChoices.choices)

    class Meta:
        model = DesiredValues
        fields = ['name', 'desired_value']
