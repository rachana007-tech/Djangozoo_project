from django.shortcuts import render
from django.http import JsonResponse
bookings=[]

def display_zoo1(request):
    return render(request,"zoo1.html")
def display_sec(request):
    return render(request,"sec.html")

tiger={
    "title":"Bengal Tiger",
    "image":"https://transforms.stlzoo.org/production/animals/amur-tiger-01-01.jpg?w=1200&h=1200&auto=compress%2Cformat&fit=crop&dm=1658935145&s=95d03aceddd44dc8271beed46eae30bc",
    "age":"20",
    "care_taker":"Zoo keeper",
    "food":"Meat",
    "donated_by": "Srilalitha",
    "description":"The Bengal tiger, also known as the Royal Bengal Tiger,"
    " is a subspecies of tiger with a brownish-orange coat marked by dark brown to black stripes,"
    " though white and golden variants exist.",
    "place":"India,Bangladesh"
}
def display_tiger(request):
    return render (request,"animal.html",context=tiger)

lion={
    "title":"Asiatic Lion",
    "image":"https://cdn.britannica.com/29/150929-050-547070A1/lion-Kenya-Masai-Mara-National-Reserve.jpg",
    "age":"20",
    "care_taker":"Zoo keeper",
    "food":"Meat",
    "donated_by": "Larry",
    "description":"A lion is a large, muscular big cat with a short, yellow-gold coat and powerful build, "
    "distinguished by the shaggy mane of the adult male",
    "place":"India,South Africa,Kenya"
    "donate:False"
}
def display_lion(request):
    return render (request,"animal.html",context=lion)
orangutan={
    "title":"Orangutan",
    "image":"https://media.istockphoto.com/id/899748046/photo/orangutans.jpg?s=612x612&w=0&k=20&c=C97XcWZoGVWGfzCaZCdq3eSuGYNiwLq62si9-pqcFpk=",
    "age":"10",
    "care_taker":"Zoo keeper",
    "food":"Bananas",
    "donated_by": "SRM society",
    "description":"Orangutans are great apes native to the rainforests of Indonesia and Malaysia. They are now found only in parts of Borneo and Sumatra,"
    " but during the Pleistocene they ranged throughout Southeast Asia and South China.",
    "place":"Siberia,South-east asia",
    "donate":"True",
}
def display_orangutan(request):
    return render (request,"animal.html",context=orangutan)
zebra={
    "title":"Zebra",
    "image":"https://www.worldlandtrust.org/wp-content/uploads/2024/04/Plains-Zebra-body.jpg",
    "age":"10",
    "care_taker":"zoo keeper",
    "food":"Grass",
    "donated_by": "pvr society",
    "description":"Orangutans are great apes native to the rainforests of Indonesia and Malaysia. They are now found only in parts of Borneo and Sumatra,"
    " but during the Pleistocene they ranged throughout Southeast Asia and South China.",
    "place":"India,Russia",
    "donate":"True",
}
def display_zebra(request):
    return render (request,"animal.html",context=zebra)
leopard={
    "title":"Indian Leopard",
    "image":"https://cdn.britannica.com/79/244079-050-859BCF33/Leopard-Panthera-pardus.jpg",
    "age":"10",
    "care_taker":"zoo keeper",
    "food":"Meat",
    "donated_by": "snv society",
    "description":"The leopard is one of the five extant cat species in the genus Panthera."
    " It has a pale yellowish to dark golden fur with dark spots grouped in rosettes",
    "place":"India,Malaysia",
    "donate":"True",
}
def display_leopard(request):
    return render (request,"animal.html",context=leopard)
