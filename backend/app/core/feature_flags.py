
# Add-on monetization - PCI compliant: only pm_xxx/cus_xxx/sub_xxx stored
ADDONS = {
    "base": {"price": 0, "features": ["properties", "units", "tenants", "leases"]},
    "accounting_pro": {"price": 49, "stripe_price_id": "price_accounting_pro", "requires": "base", "features": ["accounting", "reports"]},
    "maintenance_pro": {"price": 29, "stripe_price_id": "price_maintenance_pro", "requires": "base", "features": ["work_orders"]},
    "white_label": {"price": 99, "stripe_price_id": "price_white_label", "requires": "base", "features": ["custom_domain", "branding"]},
}

# Mock entitlement store - in prod fetch from Stripe: customer -> subscriptions
# Only store: cus_xxx, sub_xxx, pm_xxx - NEVER card_number, cvv, pan
ENTITLEMENTS_DB = {
    "org_demo": ["base", "accounting_pro"],
    "org_test": ["base"],
}

def get_entitlements(org_id: str):
    entitlements = ENTITLEMENTS_DB.get(org_id, ["base"])
    return {
        "org_id": org_id,
        "entitlements": entitlements,
        "stripe_customer": f"cus_{org_id}",  # only cus_xxx
        "stripe_subscription": f"sub_{org_id}_xxx",  # only sub_xxx
    }

def has_addon(org_id: str, addon: str) -> bool:
    ent = get_entitlements(org_id)
    return addon in ent["entitlements"]

def require_addon(org_id: str, addon: str):
    if not has_addon(org_id, addon):
        from fastapi import HTTPException
        raise HTTPException(status_code=403, detail=f"Add-on required: {addon} - Upgrade at /api/v1/addons")
