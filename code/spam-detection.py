class SpamDetector:
    def assess_intent(self, intent: Intent) -> SpamScore:
        signals = {
            'creation_velocity': self.check_creation_rate(intent.entity_id),
            'content_quality': self.nlp_quality_check(intent.content),
            'reputation': self.get_entity_reputation(intent.entity_id),
            'verification': self.get_verification_level(intent.entity_id),
            'similarity_to_spam': self.compare_to_spam_corpus(intent),
            'behavioral_patterns': self.check_behavior(intent.entity_id)
        }
        
        spam_score = self.weighted_score(signals)
        
        if spam_score > 0.8:
            return SpamScore.HIGH_RISK
        elif spam_score > 0.5:
            return SpamScore.MODERATE_RISK
        else:
            return SpamScore.LOW_RISK
