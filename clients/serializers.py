from rest_framework import serializers
from .models import HealthProgram, Client

class HealthProgramSerializer(serializers.ModelSerializer):
    """Serializer for HealthProgram model."""
    class Meta:
        model = HealthProgram
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class ClientSerializer(serializers.ModelSerializer):
    """Serializer for Client model."""
    health_program = HealthProgramSerializer(read_only=True, allow_null=True)
    health_program_id = serializers.PrimaryKeyRelatedField(
        queryset=HealthProgram.objects.all(), 
        source='health_program', 
        write_only=True, 
        allow_null=True
    )

    class Meta:
        model = Client
        fields = [
            'id', 'first_name', 'last_name', 'date_of_birth', 'gender', 
            'address', 'phone_number', 'email', 'health_program', 
            'health_program_id', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_date_of_birth(self, value):
        """Validate date_of_birth format (YYYY-MM-DD)."""
        import re
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', value):
            raise serializers.ValidationError("Date of birth must be in YYYY-MM-DD format.")
        return value

    def validate_gender(self, value):
        """Validate gender is M or F."""
        if value not in ['M', 'F']:
            raise serializers.ValidationError("Gender must be 'M' or 'F'.")
        return value