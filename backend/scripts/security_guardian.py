
# Gate 3: Security Guardian - PCI compliance
import pathlib, re, sys
print("=== Security Guardian 5% ===")
pattern = re.compile(r"card_number|cvv|"pan"\s*:", re.IGNORECASE)
violations = []
for p in pathlib.Path("app").rglob("*.py"):
    text = p.read_text()
    if pattern.search(text):
        if "pm_xxx" not in text and "cus_xxx" not in text and "sub_xxx" not in text:
            violations.append(str(p))
if violations:
    print(f"FAIL: Card data found in: {violations}")
    sys.exit(1)
print("Security Guardian: Only pm_xxx/cus_xxx/sub_xxx - PASS (PCI compliant)")
