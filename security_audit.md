# Security Audit Report - IS114-Mission-2
**Generated:** 2026-04-26 | **Grade:** C

## Executive Summary
**Status:** ⚠️ MINIMAL REQUIREMENTS | **Critical:** 0 | **High:** 0 | **Medium:** 1 | **Low:** 0

## Critical Issue
**No version pins:** pyserial, keyboard

## Action Required
```bash
cd IS114-Mission-2
cat > requirements.txt << EOF
pyserial>=3.5
keyboard>=0.13.5
EOF
pip install -r requirements.txt
```

## Security Concerns
⚠️ Hardware access (serial port, keyboard)  
⚠️ Requires elevated privileges

## Recommendations
- [ ] Pin versions
- [ ] Validate serial port inputs
- [ ] Implement access controls
- [ ] Add logging for hardware access

**Grade:** C (Needs version pinning + access controls)

