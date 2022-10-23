function metropolis_1d(p, x_init, dx, n, l)
    distribution = zeros(n)
		x = x_init
		n_steps = 0
		n_samples = 0
    while n_samples < n
				step = (rand() - 0.5) * 2 * dx
        x_new = x + step
        prob = p(x_new) / p(x)
				if mod(n_steps, l) == 0 && prob > rand()
						x = x_new
        end
				if mod(n_steps, l) == 0
					distribution[n_samples + 1] = x
					n_samples = n_samples + 1
				end
				n_steps = n_steps + 1
    end
    return(distribution)
end

