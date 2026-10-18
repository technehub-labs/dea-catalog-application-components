# OIDC Discovery

# 1. Component name and identifier
- Component name: OIDC Discovery
- Identifier: `dea:information-system-component-oidc-discovery`

# 2. Definition
The OIDC Discovery is a sub-component (F4) of the Identity Broker. It implements the OIDC Discovery endpoint (`/.well-known/openid-configuration`) that returns the OIDC provider metadata to clients.

# 3. Purpose and scope
The OIDC Discovery's purpose is to expose the OIDC provider metadata. The metadata includes the issuer URL, the authorization endpoint, the token endpoint, the userinfo endpoint, the JWKS URI, the supported scopes, the supported response types, and the supported signing algorithms. The scope is metadata publication.

# 4. Component type
IntegrationComponent (IGC)

# 5. F-level assignment
F4 (Sub-Component)

# 6. Component-domain assignment
`iscc:domain:security` (ISCC-07)

# 7. Orthogonal classification facets
- Component kind: igc
- Hosting model: cloud, on-premises
- Execution characteristics: on-demand
- Component criticality: business-critical
- Deployment pattern: replicated
- Security posture: public-internet, encrypted-in-transit
- Automation characteristics: gitops-automated

# 8. Composition (parent, children)
- Parent: `dea:information-system-component-identity-broker` (F2)
- Children: (none; F4 is a leaf in this catalogue)

# 9. Composition edges
- (none; the parent is recorded in the `parent` field)

# 10. Functional realization (functions realized by this component)
- `dea:information-system-function-oidc-metadata-publication`: executes

# 11. Cross-references (components related by other metamodel relationships)
- (none)

# 12. Hosting and deployment
The OIDC Discovery is deployed as part of the Identity Broker. The endpoint is publicly accessible; the response is cached at the edge for 1 hour.

# 13. Criticality and security posture
The OIDC Discovery is business-critical. The endpoint is publicly accessible. The response is signed; clients MUST verify the signature before using the metadata.

# 14. Performance characteristics
The OIDC Discovery handles 1,000 requests per second at peak with a p99 latency of 5ms. The response is served from a memory cache with a 1-hour TTL.

# 15. Disaster recovery posture
The OIDC Discovery inherits the Identity Broker's DR posture (RTO 15 minutes, RPO 5 minutes). The metadata is regenerated automatically on configuration changes.

# 16. Compliance posture
The OIDC Discovery is compliant with the OIDC Discovery 1.0 specification. The metadata is signed with a key that is rotated annually.

# 17. Owner
Identity Platform team (DEA-Identity@example.com)

# 18. Change history
- 1.0: 2026-10-18: Initial F4 example record (CR-IS-CAT-02B). The 02C population exercise may supersede this with the P1 component inventory.

# 19. References
- `change-requests/CR-IS-CAT-02B-documentation.md` (the CR doc that establishes this standard)
- `docs/decomposition-guide.md` (the F0-F5 model)
- `../dea-isc-identity-broker/component.yaml` (the parent F2)
- `../dea-isc-identity-broker/README.md` (the parent F2 README)
