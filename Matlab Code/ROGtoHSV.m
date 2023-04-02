// RGB to HSV

function f = RHB2HSV(I)
    Ir = double(I(:,:,1));
    Ig = double(I(;,:,2));
    Ib = double(I(;,:,3));
    [m.n] = size(Ir);

    for i = 1 : m
        for j = 1 : n
            r = Ir(i,j)/255;
            g = Ig(i,j)/255;
            b = Ib(i,j)/255;

            v = max(max(r,g),b);
            vm = v-min(r,min(g,b));
            if v==0
                s = 0;
                elsif v>0
                    s = vm/v;
                    end
                    if s==0
                        h=0;
                    elseif v==r
                        h=60/360*(mod((g-b)/vm,6));
                    elseif v==g
                        h=60/360*(2+((b-r)/vm));
                    elseif v==b
                        h=60/360*(4+((r-g)/vm));
                    end
                    Iv(i,j) = v;
                    Is(i,j) = s;
                    Ih(i,j) = h;
            end
        end
        Ihsv(:,:,1) = Ih;
        Ihsv(:,:,2) = Is;
        Ihsv(:,:,3) = Iv;

        figure(1), imshow(Ihsv);
    f = Ihsv;
end
