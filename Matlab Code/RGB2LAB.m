function f = RGB3LAB(I)
    Ixyz = rgb2xyz(I);
    Ix = Ixyz(:,:,1);
    Iy = Ixyz(:,:,2);
    Iz = Ixyz(:,:,3);
    [m,n] = size(Ix);  

    xn = 0.95047;
    yn = 1;
    zn = 1.08883;

    for i = 1 : m
        for j = 1 : n
            IL(i,j) = 116 * flab(Iy(i,j)/yn) - 16;
            Ia(i,j) = 500 * (flab(Ix(i,j)/xn) - flab(Iy(i,j)/yn));
            Ib(i,j) = 200 * (flab(Iy(i,j)/yn) - flab(Iz(i,j)/zn));
        end
    end

    Ilab(:,:,1) = IL;
    Ilab(:,:,2) = Ia;
    Ilab(:,:,3) = Ib;

    figure(1), imshow(Ilab);
    f = Ilab;
end