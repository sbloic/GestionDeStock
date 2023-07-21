from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Gestion
from .forms import AddGestionForm, UpdateGestionForm

@login_required
def gestion_list(request):
	gestions = Gestion.objects.all()
	context = {
	                "title":"stock de PROGISSA",
	                "gestions":gestions
	}
	return render(request, "gestion/gestion_list.html", context=context)
	
@login_required
def per_product_view(request, pk):
	gestion = get_object_or_404(Gestion, pk=pk)
	context = {
	            'gestion': gestion


	}
	return render(request, "gestion/per_product.html", context=context)


@login_required
def add_product(request):
    if request.method == 'POST':
        add_form = AddGestionForm(request.POST)
        if add_form.is_valid():
            new_gestion = add_form.save(commit=False)
            new_gestion.sales = float(add_form.cleaned_data['cost_per_item']) * float(add_form.cleaned_data['quantity_sold'])
            new_gestion.save()
            return redirect('/gestion/')
    else:
        new_gestion = Gestion()  # créer une instance de la classe de modèle
        add_form = AddGestionForm(instance=new_gestion)  # passer la classe de modèle à la classe de formulaire
    return render(request, "gestion/gestion_add.html", {"form": add_form})

@login_required
def delete_gestion(request, pk):
	gestion = get_object_or_404(Gestion, pk=pk)
	gestion.delete()
	return redirect('/gestion/')

@login_required
def update_gestion(request, pk):
    gestion = get_object_or_404(Gestion, pk=pk)
    if request.method == 'POST':
        Update_Form = UpdateGestionForm(request.POST, instance=gestion)
        if Update_Form.is_valid():
            new_quantity_sold = Update_Form.cleaned_data['quantity_sold']
            old_quantity_sold = gestion.quantity_sold
            gestion = Update_Form.save(commit=False)
            gestion.sales = float(gestion.cost_per_item) * float(new_quantity_sold)
            gestion.save()
            if new_quantity_sold > old_quantity_sold:
                quantity_diff = new_quantity_sold - old_quantity_sold
                gestion.quantity_in_stock -= quantity_diff
                gestion.save()
            return redirect(f"/gestion/per_product/{pk}")
    else:
        Update_Form = UpdateGestionForm(instance=gestion)
    context = {'form': Update_Form}
    return render(request, 'gestion/gestion_update.html', context=context)

		






























			


