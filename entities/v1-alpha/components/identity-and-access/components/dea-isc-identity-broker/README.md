# Identity Broker

# 1. Component name and identifier
- Component name: Identity Broker
- Identifier: `dea:information-system-component-identity-broker`

# 2. Definition
The Identity Broker is a composite component (F2) that federates identity and access decisions across multiple identity providers. It implements the OIDC and SAML protocols to expose a unified authentication and authorization surface to downstream applications.

# 3. Purpose and scope
The Identity Broker's purpose is to provide a single integration point for authentication and authorization decisions. It brokers identity assertions from upstream identity providers (e.g., enterprise SSO, social identity providers) and presents a unified assertion to downstream applications. The scope is authentication, authorization, session management, and federation.

# 4. Component type
IntegrationComponent (IGC)

# 5. F-level assignment
F2 (Composite Component)

# 6. Component-domain assignment
`iscc:domain:security` (ISCC-07)

# 7. Orthogonal classification facets
- Component kind: igc
- Hosting model: cloud, on-premises
- Execution characteristics: long-running
- Component criticality: mission-critical
- Deployment pattern: replicated
- Security posture: encrypted-at-rest, encrypted-in-transit
- Automation characteristics: gitops-automated

# 8. Composition (parent, children)
- Parent: (none; F2 is the top of the identity-and-access domain in this catalogue)
- Children:
  - `dea:information-system-component-oidc-discovery` (F4; OIDC Discovery)

# 9. Composition edges
- `dea:information-system-component-oidc-discovery`: contains (required)

# 10. Functional realization (functions realized by this component)
- `dea:information-system-function-identity-verification`: executes
- `dea:information-system-function-token-issuance`: executes
- `dea:information-system-function-session-management`: executes
- `dea:information-system-function-federation`: executes

# 11. Cross-references (components related by other metamodel relationships)
- `dea:information-system-component-policy-store`: depends-on
- `dea:information-system-component-audit-log`: produces

# 12. Hosting and deployment
The Identity Broker is deployed as a replicated service in a high-availability configuration. In the cloud, it is deployed on a managed Kubernetes platform. On-premises, it is deployed on a container orchestration platform. The deployment is automated through a GitOps pipeline.

# 13. Criticality and security posture
The Identity Broker is mission-critical. All requests and responses are encrypted in transit. The persistent state (sessions, refresh tokens) is encrypted at rest. The security posture is internal-network with selective public-internet exposure for federation.

# 14. Performance characteristics
The Identity Broker is designed to handle 10,000 requests per second at peak with a p99 latency of 50ms. The session storage is backed by a distributed in-memory store.

# 15. Disaster recovery posture
The Identity Broker has a recovery time objective (RTO) of 15 minutes and a recovery point objective (RPO) of 5 minutes. The cross-region replication is enabled.

# 16. Compliance posture
The Identity Broker is compliant with SOC 2 Type II, ISO 27001, and the relevant data protection regulations (GDPR, CCPA). The audit log is retained for 7 years.

# 17. Owner
Identity Platform team (DEA-Identity@example.com)

# 18. Change history
- 1.0: 2026-10-18: Initial F2 example record (CR-IS-CAT-02B). The 02C population exercise may supersede this with the P1 component inventory.

# 19. References
- `change-requests/CR-IS-CAT-02B-documentation.md` (the CR doc that establishes this standard)
- `docs/decomposition-guide.md` (the F0-F5 model)
- `taxonomy/` (the classification layer)
- `schemas/entities/information-system-component.v2.json` (the v2 schema)
- `templates/component-template.yaml` (the machine-readable template)
- `templates/README-template.md` (the 19-section README template)
