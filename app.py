import streamlit as st
import json
import sys
sys.path.insert(0, ".")
from rank import score_candidate, JD, W

st.set_page_config(page_title="India.Runs Candidate Ranker", page_icon="🤖")

st.title("🤖 AI Candidate Ranking System")
st.caption("India.Runs — Redrob x Hack2Skill")

st.markdown("### Paste a candidate JSON to score them")

sample = json.dumps({
  "candidate_id": "CAND_TEST_001",
  "profile": {
    "current_title": "ML Engineer",
    "years_of_experience": 6.5,
    "location": "Bangalore",
    "country": "india"
  },
  "skills": [
    {"name": "pytorch", "proficiency": "advanced", "duration_months": 36, "endorsements": 12},
    {"name": "embeddings", "proficiency": "expert", "duration_months": 24, "endorsements": 8}
  ],
  "career_history": [
    {"company": "swiggy", "duration_months": 30, "is_current": True,
     "start_date": "2022-01-01", "description": "built recommendation and ranking systems"}
  ],
  "education": [
    {"tier": "tier_1", "field_of_study": "computer science"}
  ],
  "redrob_signals": {
    "open_to_work_flag": True,
    "recruiter_response_rate": 0.85,
    "profile_completeness_score": 90,
    "last_active_date": "2026-06-01",
    "notice_period_days": 30,
    "github_activity_score": 72,
    "verified_email": True,
    "verified_phone": True,
    "linkedin_connected": True,
    "interview_completion_rate": 0.9,
    "avg_response_time_hours": 4
  }
}, indent=2)

user_input = st.text_area("Candidate JSON", value=sample, height=350)

if st.button("🚀 Score Candidate"):
    try:
        candidate = json.loads(user_input)
        result = score_candidate(candidate)

        st.success(f"### Score: `{result['score']}`")
        st.markdown(f"**Reasoning:** {result['reasoning']}")

        st.markdown("### Component Breakdown")
        for k, v in result["components"].items():
            st.progress(v, text=f"{k.capitalize():<12} {v:.2f}  (weight: {W[k]:.0%})")

    except Exception as e:
        st.error(f"Error: {e}")

st.divider()
st.markdown("**Scoring Weights:** Skills 32% · Career 25% · Experience 15% · Behavioral 18% · Education 5% · Location 5%")