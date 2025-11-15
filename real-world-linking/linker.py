"""
Real-World Linking Module
Genesis10000+ Architecture

Provides mechanisms for linking abstract concepts and AI operations
to real-world entities, events, and references.
"""

from typing import Dict, List, Optional, Any
from datetime import datetime
import hashlib
import json


class RealWorldLinker:
    """
    Real-World Linking system for grounding AI operations in reality.
    Connects abstract concepts to concrete real-world references.
    """
    
    def __init__(self):
        self.version = "1.0.0"
        self.links = {}
        self.entity_registry = {}
        self.validation_rules = {}
        self.link_graph = {}
    
    def create_link(self, abstract_concept: str, real_world_entity: str,
                    link_type: str, metadata: Optional[Dict] = None,
                    confidence: float = 1.0) -> str:
        """
        Create a link between abstract concept and real-world entity.
        Returns link ID.
        """
        link_id = self._generate_link_id(abstract_concept, real_world_entity)
        
        link = {
            "link_id": link_id,
            "timestamp": datetime.utcnow().isoformat(),
            "abstract_concept": abstract_concept,
            "real_world_entity": real_world_entity,
            "link_type": link_type,
            "metadata": metadata or {},
            "confidence": confidence,
            "validation_status": "pending"
        }
        
        # Validate link
        link["validation_status"] = self._validate_link(link)
        
        # Store link
        self.links[link_id] = link
        
        # Update graph
        self._update_link_graph(abstract_concept, real_world_entity, link_id)
        
        return link_id
    
    def register_real_world_entity(self, entity_id: str, entity_data: Dict) -> str:
        """
        Register a real-world entity in the system.
        Returns entity ID.
        """
        entity = {
            "entity_id": entity_id,
            "registered_at": datetime.utcnow().isoformat(),
            "data": entity_data,
            "verification_status": "verified",
            "linked_concepts": []
        }
        
        self.entity_registry[entity_id] = entity
        return entity_id
    
    def get_real_world_grounding(self, abstract_concept: str) -> List[Dict]:
        """
        Get all real-world groundings for an abstract concept.
        Returns list of linked entities.
        """
        groundings = []
        
        for link_id, link in self.links.items():
            if link["abstract_concept"] == abstract_concept:
                grounding = {
                    "link_id": link_id,
                    "real_world_entity": link["real_world_entity"],
                    "link_type": link["link_type"],
                    "confidence": link["confidence"],
                    "metadata": link["metadata"]
                }
                
                # Add entity details if available
                entity_id = link["real_world_entity"]
                if entity_id in self.entity_registry:
                    grounding["entity_details"] = self.entity_registry[entity_id]["data"]
                
                groundings.append(grounding)
        
        return groundings
    
    def get_abstract_concepts(self, real_world_entity: str) -> List[Dict]:
        """
        Get all abstract concepts linked to a real-world entity.
        Reverse lookup from entity to concepts.
        """
        concepts = []
        
        for link_id, link in self.links.items():
            if link["real_world_entity"] == real_world_entity:
                concepts.append({
                    "link_id": link_id,
                    "abstract_concept": link["abstract_concept"],
                    "link_type": link["link_type"],
                    "confidence": link["confidence"]
                })
        
        return concepts
    
    def validate_grounding(self, link_id: str, validation_data: Optional[Dict] = None) -> Dict:
        """
        Validate a real-world grounding link.
        Returns validation result.
        """
        if link_id not in self.links:
            return {
                "valid": False,
                "reason": "Link not found"
            }
        
        link = self.links[link_id]
        
        validation_result = {
            "link_id": link_id,
            "timestamp": datetime.utcnow().isoformat(),
            "valid": True,
            "confidence": link["confidence"],
            "checks": []
        }
        
        # Check confidence threshold
        if link["confidence"] < 0.5:
            validation_result["checks"].append({
                "check": "confidence_threshold",
                "passed": False,
                "message": "Confidence below threshold"
            })
            validation_result["valid"] = False
        else:
            validation_result["checks"].append({
                "check": "confidence_threshold",
                "passed": True
            })
        
        # Check entity registration
        if link["real_world_entity"] in self.entity_registry:
            validation_result["checks"].append({
                "check": "entity_registered",
                "passed": True
            })
        else:
            validation_result["checks"].append({
                "check": "entity_registered",
                "passed": False,
                "message": "Entity not registered"
            })
        
        return validation_result
    
    def strengthen_link(self, link_id: str, evidence: Dict):
        """
        Strengthen a link based on new evidence.
        Increases confidence and adds supporting data.
        """
        if link_id in self.links:
            link = self.links[link_id]
            
            # Increase confidence
            current_confidence = link["confidence"]
            evidence_weight = evidence.get("weight", 0.1)
            new_confidence = min(current_confidence + evidence_weight, 1.0)
            
            link["confidence"] = new_confidence
            
            # Add evidence to metadata
            if "evidence" not in link["metadata"]:
                link["metadata"]["evidence"] = []
            
            link["metadata"]["evidence"].append({
                "timestamp": datetime.utcnow().isoformat(),
                "evidence": evidence
            })
    
    def get_link_graph(self) -> Dict:
        """
        Get the complete link graph showing all connections.
        """
        return {
            "timestamp": datetime.utcnow().isoformat(),
            "total_links": len(self.links),
            "total_entities": len(self.entity_registry),
            "graph": self.link_graph
        }
    
    def _generate_link_id(self, concept: str, entity: str) -> str:
        """Generate unique link ID."""
        link_string = f"{concept}:{entity}:{datetime.utcnow().isoformat()}"
        return hashlib.sha256(link_string.encode()).hexdigest()[:16]
    
    def _validate_link(self, link: Dict) -> str:
        """Validate link integrity and consistency."""
        # Check confidence
        if link["confidence"] < 0.5:
            return "low_confidence"
        
        # Check if entity is registered
        if link["real_world_entity"] not in self.entity_registry:
            return "unregistered_entity"
        
        return "validated"
    
    def _update_link_graph(self, concept: str, entity: str, link_id: str):
        """Update the link graph with new connection."""
        if concept not in self.link_graph:
            self.link_graph[concept] = {
                "type": "abstract_concept",
                "links": []
            }
        
        self.link_graph[concept]["links"].append({
            "target": entity,
            "link_id": link_id,
            "type": "real_world_entity"
        })
    
    def export_audit_data(self) -> Dict:
        """Export linking data for public audit."""
        return {
            "version": self.version,
            "timestamp": datetime.utcnow().isoformat(),
            "statistics": {
                "total_links": len(self.links),
                "total_entities": len(self.entity_registry),
                "validated_links": sum(1 for l in self.links.values() if l["validation_status"] == "validated"),
                "average_confidence": sum(l["confidence"] for l in self.links.values()) / len(self.links) if self.links else 0.0
            }
        }
