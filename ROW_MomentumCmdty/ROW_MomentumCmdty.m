%% Momentum strategy for commodities
filename = 'ROW_Data_2.xlsx';
overridedata = 0;

%Get the agriculture and other data
%Override data only if necessary
if overridedata == 1
    sheetname = 'Agriculture2';
    [~,~,raw_Agri] = xlsread(filename,sheetname);
    
    sheetname = 'Others';
    [~,~,raw_Others] = xlsread(filename,sheetname);
    
    sheetname = 'COMBATS6';
    [~,~,raw_combats] = xlsread(filename,sheetname);
end

recalculate = 0;
if recalculate == 1
    % Calculate monthly returns for both dataset
    % For this Build time series of settlement price, 
    % then get returns by diff of log
    [settlmtPrc_Agri,timeSeriesCol_Agri] = CalculateMonthlyReturns(raw_Agri);
    [settlmtPrc_Oth, timeSeriesCol_Other] = CalculateMonthlyReturns(raw_Others);
    [prc_combats, timeSeries_combats] = CalculateMonthlyReturns(raw_combats);
end 

figure(1)
subplot(2,1,1)
plot(settlmtPrc_Agri)
title('Agriculture Prices')
legend('location','west')
ylabel('prices')
xlabel('time')
subplot(2,1,2)
plot(timeSeriesCol_Agri)
title('Agriculture Monthly Returns')
legend('location','west')
ylabel('returns')
xlabel('time')

figure(2)
subplot(2,1,1)
plot(settlmtPrc_Oth)
title('Other Cmdty Prices')
legend('location','west')
ylabel('prices')
xlabel('time')
subplot(2,1,2)
plot(timeSeriesCol_Other)
title('Other Cmdty Monthly Returns')
legend('location','west')
ylabel('returns')
xlabel('time')

figure(3)
subplot(2,1,1)
plot(prc_combats)
title('comBATS 6 Prices')
legend('location','west')
ylabel('prices')
xlabel('time')
subplot(2,1,2)
plot(timeSeries_combats)
title('comBATS 6 Returns')
legend('location','southwest')
ylabel('returns')
xlabel('time')


holdingPeriods = [1 6 12 24 36];
rankingPeriods = [1 3 6];

returnResults = zeros(length(rankingPeriods),length(holdingPeriods));
sdResults = zeros(length(rankingPeriods),length(holdingPeriods));
sharpRatResults = zeros(length(rankingPeriods),length(holdingPeriods));


for rp = 1:length(rankingPeriods)
    for hp = 1:length(holdingPeriods)
        [ret,stdev,sharpRat] = CalculateMomentumReturns(merge(timeSeriesCol_Agri,timeSeriesCol_Other),holdingPeriods(hp),rankingPeriods(rp));
        returnResults(rp,hp) = ret;
        sdResults(rp,hp) = stdev;
        sharpRatResults(rp,hp) = sharpRat;
    end
end 

returnResults
sdResults
sharpRatResults



