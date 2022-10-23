
function metropolis_1d(p, x_init, y_init, dx, dy, n, l)
	distribution = zeros(n,2)
	x = x_init
	y = y_init	
	n_steps = 0
	n_samples = 0
	while n_samples < n
		step_x = (rand() - 0.5) * 2 * dx
		step_y = (rand() - 0.5) * 2 * dy

		x_new = x + step_x
		prob_x = p(x_new,y) / p(x,y)
		y_new = y + step_y
		prob_x = p(x,y_new) / p(x,y)

		if mod(n_steps, l) == 0 && prob_x > rand()
			x = x_new
		end

		if mod(n_steps, l) == 0 && prob_y > rand()
			y = y_new
		end

		if mod(n_steps, l) == 0
			distribution[n_samples + 1,1] = x
			distribution[n_samples + 1,2] = y 
			n_samples = n_samples + 1
		end
		n_steps = n_steps + 1
	end
	return(distribution)
end


