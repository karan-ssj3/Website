# Domain Setup for karanbhutani.com

## Current Hostinger DNS Records:
- **A Record**: @ → 84.32.84.32
- **CNAME**: www → karanbhutani.com
- **CAA Records**: Various SSL certificate issuers (keep these!)

## Steps to Connect to Reflex Cloud:

### 1. Get DNS Info from Reflex Cloud:
   - Go to: https://cloud.reflex.dev
   - Navigate to your app settings
   - Look for "Custom Domain" or "DNS Settings"
   - Copy the CNAME target or IP address

### 2. Update Hostinger DNS:

#### If Reflex gives you a CNAME target (e.g., `app-xxx.reflex.run`):
   1. **Change A Record to CNAME**:
      - Edit the A record (@ → 84.32.84.32)
      - Change Type: A → CNAME
      - Change Points to: 84.32.84.32 → [Reflex CNAME target]
      - TTL: 3600

   2. **Update www CNAME**:
      - Edit: www → karanbhutani.com
      - Change Points to: karanbhutani.com → [Reflex CNAME target]
      - TTL: 3600

#### If Reflex gives you an IP address:
   1. **Update A Record**:
      - Edit: @ → 84.32.84.32
      - Change Points to: 84.32.84.32 → [Reflex IP address]
      - TTL: 3600

   2. **Keep www CNAME as is** (or update if Reflex specifies)

### 3. Keep CAA Records:
   - Don't delete the CAA records
   - They're needed for SSL certificates

### 4. Wait for DNS Propagation:
   - Usually 15-30 minutes
   - Check at: https://dnschecker.org
   - Search for: karanbhutani.com

### 5. Verify in Reflex Cloud:
   - Go back to Reflex Cloud dashboard
   - Add your custom domain: karanbhutani.com
   - Reflex will verify DNS and provision SSL

## Important Notes:
- ✅ Keep all CAA records (they're for SSL)
- ✅ DNS changes take 15-30 minutes to propagate
- ✅ Reflex Cloud will automatically provide SSL/HTTPS
- ✅ Both karanbhutani.com and www.karanbhutani.com will work

## Troubleshooting:
- If domain doesn't work after 30 minutes: Check DNS propagation status
- If SSL error: Wait for Reflex to provision certificate (can take a few hours)
- If www doesn't work: Make sure www CNAME is pointing to Reflex domain

