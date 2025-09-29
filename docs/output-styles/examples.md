# Usage Examples

See professional output styles in action with real-world scenarios.

## 💼 Business & Strategy Examples

### Strategic Consultant: Market Expansion Analysis

**Prompt**: "Should our B2B SaaS company expand into the European market?"

**Response**:

```text
**Executive Summary**:
- European expansion presents €18M opportunity with 24-month ROI
- Regulatory complexity requires staged entry via UK/Germany
- Recommend partnership model over direct expansion

**Situation Analysis (Porter's Five Forces)**:
- **Competitive Intensity**: Medium (3 established players, fragmented market)
- **Supplier Power**: Low (abundant cloud infrastructure)
- **Buyer Power**: Medium-High (enterprise procurement processes)
- **Substitution Threat**: Medium (on-premise alternatives declining)
- **Entry Barriers**: Medium (GDPR compliance, localization required)

**Strategic Options**:
1. **Direct Expansion**: €25M investment, high risk/reward, 36-month break-even
2. **Partnership Model**: €8M investment, moderate risk, 18-month break-even
3. **Acquisition Strategy**: €15M investment, faster entry, 24-month break-even

**Recommended Action**: Partnership model with tier-1 markets (UK, Germany, Netherlands)

**Implementation Roadmap**:
- Q1: Partner identification and due diligence
- Q2: Partnership agreements and GDPR compliance
- Q3: Localized product launch in UK
- Q4: Expansion to Germany and Netherlands

**Confidence Assessment**: 8/10 (based on market research and competitive analysis)
```

### Product Manager: Feature Prioritization

**Prompt**: "Help prioritize our mobile app feature backlog"

**Response**:

```text
**Problem Statement**: Mobile app backlog contains 12 features without clear prioritization framework, impacting sprint planning and resource allocation.

**Recommended Framework**: RICE scoring (Reach × Impact × Confidence ÷ Effort)

**Top 5 Priorities**:
1. **Push Notifications** (RICE: 450)
   - Reach: 10,000 users, Impact: 3, Confidence: 90%, Effort: 3
   - User story: "As a user, I want push notifications so I don't miss important updates"

2. **Offline Mode** (RICE: 320)
   - Reach: 8,000 users, Impact: 4, Confidence: 80%, Effort: 8
   - User story: "As a mobile user, I want offline access so I can work without connectivity"

3. **Dark Mode** (RICE: 280)
   - Reach: 7,000 users, Impact: 2, Confidence: 95%, Effort: 2
   - User story: "As a user, I want dark mode so I can reduce eye strain"

**Implementation Strategy**:
- **Sprint 1-2**: Push notifications with segmentation
- **Sprint 3-5**: Offline mode MVP with core features
- **Sprint 6**: Dark mode UI implementation

**Success Metrics**:
- Push notification engagement: >25% click-through rate
- Offline mode adoption: >40% of users within 30 days
- Dark mode usage: >60% of users switch within first week

**Confidence Level**: 7/10 (based on user research and technical feasibility analysis)
```

## 🔧 Technical & Analysis Examples

### Data Scientist: A/B Test Analysis

**Prompt**: "Analyze our signup form A/B test results"

**Response**:

```text
**Hypothesis**: Simplified signup form (Version B) will increase conversion rate compared to detailed form (Version A).

**Data Overview**:
- Sample size: 2,847 visitors (A: 1,423, B: 1,424)
- Test duration: 14 days
- Primary metric: Signup conversion rate
- Secondary metrics: Form completion time, abandonment rate

**Statistical Analysis**:
- **Version A**: 127 conversions, 8.93% conversion rate
- **Version B**: 156 conversions, 10.96% conversion rate
- **Difference**: +2.03 percentage points (+22.7% relative improvement)
- **Statistical significance**: p < 0.05, 95% confidence interval: [0.4%, 3.7%]
- **Statistical power**: 82% (adequate for decision-making)

**Secondary Findings**:
- Form completion time: B averaged 34% faster (2.1 min vs 3.2 min)
- Abandonment rate: B had 28% lower abandonment (15% vs 21%)
- Quality of signups: No significant difference in activation rates

**Business Impact**:
- Expected monthly conversion increase: +47 signups
- Estimated monthly revenue impact: +$2,350 (based on $50 LTV)
- Annual revenue potential: +$28,200

**Recommendation**: Deploy Version B immediately. Monitor activation rates for 30 days to confirm signup quality remains consistent.

**Confidence Level**: 9/10 (high statistical significance and consistent secondary metrics)
```

### Technical Writer: API Documentation

**Prompt**: "Document our user authentication API endpoint"

**Response**:

