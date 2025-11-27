from math import exp

def calculate_time_decay(base_score: float, days_inactive: int) -> float:
    """
    Reputation decays with inactivity to incentivize engagement
    """
    decay_rate = 0.02  # 2% per week of inactivity
    weeks_inactive = days_inactive / 7
    decay_factor = exp(-decay_rate * weeks_inactive)
    
    # Minimum floor to prevent complete erasure
    min_retention = 0.5  # Retain at least 50% of score
    
    return base_score * max(decay_factor, min_retention)


def calculate_incentive_multiplier(entity) -> float:
    """
    Entities with higher reputation get better matches
    """
    base_multiplier = 1.0
    
    if entity.reputation_score >= 90:
        base_multiplier *= 1.5  # 50% boost
    elif entity.reputation_score >= 75:
        base_multiplier *= 1.25  # 25% boost
    elif entity.reputation_score >= 60:
        base_multiplier *= 1.1   # 10% boost
    
    if entity.verification_level >= 4:
        base_multiplier *= 1.3   # Verified entities
    
    if entity.response_time < 4:  # < 4 hours
        base_multiplier *= 1.2
    
    return base_multiplier
