function f = RGB2YUV(I)
    Ir = I(:,:,1);
    Ig = I(:,:,2);
    [m,n] = size(Ir);

    k = [0.299 0.587 0.114; -0.147 -0.289 0.436; 0.615 -0.515 -0.100];

    for i = 1 : m
        for j = 1 : n
            rgb = [Ir(i,j);Ig(i,j);Ib(i,j)];
            yuv = k*double(rgb);
            Iy(i,j) = yuv(1,:);
            Iu(i,j) = yuv(2,:);
            Iv(i,j) = yuv(3,:);
        end
    end

    IYuv(:,:,1) = Iy;
    IYuv(:,:,2) = Iu;
    IYuv(:,:,3) = Iv;

    figure(1), imshow(IYuv);

    f = IYuv;

end