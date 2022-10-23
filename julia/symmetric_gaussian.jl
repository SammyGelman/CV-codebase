# Parameters:
sigma = 1.0

function gaussian(x)
    return 1/ sqrt(2 * pi * sigma) * exp(-0.5 * (x / sigma) ^ 2)
end

function gaussian_2d()
    function p(x, y)
        return gaussian(x) * gaussian(y)
    end
end
