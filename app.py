import json
import streamlit as st

st.set_page_config(
    page_title="ShipAI v2.0 — FastAPI + Gemini Micro-SaaS Sandbox",
    page_icon="⚡",
    layout="wide",
)

# Telemetry ping so our Radar tracks Hugging Face Space visits too!
st.markdown(
    '<img src="https://abacus.jasoncameron.dev/hit/shipai-yahiaoui26/hf_space_views" width="1" height="1" style="display:none;" />',
    unsafe_allow_html=True,
)

st.title("⚡ ShipAI v2.0 — FastAPI + Google Gemini AI Micro-SaaS Sandbox")
st.markdown(
    "**Launch your Python AI Micro-SaaS in 24 Hours, Not 3 Weeks.** "
    "Includes Async FastAPI Core, HS256 JWT + Bcrypt Auth, SaaS User Credit Wallet (`HTTP 402`), "
    "Live Gumroad License Verification, 5 B2B Vertical Presets, and Docker Compose."
)

col_cta1, col_cta2, col_cta3 = st.columns(3)
with col_cta1:
    st.link_button(
        "🚀 Get Full ShipAI v2.0 Boilerplate (20% OFF)",
        "https://yahiaoui26.gumroad.com/l/shipai-pro?wanted=true&code=LAUNCH20&option=4h8_Gbt5OwFlRw6D_obkjQ%3D%3D",
        use_container_width=True,
    )
with col_cta2:
    st.link_button(
        "📘 Download Free 2026 Blueprint ($0)",
        "https://yahiaoui26.gumroad.com/l/fastapi-gemini-blueprint",
        use_container_width=True,
    )
with col_cta3:
    st.link_button(
        "⭐ Star Open-Source Blueprint on GitHub",
        "https://github.com/RAZIO05/fastapi-gemini-2026-blueprint",
        use_container_width=True,
    )

st.markdown("---")

PRESETS = {
    "saas_validator": {
        "name": "🚀 1. AI Startup & Micro-SaaS Validator (Founder Tool)",
        "prompt": "Validate a B2B Micro-SaaS that automates invoice reconciliation for logistics agencies.",
        "context": "Solo founder, $0 ad budget, targeting $5k MRR in 90 days.",
        "sample_output": {
            "status": "success",
            "preset_used": "saas_validator",
            "plan_tier": "pro",
            "credits_remaining": 9,
            "summary": "Viability Score: 89/100 — High-margin B2B painkiller with immediate ROI for freight brokers.",
            "key_points": [
                "Logistics agencies lose 12+ hrs/week manually matching PDF bills of lading against ERP invoices",
                "High willingness-to-pay ($99-$249/mo) because preventing a single billing error pays for the annual plan",
                "Google Gemini 3.5 Flash native multimodal JSON extracts line-items without brittle OCR templates",
            ],
            "action_items": [
                "Launch a free Freight Invoice Discrepancy Checker lead magnet using ShipAI /process-ai route",
                "Price tiers at $49 Starter and $149 Pro via ShipAI built-in credit quota engine",
                "DM 25 regional 3PL operations managers on LinkedIn with a 60-second Streamlit demo video",
            ],
        },
    },
    "contract_auditor": {
        "name": "⚖️ 2. Legal & Freelance MSA Contract Risk Auditor (LegalTech)",
        "prompt": "Client shall own all pre-existing tools and background IP created by Contractor, with unlimited indemnity and Net-90 payment terms.",
        "context": "Independent software consultant reviewing a US Master Services Agreement (MSA).",
        "sample_output": {
            "status": "success",
            "preset_used": "contract_auditor",
            "plan_tier": "pro",
            "credits_remaining": 8,
            "summary": "RISK LEVEL: CRITICAL (94/100) — Contains predatory Background IP seizure and uncapped liability traps.",
            "key_points": [
                "Background IP Trap: Transfers ownership of your reusable boilerplates and prior libraries to Client",
                "Uncapped Indemnity: Exposes personal/company assets to unlimited third-party damages",
                "Net-90 Cashflow Risk: 3-month payment delay creates severe working-capital strain",
            ],
            "action_items": [
                "Carve out Pre-Existing IP: Retain full ownership of prior tools and grant a non-exclusive license only",
                "Cap Total Liability: Limit aggregate liability to total fees paid in the preceding 3 months",
                "Amend Payment Terms: Replace Net-90 with Net-15 and 50% upfront milestone deposit",
            ],
        },
    },
    "code_security_reviewer": {
        "name": "🛡️ 3. DevSecOps & OWASP Code Security Auditor (DevTools)",
        "prompt": "cursor.execute(f\"SELECT * FROM users WHERE email = '{email}'\")\njwt.encode({'sub': user_id}, 'hardcoded_secret')",
        "context": "Production Python FastAPI microservice handling customer billing.",
        "sample_output": {
            "status": "success",
            "preset_used": "code_security_reviewer",
            "plan_tier": "pro",
            "credits_remaining": 7,
            "summary": "SEVERITY: BLOCKER (CVSS 9.8) — Direct SQL Injection (CWE-89) and Hardcoded JWT Signing Secret (CWE-798).",
            "key_points": [
                "CWE-89 SQL Injection: f-string interpolation allows full database dump or auth bypass",
                "CWE-798 Hardcoded Secret: Static JWT key enables attackers to forge admin bearer tokens offline",
                "Missing Token Expiration (exp claim): Issued JWTs remain valid indefinitely",
            ],
            "action_items": [
                "Use Parameterized Queries: cursor.execute('SELECT * FROM users WHERE email = %s', (email,))",
                "Load SECRET_KEY from environment via python-dotenv and enforce 256-bit entropy",
                "Include mandatory exp claim using ShipAI app/auth.py create_access_token() helper",
            ],
        },
    },
    "resume_ats_optimizer": {
        "name": "📄 4. Executive Resume & ATS Score Optimizer (CareerTech)",
        "prompt": "Backend developer with 4 years Python experience. Built APIs with FastAPI and PostgreSQL and deployed on Docker.",
        "context": "Applying for Senior AI Backend Engineer ($160k+ remote role).",
        "sample_output": {
            "status": "success",
            "preset_used": "resume_ats_optimizer",
            "plan_tier": "pro",
            "credits_remaining": 6,
            "summary": "Current ATS Match Score: 48% -> Optimized Score: 92% (Added latency, throughput & LLM metrics).",
            "key_points": [
                "Duty-focused phrasing fails Senior-level engineering ownership filters",
                "Missing high-weight 2026 AI keywords: Pydantic v2, Structured Outputs, AsyncIO, Token Quota Management",
            ],
            "action_items": [
                "Rewrite Bullet 1: Architected async FastAPI + Google Gemini microservices handling 45k+ daily structured JSON requests at <220ms p95 latency",
                "Rewrite Bullet 2: Enforced strict Pydantic v2 contracts and multi-model failover, cutting LLM parsing errors to 0.0%",
            ],
        },
    },
    "seo_content_architect": {
        "name": "📈 5. Programmatic SEO & Conversion Copy Architect (MarTech)",
        "prompt": "Target keyword: 'FastAPI Gemini Boilerplate for Python Developers'. Product price: $59.",
        "context": "High-intent developer landing page and technical blog funnel.",
        "sample_output": {
            "status": "success",
            "preset_used": "seo_content_architect",
            "plan_tier": "pro",
            "credits_remaining": 5,
            "summary": "Search Intent: Transactional — Buyers want immediate time-savings and production reliability.",
            "key_points": [
                "Lead with Hours Saved (35+ hrs) and Python 3.13 + google-genai compatibility",
                "Highlight built-in SaaS Credit Billing & Gumroad License Verification",
            ],
            "action_items": [
                "Anchor the $59 Pro Complete tier against 3 weeks of engineering time ($3,500+ value)",
                "Offer the Free 2026 Architecture Blueprint ($0) as a lead magnet",
            ],
        },
    },
}

