print "====================";
print "Przypisywanie wartości, operacje arytmetyczne, wypisywanie na ekran";
print "--------------------";
x = 10;
y = 20;

print "x, y=", x, y;
print "x+y=", x+y;
print "x-y=", x-y;
print "x*y=", x*y;
print "x/y= (dzielenie całkowitoliczbowe)", x/y;

x = 10.;
print "x, y=", x, y;
print "x/y= (dzielenie rzeczywiste)", x/y;

x += y;
print "x += y", x;

x -= y;
print "x -= y", x;

x *= y;
print "x *= y", x;

x /= y;
print "x /= y", x;



print "====================";
print "Tworzenie macierzy";
print "--------------------";
a = [[1,2,3],
     [4,5,6],
     [7,8,9]];
print a;

print "====================";
print "Dodawanie macierzy";
print "--------------------";
b = [[3,2,1],
     [6,5,4],
     [9,8,7]];

print a .+ b;

print "====================";
print "Odejmowanie macierzy";
print "--------------------";

print a .- b;

print "====================";
print "Mnożenie macierzy przez skalar";
print "--------------------";
c = 3;
print a * c;

print "====================";
print "Tworzenie macierzy diagonalnej (4x4)";
print "--------------------";
print eye(4);

print "====================";
print "Tworzenie macierzy wypełnionej jedynkami (1x4)";
print "--------------------";
print ones(1,4);

print "====================";
print "Tworzenie macierzy wypełnionej zerami (4x4)";
print "--------------------";
print zeros(4);

print "====================";
print "Prezentacja działania funkcji if";
print "--------------------";
N = 10;
M = 20;

if(N==10)
    print "N==10";
else if(N!=10)
    print "N!=10";


if(N>5) {
    print "N>5";
}
else if(N>=0) {
    print "N>=0";
}

if(N<10) {
    print "N<10";
}
else if(N<=15)
    print "N<=15";

print "====================";
print "Prezentacja działania pętli while";
print "--------------------";
k = 10;
while(k>0)
    k = k - 1;
print "k= ", k;

print "====================";
print "Prezentacja działania polecenia break";
print "--------------------";
for i = 1:N {
    if(i<=N/2)
        print i;
    else if(i<=10){
        print "break";
        break;}
    else if(i<=N/4)
        continue;
}


print "====================";
print "<SAMPLE>";
print "--------------------";

