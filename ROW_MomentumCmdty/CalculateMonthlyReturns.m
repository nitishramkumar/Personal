function [timeSeriesCol,timeSeriesCol_Ret]  = CalculateMonthlyReturns(rawData)
    %Build time series using provided data
    timeSeriesCol = BuildTimeSeries(rawData);
    
    %diff of the logs are the returns 
    timeSeriesCol_Ret = diff(log(timeSeriesCol));
    
    %convert to monthly data
    timeSeriesCol_Ret = tomonthly(timeSeriesCol_Ret,'CalcMethod','CumSum');
end

