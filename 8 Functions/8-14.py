def car(mf,mn,**info):
    info['manufactur']=mf
    info['manuname']=mn
    return info
car_info=car('hetanshi','prajapati',color='blue',tow_package='True')
print(car_info)