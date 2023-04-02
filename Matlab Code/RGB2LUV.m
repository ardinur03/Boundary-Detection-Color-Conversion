function f = RGB2LUV(I)
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
            Li = double(Iy(i,j)/yn);
            if Li > 0.008856
                IL(i,j) = 116 * nthroot(Li,3) - 16;
            else
                IL(i,j) = 903.3 * Li;
            end

            u = 4 * Ix(i,j) / (Ix(i,j) + 15 * Iy(i,j) + 3 * Iz(i,j));
            un = 4 * xn / (xn + 15 * yn + 3 * zn);
            v = 9 * Iy(i,j) / (Ix(i,j) + 15 * Iy(i,j) + 3 * Iz(i,j));
            vn = 9 * yn / (xn + 15 * yn + 3 * zn);
            Iu(i,j) = 13 * IL(i,j) * (u - un);
            Iv(i,j) = 13 * IL(i,j) * (v - vn);
        end
    end

    ILuv(:,:,1) = IL;
    ILuv(:,:,2) = Iu;
    ILuv(:,:,3) = Iv;

    figure(1), imshow(ILuv);

    f = ILuv;
end