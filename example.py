def get_vat(payment, percent=18):
    try:    
        payment = float(payment)
        percent = int(percent)
        vat = payment / 100 * percent
        vat = round(vat,2)
        return "Сумма НДС {} рублей".format(vat)
    except (TypeError,ValueError):
        return 'Ошибка, проверьте воод'     

result = get_vat(1000, 18)
print(result)