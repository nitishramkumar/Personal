function [ret,stdev,shpRat] = CalculateMomentumReturns(Complete_Returns,holdingPeriod,rankingPeriod)
    
    totalMonths = size(Complete_Returns,1);
    totalAssets = size(Complete_Returns,2);
    
    rolling_returns = zeros(totalMonths-holdingPeriod-rankingPeriod,1);
    Com_returns_mat = fts2mat(Complete_Returns);
    
    for count = 1+rankingPeriod : totalMonths-holdingPeriod
        
        %Get all data corresponding to the ranking period.
        %Find the average for every asset
        ranking_returns = Complete_Returns(count-rankingPeriod:count-1);
        ranking_ftsMat = fts2mat(ranking_returns);
        ranking_avg = mean(ranking_ftsMat,1);
        
        %Isolate the top and bottom quintile returns
        ranking_sort = sort(ranking_avg);
        longassets = ranking_sort(floor(4*totalAssets/5):end);
        shortassets = ranking_sort(1:floor(totalAssets/5));
        
        %Identify the assets for the quintile data
        %and find future returns based on holding period
        longassetsPos = find(ismember(ranking_avg,longassets));
        shortassetsPos = find(ismember(ranking_avg,shortassets));
        
        longAssetRet_holding = Com_returns_mat(count+1:count+holdingPeriod,longassetsPos);
        shortAssetRet_holding = Com_returns_mat(count+1:count+holdingPeriod,shortassetsPos);
        
        %Average the returns over the holding period
        %Perform sum(long_avg) - sum(short_Avg)
        rolling_returns(count-rankingPeriod) = sum(mean(longAssetRet_holding,1)) - sum(mean(shortAssetRet_holding,1));
       
    end
    ret = mean(rolling_returns);
    stdev = std(rolling_returns);
    shpRat = ret/stdev;
end

