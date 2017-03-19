%% Import data from text files
h_data = importdata('saved_data/h_list_1.txt')

% Defining initial constants for the Fourier Transformed function
lmda = 700 * 10^(-9) % Wavelength of laser in m
fl = 0.51 % Focal length of lens used in m
d = 0.001745 % Distance between circular apertures in m
D = 0.000485 % Averaged diameter of the size of one circular aperture in m

%% Plotting horizontal data into MATLAB's graphing function
h_domain = 0:1:1279;    % Defined domain as from 0 to 1279 in steps of 1

%figure(1)               % Figure value of 1 for the horizontal data
%plot(h_domain,h_data,'LineWidth',1)   % Plotting the imported horizontla data


%% Single circle aperture
n = 51 ; % size of matrix, odd
R = 0.000485/2 ; % radius
R = 19
n2 = floor(n/2) ;
[x,y] = meshgrid(-n2:n2) ;
circ = sqrt(x.^2 + y.^2) < R ;

circ = double(circ) ; % convert from logical to double
%imshow(M)

ft_circ = fft(circ)
imshow(ft_circ)

%plot(x,ft_circ)

%% Plot Bessel function - need to adapt this for my own image analyser
% Defining the domain for the theoretical function
theo_domain = sqrt(linspace(0,1279,100).^2 + linspace(0,1023,100).^2)


u = 1/(lmda*fl)
v = 1/(lmda*fl)

size(theo_domain)

% Calculating the Fourier Transformed function
%f = (besselj(0,theo_domain-690) * cos(pi) * 190).^2
bsl = besselj(0,(pi*sqrt((u*x).^2+(v*y).^2)*D))
f = ((2 * cos(pi*u*x*d).*bsl*(pi*D^2))/(4*pi*D)).^2

%figure(2)               % Figure value of 2 for the theoretical data
hold on
plot(x,f,'LineWidth',1)
%xlim([0 1280])           % Setting axis limits
%ylim([0 255])
hold off
%axis([0 20 -.5 1])
grid off
legend('Horizontal Intensity','Theoretical Model','Location','Best')
%title('Bessel Functions of the First Kind for v = 0')
xlabel('Distance (px)')
ylabel('Intensity')
