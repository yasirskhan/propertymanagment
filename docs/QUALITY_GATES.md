# Quality Gates - 5%
1. Parity Check: Properties, Units, Tenants, Leases CRUD must work
2. Accounting Guardian: No negative rents
3. Security Guardian: No card_number/cvv/pan - only pm_xxx/cus_xxx/sub_xxx
Run: python scripts/check_parity.py && python scripts/accounting_guardian.py && python scripts/security_guardian.py
