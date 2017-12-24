#!/usr/bin/env python
from rest_framework import serializers
from .models import Bucketlist

class BucketlistSerializer(serializers.ModelSerializer):
	"""Serializer to map the model instance to JSON format."""

	class Meta:
		"""Meta class to map serializer's with the model fiels."""
		model = Bucketlist
		fields = ('id', 'name', 'date_created', 'date_modified')
		read_only_fields = ('date_created', 'date_modified')