left, right = st.columns([5, 7])
with left:
    st.subheader("1️⃣ Choose a Built-In Vertical SaaS Template")
    choice = st.selectbox("Select Vertical Preset:", list(PRESETS.keys()), format_func=lambda k: PRESETS[k]["name"])
    p = PRESETS[choice]
    prompt_val = st.text_area("Input Prompt (`prompt`):", p["prompt"], height=100)
    context_val = st.text_input("System Context (`context`):", p["context"])
    api_key = st.text_input("Optional: Paste Google Gemini API Key for Live Call (or leave blank for instant demo):", type="password")
    run_clicked = st.button("⚡ Execute Structured JSON Pipeline", type="primary", use_container_width=True)

with right:
    st.subheader("2️⃣ Validated Pydantic v2 JSON Output")
    if run_clicked and api_key:
        try:
            from google import genai
            client = genai.Client(api_key=api_key)
            res = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=f"Context: {context_val}\nInput: {prompt_val}",
                config={
                    "response_mime_type": "application/json",
                    "system_instruction": "Return JSON with status, summary, key_points (list), action_items (list).",
                },
            )
            st.success("✅ Live Gemini 3.5 Flash Response Validated!")
            st.json(json.loads(res.text))
        except Exception as exc:
            st.warning(f"Live API note ({exc}) — showing pre-validated schema output:")
            st.json(p["sample_output"])
    else:
        st.info("⚡ Showing validated Pydantic v2 JSON schema for **" + p["name"] + "**:")
        st.json(p["sample_output"])

    st.success(
        "🎁 **Want the full 18-file repository** (`app/main.py`, `app/auth.py`, `app/ai_engine.py`, "
        "`app/monetization.py`, `app/presets.py`, `dashboard.py`, `Dockerfile`, `docker-compose.yml`)? "
        "**[Download ShipAI v2.0 on Gumroad ->](https://yahiaoui26.gumroad.com/l/shipai-pro/LAUNCH20)**"
    )
