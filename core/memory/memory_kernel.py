"""
Memory Kernel Module
Genesis10000+ Architecture

Implements adaptive memory management with context-aware retention
and real-world linking capabilities.
"""

import json
import hashlib
from datetime import datetime
from typing import Dict, List, Optional, Any
from collections import defaultdict


class MemoryKernel:
    """
    Core memory management system with adaptive retention and linking.
    Supports both short-term and long-term memory with resonance-based prioritization.
    """
    
    def __init__(self):
        self.version = "1.0.0"
        self.memory_store = {
            "short_term": [],
            "long_term": {},
            "resonance_map": defaultdict(float)
        }
        self.real_world_links = {}
        self.memory_capacity = {
            "short_term": 1000,
            "long_term": float('inf')
        }
    
    def store(self, data: Any, context: Optional[Dict] = None, 
              memory_type: str = "short_term") -> str:
        """
        Store data in memory with optional context.
        Returns a memory identifier.
        """
        memory_id = self._generate_memory_id(data)
        
        memory_entry = {
            "id": memory_id,
            "data": data,
            "context": context or {},
            "timestamp": datetime.utcnow().isoformat(),
            "access_count": 0,
            "resonance_score": 0.5
        }
        
        if memory_type == "short_term":
            self.memory_store["short_term"].append(memory_entry)
            self._prune_short_term_memory()
        else:
            self.memory_store["long_term"][memory_id] = memory_entry
        
        return memory_id
    
    def recall(self, memory_id: str) -> Optional[Dict]:
        """Recall a memory by its identifier."""
        # Check short-term memory
        for entry in self.memory_store["short_term"]:
            if entry["id"] == memory_id:
                entry["access_count"] += 1
                self._update_resonance(memory_id, 0.1)
                return entry
        
        # Check long-term memory
        if memory_id in self.memory_store["long_term"]:
            entry = self.memory_store["long_term"][memory_id]
            entry["access_count"] += 1
            self._update_resonance(memory_id, 0.1)
            return entry
        
        return None
    
    def link_to_real_world(self, memory_id: str, real_world_ref: str, 
                           metadata: Optional[Dict] = None):
        """
        Create a link between memory and real-world reference.
        Enables grounding of abstract concepts.
        """
        link_id = f"{memory_id}:{real_world_ref}"
        
        self.real_world_links[link_id] = {
            "memory_id": memory_id,
            "real_world_ref": real_world_ref,
            "metadata": metadata or {},
            "created_at": datetime.utcnow().isoformat(),
            "strength": 1.0
        }
        
        return link_id
    
    def get_linked_memories(self, real_world_ref: str) -> List[Dict]:
        """Retrieve all memories linked to a real-world reference."""
        linked = []
        for link_id, link_data in self.real_world_links.items():
            if link_data["real_world_ref"] == real_world_ref:
                memory = self.recall(link_data["memory_id"])
                if memory:
                    linked.append({
                        "memory": memory,
                        "link": link_data
                    })
        return linked
    
    def _generate_memory_id(self, data: Any) -> str:
        """Generate unique identifier for memory entry."""
        content = json.dumps(data, sort_keys=True, default=str)
        timestamp = datetime.utcnow().isoformat()
        return hashlib.sha256(f"{content}:{timestamp}".encode()).hexdigest()[:16]
    
    def _update_resonance(self, memory_id: str, delta: float):
        """Update resonance score for a memory."""
        self.memory_store["resonance_map"][memory_id] += delta
    
    def _prune_short_term_memory(self):
        """Prune short-term memory based on capacity and resonance."""
        if len(self.memory_store["short_term"]) > self.memory_capacity["short_term"]:
            # Sort by resonance score (ascending) and remove lowest
            self.memory_store["short_term"].sort(
                key=lambda x: self.memory_store["resonance_map"].get(x["id"], 0)
            )
            # Promote high-resonance memories to long-term
            for entry in self.memory_store["short_term"][-10:]:
                if self.memory_store["resonance_map"].get(entry["id"], 0) > 0.8:
                    self.memory_store["long_term"][entry["id"]] = entry
            
            # Keep only top items
            self.memory_store["short_term"] = self.memory_store["short_term"][-self.memory_capacity["short_term"]:]
    
    def get_memory_statistics(self) -> Dict:
        """Get statistics about current memory state."""
        return {
            "short_term_count": len(self.memory_store["short_term"]),
            "long_term_count": len(self.memory_store["long_term"]),
            "real_world_links": len(self.real_world_links),
            "total_resonance_entries": len(self.memory_store["resonance_map"])
        }
    
    def export_audit_data(self) -> Dict:
        """Export memory data for public audit."""
        return {
            "version": self.version,
            "statistics": self.get_memory_statistics(),
            "timestamp": datetime.utcnow().isoformat(),
            "capacity_config": self.memory_capacity
        }
