from random import randint as r
from random import choice as c
def warnews(p,q):
	headlines = ["scramble for","battle of","invasion of","meatgrinder in"]
	for i in range(len(headlines)):
		headlines[i] = headlines[i] + " " + c([p.name,q.name])
	
	return c(headlines)
def prob(lists):
	total = 0
	for k in lists:
		total+=k.mil
	x = r(0,int(total))
	for i in lists:
		x-=i.mil
		if x<=0:
			return i
year = 1914
month = 7
system = ["democratic revolt","communist revolution","military coup"]
def civ(supp,count):
	if supp<=10:
		count.pop*=(r(33,66)/100)
		count.tech-=5
		count.sup=80
		count.mil*=(r(30,70)/100)
		count.con-=r(30,60)
		count.rev=0
		print(count.name,"got embroiled in a civil war!")
	return count
def recruit(count):
	x = int(count.pop*(count.sup-count.rev)*count.con/10000)
	count.mil+=x
	count.pop-=(x/1000)
	count.tech+=int(r(0,4)/4)
	count.sup+=2
	count.sup-=int(count.mil/1000)
	return count
class country:
	def __init__(self,name,pop,tech,sup,mil,rev):
		self.name = name
		self.pop = pop
		self.tech = tech
		self.sup = sup
		self.mil = mil
		self.con = 100
		self.rev = rev
		self.cas = 0
		self.res = "d"
lis = [country("Russia",150,20,50,1500,0),country("England",300,30,40,750,10),country("France",250,30,40,1000,5),country("Germany",70,30,65,1000,0),country("Austria",50,25,45,700,5),country("Italy",40,25,50,500,0),country("Ottoman",80,20,45,800,10),country("USA",150,35,55,500,5),country("Belgium",60,25,50,300,10),country("Nether",50,25,55,300,5),country("Qing",200,15,35,1500,5),country("Japan",40,20,80,500,0),country("Spain",70,30,50,500,5),country("Portug",80,25,40,500,5)]
ally = []
axis = []
neutral = []
for i in lis:
	pro = r(1,8)
	if pro in [1,2]:
		ally.append(i)
		print(i.name,"in allies")
	elif pro in [3,4]:
		axis.append(i)
		print(i.name,"in axis")
	else:
		neutral.append(i)
print("\n"*5)

def jwar():
	jw = r(1,20-int((1.5*len(neutral))))
	try:
		if jw == 1:
			j = neutral.pop()
			ally.append(j)
			print(j.name,"joined the war on allied side!")
		elif jw == 2:
			j = neutral.pop()
			axis.append(j)
			print(j.name,"joined the war on axis side!")
	except:
		pass

while True:
	Dat = str(month)+"/"+str(year)
	cons = input("Date : "+Dat+" -:")
	if cons == "s" or cons == "stat":
		print("Allies")
		print("name\tpop\ttech\tsup\tmil\tcasual\tcontrol")
		alte = 0
		alpo = 0
		almil = 0
		alca = 0
		alco = 0
		axte = 0
		axpo = 0
		axmil = 0
		axca = 0
		axco = 0
		for q in ally:
			print(q.name,int(q.pop)*1000,q.tech,q.sup,int(q.mil),int(q.cas),q.con,sep="\t")
			alte+=q.tech
			alpo+=q.pop
			almil+=q.mil
			alca+=q.cas
			alco+=q.con
		print("Total",int(alpo)*1000,alte//len(ally),"-",int(almil),int(alca),alco//len(ally),"\n",sep="\t")
		print("Axis")
		for q in axis:
			print(q.name,int(q.pop)*1000,q.tech,q.sup,int(q.mil),int(q.cas),q.con,sep="\t")
			axte+=q.tech
			axpo+=q.pop
			axmil+=q.mil
			axca+=q.cas
			axco+=q.con
		print("Total",int(axpo)*1000,axte//len(axis),"-",int(axmil),int(axca),axco//len(axis),"\n",sep="\t")
	if cons == "t" or cons == "turn":
		a = prob(ally)
		b = prob(axis)
		x = r(75,125)/100
		y = r(75,125)/100
		if a.mil*a.tech*a.sup*x>=b.mil*b.tech*b.sup*y*1.1:
			terc = r(2,15)
			a.cas+=b.tech*b.sup*y*0.08
			a.mil-=b.tech*b.sup*y*0.08
			b.cas+=a.tech*a.sup*x*0.1
			b.mil-=a.tech*a.sup*x*0.1
			a.sup-=4
			a.con+=terc
			a.rev+=0.5
			b.sup-=8
			b.rev+=1
			b.con-=terc
			a.res = "w"
			b.res = "l"
		elif a.mil*a.tech*a.sup*x*1.1<=b.mil*b.tech*b.sup*y:
			terc = r(2,15)
			a.cas+=b.tech*b.sup*y*0.1
			a.mil-=b.tech*b.sup*y*0.1
			b.cas+=a.tech*a.sup*x*0.08
			b.mil-=a.tech*a.sup*x*0.08
			b.sup-=4
			b.con+=terc
			b.rev+=0.5
			a.sup-=8
			a.rev+=1
			a.con-=terc
			a.res = "w"
			b.res = "l"
		else:
			a.cas+=b.tech*b.sup*0.09
			a.mil-=b.tech*b.sup*0.09
			b.cas+=a.tech*a.sup*0.09
			b.mil-=a.tech*a.sup*0.09
			b.sup-=6
			a.sup-=6
			a.rev+=0.5
			b.rev+=0.5
			a.res = "d"
			b.res = "d"
		if a.mil<=0 or a.con<=0:
				ally.remove(a)
				print(a.name,"capitulated")
				b.sup+=10
				b.con+=a.con
				b.tech+=5
		if b.mil<=0 or b.con<=0:
				axis.remove(b)
				print(b.name,"capitulated")
				a.sup+=10
				a.con+=b.con
				a.tech+=5
		a = civ(a.sup,a)
		b = civ(b.sup,b)
		for l in range(len(ally)):
			ally[l] = recruit(ally[l])
		for m in range(len(axis)):
			axis[m] = recruit(axis[m])
		month+=1
		if month==12:
			year+=1
			month=0
		if a.rev>=a.sup:
			ally.remove(a)
			print(c(system),"took place in",a.name)
		if b.rev>=b.sup:
			axis.remove(b)
			print(c(system),"took place in",b.name)
		if ally == []:
			print("Axis won WW1")
			break
		if axis == []:
			print("Ally won WW1")
			break
		jwar()
	if cons == "n" or cons == "news":
		print(warnews(a,b))
