from functools import wraps
import time

def timer(func):
   #fonk çalışma süresini ölçer
    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        print(f"[çalışma süresi] {func.__name__}: {elapsed:.4f}s")
        return result
    return wrapper


def required_columns(required: set[str]): 
    #eksik satırları kontrol eder
    def decorator(func):
        @wraps(func)
        def wrapper(rows, *args, **kwargs):
            if not rows:
                raise ValueError("Boş veri seti!")
            keys = set(rows[0].keys())
            missing = required - keys
            if missing:
                raise ValueError(f"Eksik kolon(lar): {', '.join(missing)}")
            return func(rows, *args, **kwargs)
        return wrapper
    return decorator
