# Velim Protocol Schemas

This directory contains the JSON schema definitions for the Velim protocol.

## Files

### [`intent-schema.json`](./intent-schema.json)
Complete schema for intent-signals (wishes) in the Velim protocol. Defines structure for:
- Intent metadata (ID, entity, version, timestamps)
- Content (title, description, tags, location)
- Requirements (must-haves, nice-to-haves, deal-breakers)
- Constraints (budget, timeline, capacity)
- Matching preferences
- Attestation proofs

### [`entity-profile-schema.json`](./entity-profile-schema.json)
Complete schema for entity profiles. Defines structure for:
- Identity information
- Verification methods and badges
- Capabilities and offerings
- Reputation scores and statistics
- Agent interface configuration
- Privacy settings

### [`attestation-schema.json`](./attestation-schema.json)
Schema for chain-agnostic attestations. Defines:
- Attestation metadata
- Cryptographic proofs
- Chain anchoring information
- Revocation status

## Usage

These schemas are referenced in the main whitepaper (`velim_v1.md`) and serve as the canonical definition for Velim protocol data structures.

## Versioning

Current version: **1.0.0**

Schema changes follow semantic versioning:
- Major version: Breaking changes
- Minor version: Backward-compatible additions
- Patch version: Clarifications and fixes
