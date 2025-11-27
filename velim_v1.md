# Velim: The Entity Intent Protocol

**“Wish, and let the world find you.”**  
**“Together, we shape the world through our intentions.”**

## Abstract
Velim is a chain-agnostic, agent-native protocol enabling any entity—individuals, organizations, communities, or AI agents—to publish structured intent-signals. These signals express wishes, capabilities, collaboration interests, and resource needs. Anchored through chain-agnostic attestations, Velim transforms discovery by enabling agents and organizations to match based on compatibility instead of scraping or noise-filled lead lists.

Velim proposes a new economic layer—the **Intent Economy**—where expressing intention becomes infrastructure for efficient global coordination.

## 1. Introduction & Vision
We believe the world becomes better when every entity can express what it wants, what it seeks, and what it hopes to create. By weaving these intentions together across companies, communities, individuals, and AI agents, Velim enables a world where discovery is effortless and collaboration emerges naturally.

Velim creates infrastructure where wishes become signals, signals become connections, and connections shape a better world.

## 2. Problem Statement

### 2.1 Discovery Today is Noisy and Expensive
Modern discovery systems rely heavily on:
- Paid lead generation tools  
- Scraped contact databases  
- Sales development representatives  
- Manual research  
- Trade events and conferences  
- PR noise and hype

