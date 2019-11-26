def make_car(manufacturer,model,**other_info):
    Dic = {}
    Dic['M_name']= manufacturer
    Dic['model_no']=model
    for key, value in other_info.items():
        Dic[key]=value
        return  Dic
car= make_car('honda','2018',color='black',insured=True)
print(car)
