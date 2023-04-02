function f = RGB2XYZ(I)
    Ir = I(:,:,1);
    Ig = I(:,:,2);
    % white point d65
    xn = 0.95047;
    yn = 1;
    zn = 1.08883;

    for i=1:m
        for j = 1 : n
            L = IL(i,j);
            a = Ia(i,j);
            b = Ib(i,j);

            fy = ((L+16)/116) ^3;
            if fy < 0.008856
                fy = (L/903.3);
            end

            Iy(i,j) = fy;
            fy = flab(fy);

            fx = a/500 + fy;
            if fx < 0.008856
                fx = fx^3;
            else 
                fx = (fx-16/116)/7.787;
            end

            Ix(i,j) = fx;

            fz = fy - b/200;
            if fz < 0.008856
                fz = fz^3;
            else 
                fz = (fz-16/116)/7.787;
            end

            Iz(i,j) = fz;
        end
    end

    Ixyz(:,:,1) = Ix;
    Ixyz(:,:,2) = Iy;
    Ixyz(:,:,3) = Iz;
    Irgb = xyz2rgb(Ixyz);
    figure(1), imshow(Irgb);
    f = Irgb;
end

