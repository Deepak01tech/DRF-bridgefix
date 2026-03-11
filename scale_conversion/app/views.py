from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['Post'])
def scale_conversion_view(request):
    '''View to convert length from mm to cm,metre,inches,foot .'''
    # enter the length in mm and convert it to cm,metre, inches,foot

    length = request.data.get('length')
    if length is not None:
        try:
            length = float(length)
            cm = length / 10
            metre = length / 1000
            inches = length / 2.54
            feet= inches / 12
            # return render(request, 'scale_conversion.html', {'inches': inches})
            return Response({'centimetre':cm,'metre':metre,'inches': inches, 'feet': feet})
        except ValueError:
            # return render(request, 'scale_conversion.html', {'error': 'Invalid input. Please enter a number.'})
            return Response({'error': 'Invalid input. Please enter a number.'})
    else:
        # return render(request, 'scale_conversion.html')
        return Response({'error': 'Please provide a length in cm.'})

