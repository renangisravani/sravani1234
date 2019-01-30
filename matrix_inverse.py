l=input("enter no.of rows for matrix:");
m=input("enter no.of coloums for matrix:");
a=[];
print("enter elements for matrix a");
for i in range (0,l):
	a.append([]);
for i in range (0,l):
	for j in range (0,m):
		a[i].append(j);
		a[i][j]=0;
for i in range (0,l):
	for j in range (0,m):
		a[i][j]=input();
print(a);
print(a**-1);
