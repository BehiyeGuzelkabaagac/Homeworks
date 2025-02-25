#Görev1

x = 8
y = 3.2
z = 8j + 18
a = "Hello World"
b = True
c = 23< 22
l = [1, 2, 3, 4]
d = {"Name": "Jake",
     "Age": 27,
     "Adress": "Downtown"}
t = ( "Machine Learning", "Data Science" )
s = {"Python", "Machine Learning", "Data Science"}
print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))
print(type(c))
print(type(l))
print(type(d))
print(type(t))
print(type(s))

#Görev2
text = "The goal is to turn data into information,and information into insight."
text = text.upper().replace(","," ").replace("."," ").split()
print(text)

#Görev3
lst = ["D", "A", "T" , "A", "S", "C" ,"I", "E", "N","C" ,"E"]
#adim1
print(len(lst))
#adim2
print(lst[0],lst[10])
#adim3
newlist = lst[0:4]
print(newlist)
#adim4
lst.pop(8)
#adim5
lst.append("Z")

#adim6
lst.insert(8,"N")
print(lst)

#Görev4

dict = {'Christian': ["America",18],
        'Daisy': ["England",12],
        'Antonio': ["Spain",22],
        'Dante': ["Italy",25]}
#adim1
print(dict.keys())
#adim2
print(dict.values())
#adim3
dict["Daisy"] = ["England",13]
print(dict)
#adim4
dict.update({"Ahmet": ["Türkey", 24]})
print(dict)
#adim5
del dict["Antonio"]

#Görev5
l = [2,13,18,93,22]

def func(l):
    even = list(filter(lambda x: x % 2 ==0, l))
    odd = list(filter(lambda x: x % 2 == 1, l))
    return even, odd 
even_list, odd_list=func(l)
print(even_list, odd_list)

#Görev6
#hocaya sor!

#Görev7
ders_kodu = ["CMP1005", "PSY1001", "HUK1005" , "SEN2204" ]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]
for a,b,c in zip(ders_kodu, kredi, kontenjan):
    print("Kredisi",b ,"olan", a,"kodlu dersin kontenjani",c, "kisiliktir.")


#Görev8
kume1 = set(["data", "python"] )
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

a = kume1.issuperset(kume2)
print(a)
b = kume2.symmetric_difference(kume1)
print(b)




