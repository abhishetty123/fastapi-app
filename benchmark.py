from random import Random
from statistics import median
from time import perf_counter_ns

from core.database import SessionLocal
from services.user import (
    get_user_by_mail_service,
    get_user_by_mail_raw,
)

functions = {
    "ORM": get_user_by_mail_service,
    "Raw SQL": get_user_by_mail_raw,
}
samples = {name: [] for name in functions}
rng = Random(42)

with SessionLocal() as db:
    email = "abhilash@example.com"  # Use an existing email

    # Warm up the connection and query caches.
    for _ in range(20):
        for function in functions.values():
            assert function(email, db) is not None

    for _ in range(500):
        names = list(functions)
        rng.shuffle(names)

        for name in names:
            start = perf_counter_ns()
            result = functions[name](email, db)
            elapsed = perf_counter_ns() - start
            samples[name].append(elapsed / 1_000)
            del result

for name, timings in samples.items():
    print(f"{name}: {median(timings):.1f} µs median")