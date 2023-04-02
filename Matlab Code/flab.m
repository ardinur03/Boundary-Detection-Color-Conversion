function x = flab(q)
    qn = double(q);
    if qn > 0.008856
        x = nthroot(qn,3);
    else
        x = 7.787*qn + 16/116;
    end
end