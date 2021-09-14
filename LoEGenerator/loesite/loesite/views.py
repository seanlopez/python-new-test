from django.shortcuts import render
from django.http import FileResponse
from .editor import loe_editor

def portal_display(request):
    return render(request, "ise_loe_generator.html")

def ise_form_process(request):
    form_dict = request.POST.dict()
    editor = loe_editor.loe_editor(form_dict, "./LoETemplate/Security LoE Template v0.2.xlsx", "ISE")
    editor.ise_requirement_phase_editor()
    editor.ise_design_phase_editor()
    editor.ise_nip_phase_editor()
    editor.ise_nruf_phase_editor()
    editor.ise_lab_testing_phase_editor()
    editor.ise_implementation_phase_editor()
    editor.ise_kt_phase()
    filename = editor.save_close_sheet("./output_LoE")

    return render(request, "downloadpage.html", {"customer_name": form_dict["customer_name"], "filename": filename})

def file_download(request):
    get_info = request.GET
    filename = get_info.get("keyjobs")
    file = open(f'./output_LoE/{filename}', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response
