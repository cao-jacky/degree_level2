%% Initial imports and definitions
% Import data from text files
h_data = importdata('saved_data/h_list_1.txt')

% Defining initial constants for the Fourier Transformed function
lmda = 700 * 10^(-9) % Wavelength of laser in m
fl = 0.51 % Focal length of lens used in m
d = 0.001745 % Distance between circular apertures in m
D = 0.000485 % Averaged diameter of the size of one circular aperture in m

% Defining x and y for our images
%x = linspace(0,1279,200)
%y = linspace(0,1023,200)

x = 0:10:1279
y = 0:10:1279

%% Plotting horizontal data into MATLAB's graphing function
h_domain = 0:1:1279;    % Defined domain as from 0 to 1279 in steps of 1

%figure(1)               % Figure value of 1 for the horizontal data
plot(h_domain,h_data,'LineWidth',1)   % Plotting the imported horizontla data

%% Ploting Bessel function
% Define the domain for the theoretical function
%theo_domain = sqrt(x.^2 + y.^2)
theo_domain = sqrt(linspace(0,1279,100).^2 + linspace(0,1023,100).^2)

u = 1/(lmda*fl) % Spatial frequency, u
v = 1/(lmda*fl) % Spatial freqneucy, v

%u = 1
%v = 1

omega = sqrt((u*x).^2+(v*y).^2)

% Calculating the Fourier Transformed function
%f = 1/10 * (2 .* (besselj(0,theo_domain-690) .* cos(pi*theo_domain))/1.*theo_domain).^2
%bsl = besselj(0,(pi.*sqrt((u.*x).^2+(v.*y).^2)*D))
%f = ((2 * cos(pi*u.*x*d).*bsl.*(pi*D^2))./(4.*pi.*D)).^2

f = 40000 * (besselj(0,(theo_domain-690)/0.89) .* cos(pi*theo_domain)).^2 + 10

%figure(2)               % Figure value of 2 for the theoretical data
hold on
plot(theo_domain,f,'LineWidth',1.5)
xlim([0 1280])           % Setting axis limits
ylim([0 255])
hold off
%axis([0 20 -.5 1])
grid off
legend('Horizontal Intensity','Theoretical Model','Location','Best')
%title('Bessel Functions of the First Kind for v = 0')
xlabel('Distance (px)')
ylabel('Intensity')
