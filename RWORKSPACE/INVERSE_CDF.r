# What we want to generate exp(2)
u = runif(10000)
x = -(1/2)*log(u)
hist(x, nclass=100)
