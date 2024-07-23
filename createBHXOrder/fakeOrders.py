import json
import random
import datetime
categoryF1 = ["8781","8139","8790","8782","8783","8788","8785","8779","12439","8400","2565","2513","2947"]
categoryNF1 = ['8275', '2382', '2282', '7199', '5436',"8820", '8', '7086', '3003', '3238', '4585', '2486', '2385', '3525', '2443', '10340', '6642', '2530', '2463', '2491', '14', '8638', '3727', '3233', '5872', '6597', '3365', '2683', '7579', '8318', '7171', '7478', '2483', '2566', '2388', '2446', '3124', '7082', '3728', '2511', '3507', '8286', '10338', '56', '2965', '2564', '6553', '3506', '2507', '7558', '8163', '2943', '3026', '8791', '2484', '3104', '3188', '3265', '2804', '6653', '2504', '7599', '3004', '4929', '7258', '3362', '7779', '3360', '3023', '8645', '2944', '4352', '3345', '7694', '7162', '2883', '3465', '7083', '3028', '2519', '8159', '3368', '3234', '3359', '3487', '2386', '9', '7172', '2510', '2563', '3027', '7259', '7461', '3732', '7068', '2809', '8158', '3235', '8285', '7460', '7169', '6562', '2516', '2444', '3357', '8160', '9081', '3358', '7459', '8966', '3361', '4888', '2286', '2485', '2517', '3708', '2787', '2289', '3740', '2687', '9498', '30', '2803', '3237', '2903', '8320', '7622', '7598', '2567', '3364', '3063', '2465', '9027', '12538', '2464', '2493', '8681', '3485', '4326', '2806', '8938', '2526', '3226', '2945', '10778', '8678', '2387', '2524', '7170', '7618', '8271']

with open('products.json',encoding="utf8") as f:
    data = json.load(f)

orders = []
for index in range(0, 50000):
    listTemp = random.sample(data, len(data))
    categoryF = random.sample(categoryF1, len(categoryF1))
    categoryNF = random.sample(categoryNF1, len(categoryNF1)) 
    cItems = random.randint(2,10)
    items = []
    for i in range(1,cItems):
        percent = random.randint(1, 10)
        if(percent > 3):
            categoryId = categoryF[random.randint(0,len(categoryF)-1)]
            for j in listTemp:
                if(j["idCate"] == categoryId):
                    itemTemp = {"productId":j["id"],"categoryId":categoryId, "quantity":random.randint(1,3)}
        else:
            categoryId = categoryNF[random.randint(0,len(categoryNF)-1)]
            for j in listTemp:
                if(j["idCate"] == categoryId):
                    itemTemp = {"productId":j["id"],"categoryId":categoryId, "quantity":random.randint(1,3)}
        items.append(itemTemp)
    orders.append({"orderId":str(index),"userId":random.randint(1,1000),"items":items})

with open("orrders.json", "w") as write_file:
    json.dump(orders, write_file)

json_string = json.dumps(orders)









