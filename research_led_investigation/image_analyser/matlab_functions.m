%% Import data from text files
h_data = importdata('saved_data/h_list_1.txt')

%% Plotting horizontal data into MATLAB's graphing function
h_domain = 0:1:1279;    % Defined domain as from 0 to 1279 in steps of 1
figure(1)               % Figure value of 1 for the horizontal data
plot(h_domain,h_data)   % Plotting the imported horizontla data


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
grid off
legend('J_0','Location','Best')
title('Bessel Functions of the First Kind for v = 0')
xlabel('X')
ylabel('J_v(X)')
