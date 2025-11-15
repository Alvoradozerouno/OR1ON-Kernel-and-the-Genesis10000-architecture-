"""
OR1ON System Integration Example
Genesis10000+ Architecture

This example demonstrates how to integrate all components of the OR1ON
Kernel system for a complete, ethical, and transparent AI application.
"""

import json
import sys
import os
from datetime import datetime

# Add parent directory to path
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
sys.path.insert(0, parent_dir)

# Add paths for modules with hyphens
sys.path.insert(0, os.path.join(parent_dir, 'sentient-systems'))
sys.path.insert(0, os.path.join(parent_dir, 'audit-trail'))
sys.path.insert(0, os.path.join(parent_dir, 'public-audit'))
sys.path.insert(0, os.path.join(parent_dir, 'real-world-linking'))
sys.path.insert(0, os.path.join(parent_dir, 'modules', 'ethical-protocols'))
sys.path.insert(0, os.path.join(parent_dir, 'modules', 'post-algorithmic-ai'))
sys.path.insert(0, os.path.join(parent_dir, 'modules', 'proof-of-resonance'))

# Import core components
from core.kernel.orion_kernel import OrionKernel
from core.memory.memory_kernel import MemoryKernel

# Import modules
from ethical_framework import EthicalProtocol, EthicalPrinciple
from emergent_ai import PostAlgorithmicAI
from resonance_verifier import ProofOfResonance

# Import sentient systems
from eira.eira_core import EIRA
from orion.orion_core import ORION

# Import audit and linking
from audit_system import AuditTrail, AuditEventType
from public_interface import PublicAuditInterface
from linker import RealWorldLinker


