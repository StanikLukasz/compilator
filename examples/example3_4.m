a = [[1,2,3],
     [4,5,6],
     [7,8,9]];

b = -a;

print b;

print a .+ b;

print eye(4);

print ones(4) .* 4;

c = [2,2,2];

print a * c;

x = 0;
y = zeros(5);
z = x + y;

x = eye(5);
y = eye(8);
z = x + y;

x = [ 1,2,3,4,5 ];
y = [ [1,2,3,4,5],
      [1,2,3,4,5] ];
z = x + y;

x = zeros(5);
y = zeros(5,7);
z = x + y;

x = ones(3,5);
z = x[7,10];
v = x[2,3,4];
