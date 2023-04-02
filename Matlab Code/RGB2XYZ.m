function f = RGB2XYZ(I)
    Ir = I(:,:,1);
    Ig = I(:,:,2);

    Ib = I(:,:,3);
    [m,n] = size(Ir);

    k = [0.49 0.31 0.20; 0.17697 0.81240 0.01063; 0.00 0.01 0.99;];

    for i = 1 : m
        for j = 1 : n
            rgb = [Ir(i,j); Ig(i,j); Ib(i,j)];
            xyz = (1/0.17697) * k * double(rgb);
            Ix(i,j) = xyz(1,:);
            Iy(i,j) = xyz(2,:);
            Iz(i,j) = xyz(3,:);
        end
    end

    Ixyz(:,:,1) = Ix;
    Ixyz(:,:,2) = Iy;
    Ixyz(:,:,3) = Iz;

    figure(1), imshow(Ixyz);
    f = Ixyz;
end

