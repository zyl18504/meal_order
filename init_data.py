#encoding=utf8

user_dict = {
	'allen@conversant.com.cn':'123123'
}


restaurant_list = [u'餐厅A',u'餐厅B',u'餐厅C',u'餐厅D',u'餐厅E',u'餐厅F',u'餐厅G',u'餐厅H',u'餐厅I',u'餐厅J',u'餐厅K']

category_list = [u'凉菜',u'热菜',u'主食',u'酒水饮料']

menu_dict = {
	u'餐厅A':[
			{'name':u'酸辣土豆丝','price':16,'category':u'热菜'},
			{'name':u'醋溜土豆丝','price':17,'category':u'热菜'},
			{'name':u'麻辣土豆丝','price':15,'category':u'热菜'},
			{'name':u'清蒸土豆丝','price':18,'category':u'热菜'},
			{'name':u'红烧土豆丝','price':16,'category':u'热菜'},
			{'name':u'酸甜土豆丝','price':14,'category':u'热菜'}
			],
	u'餐厅B':[
			{'name':u'酸辣白菜','price':16,'category':u'热菜'},
			{'name':u'醋溜白菜','price':17,'category':u'热菜'},
			{'name':u'麻辣白菜','price':15,'category':u'热菜'},
			{'name':u'清蒸白菜','price':18,'category':u'热菜'},
			{'name':u'红烧白菜','price':16,'category':u'热菜'},
			{'name':u'酸甜白菜','price':14,'category':u'热菜'}
			],
	u'餐厅C':[
			{'name':u'酸辣豆腐','price':16,'category':u'热菜'},
			{'name':u'醋溜豆腐','price':17,'category':u'热菜'},
			{'name':u'麻辣豆腐','price':15,'category':u'热菜'},
			{'name':u'清蒸豆腐','price':18,'category':u'热菜'},
			{'name':u'红烧豆腐','price':16,'category':u'热菜'},
			{'name':u'酸甜豆腐','price':14,'category':u'热菜'}
			],
	u'餐厅D':[
			{'name':u'酸辣米饭','price':16,'category':u'主食'},
			{'name':u'醋溜米饭','price':17,'category':u'主食'},
			{'name':u'麻辣米饭','price':15,'category':u'主食'},
			{'name':u'清蒸米饭','price':18,'category':u'主食'},
			{'name':u'红烧米饭','price':16,'category':u'主食'},
			{'name':u'酸甜米饭','price':14,'category':u'主食'}
			],
}

from meal_order.models import *

#init user data
for u in user_dict.keys():
	new_user = User()
	new_user.email = u
	new_user.password = user_dict[u]
	new_user.save()




#init Restaurant data
for res in restaurant_list:
     r = Restaurant()
     r.name = res
     r.number = 0
     r.save()



# #init category data
for category in category_list:
    ca = Category()
    ca.name = category
    ca.save()




#init menu data
for res_name in menu_dict.keys():
    for menu in menu_dict[res_name]:
        new_menu = Food()
        new_menu.name = menu['name']
        new_menu.price = menu['price']
        new_menu.category = Category.objects.get(name=menu['category'])
        new_menu.restaurant = Restaurant.objects.get(name=res_name)
        new_menu.number = 0
        new_menu.save()