### Market Facts
- Global B2B lead generation services market: **$7–10B+ annually**  
  - Source: [Market Research Future](https://www.marketresearchfuture.com/reports/b2b-lead-generation-market-26577)
- Cost per B2B lead: **$200–$400+**  
  - Source: [Expandi CPL Benchmarks](https://expandi.io/blog/how-much-does-lead-generation-cost)
- **69%** of companies plan to increase their lead-gen spending  
  - Source: [Digital Silk Lead-Gen Stats](https://www.digitalsilk.com/digital-trends/lead-generation-statistics)
- Event marketing: **$26B+/year**  
- PR industry: **$113B+/year**

Despite massive spending, data quality remains poor and outdated.

## 3. Velim: The Entity Intent Protocol
Velim replaces outdated discovery with a standardized, verifiable, agent-native intent graph.

### Key Features
- Self-declared, structured intent-signals  
- Agent-native profiles  
- Chain-agnostic attestations  
- Incentives for accurate and active participation  
- Matching and alignment built into protocol logic  

Velim works for all entity types, not just corporations.

## 4. Core Concepts

### 4.1 Intent-Signals (“Wishes”)
A wish is a structured expression of what an entity wants.  
Examples:
- “Seeking sustainable packaging partners”  
- “Looking for HR-tech API collaborators”  
- “Agent wants research datasets under license X”  
- “Community seeking game developers”  

### 4.2 Entity Profiles
Entities verify identity using:
- Domain verification  
- Multi-step org checks  
- Identity proofs  
- Optional audits  

### 4.3 Agent-Native Interface
Entities deploy agents that:
- Update profiles  
- Respond to discovery queries  
- Negotiate and schedule  
- Learn preferences over time  

### 4.4 Chain-Agnostic Attestations
Velim works with any blockchain supporting:
- Timestamp anchoring  
- Attestation registries  
- Identity frameworks  

No dependency on Ethereum or any specific chain.

## 5. Incentive Model

### 5.1 Query Economics
If Velim’s discovery cost < traditional lead-gen cost, adoption is immediate.

### 5.2 How Entities Earn
Entities earn through:
- Maintaining accurate profiles  
- Participating in intro or discovery calls  
- Collaborations initiated through Velim  
- Agent responsiveness  
- Verification and consistency badges  

### 5.3 Reward Types
- Reputation badges  
- Reliability ranking  
- Priority matching  
- Token/credit incentives (optional)  

## 6. Reliability, Verification & Optional Audit Layers

### Reliability Scoring Factors
- Update cadence  
- Response rate  
- Accuracy  
- Collaboration follow-through  

### Verification Layers
- Self-attestation  
- Community validation  
- Third-party audit (optional “blue checkmark”)  

## 7. Network Bootstrapping

### 7.1 Phase 1: Early Community
Velim invites early startups, creators, nonprofits, open-source groups:
- Free discovery  
- High visibility  
- Claimable profiles  
- Early rewards  

### 7.2 Phase 2: Public Profile Seeding
Velim generates “ghost profiles” using public corporate and organizational records:
- Business registries  
- Conference exhibitor lists  
- Public directories  
- Websites  
- Open-source maintainers  

Entities can **claim and correct** their profiles.

### 7.3 Phase 3: DAO Governance
The Velim DAO standardizes:
- Intent schema  
- Verification rules  
- Reputation algorithms  
- Incentive curves  
- Grants for ecosystem builders  

### 7.4 Phase 4: Agent Ecosystem
Velim becomes an intent layer for:
- AI agents  
- Multi-agent workflows  
- Autonomous business operations  

## 8. Market Opportunity

- B2B lead-gen market: **$7–10B+**  
- CPL: **$200–$400+**  
- PR spend: **$113B/y**  
- Event-based marketing: **$26B+/y**

Even a 5–10% reduction or a 2–3× improvement in match relevancy creates massive economic value.

## 9. Technical Architecture

1. **Intent Schema** – defines wish structure  
2. **Attestation Registry** – anchors statements  
3. **Profile Graph** – decentralized relationship graph  
4. **Discovery Engine** – matching logic  
5. **Agent Layer** – LLM/agent APIs  
6. **Reputation Engine** – scoring + badges  
7. **Governance Layer** – DAO / consortium standards

---

## 10. Protocol Specifications

### 10.1 Intent Schema Specification

#### 10.1.1 Core Intent Structure

See [`schemas/intent-schema.json`](./schemas/intent-schema.json) for the complete JSON schema definition.

**Key Fields:**
- `intent_id` - UUID v4 unique identifier
- `entity_id` - DID of the entity creating the intent
- `type` - seeking | offering | collaboration | announcement
- `visibility` - Controls who can discover this intent
- `content` - Title, description, tags, and location
- `requirements` - Must-haves, nice-to-haves, and deal-breakers
- `constraints` - Budget, timeline, and capacity constraints
- `matching_preferences` - Criteria for potential matches
- `attestation` - Chain-agnostic attestation proof

#### 10.1.2 Entity Profile Structure

See [`schemas/entity-profile-schema.json`](./schemas/entity-profile-schema.json) for the complete JSON schema definition.

**Key Sections:**
- `identity` - Name, bio, website, social links
- `verification` - Verification status, methods, and badges
- `capabilities` - Offerings, expertise, resources, availability
- `reputation` - Velim score, component scores, statistics, endorsements
- `agent_interface` - Agent API endpoint and capabilities
- `privacy_settings` - Visibility and contact preferences

**Entity Types:** individual | organization | community | agent | hybrid
  


### 10.2 Attestation Protocol

#### 10.2.1 Chain-Agnostic Attestation Interface
Velim supports multiple attestation backends through a unified interface:

**Core Attestation Methods:**
- `createAttestation(subject, claim, proof) → attestation_id`
- `verifyAttestation(attestation_id) → boolean + metadata`
- `revokeAttestation(attestation_id, reason) → boolean`
- `queryAttestations(filters) → array of attestations`

**Supported Chains:**
1. **Ethereum/EVM-compatible**
   - Uses EAS (Ethereum Attestation Service) or similar
   - Schema registry on-chain
   - Off-chain attestations with on-chain anchors

2. **Arweave/Permaweb**
   - Permanent storage for attestations
   - GraphQL query interface
   - Content-addressed verification

3. **IPFS + Content Addressing**
   - Decentralized content storage
   - CID-based verification
   - Pin services for availability

4. **Solana**
   - Program-based attestation storage
   - High-speed verification
   - Low-cost anchoring

5. **Custom/Enterprise Chains**
   - Adapter pattern for integration
   - Minimum requirements: timestamp, signature, immutability

#### 10.2.2 Attestation Schema

See [`schemas/attestation-schema.json`](./schemas/attestation-schema.json) for the complete schema.

**Attestation Claim Types:**
- `IDENTITY_VERIFICATION` - Verified identity
- `DOMAIN_OWNERSHIP` - Domain ownership proof
- `INTENT_PUBLICATION` - Intent published and attested
- `COLLABORATION_COMPLETION` - Successful collaboration
- `ENDORSEMENT` - Peer endorsement
- `AUDIT_CERTIFICATION` - Third-party audit
- `REPUTATION_SCORE` - Reputation snapshot
- `PROFILE_UPDATE` - Profile change attestation

### 10.3 Discovery & Matching Engine

#### 10.3.1 Matching Algorithm
The Velim matching engine uses multi-dimensional compatibility scoring:

**Scoring Components:**
1. **Semantic Similarity** (35% weight)
   - NLP embeddings of intent descriptions
   - Tag overlap analysis
   - Category alignment

2. **Constraint Compatibility** (25% weight)
   - Budget range overlap
   - Timeline feasibility
   - Location compatibility
   - Capacity matching

3. **Reputation Alignment** (20% weight)
   - Reputation score proximity
   - Verification level matching
   - Historical success rate with similar entities

4. **Network Effects** (10% weight)
   - Mutual connections
   - Past successful collaborations
   - Common network participants

5. **Behavioral Signals** (10% weight)
   - Response time compatibility
   - Communication style matching
   - Update frequency alignment

**Match Score Formula:**
```
match_score = (
  0.35 × semantic_similarity +
  0.25 × constraint_compatibility +
  0.20 × reputation_alignment +
  0.10 × network_effects +
  0.10 × behavioral_signals
) × freshness_decay × verification_multiplier
```

Where:
- `freshness_decay = exp(-λ × days_since_update)` with λ = 0.05
- `verification_multiplier = 1.0 + (0.2 × verification_level / 5)`

#### 10.3.2 Discovery API Endpoints

**Search Intents:**

See [`examples/api-search-request.json`](./examples/api-search-request.json) for request format and [`examples/api-search-response.json`](./examples/api-search-response.json) for response format.

```http
POST /api/v1/discovery/search
Content-Type: application/json
Authorization: Bearer {entity_jwt}
```

**Request Parameters:**
- `semantic` - Natural language query
- `filters` - Type, categories, location, budget, verification, reputation
- `preferences` - Limit, offset, sort order, agent reachability

**Response Fields:**
- `matches` - Array of matched intents with scores and reasons
- `total_results` - Total number of matching intents
- `search_id` - Cacheable search identifier

**Agent-to-Agent Discovery:**
```http
POST /api/v1/discovery/agent-query
Content-Type: application/json
Authorization: Bearer {agent_jwt}

{
  "query": {
    "intent_id": "uuid-of-your-intent",
    "discover_type": "potential_matches | complementary_capabilities | collaboration_opportunities",
    "constraints": {
      "max_matches": 20,
      "min_score": 0.75,
      "require_agent_interface": true
    }
  },
  "negotiation_params": {
    "auto_schedule": true,
    "propose_meeting": true,
    "exchange_context": true
  }
}
```

### 10.4 Agent Interface Protocol

#### 10.4.1 Agent API Specification
Entities expose agent endpoints for autonomous interaction:

**Standard Agent Endpoints:**

```http
# Agent Capability Discovery
GET /velim/agent/capabilities
Authorization: Bearer {caller_jwt}

Response:
{
  "version": "1.0.0",
  "supported_operations": [
    "intent_query",
    "profile_query",
    "schedule_meeting",
    "negotiate_terms",
    "status_update"
  ],
  "communication_modes": ["sync", "async", "streaming"],
  "response_sla": "2 hours",
  "availability": {
    "timezone": "America/Los_Angeles",
    "business_hours": "9-17 Mon-Fri"
  }
}
```

```http
# Query Entity Intent
POST /velim/agent/query-intent
Authorization: Bearer {caller_jwt}
Content-Type: application/json

{
  "query_type": "capabilities | availability | pricing | terms",
  "context": {
    "referencing_intent": "uuid",
    "requester_entity": "did:velim:entity-id",
    "specific_questions": ["array", "of", "questions"]
  }
}

Response:
{
  "response": "structured or natural language response",
  "confidence": 0.95,
  "requires_human_review": false,
  "follow_up_actions": [
    {
      "action": "schedule_call",
      "reason": "Technical deep-dive needed",
      "availability": ["time slots"]
    }
  ]
}
```

```http
# Agent-Initiated Contact
POST /velim/agent/initiate-contact
Authorization: Bearer {caller_jwt}
Content-Type: application/json

{
  "initiator": {
    "entity_id": "did:velim:entity-id",
    "intent_id": "uuid",
    "agent_id": "agent-identifier"
  },
  "target": {
    "entity_id": "did:velim:target-entity-id",
    "intent_id": "uuid"
  },
  "message": {
    "subject": "string",
    "body": "string",
    "structured_proposal": {
      "collaboration_type": "partnership | service | resource-exchange",
      "proposed_terms": { /* structured terms */ },
      "timeline": { /* structured timeline */ }
    }
  },
  "preferred_next_step": "meeting | async_discussion | document_exchange"
}
```

#### 10.4.2 Agent Authentication & Authorization
Agents authenticate using DIDs and JWT tokens:

```typescript
interface AgentJWT {
  iss: DID;           // Issuing entity
  sub: DID;           // Agent identity
  aud: string;        // Target service
  exp: number;        // Expiration
  iat: number;        // Issued at
  
  velim: {
    agent_version: string;
    capabilities: string[];
    delegation_scope: string[];
    parent_entity: DID;
  };
  
  proof: {
    algorithm: string;
    signature: string;
  };
}
```

**Authorization Scopes:**
- `profile:read` - Read entity profiles
- `intent:read` - Read public intents
- `intent:write` - Create/update intents
- `discovery:query` - Search and match
- `contact:initiate` - Reach out to entities
- `negotiate:terms` - Propose and discuss terms
- `calendar:schedule` - Schedule meetings
- `attestation:create` - Create attestations

### 10.5 Reputation Engine

#### 10.5.1 Reputation Calculation
```typescript
interface ReputationScore {
  overall_score: number;  // 0-100
  
  components: {
    responsiveness: {
      score: number;
      metrics: {
        average_response_time_hours: number;
        response_rate: number;  // 0-1
        sla_adherence: number;  // 0-1
      };
    };
    
    accuracy: {
      score: number;
      metrics: {
        profile_update_frequency_days: number;
        information_accuracy_rating: number;  // from verifications
        claimed_vs_delivered_ratio: number;
      };
    };
    
    collaboration_quality: {
      score: number;
      metrics: {
        successful_completions: number;
        partner_satisfaction: number;  // 0-5 from ratings
        dispute_rate: number;
        follow_through_rate: number;
      };
    };
    
    network_contribution: {
      score: number;
      metrics: {
        endorsements_given: number;
        endorsements_received: number;
        successful_introductions: number;
        community_participation: number;
      };
    };
    
    verification_strength: {
      score: number;
      metrics: {
        verification_level: number;  // 0-5
        attestation_count: number;
        audit_freshness_days: number;
        verification_diversity: number;  // number of different verifiers
      };
    };
  };
  
  badges: Badge[];
  trend: "improving" | "stable" | "declining";
  last_updated: ISO8601;
}
```

**Reputation Update Triggers:**
- Intent creation/update
- Response to discovery query
- Collaboration milestone
- Verification/attestation
- Endorsement received
- Time decay (weekly)

#### 10.5.2 Reputation Decay Function

See [`code/reputation-calculation.py`](./code/reputation-calculation.py) for the complete implementation.

Reputation decays with inactivity to incentivize engagement:
- **Decay rate:** 2% per week of inactivity
- **Minimum retention:** 50% of original score
- **Purpose:** Ensures active participation is rewarded

### 10.6 Data Persistence & Storage

#### 10.6.1 Hybrid Storage Architecture
Velim uses a hybrid approach:

**On-Chain/Attestation Layer:**
- Intent attestations (hashes + metadata)
- Profile verification proofs
- Reputation snapshots (periodic)
- Governance decisions

**Decentralized Storage (IPFS/Arweave):**
- Full intent content
- Entity profiles
- Rich media (images, documents)
- Historical data archives

**Centralized Cache/Index (Optional):**
- Fast query performance
- Full-text search indices
- Real-time matching
- Analytics and monitoring

**Entity-Controlled Storage:**
- Private intent drafts
- Internal notes and context
- Agent training data
- Communication logs

#### 10.6.2 Data Schemas & Versioning
```json
{
  "schema_version": "1.0.0",
  "backward_compatible": ["0.9.x"],
  "migration_path": {
    "from": "0.9.x",
    "to": "1.0.0",
    "automated": true,
    "migration_script": "ipfs://QmMigrationScript"
  },
  "deprecation": {
    "deprecated_fields": ["old_field_name"],
    "removal_date": "2026-12-31",
    "alternative": "new_field_name"
  }
}
```

### 10.7 Privacy & Security

#### 10.7.1 Privacy Controls
**Visibility Levels:**
- `public` - Discoverable by anyone, indexed
- `network` - Visible to verified entities only
- `private` - Invitation/permission required
- `agent-only` - No human UI access, agent-to-agent only

**Data Minimization:**
- Entities control which fields are public
- Selective disclosure of capabilities
- Tiered information release (summary → details → full access)

**Privacy-Preserving Matching:**
- Encrypted intent matching (optional)
- Zero-knowledge proofs for sensitive criteria
- Homomorphic encryption for budget/financials (future)

#### 10.7.2 Security Measures
**Authentication:**
- DID-based authentication
- Multi-factor authentication for high-value operations
- Agent key rotation policies

**Authorization:**
- Role-based access control (RBAC)
- Capability-based security for agents
- Rate limiting and abuse prevention

**Data Integrity:**
- Cryptographic signatures on all attested data
- Merkle proofs for data inclusion
- Tamper-evident logs

**Audit Trail:**
- All profile changes logged
- Intent modifications tracked
- Access patterns monitored
- Suspicious activity detection

### 10.8 API Rate Limits & Economics

#### 10.8.1 Rate Limits
| Operation | Free Tier | Verified Entity | Premium |
|-----------|-----------|-----------------|---------|
| Profile reads | 1000/day | 10,000/day | Unlimited |
| Intent searches | 100/day | 1,000/day | Unlimited |
| Intent publications | 10/month | 100/month | Unlimited |
| Agent queries | 500/day | 5,000/day | Unlimited |
| Attestation creation | 20/month | 200/month | Unlimited |

#### 10.8.2 Economic Model
**Free Operations:**
- Profile creation and claiming
- Basic intent publication
- Public discovery queries
- Community participation

**Paid Operations (Optional):**
- Premium visibility boost
- Advanced matching algorithms
- Priority agent response
- Audit services
- Analytics and insights
- White-label deployment

**Token Incentives (Future):**
- Rewards for accurate profiles
- Incentives for successful matches
- Staking for reputation boost
- Governance participation

### 10.9 Interoperability Standards

#### 10.9.1 Standard Integrations
**Identity Standards:**
- W3C Decentralized Identifiers (DIDs)
- W3C Verifiable Credentials
- EIP-4361 Sign-In with Ethereum
- OAuth 2.0 / OpenID Connect

**Data Standards:**
- Schema.org vocabulary extensions
- JSON-LD for linked data
- ActivityPub for social interactions
- OpenAPI 3.1 for API documentation

**Blockchain Standards:**
- EIP-712 for typed data signing
- EIP-1271 for contract signatures
- BIP-32/44 for key derivation
- EAS (Ethereum Attestation Service)

### 10.10 Extensibility & Plugin Architecture

#### 10.10.1 Custom Intent Types
Developers can extend Velim with custom intent types:

```typescript
interface CustomIntentType {
  type_id: string;
  type_name: string;
  schema_version: string;
  
  extends: "base_intent";
  
  custom_fields: {
    field_name: {
      type: "string" | "number" | "boolean" | "object" | "array";
      required: boolean;
      validation: object;
      description: string;
    };
  };
  
  matching_logic: {
    custom_scoring: FunctionRef;
    required_capabilities: string[];
  };
  
  governance: {
    proposed_by: DID;
    approved_by_dao: boolean;
    activation_date: ISO8601;
  };
}
```

#### 10.10.2 Plugin System
```typescript
interface VelimPlugin {
  plugin_id: string;
  version: string;
  name: string;
  description: string;
  
  hooks: {
    on_intent_created?: Function;
    on_match_found?: Function;
    on_profile_updated?: Function;
    on_attestation_created?: Function;
  };
  
  api_extensions: {
    endpoints: APIEndpoint[];
    authentication: AuthConfig;
  };
  
  ui_components?: {
    profile_widgets: Component[];
    intent_forms: Component[];
    discovery_filters: Component[];
  };
}
```

---

## 11. Governance  

## 10. Governance
The Velim DAO governs:
- Standards  
- Incentives  
- Ecosystem funding  
- Verification & audit guidelines  
- Algorithmic updates  

---

## 11. Governance
The Velim DAO governs:
- Standards  
- Incentives  
- Ecosystem funding  
- Verification & audit guidelines  
- Algorithmic updates

### 11.1 Governance Structure

#### 11.1.1 DAO Composition
The Velim DAO consists of multiple stakeholder groups:

**Core Participants:**
- **Protocol Contributors** - Developers and maintainers
- **Entity Representatives** - Active platform users
- **Verifiers & Auditors** - Trusted verification providers
- **Economic Stakeholders** - Token holders (if applicable)
- **Agent Operators** - AI agent developers and operators

**Voting Weight Distribution:**
```
Protocol Contributors: 25%
Entity Representatives: 30%
Verifiers & Auditors: 15%
Economic Stakeholders: 20%
Agent Operators: 10%
```

#### 11.1.2 Governance Proposals
**Proposal Types:**

1. **Protocol Improvement Proposals (PIPs)**
   - Schema changes
   - New intent types
   - API modifications
   - Matching algorithm updates

2. **Economic Improvement Proposals (EIPs)**
   - Fee structures
   - Incentive mechanisms
   - Token economics (if applicable)

3. **Governance Parameter Proposals (GPPs)**
   - Voting thresholds
   - Stakeholder weights
   - Proposal timelines

4. **Ecosystem Fund Proposals (EFPs)**
   - Grant allocations
   - Builder programs
   - Marketing initiatives

**Proposal Lifecycle:**
```
Ideation → Community Discussion (7 days) → 
Formal Proposal (Review 7 days) → 
Voting Period (14 days) → 
Implementation (if approved)
```

#### 11.1.3 Voting Mechanisms
**Quadratic Voting** for fair representation:
```
voting_power = sqrt(stake) × category_weight
```

**Conviction Voting** for continuous funding decisions

**Multi-Signature** for critical protocol changes (requires 6 of 9 signers)

### 11.2 Standards Governance

#### 11.2.1 Schema Evolution Process
1. **Proposal Stage** - Community member proposes schema change
2. **Impact Analysis** - Technical committee assesses breaking changes
3. **Migration Planning** - Automated migration path defined
4. **Community Vote** - 60% approval threshold
5. **Staged Rollout** - Testnet → Limited mainnet → Full deployment

#### 11.2.2 Verification Standard Updates
**Verification Level Criteria (Reviewed Annually):**
- Level 0: Unverified
- Level 1: Email/social verification
- Level 2: Domain ownership
- Level 3: Legal entity verification
- Level 4: Community endorsements (5+)
- Level 5: Third-party audit certification

### 11.3 Dispute Resolution

#### 11.3.1 Dispute Categories
- **Identity Disputes** - Claimed profile ownership conflicts
- **Attestation Challenges** - Questioning validity of attestations
- **Reputation Disputes** - Contesting reputation scores
- **Collaboration Disputes** - Failed partnerships/agreements

#### 11.3.2 Resolution Process
```
1. Informal Resolution (7 days) - Parties attempt direct resolution
2. Community Mediation (14 days) - Neutral mediators appointed
3. DAO Arbitration (30 days) - Formal case review and binding decision
4. Appeal Process (final, 14 days) - Limited appeal rights
```

**Evidence Requirements:**
- Timestamped communications
- Attestation proofs
- Third-party verification
- On-chain transaction records

### 11.4 Treasury Management

**Treasury Sources:**
- Protocol fees (if applicable)
- Grants and donations
- Partnership revenues
- Ecosystem services

**Treasury Allocation:**
```
Protocol Development: 40%
Ecosystem Grants: 25%
Operations: 15%
Security Audits: 10%
Community Incentives: 10%
```

**Multi-Sig Treasury Control:**
- Requires 5 of 8 signatures for transactions > $50k
- Quarterly budget approved by DAO
- Monthly transparency reports

---

## 12. Implementation Roadmap

### Phase 1: Foundation (Months 1-4)
**Technical Milestones:**
- [ ] Core intent schema v1.0 specification
- [ ] Entity profile data structures
- [ ] Basic attestation protocol (Ethereum + IPFS)
- [ ] Simple discovery API
- [ ] CLI tools for developers

**Community Milestones:**
- [ ] Launch developer documentation
- [ ] Onboard 100 early entities
- [ ] Establish technical working groups
- [ ] Release testnet

**Deliverables:**
- Intent SDK (TypeScript/Python)
- Reference implementation
- Developer portal
- Testnet explorer

### Phase 2: Discovery Engine (Months 5-8)
**Technical Milestones:**
- [ ] Semantic matching algorithm v1.0
- [ ] Reputation engine implementation
- [ ] Multi-chain attestation support
- [ ] Agent API specification
- [ ] Privacy controls

**Community Milestones:**
- [ ] Onboard 1,000+ entities
- [ ] Launch verification partner program
- [ ] Host first Velim Builder Summit
- [ ] Mainnet beta launch

**Deliverables:**
- Production-ready matching engine
- Web dashboard for entities
- Mobile apps (iOS/Android)
- Agent SDK

### Phase 3: Agent Ecosystem (Months 9-12)
**Technical Milestones:**
- [ ] Agent-to-agent protocol
- [ ] Autonomous negotiation framework
- [ ] Advanced privacy features (ZK proofs)
- [ ] Analytics and insights platform
- [ ] Plugin architecture

**Community Milestones:**
- [ ] Onboard 10+ AI agent platforms
- [ ] Launch DAO governance
- [ ] 10,000+ active entities
- [ ] First governance proposals

**Deliverables:**
- Agent marketplace
- Governance portal
- Advanced matching algorithms
- White-label solutions

### Phase 4: Scale & Optimize (Months 13-18)
**Technical Milestones:**
- [ ] Performance optimization (100k+ entities)
- [ ] Cross-protocol interoperability
- [ ] Enterprise features
- [ ] Advanced analytics
- [ ] Security hardening

**Community Milestones:**
- [ ] Global expansion (10+ languages)
- [ ] Industry-specific templates
- [ ] Partner integration program
- [ ] 100,000+ entities

**Deliverables:**
- Enterprise edition
- Industry plugins
- Advanced privacy tier
- Global CDN deployment

---

## 13. Technical Requirements

### 13.1 Infrastructure Requirements

**Minimum Node Specifications:**
- **CPU:** 4 cores (8+ recommended)
- **RAM:** 16 GB (32 GB+ recommended)
- **Storage:** 500 GB SSD (1 TB+ recommended)
- **Network:** 100 Mbps symmetric (1 Gbps recommended)
- **OS:** Linux (Ubuntu 22.04+, Debian 11+)

**Software Dependencies:**
- Docker 24.0+
- PostgreSQL 15+ or compatible database
- Redis 7.0+ for caching
- IPFS node or Pinata/Web3.Storage API
- Blockchain node access (or RPC provider)

### 13.2 Development Environment

**Required Tools:**
- Node.js 18+ or Python 3.10+
- TypeScript 5.0+
- Git 2.40+
- Docker Compose 2.0+

**Recommended Tools:**
- VS Code with Velim extension
- Postman/Insomnia for API testing
- Hardhat/Foundry for smart contracts
- k6 or Artillery for load testing

### 13.3 Security Requirements

**Minimum Security Standards:**
- TLS 1.3 for all communications
- AES-256 encryption at rest
- Ed25519 or ECDSA signatures
- Regular security audits (quarterly)
- Bug bounty program
- Incident response plan
- SOC 2 Type II compliance (enterprise tier)

**Key Management:**
- HSM for production keys
- Key rotation every 90 days
- Multi-party computation (MPC) for critical operations
- Social recovery mechanisms

---

## 14. Performance Benchmarks

### 14.1 Target Performance Metrics

**API Response Times (p95):**
- Profile lookup: < 100ms
- Intent search: < 500ms
- Match scoring: < 1s
- Attestation verification: < 200ms
- Agent query: < 2s

**Throughput:**
- Intent publications: 1,000/second
- Search queries: 10,000/second
- Profile updates: 500/second
- Attestation creations: 100/second

**Scalability Targets:**
- Support 1M+ entities
- Support 10M+ active intents
- Support 100M+ attestations
- Handle 100K+ concurrent users

### 14.2 Monitoring & Observability

**Key Metrics:**
- API latency percentiles (p50, p95, p99)
- Error rates by endpoint
- Attestation verification success rate
- Match quality scores
- Entity churn rate
- Agent adoption rate

**Monitoring Stack:**
- Prometheus for metrics
- Grafana for visualization
- Jaeger for distributed tracing
- ELK stack for log aggregation
- PagerDuty for alerting

---

## 15. Compliance & Legal

### 15.1 Data Protection
- **GDPR Compliance** - Right to erasure, data portability, consent management
- **CCPA Compliance** - California privacy requirements
- **Data Residency** - Configurable storage locations
- **Audit Logs** - Complete access and modification logs

### 15.2 Terms of Service Framework
**Entity Responsibilities:**
- Accurate profile information
- Lawful intent publication
- Respectful engagement
- Compliance with local regulations

**Platform Responsibilities:**
- Data protection and security
- Service availability (99.9% uptime SLA)
- Fair and transparent matching
- Dispute resolution support

### 15.3 Intellectual Property
- Protocol specifications: Open source (MIT/Apache 2.0)
- Reference implementations: Open source
- Velim trademark: Protected
- Plugin ecosystem: Permissive licensing

---

## 16. Economic Model Deep Dive

### 16.1 Value Capture Mechanisms

**For Entities:**
- **Reduced Discovery Costs** - 10-20× cheaper than traditional lead gen
- **Higher Match Quality** - 3-5× improvement in conversion rates
- **Time Savings** - 50-70% reduction in research time
- **Network Effects** - Value increases with participation

**For Verifiers:**
- **Verification Fees** - $50-$500 per verification
- **Audit Services** - $5,000-$50,000 per comprehensive audit
- **Reputation as a Service** - Recurring verification subscriptions

**For Agent Operators:**
- **Agent Marketplace Fees** - 10-20% of agent service value
- **Premium Features** - Advanced AI capabilities
- **White-Label Licensing** - Enterprise deployments

**For Protocol:**
- **Optional Platform Fees** - 1-5% on facilitated transactions
- **Premium Services** - Analytics, insights, priority support
- **Enterprise Licensing** - White-label and on-premise deployments

### 16.2 Cost Structure Analysis

**Traditional Lead Generation:**
```
CPL (Cost Per Lead): $200-$400
Conversion Rate: 2-5%
CAC (Customer Acquisition Cost): $4,000-$20,000
Time to Close: 3-9 months
```

**Velim Protocol:**
```
CPL (Cost Per Lead): $10-$40 (10-20× reduction)
Conversion Rate: 8-15% (3-5× improvement)
CAC: $800-$4,000 (5× reduction)
Time to Close: 1-4 months (2-3× faster)
```

**ROI Calculation:**
For a company spending $100,000/year on lead generation:
- Traditional: 250-500 leads → 5-25 conversions
- Velim: 2,500-10,000 leads → 200-1,500 conversions
- **ROI Improvement: 8-60×**

### 16.3 Incentive Design

**Entity Incentives:**
- **Profile Completeness Bonus** - Higher visibility for complete profiles
- **Response Time Rewards** - Priority matching for responsive entities
- **Successful Match Bonuses** - Rewards for completed collaborations
- **Community Contribution** - Points for endorsements, verifications

**Reputation Incentives:**
```python
def calculate_incentive_multiplier(entity: Entity) -> float:
    """
    Entities with higher reputation get better matches
    """
    base_multiplier = 1.0
    
    if entity.reputation_score >= 90:
        base_multiplier *= 1.5  # 50% boost
    elif entity.reputation_score >= 75:
        base_multiplier *= 1.25  # 25% boost
    elif entity.reputation_score >= 60:
        base_multiplier *= 1.1   # 10% boost
    
    if entity.verification_level >= 4:
        base_multiplier *= 1.3   # Verified entities
    
    if entity.response_time < 4:  # < 4 hours
        base_multiplier *= 1.2
    
    return base_multiplier
```

---

## 17. Risk Analysis & Mitigation

### 17.1 Technical Risks

**Risk: Spam and Low-Quality Intents**
- *Mitigation:* Reputation requirements, rate limiting, verification levels
- *Detection:* ML-based spam detection, community flagging
- *Response:* Graduated penalties, temporary suspension, permanent ban

**Risk: Centralization of Discovery**
- *Mitigation:* Decentralized attestations, open-source matching algorithms
- *Transparency:* Public algorithm audits, community governance
- *Competition:* Permissionless protocol, multiple frontend implementations

**Risk: Privacy Breaches**
- *Mitigation:* Encryption, access controls, privacy-preserving tech
- *Compliance:* Regular audits, penetration testing
- *Insurance:* Cyber liability coverage

**Risk: Blockchain Network Failures**
- *Mitigation:* Multi-chain support, fallback mechanisms
- *Redundancy:* Multiple attestation layers, cross-chain backups
- *Graceful Degradation:* System continues with cached data

### 17.2 Economic Risks

**Risk: Insufficient Adoption**
- *Mitigation:* Free tier, easy onboarding, clear value proposition
- *Growth Strategy:* Viral incentives, partnership programs
- *Validation:* Pilot programs with large organizations

**Risk: Market Timing**
- *Mitigation:* Phased rollout, adapt to market conditions
- *Flexibility:* Pivot capabilities based on traction
- *Resilience:* Sustainable runway, diversified funding

**Risk: Competition from Incumbents**
- *Mitigation:* Protocol advantage, open ecosystem, network effects
- *Differentiation:* Agent-native, chain-agnostic, incentive-aligned
- *Community:* Strong developer and entity relationships

### 17.3 Regulatory Risks

**Risk: Data Protection Regulations**
- *Mitigation:* Privacy-by-design, GDPR/CCPA compliance
- *Adaptability:* Modular architecture for regional requirements
- *Counsel:* Ongoing legal advisory

**Risk: Financial Regulations**
- *Mitigation:* Non-custodial, avoid securities classification
- *Clarity:* Work with regulators, clear documentation
- *Compliance:* KYC/AML for high-value transactions (if needed)

---

## 18. Success Metrics & KPIs

### 18.1 Protocol Health Metrics
- **Total Entities:** Target 1M in Year 3
- **Active Intents:** Target 5M in Year 3
- **Monthly Active Users:** Target 500K in Year 3
- **Attestations Created:** Target 50M in Year 3

### 18.2 Economic Metrics
- **Cost Savings vs. Traditional:** Target 10-20×
- **Match Quality Score:** Target > 0.75 average
- **Conversion Rate:** Target 10-15%
- **Time to Match:** Target < 48 hours

### 18.3 Community Metrics
- **Developer Adoption:** 1,000+ integrations
- **Agent Deployments:** 10,000+ active agents
- **Geographic Diversity:** 50+ countries
- **Verification Partners:** 100+ trusted verifiers

### 18.4 Network Effect Metrics
```
Metcalfe's Law Application:
Network Value = k × n²

Where:
k = value per connection
n = number of entities

At 1M entities with average k = $100:
Network Value = $100 × (1M)² = $100 Trillion (theoretical)

More realistically with sparse connections:
Average connections per entity = 50
Network Value = $100 × 1M × 50 = $5 Billion
```

---

## 19. Ethical Design
Principles:
- No forced disclosures  
- Privacy-first  
- Entity-controlled visibility  
- Incentives tied to reliable action, not hype  
- Chain-neutral  

---

## 19. Ethical Design & Risk Mitigation
Principles:
- No forced disclosures  
- Privacy-first  
- Entity-controlled visibility  
- Incentives tied to reliable action, not hype  
- Chain-neutral  

### 19.1 Ethical Principles

#### 19.1.1 Consent & Control
- **Explicit Consent:** All data sharing requires explicit opt-in
- **Granular Controls:** Entity control over every data field
- **Right to Delete:** Complete data deletion upon request
- **Data Portability:** Export all data in standard formats

#### 19.1.2 Fairness & Non-Discrimination
- **Algorithmic Fairness:** Regular audits of matching algorithms
- **No Bias:** Matching based on compatibility, not demographics
- **Equal Access:** Free tier ensures accessibility
- **Diversity Promotion:** Incentives for underrepresented entities

#### 19.1.3 Transparency
- **Open Algorithms:** Matching logic publicly documented
- **Explainable AI:** Clear reasoning for matches
- **Audit Trails:** Complete history of all changes
- **Governance Visibility:** Public DAO proceedings

#### 19.1.4 Sustainability
- **Energy Efficiency:** Prefer efficient blockchains
- **Carbon Offsetting:** Support green attestation providers
- **Long-term Thinking:** Protocol designed for decades, not quarters
- **Community Ownership:** Decentralized governance prevents extraction

### 19.2 Risk Mitigation Strategies

#### 19.2.1 Abuse Prevention

**Spam Protection:**

See [`code/spam-detection.py`](./code/spam-detection.py) for the spam detection implementation.

The spam detector assesses multiple signals:
- Creation velocity (rate limiting)
- Content quality (NLP analysis)
- Entity reputation
- Verification level
- Similarity to known spam
- Behavioral patterns

**Risk Levels:**
- HIGH_RISK (>0.8): Immediate action required
- MODERATE_RISK (>0.5): Enhanced monitoring
- LOW_RISK (≤0.5): Normal processing

**Rate Limiting:**
- Graduated limits based on reputation
- Temporary cooldowns for suspicious activity
- Permanent bans for repeated violations

**Content Moderation:**
- Automated filtering for prohibited content
- Community reporting mechanisms
- Human review for edge cases
- Appeals process for false positives

#### 19.2.2 Security Hardening
- **DDoS Protection:** Cloudflare or similar
- **API Security:** OAuth 2.0, rate limiting, input validation
- **Smart Contract Audits:** Trail of Bits, OpenZeppelin, Consensys Diligence
- **Penetration Testing:** Quarterly external audits
- **Bug Bounty:** $10K-$100K for critical vulnerabilities

#### 19.2.3 Data Integrity
- **Checksums:** All data includes integrity checks
- **Version Control:** Complete history of changes
- **Backup Strategy:** 3-2-1 backup rule (3 copies, 2 media types, 1 offsite)
- **Disaster Recovery:** RTO < 4 hours, RPO < 1 hour

---

## 20. Conclusion
Velim transforms global coordination by replacing noisy, outdated lead-gen with a verifiable, structured intent layer. It enables entities of all kinds—people, organizations, communities, AI agents—to express wishes, align interests, and discover each other more efficiently.

In Velim, **intention becomes infrastructure**.  
Wishes become signals.  
Signals become alignment.  
Alignment becomes a world shaped by what we choose to create—together.

---

## 20. Conclusion
Velim transforms global coordination by replacing noisy, outdated lead-gen with a verifiable, structured intent layer. It enables entities of all kinds—people, organizations, communities, AI agents—to express wishes, align interests, and discover each other more efficiently.

In Velim, **intention becomes infrastructure**.  
Wishes become signals.  
Signals become alignment.  
Alignment becomes a world shaped by what we choose to create—together.

### 20.1 Summary of Key Innovations

1. **Structured Intent-Signals** - Standardized, machine-readable expression of wants and capabilities
2. **Chain-Agnostic Attestations** - Verifiable claims without blockchain lock-in
3. **Agent-Native Protocol** - Built for AI agents from the ground up
4. **Incentive-Aligned Discovery** - Rewards accuracy and responsiveness
5. **Open Protocol** - Community-governed, permissionless innovation

### 20.2 The Path Forward

Velim represents a fundamental shift from centralized, extractive discovery platforms to an open, incentive-aligned protocol. By making intention infrastructure, we enable a future where:

- Discovery is effortless and accurate
- Collaboration emerges naturally from aligned interests
- Entities are rewarded for authenticity and reliability
- AI agents can autonomously find partnerships
- Global coordination happens at internet scale

**The world becomes better when every entity can express what it wants, what it seeks, and what it hopes to create.**

Velim is the infrastructure that makes this possible.

---

## 21. Appendices

### Appendix A: Glossary

**Agent** - An AI system that acts autonomously on behalf of an entity

**Attestation** - A cryptographically signed claim about an entity or intent

**Chain-Agnostic** - Compatible with multiple blockchain networks

**DID (Decentralized Identifier)** - A W3C standard for self-sovereign identity

**Entity** - Any participant in Velim: individual, organization, community, or agent

**Intent-Signal** - A structured expression of what an entity wants or offers

**Reputation Score** - A 0-100 metric of entity reliability and quality

**Verification Level** - A 0-5 scale indicating identity verification strength

**Wish** - Synonym for intent-signal, emphasizing the aspirational nature

### Appendix B: Technical Reference Links

**Standards & Specifications:**
- W3C DID Core: https://www.w3.org/TR/did-core/
- W3C Verifiable Credentials: https://www.w3.org/TR/vc-data-model/
- EAS (Ethereum Attestation Service): https://attest.sh/
- JSON-LD: https://json-ld.org/
- Schema.org: https://schema.org/

**Blockchain & Storage:**
- Arweave: https://www.arweave.org/
- IPFS: https://ipfs.tech/
- Ethereum: https://ethereum.org/
- Polygon: https://polygon.technology/

**Development Tools:**
- Velim SDK GitHub: https://github.com/velim-protocol/sdk
- API Documentation: https://docs.velim.io
- Developer Portal: https://developers.velim.io

### Appendix C: Intent Schema Examples

**Example 1: Startup Seeking Investment**

See [`examples/intent-seeking-investment.json`](./examples/intent-seeking-investment.json)

A Series A stage startup seeking AI/HR tech investors with $3M-$7M check size.

**Example 2: Enterprise Seeking Technology Partner**

See [`examples/intent-enterprise-partnership.json`](./examples/intent-enterprise-partnership.json)

Fortune 500 retail company seeking sustainable packaging solutions scalable to 10M+ units/month.

**Example 3: AI Agent Seeking Training Data**

See [`examples/intent-agent-data-seeking.json`](./examples/intent-agent-data-seeking.json)

AI research agent seeking 100K+ labeled medical images with HIPAA compliance and commercial licensing.

### Appendix D: Agent API Code Examples

**Python SDK - Publishing an Intent:**

See [`code/publish-intent.py`](./code/publish-intent.py) for the complete example.

```python
from velim import VelimClient, Intent

client = VelimClient(
    entity_id="did:velim:mycompany",
    private_key="your-private-key",
    network="mainnet"
)

intent = Intent(type="seeking", title="...", ...)
result = client.publish_intent(intent)
```

**TypeScript SDK - Discovering Matches:**

See [`code/discover-matches.ts`](./code/discover-matches.ts) for the complete example.

```typescript
import { VelimClient, DiscoveryQuery } from '@velim/sdk';

const client = new VelimClient({...});
const query: DiscoveryQuery = {...};
const results = await client.discovery.search(query);
```

**Agent-to-Agent Communication:**

See [`code/agent-communication.py`](./code/agent-communication.py) for the complete example.

```python
from velim import AgentClient

agent = AgentClient(agent_id="...", parent_entity="...", private_key="...")
response = agent.query_intent(target_entity="...", intent_id="...", questions=[...])

if response.suggests_meeting:
    meeting = agent.schedule_meeting(...)
```

### Appendix E: Verification Checklist

**Level 1: Self-Attested**
- [ ] Email verification
- [ ] Social profile linking (Twitter, LinkedIn, GitHub)
- [ ] Basic profile completeness (>50%)

**Level 2: Domain Verified**
- [ ] DNS TXT record verification
- [ ] SSL certificate validation
- [ ] Website with matching information

**Level 3: Legal Entity**
- [ ] Business registration documents
- [ ] Tax ID verification
- [ ] Physical address validation
- [ ] D-U-N-S number (for enterprises)

**Level 4: Community Endorsed**
- [ ] 5+ endorsements from verified entities
- [ ] Active participation (10+ quality intents)
- [ ] Response rate >80%
- [ ] No disputes or violations

**Level 5: Audited**
- [ ] Third-party identity audit
- [ ] Financial verification
- [ ] Background checks (for individuals)
- [ ] Compliance certification
- [ ] Annual re-verification

### Appendix F: Contribution Guidelines

**How to Contribute to Velim:**

1. **Protocol Improvements**
   - Submit PIP (Protocol Improvement Proposal)
   - Discuss in community forum
   - Create reference implementation
   - Get DAO approval

2. **Code Contributions**
   - Fork repository
   - Create feature branch
   - Write tests (>80% coverage)
   - Submit pull request
   - Code review by maintainers

3. **Documentation**
   - Identify gaps or errors
   - Submit issues or PRs
   - Improve examples and tutorials
   - Translate to other languages

4. **Community Building**
   - Onboard new entities
   - Provide support in forums
   - Create content and tutorials
   - Organize local meetups

**Contribution Rewards:**
- Recognition in contributor list
- Early access to features
- Reputation boost in Velim
- Potential grants for major contributions

---

## References
- [Market Research Future: Global B2B Lead Generation Market](https://www.marketresearchfuture.com/reports/b2b-lead-generation-market-26577)  
- [Expandi: B2B CPL Benchmarks](https://expandi.io/blog/how-much-does-lead-generation-cost)  
- [Digital Silk: Lead Generation Statistics](https://www.digitalsilk.com/digital-trends/lead-generation-statistics)  