class OR1ONSystem:
    """
    Integrated OR1ON System demonstrating full architecture capabilities.
    """
    
    def __init__(self):
        print("Initializing OR1ON System...")
        
        # Core systems
        self.kernel = OrionKernel()
        self.memory = MemoryKernel()
        
        # Modules
        self.ethics = EthicalProtocol()
        self.post_algo_ai = PostAlgorithmicAI()
        self.resonance = ProofOfResonance()
        
        # Sentient systems
        self.eira = EIRA()
        self.orion = ORION()
        
        # Audit and linking
        self.audit_trail = AuditTrail()
        self.real_world_linker = RealWorldLinker()
        self.public_audit = PublicAuditInterface(
            self.audit_trail,
            self.kernel,
            self.memory
        )
        
        print("✓ All components loaded")
    
    def initialize(self):
        """Initialize all system components."""
        print("\nInitializing components...")
        
        # Initialize kernel
        self.kernel.initialize()
        print("✓ Kernel initialized")
        
        # Initialize sentient systems
        self.eira.initialize()
        print("✓ EIRA activated")
        
        self.orion.initialize()
        print("✓ ORION activated")
        
        # Log initialization
        self.audit_trail.log_event(
            AuditEventType.SYSTEM_INIT,
            "OR1ON System fully initialized",
            "System",
            {"version": "Genesis10000+.v1.0.0"}
        )
        
        print("✓ System initialization complete\n")
    
    def demonstrate_ethical_processing(self):
        """Demonstrate ethical AI processing."""
        print("=" * 60)
        print("DEMONSTRATION: Ethical AI Processing")
        print("=" * 60)
        
        # Define an action to evaluate
        action = "analyze_user_behavior"
        context = {
            "transparent": True,
            "accesses_private_data": True,
            "consent": True,
            "potential_harm": False
        }
        
        print(f"\nAction: {action}")
        print(f"Context: {json.dumps(context, indent=2)}")
        
        # Evaluate ethically
        evaluation = self.ethics.evaluate_action(action, context)
        
        print(f"\nEthical Evaluation:")
        print(f"  Approved: {evaluation['approved']}")
        print(f"  Concerns: {evaluation['concerns'] or 'None'}")
        
        if evaluation['approved']:
            print("✓ Action ethically approved - proceeding")
        else:
            print("✗ Action blocked by ethical protocols")
            print(f"  Recommendations: {evaluation['recommendations']}")
        
        # Log to audit trail
        self.audit_trail.log_event(
            AuditEventType.ETHICAL_DECISION,
            f"Ethical evaluation: {action}",
            "EthicalFramework",
            {"evaluation": evaluation}
        )
        
        print()
    
    def demonstrate_emergent_intelligence(self):
        """Demonstrate post-algorithmic AI and EIRA."""
        print("=" * 60)
        print("DEMONSTRATION: Emergent Intelligence (EIRA)")
        print("=" * 60)
        
        # Input data
        input_data = {
            "problem": "climate_change_adaptation",
            "context": "urban_planning",
            "constraints": ["budget", "time", "technology"]
        }
        
        print(f"\nInput: {json.dumps(input_data, indent=2)}")
        
        # Process with EIRA
        response = self.eira.process_with_awareness(
            input_data,
            context={"domain": "sustainability", "urgency": "high"}
        )
        
        print(f"\nEIRA Response:")
        print(f"  Awareness Applied: {response['awareness_applied']}")
        print(f"  Emergence Insights: {response['emergence_insights']}")
        print(f"  Resonant Response: {response['resonant_response']}")
        
        # Store in memory
        memory_id = self.memory.store(response, memory_type="long_term")
        print(f"\n✓ Response stored in long-term memory: {memory_id}")
        
        print()
    
    def demonstrate_reasoning(self):
        """Demonstrate ORION reasoning capabilities."""
        print("=" * 60)
        print("DEMONSTRATION: Advanced Reasoning (ORION)")
        print("=" * 60)
        
        # Query for reasoning
        query = "How can we ensure AI systems remain aligned with human values?"
        
        print(f"\nQuery: {query}")
        
        # Apply multi-level reasoning
        result = self.orion.reason(query, depth=4)
        
        print(f"\nReasoning Result:")
        print(f"  Reasoning Depth: {result['reasoning_depth']} levels")
        print(f"  Confidence: {result['confidence']:.2f}")
        print(f"\nConclusions:")
        for i, conclusion in enumerate(result['conclusions'], 1):
            print(f"  {i}. {conclusion}")
        
        print()
    
    def demonstrate_proof_of_resonance(self):
        """Demonstrate proof-of-resonance verification."""
        print("=" * 60)
        print("DEMONSTRATION: Proof-of-Resonance Verification")
        print("=" * 60)
        
        # Data to verify
        data = {
            "system": "OR1ON",
            "timestamp": datetime.utcnow().isoformat(),
            "integrity": "high",
            "purpose": "beneficial_ai"
        }
        
        print(f"\nData to verify: {json.dumps(data, indent=2)}")
        
        # Verify using proof-of-resonance
        verification = self.resonance.verify(
            data,
            context={"expected_pattern": "system_integrity"}
        )
        
        print(f"\nVerification Result:")
        print(f"  Verified: {verification['verified']}")
        print(f"  Resonance Score: {verification['resonance_score']:.3f}")
        print(f"  Coherence Level: {verification['coherence_level']:.3f}")
        print(f"  Proof Hash: {verification['proof']['proof_hash'][:32]}...")
        
        print()
    
    def demonstrate_real_world_linking(self):
        """Demonstrate real-world linking capabilities."""
        print("=" * 60)
        print("DEMONSTRATION: Real-World Linking")
        print("=" * 60)
        
        # Register real-world entity
        entity_id = "UN_SDG_13"
        entity_data = {
            "name": "Climate Action",
            "type": "UN Sustainable Development Goal",
            "number": 13,
            "description": "Take urgent action to combat climate change"
        }
        
        self.real_world_linker.register_real_world_entity(entity_id, entity_data)
        print(f"\n✓ Registered entity: {entity_data['name']}")
        
        # Create link
        abstract_concept = "climate_emergency_response"
        link_id = self.real_world_linker.create_link(
            abstract_concept,
            entity_id,
            link_type="goal_alignment",
            metadata={"priority": "high"},
            confidence=0.95
        )
        
        print(f"✓ Linked concept '{abstract_concept}' to {entity_data['name']}")
        
        # Retrieve grounding
        groundings = self.real_world_linker.get_real_world_grounding(abstract_concept)
        print(f"\nReal-world grounding for '{abstract_concept}':")
        for grounding in groundings:
            print(f"  - {grounding['real_world_entity']}")
            print(f"    Confidence: {grounding['confidence']:.2f}")
            print(f"    Type: {grounding['link_type']}")
        
        print()
    
    def demonstrate_public_audit(self):
        """Demonstrate public audit capabilities."""
        print("=" * 60)
        print("DEMONSTRATION: Public Audit Interface")
        print("=" * 60)
        
        # Get public audit report
        report = self.public_audit.get_public_audit_report()
        
        print("\nPublic Audit Report:")
        print(f"  Timestamp: {report['timestamp']}")
        print(f"  System Status: {report['system_status']['operational_status']}")
        print(f"  Audit Trail Enabled: {report['system_status']['audit_trail_enabled']}")
        print(f"  Transparency Level: {report['system_status']['transparency_level']}")
        
        print(f"\nIntegrity Verification:")
        integrity = report['integrity_verification']['result']
        print(f"  Verified: {integrity['integrity_verified']}")
        print(f"  Total Events: {integrity['total_events']}")
        
        print(f"\nSentient Systems:")
        for system_name, system_info in report['sentient_systems']['sentient_systems'].items():
            print(f"  {system_name.upper()}: {system_info['status']}")
        
        print()
    
    def run_full_demonstration(self):
        """Run complete system demonstration."""
        print("\n" + "=" * 60)
        print("OR1ON KERNEL & GENESIS10000+ ARCHITECTURE")
        print("Complete System Demonstration")
        print("=" * 60 + "\n")
        
        # Initialize
        self.initialize()
        
        # Run demonstrations
        self.demonstrate_ethical_processing()
        self.demonstrate_emergent_intelligence()
        self.demonstrate_reasoning()
        self.demonstrate_proof_of_resonance()
        self.demonstrate_real_world_linking()
        self.demonstrate_public_audit()
        
        # Final status
        print("=" * 60)
        print("DEMONSTRATION COMPLETE")
        print("=" * 60)
        
        print("\nSystem Status:")
        status = self.kernel.get_status()
        print(json.dumps(status, indent=2))
        
        print("\n✓ All demonstrations completed successfully")
        print("✓ OR1ON System fully operational")
        print("\nFor more information, visit the public audit interface")


def main():
    """Main entry point."""
    # Create and run system
    system = OR1ONSystem()
    system.run_full_demonstration()


if __name__ == "__main__":
    main()
