import numpy as np
import pandas as pd
from scipy.optimize import minimize

def create_initial_weights(number_of_assets):
    return np.array([1/number_of_assets] * number_of_assets)

def negative_sharpe_ratio(weights, expected_return, cov_matrix, riskfree_rate):
    portfolio_return = np.dot(weights, expected_return)
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    sharpe_ratio = (portfolio_return - riskfree_rate) / portfolio_volatility
    return -sharpe_ratio

def minimize_negative_sharpe_ratio(number_of_assets, negative_sharpe_ratio, initial_weights, expected_returns_array, cov_matrix, riskfree_rate):
    constraints = ({
    'type': 'eq', # Needs a equality constraint
    'fun': lambda w: np.sum(w) - 1 # Sum of weights needs to equal 1, not less nor more
    })
    
    # Limiting range of weights from 0 to 1
    bounds = tuple((0, 1) for _ in range(number_of_assets))

    result = minimize(
    fun=negative_sharpe_ratio,
    x0=initial_weights,
    args=(expected_returns_array, cov_matrix.values, riskfree_rate),
    method='SLSQP',
    bounds=bounds,
    constraints=constraints)

    optimal_weights = result.x
    max_sharpe = -result.fun  # Minimised optimal sharpe

    return optimal_weights, max_sharpe

def entropy(weights):
    # Add a small epsilon to avoid log(0)
    epsilon = 1e-10
    weights = np.clip(weights, epsilon, 1)
    return -np.sum(weights * np.log(weights))

def negative_sharpe_with_entropy(weights, expected_return, cov_matrix, riskfree_rate, entropy_weight=0.05):
    portfolio_return = np.dot(weights, expected_return)
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    sharpe_ratio = (portfolio_return - riskfree_rate) / portfolio_volatility
    
    # We want to penalize concentration: add entropy term (negated because we minimize)
    penalty = -entropy(weights)  # negative because entropy is maximized
    return -sharpe_ratio + entropy_weight * penalty

def minimize_negative_sharpe_ratio_with_entropy (number_of_assets, initial_weights, expected_returns_array, cov_matrix, riskfree_rate, entropy_weight=0.05):
    constraints = ({
        'type': 'eq',
        'fun': lambda w: np.sum(w) - 1
    })

    bounds = tuple((0, 1) for _ in range(number_of_assets))

    result = minimize(
        fun=negative_sharpe_with_entropy,
        x0=initial_weights,
        args=(expected_returns_array, cov_matrix.values, riskfree_rate, entropy_weight),
        method='SLSQP',
        bounds=bounds,
        constraints=constraints
    )

    optimal_weights = result.x
    max_sharpe_with_entropy = -result.fun

    return optimal_weights, max_sharpe_with_entropy
