
def test_pci_compliant():
    # Ensure no card data patterns without pm_xxx/cus_xxx/sub_xxx
    import pathlib
    forbidden = ["card_number", "cvv"]
    for p in pathlib.Path("app").rglob("*.py"):
        text = p.read_text()
        for f in forbidden:
            if f in text.lower():
                assert "pm_xxx" in text or "cus_xxx" in text or "sub_xxx" in text, f"Card data found in {p}"

def test_addon_model():
    from app.core.feature_flags import ADDONS
    assert "base" in ADDONS
    assert "accounting_pro" in ADDONS
    assert ADDONS["accounting_pro"]["price"] == 49
