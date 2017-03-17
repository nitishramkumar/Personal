function [cleaned] = RemoveQuotes(value)
    cleaned = strrep(value,'''','')
end

