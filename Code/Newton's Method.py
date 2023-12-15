# solve the unconstrained optimization problem min f(x,y) = exp(x)+y^2-3x
# true optimum should be y = 0 and x = log(3) = 1.09861

df = lambda x: np.array([np.exp(x[0])-3,2*x[1]])
d2f = lambda x: np.array([[np.exp(x[0]), 0],
                           [0,2]])

xOpt = newton(df,d2f,np.array([0,1]),1e-12)

print(xOpt)