from django.shortcuts import render,redirect
from django.http import HttpResponse, request, HttpResponseRedirect
from django.views.generic import View,CreateView, DeleteView, ListView
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
#from weasyprint import HTML
#from weasyprint.text.fonts import FontConfiguration
from refugio.printreports import render_to_pdf
from .forms import MascotaForm, VacunaForm
from .models import Mascota, Vacuna
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.


#@method_decorator(login_required, name='dispatch')    
class VacunaCreate(CreateView):
	model = Vacuna
	template_name = 'vacuna/vacuna-form.html'
	form_class = VacunaForm
	success_url = reverse_lazy('vacuna_listar')

    
	def get_context_data(self, **kwargs):
		context = super(VacunaCreate, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		if form.is_valid():
			solicitud = form.save()
			solicitud.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form)) 

class ListMascotasPDF(View):
    def get(self, request, *args, **kwargs):
        mascota = Mascota.objects.all()
        data = {
                'mascotas': mascota,
                'cantidad': mascota.count()
        }
        pdf = render_to_pdf('mascota/reportmascota-pdf.html',data)
        return HttpResponse(pdf,content_type="application/pdf")

class ListVacunaPDF(View):
    def get(self, request, *args, **kwargs):
        vacuna = Vacuna.objects.all()
        data = {
                'vacunas': vacuna,
                'cantidad': vacuna.count()
        }
        pdf = render_to_pdf('vacuna/reportvacuna-pdf.html',data)
        return HttpResponse(pdf,content_type="application/pdf")


class VacunaList(ListView):
	model = Vacuna
	template_name = 'vacuna/vacuna-list.html'
	paginate_by = 5



    

def mascota_crear(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
        return redirect("mascota_listar")
    else:
        form = MascotaForm()
    return render(request, 'mascota/mascota_form.html', {'form': form})


class MascotaList(ListView):
	model = Mascota
	template_name = 'mascota/mascota_list.html'
	paginate_by = 5 

    

class MascotaListImagenes(ListView):
	model = Mascota
	template_name = 'mascota/mascota_listar_imagenes.html'
	paginate_by = 5 

def mascota_edit(request, folio_mascota):
    mascota = Mascota.objects.get(folio = folio_mascota)
    if request.method == 'GET':
        form = MascotaForm(instance=mascota)
    else:
        form = MascotaForm(request.POST, files=request.FILES,instance = mascota)
        if form.is_valid():
            form.save()
        return redirect('mascota_listar')
    return render(request, 'mascota/mascota_form.html',{'form':form})

def mascota_delete(request, folio_mascota):
    mascota = Mascota.objects.get(folio = folio_mascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascota_listar')
    return render(request, 'mascota/mascota_delete.html',{'mascota':mascota})

class VacunaDelete(DeleteView):
	model = Vacuna
	template_name = 'vacuna/vacuna_delete.html'
	success_url = reverse_lazy('vacuna_listar')

def vacuna_edit(request, id_vacuna):
    vacuna = Vacuna.objects.get(id = id_vacuna)
    if request.method == 'GET':
        form = VacunaForm(instance=vacuna)
    else:
        form = VacunaForm(request.POST, files=request.FILES,instance = vacuna)
        if form.is_valid():
            form.save()
        return redirect('vacuna_listar')
    return render(request, 'vacuna/vacuna-form.html',{'form':form})
