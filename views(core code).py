from django.shortcuts import render, redirect
from .models import EcoCom, AvgInc

def ini_ectcalculate(request):
	ecocoms = EcoCom.objects.order_by('-date_added')
	pageview = len(ecocoms)
	"""Make a new calculation."""
	if request.POST.get('ectext') and request.POST.get('aitext'):
		ecform = EcoCom()
		ecform.ectext = request.POST.get('ectext')
		ecform.owner = request.user
		ecform.save()
		aiform = AvgInc()
		aiform.aitext = request.POST.get('aitext')
		aiform.owner = request.user
		aiform.save()
		return redirect('ect_cal:ectcalculate')
			
	else:
	# No data submitted; create a blank form.
		ecform = EcoCom()
		aiform = AvgInc()
	
	context = {'ecform': ecform, 'aiform': aiform, 'pageview': pageview}
	return render(request, 'ect_cal/ini_ectcalculate.html', context)
	
def ectcalculate(request):
	"""Show the result of the calculation."""
	ecocoms = EcoCom.objects.order_by('-date_added')
	avgincs = AvgInc.objects.order_by('-date_added')
	pageview = len(ecocoms)
	ecocom = ecocoms[0]
	avginc = avgincs[0]
	gap = int(ecocom.ectext) - int(avginc.aitext)*3
	"""Make a new calculation."""
	if request.POST.get('ectext') and request.POST.get('aitext'):
		ecform = EcoCom()
		ecform.ectext = request.POST.get('ectext')
		ecform.owner = request.user
		ecform.save()
		aiform = AvgInc()
		aiform.aitext = request.POST.get('aitext')
		aiform.owner = request.user
		aiform.save()
		return redirect('ect_cal:ectcalculate')
			
	else:
	# No data submitted; create a blank form.
		ecform = EcoCom()
		aiform = AvgInc()
	
	if gap <= 0:
		process = "该劳动者的经济补偿金免征个人所得税"
		result = "0"
	elif gap >0 and gap <= 36000:
		pro_result = gap*0.03
		process = "( " + str(ecocom.ectext) + " - " + str(avginc.aitext) + "*3 ) * 3% = " + str(pro_result)+ " 元"
		result = str(pro_result)
	elif gap >36000 and gap <= 144000:
		pro_result = gap*0.1-2520
		process = "( " + str(ecocom) + " - " + str(avginc) + "*3 ) * 10% - 2520 = " + str(pro_result)+ " 元"
		result = str(pro_result)
	elif gap >144000 and gap <= 300000:
		pro_result = gap*0.2-16920
		process = "( " + str(ecocom) + " - " + str(avginc) + "*3 ) * 20% -16920 = " + str(pro_result)+ " 元"
		result = str(pro_result)
	elif gap >300000 and gap <= 420000:
		pro_result = gap*0.25-31920
		process = "( " + str(ecocom) + " - " + str(avginc) + "*3 ) * 25% -31920 = " + str(pro_result)+ " 元"
		result = str(pro_result)
	elif gap >420000 and gap <= 660000:
		pro_result = gap*0.3-52920
		process = "( " + str(ecocom) + " - " + str(avginc) + "*3 ) * 30% -52920 = " + str(pro_result)+ " 元"
		result = str(pro_result)
	elif gap >660000 and gap <= 960000:
		pro_result = gap*0.35-85920
		process = "( " + str(ecocom) + " - " + str(avginc) + "*3 ) * 35% -85920 = " + str(pro_result)+ " 元"
		result = str(pro_result)
	elif gap >960000 :
		pro_result = gap*0.40-181920
		process = "( " + str(ecocom) + " - " + str(avginc) + "*3 ) * 40% -181920 = " + str(pro_result)+ " 元"
		result = str(pro_result)
		
	context = {'ecform': ecform, 'aiform': aiform, 'ecocom': ecocom, 'avginc': avginc, 'process': process, 'result': result, 'pageview': pageview}
	return render(request, 'ect_cal/ectcalculate.html', context)
