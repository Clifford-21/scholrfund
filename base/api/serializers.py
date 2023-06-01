from rest_framework import serializers
from applier.models import Learner, Address, Application

class LearnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Learner
        fields = "__all__"

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"