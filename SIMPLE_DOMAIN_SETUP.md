# Simple Domain Setup - Step by Step

## 🎯 Your Goal:
Connect `karanbhutani.com` to your Reflex portfolio website

---

## Step 1: Find Your Reflex URL

**Where to find it:**
1. Go to: https://cloud.reflex.dev
2. Login to your account
3. Click on your app (probably called "portfolio-website")
4. Look for your app URL - it will look like:
   - `portfolio-website-xxxxx.reflex.run`
   - OR `app-xxxxx.reflex.run`
   - OR similar format

**OR check your terminal** - the deployment command should have shown a URL when it finished.

**Write down this URL - you'll need it for Step 2!**

---

## Step 2: Update Hostinger DNS (I'll help with exact values)

Once you have the Reflex URL, we'll update these 2 records in Hostinger:

### Record 1: Root Domain (@)
- Change the A record to CNAME
- Point it to your Reflex URL

### Record 2: www Subdomain  
- Update the CNAME
- Point it to your Reflex URL

---

## Step 3: Add Domain in Reflex Cloud

1. Go back to Reflex Cloud dashboard
2. Find "Custom Domain" or "Domains" section
3. Click "Add Domain"
4. Enter: `karanbhutani.com`
5. Reflex will verify and set up SSL automatically

---

## Step 4: Wait & Test

- Wait 15-30 minutes
- Visit: https://karanbhutani.com
- Your portfolio should be live! 🎉

---

## Need Help?

**Just share your Reflex app URL and I'll tell you exactly what to put in Hostinger!**

