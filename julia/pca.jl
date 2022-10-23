using LinearAlgebra 

PCA(cov_matrix,X)
	svd_matrix = svd(cov_matrix)
	reduced_svd = svd_matrix.U[:,1,(columns(cov_matrix)-1)]
	z = reduced_svd'*X
Return

