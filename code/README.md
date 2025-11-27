# Velim Protocol Code Examples

This directory contains code examples demonstrating how to interact with the Velim protocol.

## SDK Examples

### [`publish-intent.py`](./publish-intent.py)
**Python SDK - Publishing an Intent**
- Initialize Velim client with DID authentication
- Create and configure an intent object
- Publish intent and receive attestation

### [`discover-matches.ts`](./discover-matches.ts)
**TypeScript SDK - Discovering Matches**
- Search for matching intents using semantic queries
- Apply filters and preferences
- Process and display match results

### [`agent-communication.py`](./agent-communication.py)
**Agent-to-Agent Communication**
- Initialize AI agent client
- Query another agent's intent
- Automatically schedule meetings based on responses

## Algorithm Implementations

### [`reputation-calculation.py`](./reputation-calculation.py)
**Reputation Engine Functions**
- `calculate_time_decay()` - Reputation decay over time
- `calculate_incentive_multiplier()` - Reputation-based matching boosts

### [`spam-detection.py`](./spam-detection.py)
**Spam Detection System**
- Multi-signal spam assessment
- Risk level classification
- Behavioral pattern analysis

## Usage

### Prerequisites
```bash
# Python examples
pip install velim-sdk

# TypeScript examples
npm install @velim/sdk
```

### Running Examples

**Python:**
```bash
export VELIM_PRIVATE_KEY="your-private-key"
python publish-intent.py
```

**TypeScript:**
```bash
export VELIM_PRIVATE_KEY="your-private-key"
ts-node discover-matches.ts
```

## Development

These examples are maintained alongside the protocol specification. For the latest SDK documentation, visit:
- Python SDK: https://pypi.org/project/velim-sdk/
- TypeScript SDK: https://www.npmjs.com/package/@velim/sdk
- API Docs: https://docs.velim.io
