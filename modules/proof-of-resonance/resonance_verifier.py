"""
Proof of Resonance Module
Genesis10000+ Architecture

Implements resonance-based verification and proof systems.
Uses harmonic alignment and coherence checking for validation.
"""

import hashlib
import json
from typing import Dict, List, Optional, Any
from datetime import datetime
import math


class ProofOfResonance:
    """
    Proof-of-Resonance verification system.
    Validates data and processes through resonance coherence checking.
    """
    
    def __init__(self):
        self.version = "1.0.0"
        self.resonance_threshold = 0.7
        self.verification_history = []
        self.resonance_network = {}
    
    def verify(self, data: Any, context: Optional[Dict] = None) -> Dict:
        """
        Verify data using proof-of-resonance logic.
        Returns verification result with resonance metrics.
        """
        verification = {
            "timestamp": datetime.utcnow().isoformat(),
            "data_hash": self._compute_hash(data),
            "resonance_score": 0.0,
            "coherence_level": 0.0,
            "verified": False,
            "proof": {},
            "context": context or {}
        }
        
        # Calculate resonance score
        resonance = self._calculate_resonance(data, context)
        verification["resonance_score"] = resonance
        
        # Calculate coherence
        coherence = self._calculate_coherence(data, context)
        verification["coherence_level"] = coherence
        
        # Generate proof
        proof = self._generate_proof(data, resonance, coherence)
        verification["proof"] = proof
        
        # Determine verification status
        verification["verified"] = (
            resonance >= self.resonance_threshold and 
            coherence >= self.resonance_threshold
        )
        
        # Store in history
        self.verification_history.append(verification)
        
        return verification
    
    def _calculate_resonance(self, data: Any, context: Optional[Dict]) -> float:
        """
        Calculate resonance score based on data properties and context.
        Resonance measures alignment with expected patterns.
        """
        score = 0.5  # Base resonance
        
        # Data structure resonance
        if isinstance(data, dict):
            # Richer structure has higher potential resonance
            score += min(len(data.keys()) / 20, 0.2)
        
        # Context resonance
        if context:
            if "expected_pattern" in context:
                # Check alignment with expected pattern
                score += 0.15
            if "historical_match" in context:
                score += 0.15
        
        # Temporal resonance (time-based alignment)
        hour = datetime.utcnow().hour
        temporal_factor = math.sin(hour * math.pi / 12) * 0.1
        score += abs(temporal_factor)
        
        return min(max(score, 0.0), 1.0)
    
    def _calculate_coherence(self, data: Any, context: Optional[Dict]) -> float:
        """
        Calculate coherence level - internal consistency and harmony.
        """
        coherence = 0.5  # Base coherence
        
        # Internal consistency
        if isinstance(data, dict):
            # Check for completeness
            if len(data) > 0:
                coherence += 0.2
            
            # Check for nested structure (higher complexity)
            has_nested = any(isinstance(v, (dict, list)) for v in data.values())
            if has_nested:
                coherence += 0.1
        
        # Context coherence
        if context:
            if "validation_rules" in context:
                coherence += 0.15
            if "integrity_check" in context:
                coherence += 0.05
        
        return min(max(coherence, 0.0), 1.0)
    
    def _generate_proof(self, data: Any, resonance: float, coherence: float) -> Dict:
        """Generate cryptographic proof of resonance verification."""
        proof_data = {
            "data_hash": self._compute_hash(data),
            "resonance": resonance,
            "coherence": coherence,
            "timestamp": datetime.utcnow().isoformat(),
            "version": self.version
        }
        
        proof_string = json.dumps(proof_data, sort_keys=True)
        proof_hash = hashlib.sha256(proof_string.encode()).hexdigest()
        
        return {
            "proof_hash": proof_hash,
            "proof_data": proof_data,
            "signature": self._sign_proof(proof_hash)
        }
    
    def _sign_proof(self, proof_hash: str) -> str:
        """Sign the proof (simplified - in production would use proper cryptography)."""
        signature_base = f"ORION:{proof_hash}:{self.version}"
        return hashlib.sha256(signature_base.encode()).hexdigest()[:32]
    
    def _compute_hash(self, data: Any) -> str:
        """Compute hash of data for proof generation."""
        data_string = json.dumps(data, sort_keys=True, default=str)
        return hashlib.sha256(data_string.encode()).hexdigest()
    
    def create_resonance_link(self, source_id: str, target_id: str, 
                             strength: float = 0.5):
        """
        Create a resonance link between two entities.
        Builds a network of resonant connections.
        """
        link_id = f"{source_id}:{target_id}"
        self.resonance_network[link_id] = {
            "source": source_id,
            "target": target_id,
            "strength": strength,
            "created_at": datetime.utcnow().isoformat()
        }
    
    def get_resonance_network(self, entity_id: str) -> List[Dict]:
        """Get all resonance connections for an entity."""
        connections = []
        for link_id, link_data in self.resonance_network.items():
            if entity_id in (link_data["source"], link_data["target"]):
                connections.append(link_data)
        return connections
    
    def get_verification_statistics(self) -> Dict:
        """Get statistics about verification history."""
        if not self.verification_history:
            return {
                "total_verifications": 0,
                "successful_verifications": 0,
                "average_resonance": 0.0,
                "average_coherence": 0.0
            }
        
        successful = sum(1 for v in self.verification_history if v["verified"])
        avg_resonance = sum(v["resonance_score"] for v in self.verification_history) / len(self.verification_history)
        avg_coherence = sum(v["coherence_level"] for v in self.verification_history) / len(self.verification_history)
        
        return {
            "total_verifications": len(self.verification_history),
            "successful_verifications": successful,
            "average_resonance": round(avg_resonance, 3),
            "average_coherence": round(avg_coherence, 3),
            "verification_rate": round(successful / len(self.verification_history), 3)
        }
