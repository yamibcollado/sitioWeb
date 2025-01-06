
def importe_total_carro(request):
    total=0
    if request.user.is_autheticated:
        for key, value in request.session["carro"].items():
            total=total+(float(value["precio"]*value["cantidad"]))
