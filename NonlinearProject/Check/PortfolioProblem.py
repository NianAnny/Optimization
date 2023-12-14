import numpy as np

# Portfolio Optimization
def optimize_portfolio(returns, risk_tolerance, num_portfolios=1000, num_iterations=100, elite_frac=0.2):
    num_assets = len(returns)
    # Initialize a uniform distribution for portfolio weights
    weights = np.full((num_portfolios, num_assets), 1.0 / num_assets)
    
    for _ in range(num_iterations):
        # Generate sample portfolios
        samples = np.random.dirichlet(alpha=np.ones(num_assets), size=num_portfolios)
        
        # Calculate expected return and risk (standard deviation) for each portfolio
        portfolio_returns = np.dot(samples, returns)
        portfolio_risks = np.std(samples, axis=1)
        
        # Select elite samples based on return-to-risk ratio
        fitness = portfolio_returns / portfolio_risks
        elite_idx = np.argsort(fitness)[-int(num_portfolios * elite_frac):]
        elite_samples = samples[elite_idx]

        # Update distribution parameters
        weights = np.mean(elite_samples, axis=0)

    return weights

# Example usage
returns = np.array([0.12, 0.10, 0.14])  # Expected returns of assets
optimized_weights = optimize_portfolio(returns, risk_tolerance=0.05)
print("Optimized Portfolio Weights:", optimized_weights)
