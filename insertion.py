#Gallardo Valdez Jose Jhovan
#06/09/2016
#Insertion sort

#method that sorts a list using insertion sort
def inserctionSort(lista):
	for i in range(1,len(lista)):
		valor=lista[i]
		j = i
		while j>0 and lista[j-1]>valor:
			lista[j]=lista[j-1]
			j=j-1
		lista[j]=valor


#ask the user to give numbers and then sort them
#the program stops when the the user write a "-1"
lista=[]
x=input("Write numbers:")
while(x!=-1):
	lista.append(x)
	x=input("Write a number:")

print lista
inserctionSort(lista)
print lista