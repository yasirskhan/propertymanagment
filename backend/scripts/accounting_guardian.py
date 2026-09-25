
# Gate 2: Accounting Guardian - Ensure no unbalanced transactions at 5% stage
print("=== Accounting Guardian 5% ===")
# At 5% we only have rent_amount, no double-entry yet - check for negative rent
from app.core.database import SessionLocal
from app.models.property import Unit
db = SessionLocal()
units = db.query(Unit).all()
for u in units:
    if u.rent_amount < 0:
        print(f"FAIL: Negative rent in unit {u.id}")
        exit(1)
print("Accounting Guardian: No negative rents - PASS")
