from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import UploadFileForm
import re,csv
# ^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$
choices = []
def handle_uploaded_file(f):  
    with open('website/csvtowats/upload/details.csv', 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)
    with open('website/csvtowats/upload/details.csv', 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            return row
# Imaginary function to handle an uploaded file.
# from somewhere import handle_uploaded_file   

def csvtowats(request):
    if request.method == 'POST':  
        form = UploadFileForm(request.POST, request.FILES)  
        if form.is_valid():  
            row = handle_uploaded_file(request.FILES['file'])
            choices.append(row)  
            return redirect("csvfields")
        else:
            return HttpResponse("Invalid file")
    else: 
        form = UploadFileForm()
    return render(request,'website/csvtowats.html',{'form':form}) 
def csvfields(request):
    name = request.POST.getlist("choices")
    if(name):
        data = []
        output = []
        with open('website/csvtowats/upload/details.csv', 'r') as file:
            files = csv.DictReader(file)
            for rows in files:
                for row in rows:
                    if row in name:
                        if (rows[row].isnumeric()):
                            button = f"""<button type="button" class="btn btn-secondary"><a style="text-decoration:None;color:white;"href="https://wa.me/91{rows[row]}?text=Hi!">Whatsapp!</a></button>"""
                            data.append(button)
                        else:data.append(rows[row])
                output.append(data)
                data = []
        return render(request,'website/csvfields.html',{'fields':0,'output':output,'name':name})
    return render(request,'website/csvfields.html',{'fields':choices[0]})
# Create your views here.
