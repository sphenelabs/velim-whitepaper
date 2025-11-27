import { VelimClient, DiscoveryQuery } from '@velim/sdk';

// Initialize client
const client = new VelimClient({
  entityId: 'did:velim:mycompany',
  privateKey: process.env.VELIM_PRIVATE_KEY,
  network: 'mainnet'
});

// Search for matches
const query: DiscoveryQuery = {
  semantic: "blockchain developers for DeFi project",
  filters: {
    type: ["offering", "collaboration"],
    categories: ["technology", "blockchain"],
    location: {
      regions: ["US", "EU"],
      remote_ok: true
    },
    reputation_min: 70
  },
  preferences: {
    limit: 20,
    sort_by: "match_score"
  }
};

const results = await client.discovery.search(query);

results.matches.forEach(match => {
  console.log(`Match Score: ${match.match_score}`);
  console.log(`Entity: ${match.entity.name}`);
  console.log(`Intent: ${match.intent.title}`);
  console.log(`Reasons: ${match.match_reasons.join(', ')}`);
  console.log('---');
});
