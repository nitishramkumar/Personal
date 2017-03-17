%Function to build financial time series
%Input - raw data from excel, Output - time series collection
function timeSeriesCol = BuildTimeSeries(raw)
    timeSeriesCol = fints();
    col = 1;
    while col<=size(raw,2)
        %data available only every 3 columns
        if mod(col,3) == 1
            %first value is name of asset
            comName = raw(1,col);
            comName = string(strrep(comName,'''',''));

            %first column has the date
            comDate = string(raw(3:end,col));
            comDate = strrep(rmmissing(comDate),'''','');
            comDate = datetime(comDate);

            col = col + 1;
            %second column has the data
            comPrice = str2double(string(raw(3:size(comDate,1)+2,col)));

            %create new time series with assetName as time series name
            %timeSeriesCol(floor(col/3)+1) = timeseries(comPrice,datestr(comDate),'Name',comName);
            newTs = fints(cellstr(comDate),comPrice,char(regexprep(comName,'[^\w'']','')));
            
            %Merge into collection
            timeSeriesCol = merge(timeSeriesCol,newTs);
            col = col + 1;

        elseif mod(col,3) == 0
            col = col + 1;
            continue;
        end
    end
end

