from rest_framework import serializers
from app.to_do.models import ToDo


class ToDoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToDo
        fields = ['id', 'task', 'created_at', 'do_in', 'is_finished',]
        ready_only_fields = ['creator', 'created_at']

    def create(self, validated_data):
        validated_data['creator'] = self.context['request'].user
        return super().create(validated_data)
