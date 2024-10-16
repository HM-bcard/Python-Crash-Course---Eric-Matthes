def car_info(manufacturer,model,**info):
    """Print information about a car"""
    info['make']=manufacturer
    info['model']=model
    return info

car1 = car_info('subaru','outback',color = 'burgundy',mileage=132328
                ,sunroof='no')

print(car1)
