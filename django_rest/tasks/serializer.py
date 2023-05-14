from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        
        # This is the manual form, but there's another way,
        # maybe you have a many fields.
        # fields = __all__
        
        fields = ('id', 'title', 'description', 'done')