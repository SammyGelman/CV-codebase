function rotated_gaussian(theta; mu_x=0.0, mu_y=0.0, sigma_x=1.0, sigma_y=1.0, A=1.0)
    function p(x,y)
        a = (cos(theta)^2)/(2*sigma_x^2) + (sin(theta)^2)/(2*sigma_y^2)
        b = (-sin(2*theta))/(4*sigma_x^2) + (cos(2*theta))/(4*sigma_y^2)
        c = (sin(theta)^2)/(2*sigma_x^2) + (cos(theta)^2)/(2*sigma_y^2)

        z = A*exp(-(a*(x - mu_x)^2 + 2*b*(x - mu_x)*(y - mu_y) + c*(y - mu_y)^2))
	end
    return(p)
end
#(1/2)*(log(2*pi*sigma^2)+1)

#i = pi/((c*a+b^2)^(0.5))



