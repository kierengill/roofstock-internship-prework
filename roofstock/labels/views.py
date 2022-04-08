from cProfile import label
from django.shortcuts import render, redirect
import easypost

easypost.api_key = 'EZTKc27d7f3ecfd449289dc9c08e8eb50577kqhyAq90wByO0DcFpe1QzQ'

# Create your views here.
def home(request):
    if request.method == "POST":
        data = request.POST

        print(data)
        shipment = easypost.Shipment.create(

            from_address = {
                "name": data['name'],
                "street1": data['name'],
                "street2": data['street2'],
                "city": data['city'],
                "state": data['state'],
                "zip": (data['zip']),
                "country": "US",
                "phone": data['phone'],
            },
            to_address = {
                "name": data['to_name'],
                "street1": data['to_street1'],
                "city": data['to_city'],
                "state": data['to_state'],
                "zip": data['to_zip'],
                "country": "US",
                
            },
            parcel = {
                "length": data['length'],
                "width": data['width'],
                "height": data['height'],
                "weight": data['weight'],
            },
        )

        try:
            shipment.buy(rate=shipment.lowest_rate())
        except Exception as e:
            return redirect('/errors')

        postageLabel = shipment.postage_label.label_url
        context = {
            'postage': postageLabel
        }
        return render(request, 'labels/label.html', context)

    return render(request, 'labels/dashboard.html')

def errors(request):
	return render(request, 'labels/errors.html')

def label(request):
	return render(request, 'labels/label.html')