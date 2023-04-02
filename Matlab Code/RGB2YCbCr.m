function f = RGB2YCBCR(I)
    Ir = I(:,:,1);
    Ig = I(:,:,2);
    Ib = I(:,:,3);
    [m,n] = size(Ir);

    k = [0;128;128];
    T = [0.299 0.587 0.114; -0.168 -0.331 0.500; 0.500 -0.419 -0.081];

    for i = 1 : m
        for j = 1 : n
            rgb = [Ir(i,j);Ig(i,j);Ib(i,j)];
            ycbcr = k+1*double(rgb);
            Iy(i,j) = uint8(ycbcr(1,:));
            Icb(i,j) = uint8(ycbcr(2,:));
            Icr(i,j) = uint8(ycbcr(3,:));
        end
    end

    Iycbcr(:,:,1) = Iy;
    Iycbcr(:,:,2) = Icb;
    Iycbcr(:,:,3) = Icr;

    figure(1), imshow(Iycbcr);
    f = Iycbcr;
end
