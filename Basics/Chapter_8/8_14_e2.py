def car_info(manufacturer,model,**info):
    """ Bulding a dictionary of car info"""
    info['make'] = manufacturer
    info['model'] = model
    return info


car = car_info('subaru','outback',color='blue',tow_package=True)

print(car)
