function x = CIELab(q)
    ILab = RGB2LAB(q);
    x = LAB2RGB(ILab);

    figure,
    subplot(1,3,1), imshow(q), title('Original');
    subplot(1,3,2), imshow(ILab), title('CIELab');
    subplot(1,3,3), imshow(x), title('Back to RGB');
    
end