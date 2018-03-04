clc
x=[ 4.9    2.4     3.3     1.0     1   ];
%    x1     x2      x3      x4   class
n=input('masukan jumlah epoch: ');
fprintf('====epoch awal=======\n');
Q1=-0.5;
Q2=0.3;
Q3=0.8;
Q4=-0.8;
b =0.1;
a =0.1;
h=1:1:n;loss=1:1:n;
for count=1:1:n
    h=(Q1*x(1))+(Q2*x(2))+(Q3*x(3))+(Q4*x(4))+b;
    sigmoid = 1/(1+exp(-h));
    error=(x(5)-sigmoid);
    loss(count)=error^2;
    dQ1=2*(x(5)-sigmoid)*(1-sigmoid)*sigmoid*x(1);
    dQ2=2*(x(5)-sigmoid)*(1-sigmoid)*sigmoid*x(2);
    dQ3=2*(x(5)-sigmoid)*(1-sigmoid)*sigmoid*x(3);
    dQ4=2*(x(5)-sigmoid)*(1-sigmoid)*sigmoid*x(4);
    db =2*(x(5)-sigmoid)*(1-sigmoid)*sigmoid*b;
    Q1new= Q1+(a*dQ1);
    Q2new= Q2+(a*dQ2);
    Q3new= Q3+(a*dQ3);
    Q4new= Q4+(a*dQ4);
    bnew = b +(a*db);
    Q1=Q1new;Q2=Q2new;Q3=Q3new;Q4=Q4new;
end
disp(loss);
count=1:1:n;
plot(count,loss(count));
title('Loss Graph')
xlabel('Epoch') 
ylabel('Loss') 