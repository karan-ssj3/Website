# Portfolio Website Deployment Guide

## 🚀 Deployment Options

### Option 1: Reflex Cloud (Recommended for Reflex Apps)

1. **Install Reflex hosting CLI** (already in requirements.txt):
   ```bash
   pip install reflex-hosting-cli
   ```

2. **Login to Reflex Cloud**:
   ```bash
   reflex login
   ```

3. **Deploy your app**:
   ```bash
   reflex deploy
   ```

4. **Get your deployment URL** (e.g., `your-app.reflex.run`)

---

### Option 2: Vercel (Great for Reflex Apps)

1. **Install Vercel CLI**:
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel**:
   ```bash
   vercel login
   ```

3. **Deploy from your project directory**:
   ```bash
   cd portfolio-website
   vercel
   ```

4. **Follow the prompts** and get your deployment URL (e.g., `your-app.vercel.app`)

---

### Option 3: Railway

1. **Go to** [railway.app](https://railway.app) and sign up
2. **Create a new project** and connect your GitHub repository
3. **Railway will auto-detect** your Python app and deploy
4. **Get your deployment URL** from Railway dashboard

---

### Option 4: Render

1. **Go to** [render.com](https://render.com) and sign up
2. **Create a new Web Service** and connect your GitHub repo
3. **Set build command**: `pip install -r requirements.txt && reflex export`
4. **Set start command**: `reflex run --backend-only`
5. **Get your deployment URL** from Render dashboard

---

## 🔗 Connect Your Hostinger Domain

### Step 1: Log into Hostinger

1. Go to [hpanel.hostinger.com](https://hpanel.hostinger.com)
2. Navigate to **Domains** → **Manage Domains**
3. Click on your domain

### Step 2: Configure DNS Records

Go to **DNS / Name Servers** section and add/update the following records:

#### For Reflex Cloud:
```
Type: CNAME
Name: @ (or www)
Value: your-app.reflex.run
TTL: 3600
```

#### For Vercel:
```
Type: CNAME
Name: @ (or www)
Value: cname.vercel-dns.com
TTL: 3600
```

Then in Vercel dashboard:
- Go to **Your Project** → **Settings** → **Domains**
- Add your domain (e.g., `yourdomain.com` and `www.yourdomain.com`)
- Vercel will provide specific DNS instructions

#### For Railway/Render:
```
Type: CNAME
Name: @ (or www)
Value: your-app.railway.app (or your-app.onrender.com)
TTL: 3600
```

### Step 3: Configure A Record (if needed)

Some hosting providers require an A record instead:

```
Type: A
Name: @
Value: [IP address from your hosting provider]
TTL: 3600
```

For Vercel, you might need:
```
Type: A
Name: @
Value: 76.76.21.21
TTL: 3600

Type: A
Name: @
Value: 76.223.126.88
TTL: 3600
```

### Step 4: Wait for DNS Propagation

- DNS changes can take **5 minutes to 48 hours** to propagate
- Usually takes **15-30 minutes** for most changes
- Check propagation status at: [dnschecker.org](https://dnschecker.org)

### Step 5: Enable HTTPS/SSL

Most modern hosting platforms (Vercel, Railway, Render) automatically:
- ✅ Provide free SSL certificates
- ✅ Enable HTTPS
- ✅ Handle SSL renewal automatically

---

## ✅ Verification Steps

1. **Check DNS records** are correct in Hostinger
2. **Wait for DNS propagation** (use dnschecker.org)
3. **Visit your domain** in a browser
4. **Check HTTPS** is working (should see 🔒 icon)
5. **Test all pages** work correctly

---

## 🔧 Troubleshooting

### Domain not working?
- ✅ Check DNS records are correct
- ✅ Wait longer for DNS propagation
- ✅ Clear your browser cache
- ✅ Try in incognito mode
- ✅ Check hosting provider dashboard for errors

### SSL certificate issues?
- ✅ Most platforms auto-handle SSL
- ✅ Wait 24-48 hours for SSL to provision
- ✅ Check hosting provider SSL settings

### Subdomain setup (www)?
- ✅ Add both `@` and `www` CNAME records
- ✅ Configure redirect in hosting provider (www → non-www or vice versa)

---

## 📝 Notes

- **Hostinger** is just for domain registration - you're deploying elsewhere
- **No hosting costs** for most platforms (free tiers available)
- **Custom domains are free** on most platforms
- **SSL is automatic** on modern platforms

---

## 🎯 Recommended Approach

**Best Option**: **Vercel** + **Hostinger Domain**
- ✅ Easy deployment
- ✅ Free SSL
- ✅ Fast CDN
- ✅ Great for Reflex apps
- ✅ Simple DNS setup

**Quick Start**:
1. Deploy to Vercel
2. Add domain in Vercel dashboard
3. Configure CNAME in Hostinger
4. Wait 15-30 minutes
5. Your portfolio is live! 🚀

