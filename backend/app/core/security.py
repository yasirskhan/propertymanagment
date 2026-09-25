
import re
# PCI Guard - ensure no card data stored
FORBIDDEN_PATTERNS = [
    r"card_number",
    r"\bcvv\b",
    r""pan"\s*:",
    r"\bcredit_card\b.*\d{13,19}",
]

def check_pci_compliant(code: str) -> bool:
    for pattern in FORBIDDEN_PATTERNS:
        if re.search(pattern, code, re.IGNORECASE):
            if "pm_xxx" not in code and "cus_xxx" not in code and "sub_xxx" not in code:
                return False
    return True
