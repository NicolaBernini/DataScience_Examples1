
# Estimation Procedures (MLE, MAP) Explained

Published on 
- Medium 
  - [Estimation Procedures (MLE, MAP) Explained](https://medium.com/@nicolabernini_63880/estimation-procedures-mle-map-explained-c7fb4828e3b2)

As I really liked this post about Estimation Procedures I’d like to add my 2 cents with a pair of graphs summarizing (and possibly clarifying even further) this article

[A sane introduction to maximum likelihood estimation (MLE) and maximum a posteriori (MAP)](http://blog.christianperone.com/2019/01/a-sane-introduction-to-maximum-likelihood-estimation-mle-and-maximum-a-posteriori-map/)

## What is an Estimation Procedure

![Estimation1](https://cdn-images-1.medium.com/max/800/1*9x5x5aA6zCTFF1_GDb8S2w.png)

Essentially an estimation process starts from a set of observations and a parametric model and consists of a procedure to find the point in model parameters space (hence the model parametrization) which optimizes some given metric

It means the procedure requires

- Performing Observations / Experiments to get the data points
- Performing Model Choice which implicitly defines the Latent Space
- Choosing the Metric to be optimized, e.g. choosing Likelihood we will have Maximum Likelihood Estimation (MLE)



## What is MLE

Likelihood definition is provided in equation 1 of above mentioned article as the “Probability of observing the given data points, assuming a certain parametrization”

Choosing this metric results in an estimation scheme like the following one

![MLE1](https://cdn-images-1.medium.com/max/800/1*WaMWzEv746JhIaB9v1pYuA.png)

It works as follows

- the Observation are fixed per experiment, so they do not change while performing the optimization that powers the search in the latent params space

- the optimization process is iterative, which means at every iteration there is always a params point to test (at first iteration it’s possible to use some kind of initial guess, even random, the actual capability of converging to a good value depends on a bunch of factors like the loss surface shape, the optimization algorithm used, the number of iterations, …)

- given the data points AND a certain parametrization it is possible to compute the Likelihood which according to its definition is computed as the probability of the data points assuming the parametrization

- assuming the Likelihood Function is continuous, the optimization is performed essentially using the gradient which is computed at each iteration and along with the step size choice defines the way the loss surface in the latent params space is navigated

- if the optimization algorithm is not greedy, the last value might not be the absolute best value so an Absolute Best Tracking Module is needed (trivial module: just tracking the best)

- typically as the latent space to explore is huge and the optimization problem is non convex the optimization is constrained in terms of time / number of iterations and the “best so far” is returned



## Final Notes

Possibly I’ll expand this article including the scheme for MAP or I’ll put into a new article so stay tuned


