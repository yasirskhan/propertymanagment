# PropertyManagment SaaS - 5% Deliverable
White-label + Add-on Monetization

## What is included (5%):
- Properties + Units CRUD (with tests)
- Tenants + Leases CRUD (with tests)
- Add-on entitlements: base $0 + accounting_pro $49 + maintenance_pro $29 + white_label $99
- 3 Quality Gates: Parity, Accounting, Security (PCI - only pm_xxx/cus_xxx/sub_xxx)
- SQLite + SQLAlchemy + FastAPI - runnable locally

## Run locally
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
# http://localhost:8000/docs
```

## Test
```bash
cd backend
pytest -v
```

## 5% Progress: 18/350 features = 5.1%
