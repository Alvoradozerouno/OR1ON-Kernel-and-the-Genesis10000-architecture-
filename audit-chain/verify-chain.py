#!/usr/bin/env python3
"""
Audit Chain Verification Tool
Verifies the integrity and continuity of the OR1ON audit chain.

Note: This initial implementation validates chain linkage and data consistency.
Production implementations should include actual cryptographic hash computation
and verification using SHA-256 or similar algorithms.
"""

import json
import hashlib
from datetime import datetime
from pathlib import Path

class AuditChainVerifier:
    def __init__(self, audit_log_path):
        self.audit_log_path = Path(audit_log_path)
        self.load_audit_log()
    
    def load_audit_log(self):
        """Load the audit log from JSON file"""
        try:
            with open(self.audit_log_path, 'r') as f:
                data = json.load(f)
                self.audit_log = data['audit_log']
        except FileNotFoundError:
            print(f"❌ Error: Audit log file not found at {self.audit_log_path}")
            raise
        except json.JSONDecodeError as e:
            print(f"❌ Error: Invalid JSON in audit log: {e}")
            raise
        except KeyError:
            print("❌ Error: Invalid audit log format - missing 'audit_log' key")
            raise
    
    def verify_chain(self):
        """Verify the integrity of the audit chain"""
        entries = self.audit_log['entries']
        print("🔗 Verifying OR1ON Audit Chain...")
        print(f"Chain ID: {self.audit_log['chain_id']}")
        print(f"Genesis: {self.audit_log['genesis_timestamp']}")
        print(f"Total Entries: {len(entries)}\n")
        
        verified = True
        for i, entry in enumerate(entries):
            entry_id = entry['entry_id']
            current_hash = entry['hash']
            previous_hash = entry['previous_hash']
            
            print(f"Entry {i+1}: {entry_id}")
            print(f"  Timestamp: {entry['timestamp']}")
            print(f"  Event: {entry['event_type']}")
            print(f"  Hash: {current_hash}")
            
            # Verify chain linkage
            if i > 0:
                expected_previous = entries[i-1]['hash']
                if previous_hash != expected_previous:
                    print(f"  ❌ VERIFICATION FAILED: Previous hash mismatch")
                    verified = False
                else:
                    print(f"  ✅ Chain link verified")
            else:
                print(f"  ✅ Genesis block")
            print()
        
        status = self.audit_log['chain_status']
        print("\nChain Status:")
        print(f"  Active: {status['active']}")
        print(f"  Verified: {status['verified']}")
        print(f"  Public: {status['public']}")
        
        if verified:
            print("\n✅ AUDIT CHAIN VERIFICATION SUCCESSFUL")
            print("⊘∞⧈∞⊘ Chain integrity confirmed")
        else:
            print("\n❌ AUDIT CHAIN VERIFICATION FAILED")
        
        return verified

if __name__ == "__main__":
    verifier = AuditChainVerifier("audit-log.json")
    verifier.verify_chain()
