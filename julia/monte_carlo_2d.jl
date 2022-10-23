using NPZ
include("rotated_gaussian.jl")
#import distribution data set
dist = npzread("dist_2d.npz")

#break data into x and y
x = dist[:,1]
y = dist[:,2]

#import our function with default pi value
p = rotated_gaussian((pi))

#generate z axis variables
z = zeros(length(x))

for i in 1:length(x)
	z[i] = p(x[i],y[i])
	return(z)
end

#find min vals for normalization
x_min = minimum(x)
y_min = minimum(y)
#z_min = minimum(z) (zero in our case)

#Without normilaization
#Find the max values
x_max = maximum(x)
y_max = maximum(y)
z_max = maximum(z)

#find the space range
x_range = x_max - x_min
y_range = y_max - y_min
z_range = z_max 

#Normalize the distribution
#x_norm = x .- x_min
#y_norm = y .- y_min
#z_norm = z .- z_min


#get max for x, y and z from norm which is the length of interest space
#x_range = maximum(x_norm)
#y_range = maximum(y_norm)
#z_range = maximum(z)

space = x_range*y_range*z_range

#generate random points and log them as 1's or 0's in array
points = 200000

function monte_integrate(points)
	vec = 0
	while points > 0
	x_test = rand()*x_range + x_min
	y_test = rand()*y_range + y_min
	z_test = rand()*z_range #+ z_min
	if z_test < p(x_test,y_test)
		vec += 1
	end
	points -= 1
	end
	return(vec)
end

vec = monte_integrate(points)

#calculate the numeric integral
integral = space*(vec/points)

#print answer
print(integral)
