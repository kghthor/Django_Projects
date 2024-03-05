from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views import View
# Create your views here.
from .forms import Informationform
from .models import Information

class MyView(View):
    def get(self, request, pk=None):
        if pk is not None:
            # This is the edit view
            instance = Information.objects.get(pk=pk)
            form = Informationform(instance=instance)
            return render(request, 'home/index.html', {'form': form, 'instance': instance})
        else:
            # This is the main view for listing and creating records
            form = Informationform()
            data = Information.objects.all()
            return render(request, 'home/index.html', {'form': form, 'data': data})
   
    def post(self, request, pk=None):
        if pk is not None:
            # This is the edit view, process the form for editing
            instance = Information.objects.get(pk=pk)
            form = Informationform(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('index')  # Replace 'your_redirect_url' with the appropriate URL
            else:
                return render(request, 'home/index.html', {'form': form, 'instance': instance})
        else:
            # This is the main view, process the form for creating
            form = Informationform(request.POST)
            data = Information.objects.all()
            if form.is_valid():
                form.save()
                form = Informationform()
                return render(request, 'home/index.html', {'message': "Information successfully saved", 'form': form, 'data': data})
            else:
                return render(request, 'home/index.html', {'form': form, 'data': data})


class Deleteview(View):
    def get(self, request, pk):
        print(pk)
        instance = Information.objects.get(pk=pk)
       
        instance.delete()
        return redirect('index') 
    
class Searchview(View):
    def get(self, request):
       query = request.GET.get('data', '')  # Get the search query from the request
       print(query,"fsfsfsfsafasfasfasfasfs")
       results = Information.objects.filter(name__icontains=query)
       print(results)
       data = [{'id':result.id,'name': result.name, 'mobile': result.mobile, 'email': result.email} for result in results]
       return JsonResponse({'data': data})
    


       