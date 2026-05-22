"""Utility functions for weisswurschtis."""

from typing import Any, List, TypeVar, Callable
import logging

logger = logging.getLogger(__name__)

T = TypeVar('T')


def example_function(value: int) -> int:
    """Simple example function that increments a value.
    
    Args:
        value: An integer to increment
        
    Returns:
        The input value incremented by one
        
    Example:
        >>> example_function(5)
        6
    """
    logger.debug(f"example_function called with value={value}")
    return value + 1


def process_items(items: List[Any]) -> List[Any]:
    """Process a list of items, filtering out None values.
    
    Args:
        items: List of items to process
        
    Returns:
        List of non-None items
        
    Example:
        >>> process_items([1, None, 3, None, 5])
        [1, 3, 5]
    """
    logger.debug(f"process_items called with {len(items)} items")
    filtered = [item for item in items if item is not None]
    logger.debug(f"Filtered to {len(filtered)} non-None items")
    return filtered


def retry(max_attempts: int = 3, delay: float = 1.0) -> Callable:
    """Decorator for retrying a function on failure.
    
    Args:
        max_attempts: Maximum number of retry attempts
        delay: Delay in seconds between retries
        
    Returns:
        Decorated function that retries on exception
        
    Example:
        >>> @retry(max_attempts=3, delay=0.5)
        ... def flaky_function():
        ...     pass
    """
    import time
    
    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    logger.debug(f"Attempt {attempt}/{max_attempts} for {func.__name__}")
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        logger.error(f"Failed after {max_attempts} attempts: {e}")
                        raise
                    logger.warning(f"Attempt {attempt} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
        return wrapper
    return decorator


def batched(iterable: List[T], batch_size: int) -> List[List[T]]:
    """Split an iterable into batches.
    
    Args:
        iterable: List to batch
        batch_size: Size of each batch
        
    Returns:
        List of batches
        
    Example:
        >>> batched([1, 2, 3, 4, 5], 2)
        [[1, 2], [3, 4], [5]]
    """
    if batch_size < 1:
        raise ValueError("batch_size must be at least 1")
    
    batches = [iterable[i:i + batch_size] for i in range(0, len(iterable), batch_size)]
    logger.debug(f"Split {len(iterable)} items into {len(batches)} batches of size {batch_size}")
    return batches
