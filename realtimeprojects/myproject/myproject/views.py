from django.shortcuts import render

def Error_404(req,exception):
    return render(req,'404.html',status=404)

