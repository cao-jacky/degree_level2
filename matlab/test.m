%% Testing of addition
x = 1
y = 2
z = x + y
disp(z)

%% Testing of pi
a1 = pi
disp(a1)

x1 = linspace(0,10*pi)
% y1 = [1,2,3,4,5,6,7,8,9,10]

% plot(x1,y1)

%% Plotting sine
plot(sin(x1))

%% Plotting cosine
plot(cos(x1))


%% Plot Bessel function - need to adapt this for my own image analyser
% Defining the domain
X = 0:0.1:20;

% Calculating the first five Bessel functions of the first kind.
J = zeros(5,201);
for i = 0
    J(i+1,:) = besselj(i,X);
end

plot(X,J,'LineWidth',1.5)
axis([0 20 -.5 1])
grid on
legend('J_0','Location','Best')
title('Bessel Functions of the First Kind for v = 0,1,2,3,4')
xlabel('X')
ylabel('J_v(X)')
