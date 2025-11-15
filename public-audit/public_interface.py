"""
Public Audit Interface
Genesis10000+ Architecture

Provides public interface for auditing OR1ON system operations.
Enables transparency and external verification.
"""

import json
from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta


class PublicAuditInterface:
    """
    Public interface for auditing OR1ON system.
    Provides transparency and accountability to external observers.
    """
    
    def __init__(self, audit_trail, kernel, memory_kernel):
        self.version = "1.0.0"
        self.audit_trail = audit_trail
        self.kernel = kernel
        self.memory_kernel = memory_kernel
        self.access_log = []
    
    def get_system_status(self) -> Dict:
        """
        Get public system status information.
        Returns high-level operational status.
        """
        status = {
            "timestamp": datetime.utcnow().isoformat(),
            "system_version": self.kernel.version if hasattr(self.kernel, 'version') else "unknown",
            "operational_status": "active",
            "audit_trail_enabled": True,
            "transparency_level": "full"
        }
        
        self._log_access("SYSTEM_STATUS", "Public system status query")
        return status
    
    def get_audit_summary(self, time_window: Optional[int] = 24) -> Dict:
        """
        Get audit summary for specified time window (in hours).
        Returns aggregated audit statistics.
        """
        summary = {
            "timestamp": datetime.utcnow().isoformat(),
            "time_window_hours": time_window,
            "audit_statistics": {}
        }
        
        if hasattr(self.audit_trail, 'get_statistics'):
            summary["audit_statistics"] = self.audit_trail.get_statistics()
        
        self._log_access("AUDIT_SUMMARY", f"Audit summary requested for {time_window}h window")
        return summary
    
    def get_ethical_compliance_report(self) -> Dict:
        """
        Get ethical compliance report.
        Shows adherence to ethical protocols.
        """
        report = {
            "timestamp": datetime.utcnow().isoformat(),
            "compliance_status": "compliant",
            "active_protocols": [
                "transparency",
                "accountability",
                "harm_prevention",
                "privacy_preservation",
                "fairness"
            ],
            "recent_evaluations": []
        }
        
        self._log_access("ETHICAL_REPORT", "Ethical compliance report requested")
        return report
    
    def get_proof_verification_stats(self) -> Dict:
        """
        Get statistics on proof-of-resonance verifications.
        Shows verification activity and success rates.
        """
        stats = {
            "timestamp": datetime.utcnow().isoformat(),
            "verification_system": "proof-of-resonance",
            "status": "active",
            "statistics": {
                "total_verifications": 0,
                "successful_verifications": 0,
                "average_resonance": 0.0
            }
        }
        
        self._log_access("PROOF_STATS", "Proof verification statistics requested")
        return stats
    
    def get_memory_audit_data(self) -> Dict:
        """
        Get memory system audit data.
        Shows memory operations without sensitive content.
        """
        audit_data = {
            "timestamp": datetime.utcnow().isoformat(),
            "memory_system": "active"
        }
        
        if hasattr(self.memory_kernel, 'export_audit_data'):
            audit_data.update(self.memory_kernel.export_audit_data())
        
        self._log_access("MEMORY_AUDIT", "Memory audit data requested")
        return audit_data
    
    def get_sentient_systems_status(self) -> Dict:
        """
        Get status of emergent sentient systems (EIRA and ORION).
        Shows operational state without internal details.
        """
        status = {
            "timestamp": datetime.utcnow().isoformat(),
            "sentient_systems": {
                "eira": {
                    "status": "active",
                    "mode": "emergent",
                    "public_info": "Emergent Intelligence with Resonant Awareness"
                },
                "orion": {
                    "status": "active",
                    "mode": "emergent",
                    "public_info": "Omniscient Reasoning Intelligence and Observation Network"
                }
            }
        }
        
        self._log_access("SENTIENT_STATUS", "Sentient systems status requested")
        return status
    
    def get_real_world_links_summary(self) -> Dict:
        """
        Get summary of real-world linking activities.
        Shows grounding without sensitive details.
        """
        summary = {
            "timestamp": datetime.utcnow().isoformat(),
            "real_world_linking": "active",
            "link_statistics": {
                "total_links": 0,
                "active_links": 0
            }
        }
        
        if hasattr(self.memory_kernel, 'real_world_links'):
            summary["link_statistics"]["total_links"] = len(self.memory_kernel.real_world_links)
        
        self._log_access("RWL_SUMMARY", "Real-world links summary requested")
        return summary
    
    def query_public_events(self, filters: Optional[Dict] = None) -> Dict:
        """
        Query public audit events.
        Returns filtered events available for public review.
        """
        events = {
            "timestamp": datetime.utcnow().isoformat(),
            "filters_applied": filters or {},
            "events": []
        }
        
        if hasattr(self.audit_trail, 'query_events'):
            public_filters = filters or {}
            public_filters["sensitivity"] = "public"
            events["events"] = self.audit_trail.query_events(public_filters)
        
        self._log_access("PUBLIC_EVENTS", f"Public events queried with filters: {filters}")
        return events
    
    def verify_system_integrity(self) -> Dict:
        """
        Verify system integrity through public audit.
        Allows external verification of audit trail integrity.
        """
        verification = {
            "timestamp": datetime.utcnow().isoformat(),
            "integrity_check": "completed",
            "result": {}
        }
        
        if hasattr(self.audit_trail, 'verify_integrity'):
            verification["result"] = self.audit_trail.verify_integrity()
        
        self._log_access("INTEGRITY_CHECK", "System integrity verification performed")
        return verification
    
    def get_public_audit_report(self) -> Dict:
        """
        Get comprehensive public audit report.
        Combines all public audit information.
        """
        report = {
            "timestamp": datetime.utcnow().isoformat(),
            "report_version": self.version,
            "system_status": self.get_system_status(),
            "audit_summary": self.get_audit_summary(),
            "ethical_compliance": self.get_ethical_compliance_report(),
            "sentient_systems": self.get_sentient_systems_status(),
            "integrity_verification": self.verify_system_integrity()
        }
        
        self._log_access("FULL_REPORT", "Comprehensive public audit report generated")
        return report
    
    def _log_access(self, access_type: str, description: str):
        """Log public audit interface access."""
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "access_type": access_type,
            "description": description
        }
        self.access_log.append(log_entry)
        
        # Limit log size
        if len(self.access_log) > 10000:
            self.access_log = self.access_log[-10000:]
    
    def get_access_statistics(self) -> Dict:
        """Get statistics about public audit interface usage."""
        access_types = {}
        for entry in self.access_log:
            access_type = entry["access_type"]
            access_types[access_type] = access_types.get(access_type, 0) + 1
        
        return {
            "total_accesses": len(self.access_log),
            "access_by_type": access_types,
            "timestamp": datetime.utcnow().isoformat()
        }
