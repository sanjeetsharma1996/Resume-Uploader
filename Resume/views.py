from django.shortcuts import render,redirect
from .forms import ResumeForm
from .models import ResumeModel
from django.views import View

class HomeView(View):
 def get(self, request):
  form = ResumeForm()
  candidates = ResumeModel.objects.all()
  return render(request, 'home.html', { 'candidates':candidates, 'form':form})

 def post(self, request):
  form = ResumeForm(request.POST, request.FILES)
  if form.is_valid():
   form.save()
   return redirect('/')
  else:
   return render(request, 'home.html', {'form':form})

class CandidateView(View):
 def get(self, request, pk):
  candidate = ResumeModel.objects.get(pk=pk)
  return render(request, 'candidate.html', {'candidate':candidate})


 def post(self, request, pk):
   delt_id = ResumeModel.objects.get(pk=pk)
   delt_id.delete()
   return redirect('/')




      



      