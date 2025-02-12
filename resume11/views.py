from dataclasses import fields
from django.forms import modelformset_factory
from django.shortcuts import render,redirect, get_object_or_404
from .models import per
from .models import aca
from .models import cc
from.forms import person, qualf, cer

# Create your views here.
def base(request):
    return render(request,'base.html')
def home(request):
    return render(request,'home.html')
def entry(request):
    if request.method == 'POST':
        perid = request.POST.get('perid')
        exe_id = per.objects.filter(perid=perid).first()
        if exe_id:
            return render(request, 'entry.html', {'error': 'The person id already stored'})

        personal = per(
            name=request.POST.get('name'),
            perid=request.POST.get('perid'),
            dob=request.POST.get('dob'),
            ph_no=request.POST.get('ph_no'),
            mail=request.POST.get('mail'),
            sx=request.POST.get('sx'),
            ambition=request.POST.get('ambition'),
            lan=request.POST.get('lan'),
            add=request.POST.get('add')
        )
        personal.save()

        cs_list = request.POST.getlist('cs[]')
        sch_clg_list = request.POST.getlist('sch_clg[]')
        uni_list = request.POST.getlist('uni[]')
        year_list = request.POST.getlist('year[]')
        per_list = request.POST.getlist('per[]')
        for cs, sch_clg, uni, year, percentage in zip(cs_list, sch_clg_list, uni_list, year_list, per_list):
            course = aca(
                personid=personal,
                cs=cs,
                sch_clg=sch_clg,
                uni=uni,
                year=year,
                per=percentage
            )
            course.save()

        cer_list = request.POST.getlist('cer[]')
        for cer in cer_list:
            certificate = cc(
                person1id=personal,
                cer=cer
            )
            certificate.save()
    return render(request, 'entry.html')

def report(request):
    inf=per.objects.all()
    return render(request, 'report.html',locals())
def viewres(request,id):
    per1=get_object_or_404(per,id=id)
    academic=aca.objects.filter(personid=per1)
    courses=cc.objects.filter(person1id=per1)
    context={
        'a':per1,
        'b':academic,
        'c':courses,
    }
    return render(request, 'viewres.html',context)

def editres(request,id):
    per1 = get_object_or_404(per, pk=id)
    academc = aca.objects.filter(personid=per1)
    cours = cc.objects.filter(person1id=per1)

    acaformset = modelformset_factory(aca, fields=["cs", "sch_clg", "uni", "year", "per"], extra=0)
    acaformset1 = modelformset_factory(cc, fields=["cer"], extra=0)

    form1 = person(request.POST or None, instance=per1)
    form2 = acaformset(request.POST or None, queryset=academc)
    form3 = acaformset1(request.POST or None, queryset=cours)

    if request.method == "POST":
        if form2.is_valid() and form3.is_valid():
            queryset_ids = [obj.id for obj in academc]
            submitted_ids = [
                form.cleaned_data["id"] for form in form2.forms if "id" in form.cleaned_data
            ]
            print("Queryset IDs for aca:", queryset_ids)  # Debug
            print("Submitted IDs for Form2:", submitted_ids)  # Debug

            invalid_ids = [submitted_id for submitted_id in submitted_ids if submitted_id not in queryset_ids]
            if invalid_ids:
                print("Invalid IDs:", invalid_ids)  # Debug invalid IDs

        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            form1.save()
            form2.save()
            form3.save()
            return redirect('/report')
    context = {
        "form1": form1,
        "form2": form2,
        "form3": form3,
    }
    return render(request, "editres.html", context)

def delres(request,id):
    obj=get_object_or_404(per,pk=id)
    obj1=aca.objects.filter(personid=obj)
    obj2=cc.objects.filter(person1id=obj)
    if request.method=="POST":
        obj.delete()
        obj1.delete()
        obj2.delete()
        return redirect("/report")
    return render(request,'delres.html')