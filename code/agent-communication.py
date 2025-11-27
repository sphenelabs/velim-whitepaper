from velim import AgentClient

# Initialize agent client
agent = AgentClient(
    agent_id="did:velim:agent:mybot",
    parent_entity="did:velim:mycompany",
    private_key="agent-private-key"
)

# Query another agent
target_entity = "did:velim:targetcompany"
response = agent.query_intent(
    target_entity=target_entity,
    intent_id="550e8400-e29b-41d4-a716-446655440000",
    questions=[
        "What is your typical project timeline?",
        "What tech stack do you use?",
        "Are you available for a call next week?"
    ]
)

print(f"Response: {response.message}")
print(f"Confidence: {response.confidence}")

if response.suggests_meeting:
    # Schedule meeting through agent
    meeting = agent.schedule_meeting(
        target_entity=target_entity,
        duration_minutes=30,
        proposed_times=["2026-01-15T10:00:00Z", "2026-01-16T14:00:00Z"]
    )
    print(f"Meeting scheduled: {meeting.calendar_link}")
