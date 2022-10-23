#!/usr/bin/env julia
function ring(R=3.0,a=0.1)
    function p(x,y)
        r = sqrt(x^2+y^2)
        return exp(-(((r-R))^2/(2*a)))
    end
    return p
end
