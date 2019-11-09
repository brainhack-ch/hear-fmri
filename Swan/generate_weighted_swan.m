clear all
close all
clc

load /Users/raphaelliegeois/Dropbox/Brainhack_Nov2019/Data/Rest/Run1/Rest1LR_Sub100307_Glasser.mat
load /Users/raphaelliegeois/Dropbox/Brainhack_Nov2019/Data/match_Yeo.mat
load /Users/raphaelliegeois/Dropbox/Brainhack_Nov2019/Data/ind_fear.mat

TCS = TCS(:,1:156); %to better hear modulation

channels = {'Trombone','String','Oboe','Horn','Harp','Flute','Contrebasse','Clarinet'};
nets = {'VA','DA','DMN','FP','VIS','SM','SM','LIM'};

%Find max length
m = 0;
for i = 1:8
    r1 = audioinfo([ channels{i} '.wav']);
    m = max(r1.TotalSamples,m);
end

s = zeros(m,2);
figure()
hold on
for i = 1:8
    r2 = audioread([channels{i} '.wav']);
    TC_net = mean(TCS(eval(['ind_' nets{i}]),:));
    TC_net = TC_net - min(TC_net);
    TC_net = TC_net ./ max(TC_net);
    TC_net(TC_net<0.5) = 0;
    plot(TC_net)
    w = imresize(TC_net,[1 size(r2,1)]);
    r2(:,1) = r2(:,1).* w';
    r2(:,2) = r2(:,2).* w';
    s(1:size(r2,1),:) = s(1:size(r2,1),:)+r2;
end

audiowrite('Rest_modulated.wav',s,r1.SampleRate);

audiowrite('Rest_modulated_excerpt.wav',s([round(0.5*size(s,1)):round(0.7*size(s,1))],:),r1.SampleRate);

