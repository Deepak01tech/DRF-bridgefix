from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['Post'])
def scale_conversion_view(request):
    '''View to convert length from mm to cm,metre,inches,foot .'''


    length = request.data.get('length')
    unit= request.data.get('unit')
    if length and unit is not None:
        try:
            if unit=="centimetre":

                length_in_centimetre = float(length)
                cm = length_in_centimetre 
                mm=length_in_centimetre*10
                metre = length_in_centimetre * 100
                inches = length_in_centimetre/ 2.54
                feet= length_in_centimetre / 30.48

            elif unit =="millimetre":
                length_in_millimetre = float(length)
                mm= length_in_millimetre
                cm = length_in_millimetre / 10
            
                metre = length_in_millimetre / 1000
                inches = length_in_millimetre / 25.4
                feet= length_in_millimetre/304.8
            elif unit == "metre":
                length_in_metre = float(length)
                cm = length_in_metre * 100
                mm=length_in_metre*1000
                metre = length_in_metre
                inches = length_in_metre *39.37
                feet= length_in_metre *3.281

            elif unit == "inches":
                length_in_inch = float(length)
                cm = length_in_inch *2.54 
                mm=length_in_inch*25.4
                metre = length_in_inch * 0.0254
                inches = length_in_inch
                feet= length_in_inch / 12

            elif unit == "feet":
                length_in_feet = float(length)
                cm = length_in_feet * 30.48
                mm=length_in_feet *304.8
                metre = length_in_feet / 1000
                inches = length_in_feet * 12
                feet= length_in_feet


            
            return Response({'millimetre':mm,'centimetre':cm,'metre':metre,'inches': inches, 'feet': feet})
        except ValueError:
           
            return Response({'error': 'Invalid input. Please enter a number.'})
    else:
        
        return Response({'error': 'Please provide a length and unit '})

