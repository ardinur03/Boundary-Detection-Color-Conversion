function f = RGB2NTSC(I)
    Ir = I(:,:,1);
    Ig = I(:,:,2);
    Ib = I(:,:,3);
    [m,n] = size(Ir);

    k = [0.299 0.587 0.114; -0.516 -0.274 0.322; 0.211 -0.523 -0.312];

    for i = 1 : m
        for j = 1 : n
            rgb = [Ir(i,j);Ig(i,j);Ib(i,j)];
            ycbcr = k*double(rgb);
            Iy(i,j) = double(yiq(1,:) /255);
            Icb(i,j) = double(yiq(2,:) /255);
            Icr(i,j) = double(yiq(3,:) /255);
        end
    end

    IYiq(:,:,1) = Iy;
    IYiq(:,:,2) = Icb;
    IYiq(:,:,3) = Icr;

    figure(1), imshow(IYiq);
    f = IYiq;

end
