"""
Audit Trail System
Genesis10000+ Architecture

Comprehensive audit logging and tracking system for all OR1ON operations.
Ensures transparency and accountability.
"""

import json
import hashlib
from typing import Dict, List, Optional, Any
from datetime import datetime
from enum import Enum


class AuditEventType(Enum):
    """Types of audit events."""
    SYSTEM_INIT = "system_initialization"
    KERNEL_OPERATION = "kernel_operation"
    ETHICAL_DECISION = "ethical_decision"
    AI_PROCESSING = "ai_processing"
    MEMORY_ACCESS = "memory_access"
    SENTIENT_ACTIVITY = "sentient_activity"
    PROOF_VERIFICATION = "proof_verification"
    SECURITY_EVENT = "security_event"
    DATA_ACCESS = "data_access"
    CONFIGURATION_CHANGE = "configuration_change"


class AuditTrail:
    """
    Comprehensive audit trail system for OR1ON.
    Maintains immutable log of all system activities.
    """
    
    def __init__(self):
        self.version = "1.0.0"
        self.audit_log = []
        self.event_index = {}
        self.chain_integrity = []
        self.public_audit_enabled = True
    
    def log_event(self, event_type: AuditEventType, description: str,
                  actor: str, metadata: Optional[Dict] = None,
                  sensitivity: str = "public") -> str:
        """
        Log an audit event with full context.
        Returns the event ID.
        """
        event_id = self._generate_event_id()
        
        audit_entry = {
            "event_id": event_id,
            "timestamp": datetime.utcnow().isoformat(),
            "event_type": event_type.value,
            "description": description,
            "actor": actor,
            "metadata": metadata or {},
            "sensitivity": sensitivity,
            "chain_hash": None
        }
        
        # Add chain integrity hash
        audit_entry["chain_hash"] = self._compute_chain_hash(audit_entry)
        
        # Store event
        self.audit_log.append(audit_entry)
        
        # Index event
        self._index_event(event_id, event_type, audit_entry)
        
        # Update integrity chain
        self._update_integrity_chain(audit_entry)
        
        return event_id
    
    def query_events(self, filters: Optional[Dict] = None,
                    start_time: Optional[str] = None,
                    end_time: Optional[str] = None) -> List[Dict]:
        """
        Query audit events with optional filters.
        Supports time-based and type-based filtering.
        """
        results = self.audit_log.copy()
        
        # Apply filters
        if filters:
            if "event_type" in filters:
                results = [e for e in results if e["event_type"] == filters["event_type"]]
            
            if "actor" in filters:
                results = [e for e in results if e["actor"] == filters["actor"]]
            
            if "sensitivity" in filters:
                results = [e for e in results if e["sensitivity"] == filters["sensitivity"]]
        
        # Apply time filters
        if start_time:
            results = [e for e in results if e["timestamp"] >= start_time]
        
        if end_time:
            results = [e for e in results if e["timestamp"] <= end_time]
        
        return results
    
    def verify_integrity(self) -> Dict:
        """
        Verify integrity of the audit trail.
        Checks chain consistency and detects tampering.
        """
        verification = {
            "timestamp": datetime.utcnow().isoformat(),
            "total_events": len(self.audit_log),
            "integrity_verified": True,
            "issues": []
        }
        
        # Verify chain hashes
        for i, entry in enumerate(self.audit_log):
            expected_hash = self._compute_chain_hash(entry, i - 1 if i > 0 else None)
            if entry["chain_hash"] != expected_hash:
                verification["integrity_verified"] = False
                verification["issues"].append({
                    "event_id": entry["event_id"],
                    "issue": "Chain hash mismatch"
                })
        
        return verification
    
    def export_public_audit_data(self) -> Dict:
        """
        Export audit data for public review.
        Filters sensitive information.
        """
        public_events = [
            {
                "event_id": e["event_id"],
                "timestamp": e["timestamp"],
                "event_type": e["event_type"],
                "description": e["description"],
                "actor": e["actor"]
            }
            for e in self.audit_log
            if e["sensitivity"] == "public"
        ]
        
        return {
            "version": self.version,
            "export_timestamp": datetime.utcnow().isoformat(),
            "total_public_events": len(public_events),
            "events": public_events,
            "integrity_status": self.verify_integrity()
        }
    
    def get_statistics(self) -> Dict:
        """Get statistics about audit trail."""
        event_types = {}
        for event in self.audit_log:
            event_type = event["event_type"]
            event_types[event_type] = event_types.get(event_type, 0) + 1
        
        return {
            "total_events": len(self.audit_log),
            "event_types": event_types,
            "public_events": sum(1 for e in self.audit_log if e["sensitivity"] == "public"),
            "chain_length": len(self.chain_integrity),
            "oldest_event": self.audit_log[0]["timestamp"] if self.audit_log else None,
            "newest_event": self.audit_log[-1]["timestamp"] if self.audit_log else None
        }
    
    def _generate_event_id(self) -> str:
        """Generate unique event ID."""
        timestamp = datetime.utcnow().isoformat()
        count = len(self.audit_log)
        return hashlib.sha256(f"{timestamp}:{count}".encode()).hexdigest()[:16]
    
    def _compute_chain_hash(self, entry: Dict, prev_index: Optional[int] = None) -> str:
        """Compute chain hash for integrity verification."""
        # Create hash from entry data
        entry_data = {
            "event_id": entry["event_id"],
            "timestamp": entry["timestamp"],
            "event_type": entry["event_type"],
            "description": entry["description"]
        }
        
        # Include previous hash if exists
        if prev_index is not None and prev_index >= 0:
            prev_hash = self.audit_log[prev_index].get("chain_hash", "")
            entry_data["prev_hash"] = prev_hash
        
        hash_input = json.dumps(entry_data, sort_keys=True)
        return hashlib.sha256(hash_input.encode()).hexdigest()
    
    def _index_event(self, event_id: str, event_type: AuditEventType, entry: Dict):
        """Index event for fast retrieval."""
        type_key = event_type.value
        if type_key not in self.event_index:
            self.event_index[type_key] = []
        
        self.event_index[type_key].append(event_id)
    
    def _update_integrity_chain(self, entry: Dict):
        """Update integrity chain."""
        chain_entry = {
            "event_id": entry["event_id"],
            "timestamp": entry["timestamp"],
            "hash": entry["chain_hash"]
        }
        self.chain_integrity.append(chain_entry)
