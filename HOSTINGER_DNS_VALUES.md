# Exact DNS Values for Hostinger

## Your Reflex App URL:
`portfolio-website-gold-apple.reflex.run`

---

## 📝 Update These DNS Records in Hostinger:

### Record 1: Root Domain (@)

**Current:** 
- Type: A
- Name: @
- Points to: 84.32.84.32

**Change to:**
- Type: **CNAME**
- Name: **@** (or leave blank)
- Points to: **portfolio-website-gold-apple.reflex.run**
- TTL: **3600**

---

### Record 2: www Subdomain

**Current:**
- Type: CNAME
- Name: www
- Points to: karanbhutani.com

**Change to:**
- Type: **CNAME**
- Name: **www**
- Points to: **portfolio-website-gold-apple.reflex.run**
- TTL: **3600**

---

### ✅ Keep These Records (Don't Delete):
- All CAA records (they're needed for SSL)

---

## 🎯 Step-by-Step in Hostinger:

1. **Go to:** https://hpanel.hostinger.com
2. **Navigate to:** Domains → karanbhutani.com → DNS / Name Servers
3. **Edit the A record (@ → 84.32.84.32):**
   - Click "Edit"
   - Change Type: **A** → **CNAME**
   - Change Points to: **84.32.84.32** → **portfolio-website-gold-apple.reflex.run**
   - TTL: **3600**
   - Click Save

4. **Edit the CNAME record (www → karanbhutani.com):**
   - Click "Edit"
   - Change Points to: **karanbhutani.com** → **portfolio-website-gold-apple.reflex.run**
   - TTL: **3600**
   - Click Save

---

## 📋 After Updating DNS:

1. **Wait 15-30 minutes** for DNS propagation
2. **Go to Reflex Cloud:** https://cloud.reflex.dev
3. **Open your app** (portfolio-website)
4. **Find "Custom Domain" or "Domains"** section
5. **Add your domain:** `karanbhutani.com`
6. **Reflex will verify DNS and provision SSL automatically**

---

## ✅ Verify It's Working:

After DNS propagates (15-30 min), visit:
- https://karanbhutani.com
- https://www.karanbhutani.com

Both should show your portfolio! 🎉

---

## 🔍 Check DNS Propagation:

Visit: https://dnschecker.org
- Search for: `karanbhutani.com`
- Look for Type: CNAME
- Should show: `portfolio-website-gold-apple.reflex.run`

