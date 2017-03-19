%{ In this second attempt I am going to use the FFT function as part of the
MATLAB library as opposed to just attempting to implement the cosine and 'jinc'
bessel function
%}

%% Import data from text files
h_data = importdata('saved_data/h_list_1.txt')

%% Plotting horizontal data into MATLAB's graphing function
h_domain = 0:1:1279;    % Defined domain as from 0 to 1279 in steps of 1

%figure(1)               % Figure value of 1 for the horizontal data
%plot(h_domain,h_data,'LineWidth',1)   % Plotting the imported horizontla data



%% Plot Bessel function - need to adapt this for my own image analyser
% Defining the domain for the theoretical function
lmda = 700 * 10^(-9)
theo_domain = sqrt(linspace(0,1279,100).^2 + linspace(0,1023,100).^2)

size(theo_domain)

% Calculating the first five Bessel functions of the first kind.
J = (besselj(0,theo_domain-690) * cos(pi) * 190).^2

%figure(2)               % Figure value of 2 for the theoretical data
hold on
plot(theo_domain,J,'LineWidth',1)
xlim([0 1280])           % Setting axis limits
ylim([0 255])
hold off
%axis([0 20 -.5 1])
grid off
legend('Horizontal Intensity','Theoretical Model','Location','Best')
%title('Bessel Functions of the First Kind for v = 0')
xlabel('Distance (px)')
ylabel('Intensity')
