
from fastapi import APIRouter
from app.core.feature_flags import ADDONS, get_entitlements

router = APIRouter()

@router.get("/")
def list_addons():
    return ADDONS

@router.get("/entitlements/{org_id}")
def entitlements(org_id: str):
    return get_entitlements(org_id)

@router.post("/{addon}/subscribe")
def subscribe_addon(addon: str, org_id: str):
    if addon not in ADDONS:
        return {"error": "Add-on not found"}
    # In prod: create Stripe Checkout Session - only return pm_xxx/cus_xxx/sub_xxx
    return {
        "checkout_url": f"https://checkout.stripe.com/c/pay/{addon}",
        "addon": addon,
        "stripe_ref": f"pm_xxx_demo_{addon}",
        "message": "Only pm_xxx/cus_xxx/sub_xxx stored - PCI compliant"
    }
