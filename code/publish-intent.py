from velim import VelimClient, Intent, EntityProfile

# Initialize client
client = VelimClient(
    entity_id="did:velim:mycompany",
    private_key="your-private-key",
    network="mainnet"
)

# Create intent
intent = Intent(
    type="seeking",
    title="Seeking Backend Engineers for Fintech Startup",
    description="We're hiring 3-5 senior backend engineers...",
    tags=["backend", "fintech", "golang", "kubernetes"],
    requirements={
        "must_have": ["5+ years experience", "Golang", "Microservices"],
        "nice_to_have": ["Fintech experience", "AWS certification"]
    },
    constraints={
        "budget": {
            "min": 120000,
            "max": 180000,
            "currency": "USD",
            "type": "recurring"
        },
        "timeline": {
            "start_date": "immediate",
            "duration": "P3M"
        }
    }
)

# Publish intent
result = client.publish_intent(intent)
print(f"Intent published: {result.intent_id}")
print(f"Attestation: {result.attestation_id}")
