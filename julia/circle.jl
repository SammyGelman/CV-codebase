using NPZ
using Random
function circle(r=5,points=20000)
  theta_range = LinRange(0,2*pi,500)
  r_range = LinRange(0,r,500)
  x = zeros(points)
  y = zeros(points)
    for i = 1:points
      theta = rand(theta_range)
      r = rand(r_range)
      x[i] = r*sin(theta)
      y[i] = r*cos(theta)
    end
    dist = [x y]
end

dist = circle()
npzwrite("dist_2d.npz",dist)        