```text
# User Authentication API

Authenticate users and retrieve access tokens for API requests.

## Prerequisites

- Valid API key (obtain from [Developer Dashboard](link))
- User must have active account status
- HTTPS required for all authentication requests

## Endpoint

```http
POST /api/v1/auth/login
```

## Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `email` | string | Yes | User's registered email address |
| `password` | string | Yes | User's account password |
| `remember_me` | boolean | No | Extend token expiration to 30 days (default: 24 hours) |

## Request Example

```json
{
  "email": "user@example.com",
  "password": "securePassword123",
  "remember_me": true
}
```

## Response Format

### Success Response (200 OK)

```json
{
  "status": "success",
  "data": {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "Bearer",
    "expires_in": 86400,
    "user": {
      "id": 12345,
      "email": "user@example.com",
      "name": "John Doe",
      "role": "user"
    }
  }
}
```

### Error Response (401 Unauthorized)

```json
{
  "status": "error",
  "message": "Invalid email or password",
  "code": "AUTH_INVALID_CREDENTIALS"
}
```

## Using the Access Token

Include the token in the Authorization header for subsequent requests:

```text
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

## Error Codes

| Code | Description | Solution |
|------|-------------|----------|
| `AUTH_INVALID_CREDENTIALS` | Email/password incorrect | Verify credentials |
| `AUTH_ACCOUNT_LOCKED` | Account temporarily locked | Contact support |
| `AUTH_RATE_LIMITED` | Too many login attempts | Wait 15 minutes |

## Next Steps

- [Using Access Tokens](tokens.md)
- [API Rate Limits](rate-limits.md)
- [Error Handling Best Practices](error-handling.md)

## 🎨 Creative & Design Examples

### UX Researcher: User Journey Analysis

**Prompt**: "Analyze the user onboarding journey for our mobile app"

**Response**:

```text
**Research Objective**: Identify friction points in mobile app onboarding that impact user activation and retention.

**Methodology**:
- User session recordings analysis (n=150)
- Post-onboarding surveys (n=89)
- Heuristic evaluation using Nielsen's principles
- Task completion time measurement

**User Journey Mapping**:

**Stage 1: App Download → First Launch**
- **Touchpoints**: App store, splash screen, permissions requests
- **User Goal**: Understand app value and start using features
- **Pain Points**: 3 permission requests create friction (camera, notifications, location)
- **Drop-off Rate**: 15% abandon after permission requests

**Stage 2: Account Creation**
- **Touchpoints**: Signup form, email verification, profile setup
- **User Goal**: Create account with minimal effort
- **Pain Points**: Email verification required before app usage, 6-field form too long
- **Drop-off Rate**: 22% abandon during signup process

**Stage 3: Core Feature Discovery**
- **Touchpoints**: Feature tour, empty states, first-use prompts
- **User Goal**: Understand primary app functionality
- **Pain Points**: Feature tour skipped by 67% of users, unclear value proposition
- **Completion Rate**: Only 45% complete initial feature setup

**Key Findings**:
1. **Permission Fatigue**: Sequential permission requests create early abandonment
2. **Verification Friction**: Email verification blocks immediate value demonstration
3. **Feature Overwhelm**: 8-step tutorial provides too much information upfront
4. **Value Gap**: 34% of users unclear on primary app benefit after onboarding

**Recommendations** (Priority: High → Medium → Low):

**High Priority**:
- Implement progressive permission requests (request when feature needed)
- Allow app usage before email verification with gentle prompts
- Reduce tutorial to 3 core steps with contextual help available

**Medium Priority**:
- Add interactive onboarding elements (progressive disclosure)
- Implement smart defaults based on user type detection
- Create personalized onboarding paths for different user segments

**Low Priority**:
- A/B test social login options (Google, Apple)
- Add gamification elements to onboarding completion
- Implement onboarding analytics dashboard for ongoing optimization

**Success Metrics**:
- Increase Day 1 retention from 68% to 80%
- Reduce onboarding abandonment from 37% to 25%
- Improve feature adoption rate from 45% to 65%

**Confidence Level**: 8/10 (based on substantial user research data and established UX principles)
```

## ⚙️ Operations & Compliance Examples

### Project Coordinator: Implementation Planning

**Prompt**: "Plan the implementation of our new customer portal feature"

**Response**:

