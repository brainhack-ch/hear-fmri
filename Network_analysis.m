clear all 
clc 

%% Load data
%load('Rest/Run1/Rest1LR_Sub100307_Glasser.mat');
load('Emotion/TaskEm_Sub100307_Glasser.mat');
load('Emotion/Paradigm_Emotion.mat');
number = 100307;
Emotion.convolved(1:35)=0;
Emotion.convolved(65:95)=0;
Emotion.convolved(125:150)=0;

load('match_Yeo.mat');
load('ind_fear.mat');
 %% Z-score (normalizing the data

Z_TCS = zscore(TCS.');
Z_TCS = Z_TCS.';

%% Method 2: confidence intervals 

% Separate regions by network
TCS_Visual = Z_TCS(ind_full == 1, :);
TCS_Motor = Z_TCS(ind_full == 2, :);
TCS_Dorsal = Z_TCS(ind_full == 3, :);
TCS_Ventral = Z_TCS(ind_full == 4, :);
TCS_Limbic = Z_TCS(ind_full == 5, :);
TCS_Fronto = Z_TCS(ind_full == 6, :);
TCS_Default = Z_TCS(ind_full == 7, :);
TCS_Fear = Z_TCS(ind_fear, :);

upper_threshold = 80;
lower_threshold = 100-upper_threshold;

% Determine the percentile values for each network
threshold_visual =  prctile(TCS_Visual, [lower_threshold upper_threshold],'all');
threshold_motor = prctile(TCS_Motor, [lower_threshold upper_threshold],'all');
threshold_dorsal = prctile(TCS_Dorsal, [lower_threshold upper_threshold],'all');
threshold_ventral = prctile(TCS_Ventral, [lower_threshold upper_threshold],'all');
threshold_limbic = prctile(TCS_Limbic, [lower_threshold upper_threshold],'all');
threshold_fronto = prctile(TCS_Fronto, [lower_threshold upper_threshold],'all');
threshold_default = prctile(TCS_Default, [lower_threshold upper_threshold],'all');
threshold_fear = prctile(TCS_Fear, [lower_threshold upper_threshold], 'all');

% Matrices to iterate in loop
loop_threshold = [threshold_visual; threshold_motor; threshold_dorsal; threshold_ventral; ...
               threshold_limbic; threshold_fronto; threshold_default; threshold_fear];
loop_TCS = [TCS_Visual; TCS_Motor; TCS_Dorsal; TCS_Ventral; TCS_Limbic; TCS_Fronto; ...
            TCS_Default; TCS_Fear];
loop_colour = ['r'; 'b'; 'k'; 'm'; 'c'; 'g'; 'y'; 'r'];   
loop_index_start = [1; 59; 112; 158; 207; 235; 283; 361; 379];


% Assign 1 or -1 values based on activation or deactivation of networks
output_fear = [];
for i= 1:size(loop_colour,1)

   mean_pos = mean(loop_TCS(loop_index_start(i):loop_index_start(i+1)-1,:)) > loop_threshold(2*i);
   mean_neg = mean(loop_TCS(loop_index_start(i):loop_index_start(i+1)-1,:)) < loop_threshold(2*i-1);
   mean_network = mean_pos - mean_neg;
   output_fear = [output_fear; mean_network];
end
output_fear = [output_fear; Emotion.convolved];




% Plot results
time = (1:100:size(TCS,2))*0.72;
figure('DefaultAxesFontSize', 18)
imagesc(output_fear);
title(['The Activity of Each Network ' , int2str(number)], 'FontSize', 20);
ylabel('The Different Networks')
xlabel('Time(s)')

ay = gca;
ay.YTick = [1 2 3 4 5 6 7 8 9];
ay.YTickLabel= {'Visual', 'Motor', 'Dorsal', 'Ventral', 'Limbic', 'Fronto', ...
            'Default', 'Fear', 'Paradigm'};
        
ax = gca;
ax.XTick = 1:100:size(TCS,2);
ax.XTickLabel = string(round(time));

% Create output
filename = ['output ' int2str(number)];
save(filename);




