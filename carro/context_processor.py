def importe_total_carro(request):
    
    carro = request.session.get('carro', {})

    total = 0
    
    for key, value in carro.items():
        total += value['precio'] * value['cantidad'] 
    return {'importe_total_carro': total}
    