```text
**Project Overview**: Customer Portal Implementation
- **Scope**: Self-service portal with account management, billing, and support ticketing
- **Timeline**: 12 weeks from kickoff to production launch
- **Team**: 8 members across engineering, design, QA, and product

**Work Breakdown Structure**:

**Phase 1: Foundation (Weeks 1-3)**
1.1 Requirements gathering and validation (5 days)
1.2 Technical architecture design (8 days)
1.3 UI/UX design and prototyping (10 days)
1.4 Database schema design (3 days)
1.5 Development environment setup (2 days)

**Phase 2: Core Development (Weeks 4-8)**
2.1 Authentication system integration (8 days)
2.2 Account management features (12 days)
2.3 Billing interface development (10 days)
2.4 Support ticket system (8 days)
2.5 Frontend component development (15 days)

**Phase 3: Integration & Testing (Weeks 9-11)**
3.1 Backend API integration (5 days)
3.2 Security testing and compliance review (8 days)
3.3 User acceptance testing (10 days)
3.4 Performance optimization (5 days)
3.5 Documentation and training materials (5 days)

**Phase 4: Launch (Week 12)**
4.1 Production deployment preparation (2 days)
4.2 Soft launch with beta users (3 days)
4.3 Full production launch and monitoring (2 days)

**Dependencies & Critical Path**:
- **Critical Path**: Requirements → Architecture → Core Development → Testing → Launch
- **External Dependencies**:
  - Payment gateway API integration (Week 5)
  - Legal review of terms and privacy policy (Week 9)
  - Customer support training completion (Week 11)

**Resource Allocation**:
- **Frontend Developer** (2): 80% allocation, Weeks 2-10
- **Backend Developer** (2): 90% allocation, Weeks 1-11
- **UI/UX Designer** (1): 60% allocation, Weeks 1-8
- **QA Engineer** (1): 70% allocation, Weeks 6-12
- **Product Manager** (1): 50% allocation, Weeks 1-12
- **DevOps Engineer** (1): 30% allocation, Weeks 10-12

**Risk Assessment & Mitigation**:

**High Risk**:
- Payment integration complexity → Start integration early, allocate buffer time
- Security compliance requirements → Engage security team early in design phase

**Medium Risk**:
- Scope creep from stakeholders → Lock requirements after Week 2, change control process
- Resource availability conflicts → Confirm team allocation commitments upfront

**Low Risk**:
- Third-party API rate limits → Implement caching and fallback strategies

**Success Metrics**:
- **Schedule**: Launch within 12-week timeline (±1 week acceptable)
- **Quality**: <5 critical bugs in first month post-launch
- **Adoption**: 30% of customers use portal within 60 days
- **Performance**: Portal loads in <2 seconds for 95th percentile

**Communication Plan**:
- **Daily standups**: Development team progress sync
- **Weekly stakeholder updates**: Progress, risks, and blockers
- **Bi-weekly steering committee**: Go/no-go decisions and resource allocation

**Confidence Level**: 7/10 (based on similar project experiences, confirmed resource availability)
```

## 🔄 Style Switching Example

### Multi-Perspective Analysis

**Scenario**: "Our SaaS product has declining user engagement. How should we address this?"

**Strategic Consultant Perspective**:

```bash
/output-style strategic-consultant
```

```text
**Executive Summary**: User engagement decline indicates potential product-market fit erosion requiring strategic intervention.

**Root Cause Analysis**:
- Market maturation reducing novelty factor
- Competitive pressure from new entrants
- Possible feature bloat affecting core value proposition

**Strategic Options**:
1. **Product Pivot**: Focus on highest-value use cases
2. **Market Expansion**: Target new customer segments
3. **Value Reinforcement**: Enhance core features and user education

**Recommendation**: Implement value reinforcement strategy with systematic user research to identify engagement drivers.
```

**Data Scientist Perspective**:

```bash
/output-style data-scientist
```

```text
**Hypothesis**: User engagement decline correlates with specific user segments, feature usage patterns, or external factors.

**Analysis Framework**:
- Cohort analysis to identify when decline started
- Feature usage correlation with engagement metrics
- User segmentation analysis by engagement levels

**Key Metrics to Investigate**:
- Daily/Monthly Active Users trend analysis
- Session duration and frequency changes
- Feature adoption rates by user cohort
- Churn prediction model inputs

**Recommended Approach**: Implement comprehensive analytics review with statistical significance testing to identify actionable insights.

**Confidence Level**: 6/10 (requires access to actual user data for validation)
```

**Product Manager Perspective**:

```bash
/output-style product-manager
```

```text
**Problem Statement**: User engagement metrics show consistent decline over past 3 months, impacting retention and revenue growth.

**User Impact Assessment**:
- Identify which user personas are most affected
- Map engagement decline to specific user journey stages
- Prioritize fixes based on impact on core business metrics

**Immediate Actions**:
1. Conduct user interviews with recently disengaged users
2. Analyze support tickets for common pain points
3. Review recent product changes that correlate with decline

**Success Metrics**:
- Increase DAU by 15% within 60 days
- Improve session duration by 20%
- Reduce churn rate by 10%

**Implementation Timeline**:
- Week 1-2: User research and data analysis
- Week 3-4: Solution prioritization and development planning
- Week 5-8: Implementation and testing
- Week 9-12: Launch and impact measurement

**Confidence Level**: 8/10 (based on established product improvement frameworks)
```

---

**💡 Style Switching Tip**: Use multiple perspectives on the same problem to ensure comprehensive
analysis and better decision-making. Each professional style reveals different aspects and solutions.
