#!/usr/bin/env julia
function part(mu_x, mu_y, theta=pi, sigma_x=1.0, sigma_y=1.0, A=1.0)
    function p(x,y)
        return A*exp(-((x - mu_x)^2 + (y - mu_y)^2))
    end
    return p 
end

mu = 3.0

plus_plus = part(mu,mu)
plus_minus = part(mu,-mu)
minus_plus = part(-mu,mu)
minus_minus = part(-mu,-mu)

function tricky_gaussian()
    function p(x,y)
         return plus_plus(x,y) + plus_minus(x,y) + minus_plus(x,y) + minus_minus(x,y)    
    end
    return p
end

