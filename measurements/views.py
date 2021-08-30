from .logic.logic_measurements import get_all_measurements, get_specific_measurement, delete_specific_measurement
from django.http import HttpResponse
from django.core import serializers

def get_measurements(request):
    measurements = get_all_measurements()
    measurements_list = serializers.serialize('json', measurements)
    return HttpResponse(measurements_list, content_type='application/json')

def get_measurement(request, id):
    measurement = get_specific_measurement(id=id)
    return HttpResponse(measurement, content_type='application/json')

def delete_measurement(request, id):
    measurement = delete_specific_measurement(id=id)
    return HttpResponse(measurement, content_type='application/json')