def animal_data(request):
    animals=[
        {
    "title":"Bengal Tiger",
    "image":"https://transforms.stlzoo.org/production/animals/amur-tiger-01-01.jpg?w=1200&h=1200&auto=compress%2Cformat&fit=crop&dm=1658935145&s=95d03aceddd44dc8271beed46eae30bc",
    "age":"20",
    "care_taker":"Zoo keeper",
    "food":"Meat",
    "donated_by": "Srilalitha",
    "description":"The Bengal tiger, also known as the Royal Bengal Tiger,"
    " is a subspecies of tiger with a brownish-orange coat marked by dark brown to black stripes,"
    " though white and golden variants exist.",
    "place":"India,Bangladesh"
},
{
    "title":"Asiatic Lion",
    "image":"https://cdn.britannica.com/29/150929-050-547070A1/lion-Kenya-Masai-Mara-National-Reserve.jpg",
    "age":"20",
    "care_taker":"Zoo keeper",
    "food":"Meat",
    "donated_by": "Larry",
    "description":"A lion is a large, muscular big cat with a short, yellow-gold coat and powerful build, "
    "distinguished by the shaggy mane of the adult male",
    "place":"India,South Africa,Kenya"
    "donate:False"
},
{
    "title":"Orangutan",
    "image":"https://media.istockphoto.com/id/899748046/photo/orangutans.jpg?s=612x612&w=0&k=20&c=C97XcWZoGVWGfzCaZCdq3eSuGYNiwLq62si9-pqcFpk=",
    "age":"10",
    "care_taker":"Zoo keeper",
    "food":"Bananas",
    "donated_by": "SRM society",
    "description":"Orangutans are great apes native to the rainforests of Indonesia and Malaysia. They are now found only in parts of Borneo and Sumatra,"
    " but during the Pleistocene they ranged throughout Southeast Asia and South China.",
    "place":"Siberia,South-east asia",
    "donate":"True",
},
{
    "title":"Zebra",
    "image":"https://www.worldlandtrust.org/wp-content/uploads/2024/04/Plains-Zebra-body.jpg",
    "age":"10",
    "care_taker":"zoo keeper",
    "food":"Grass",
    "donated_by": "pvr society",
    "description":"Orangutans are great apes native to the rainforests of Indonesia and Malaysia. They are now found only in parts of Borneo and Sumatra,"
    " but during the Pleistocene they ranged throughout Southeast Asia and South China.",
    "place":"India,Russia",
    "donate":"True",
},
{
    "title":"Indian Leopard",
    "image":"https://cdn.britannica.com/79/244079-050-859BCF33/Leopard-Panthera-pardus.jpg",
    "age":"10",
    "care_taker":"zoo keeper",
    "food":"Meat",
    "donated_by": "snv society",
    "description":"The leopard is one of the five extant cat species in the genus Panthera."
    " It has a pale yellowish to dark golden fur with dark spots grouped in rosettes",
    "place":"India,Malaysia",
    "donate":"True",
},
{
    "title":"White tailed deer",
    "image":"https://content.osgnetworks.tv/bowhunter/content/photos/whitetail-buck-standing-on-powerline.jpg",
    "age":"8",
    "care_taker":"zoo keeper",
    "food":"Grass",
    "donated_by": "J K society",
    "description":"The white-tailed deer (Odocoileus virginianus), also known commonly as the whitetail and the Virginia deer, is a medium-sized species of deer native to North, Central and South America. "
    "It is the most widely distributed mainland ungulate herbivore in the Americas;",
    "donate":"True",
},
{
    "title":"Peacock",
    "image":"https://content.osgnetworks.tv/bowhunter/content/photos/whitetail-buck-standing-on-powerline.jpg",
    "age":"8",
    "care_taker":"zoo keeper",
    "food":"Grains",
    "donated_by": "J K society",
    "description":"The white-tailed deer (Odocoileus virginianus), also known commonly as the whitetail and the Virginia deer, is a medium-sized species of deer native to North, Central and South America. "
    "It is the most widely distributed mainland ungulate herbivore in the Americas;",
    "donate":"True",

},{
    "title":"Elephant",
    "image":"https://content.osgnetworks.tv/bowhunter/content/photos/whitetail-buck-standing-on-powerline.jpg",
    "age":"20",
    "care_taker":"zoo keeper",
    "food":"Grass",
    "donated_by": "P K society",
    "description":"The white-tailed deer (Odocoileus virginianus), also known commonly as the whitetail and the Virginia deer, is a medium-sized species of deer native to North, Central and South America. "
    "It is the most widely distributed mainland ungulate herbivore in the Americas;",
    "donate":"True",
},{
    "title":"Giraffe",
    "image":"https://content.osgnetworks.tv/bowhunter/content/photos/whitetail-buck-standing-on-powerline.jpg",
    "age":"17",
    "care_taker":"zoo keeper",
    "food":"Grass",
    "donated_by": "L K society",
    "description":"The white-tailed deer (Odocoileus virginianus), also known commonly as the whitetail and the Virginia deer, is a medium-sized species of deer native to North, Central and South America. "
    "It is the most widely distributed mainland ungulate herbivore in the Americas;",
    "donate":"True",
},{
    "title":"Monkey",
    "image":"https://content.osgnetworks.tv/bowhunter/content/photos/whitetail-buck-standing-on-powerline.jpg",
    "age":"12",
    "care_taker":"zoo keeper",
    "food":"Banana",
    "donated_by": "V K society",
    "description":"The white-tailed deer (Odocoileus virginianus), also known commonly as the whitetail and the Virginia deer, is a medium-sized species of deer native to North, Central and South America. "
    "It is the most widely distributed mainland ungulate herbivore in the Americas;",
    "donate":"True",
},
   ]
    return JsonResponse({'status':200,'data':animals})
def zoo_data(request):
    zoos = [
        {"name": "Mysore Zoo", "location": "India"},
        {"name": "Singapore Zoo", "location": "Singapore"},
        {"name": "London Zoo", "location": "UK"},
        {"name": "Berlin Zoo", "location": "Germany"},
        {"name": "San Diego Zoo", "location": "USA"},
        {"name": "Toronto Zoo", "location": "Canada"},
        {"name": "Beijing Zoo", "location": "China"},
        {"name": "Tokyo Zoo", "location": "Japan"},
        {"name": "Nairobi Zoo", "location": "Kenya"},
        {"name": "Sydney Zoo", "location": "Australia"},
    ]
    return JsonResponse({'status': 200, 'data': zoos})
   
def login(request):
    email_value=request.GET.get('email')
    password_value=request.GET.get('password')
    print(email_value)
    print(password_value)
    if email_value=="admin@gmail.com" and password_value=="admin@123":
       return JsonResponse({'message':'Login suscessful'})
    else:
     return JsonResponse({'message':'Invalid credentials'})

def book_ticket(request):
    name = request.GET.get('name')
    persons = request.GET.get('number_of_persons')
    email = request.GET.get('email')

    if not name or not persons or not email:
        return JsonResponse({'error': 'Missing one or more fields'})

  
    booking = {
        'name': name,
        'number_of_persons': persons,
        'email': email
    }

    bookings.append(booking)

    return JsonResponse({
        'status': 200,
        'message': 'Ticket booked successfully and added to array',
        'total_bookings': len(booking),
        'bookings': bookings
    })

  