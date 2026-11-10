# P4 Coverage Report (CR-IS-CAT-02C-P4)

**Date**: 2026-11-10
**Scope**: P4 vendor-neutral component tranche (34 F0 + 63 F1 + 141 F2 =
238 records across 8 of 10 ISCC domains)
**Source**: vendor-neutral ISF/ISC reference catalog (OpenDEAM metamodel crawl)

## 1. Population methodology

The P4 tranche admits generic component classes realized by at least 3 distinct vendors; per
G-12 vendor products never become canonical component records. The F0-F5 model from
docs/decomposition-guide.md is applied: F0 (system class) contains F1 (component groups); F1
contains F2 (composite components); composition edges use kind=contains, cardinality=required.

## 2. Population summary

| Domain | F0 classes | F1 groups | F2 components | Total |
|---|---|---|---|---|
| Customer Experience | 3 | 7 | 19 | 29 |
| Employee Experience | 2 | 2 | 12 | 16 |
| Partner Integration | 2 | 2 | 2 | 6 |
| Core Operations | 14 | 39 | 83 | 136 |
| Data and Analytics | 3 | 3 | 3 | 9 |
| Integration | 4 | 4 | 5 | 13 |
| Security | 1 | 1 | 6 | 8 |
| Development Platform | 5 | 5 | 11 | 21 |

## 3. Class to domain mapping

| Generic system class | ISCC domain | Kind | Type |
|---|---|---|---|
| Card Payment Network | Core Operations | apc | ApplicationComponent |
| Claims Management System | Core Operations | apc | ApplicationComponent |
| Core Banking System | Core Operations | apc | ApplicationComponent |
| Electronic Health Record (EHR) System | Core Operations | apc | ApplicationComponent |
| Enterprise Resource Planning (ERP) System | Core Operations | apc | ApplicationComponent |
| Manufacturing Execution System (MES) | Core Operations | apc | ApplicationComponent |
| Mobile Core Network (EPC/5GC) | Core Operations | apc | ApplicationComponent |
| Payment Processing Platform | Core Operations | apc | ApplicationComponent |
| Policy Administration System | Core Operations | apc | ApplicationComponent |
| Radio Access Network (RAN) | Core Operations | apc | ApplicationComponent |
| Telecom Business Support System (BSS) | Core Operations | apc | ApplicationComponent |
| Telecom Operations Support System (OSS) | Core Operations | apc | ApplicationComponent |
| Transportation Management System (TMS) | Core Operations | apc | ApplicationComponent |
| Warehouse Management System (WMS) | Core Operations | apc | ApplicationComponent |
| Customer Relationship Management (CRM) System | Customer Experience | apc | ApplicationComponent |
| Customer Service Ticketing Platform | Customer Experience | apc | ApplicationComponent |
| E-Commerce Platform | Customer Experience | apc | ApplicationComponent |
| Cloud Data Warehouse | Data and Analytics | data | ApplicationComponent |
| Data Lakehouse Platform | Data and Analytics | data | ApplicationComponent |
| Workflow Orchestration Platform | Data and Analytics | apc | ApplicationComponent |
| Cloud Infrastructure Platform | Development Platform | igc | IntegrationComponent |
| Container Orchestration Platform | Development Platform | igc | IntegrationComponent |
| Continuous Integration / Continuous Delivery (CI/CD) Platform | Development Platform | igc | IntegrationComponent |
| Infrastructure as Code (IaC) Platform | Development Platform | igc | IntegrationComponent |
| Issue Tracking Platform | Development Platform | igc | IntegrationComponent |
| Human Capital Management (HCM) System | Employee Experience | apc | ApplicationComponent |
| IT Service Management (ITSM) Platform | Employee Experience | apc | ApplicationComponent |
| Communications Platform (CPaaS) | Integration | igc | IntegrationComponent |
| Email Delivery Platform | Integration | igc | IntegrationComponent |
| Event Streaming Platform | Integration | igc | IntegrationComponent |
| IoT Device Management Platform | Integration | igc | IntegrationComponent |
| Financial Messaging Network | Partner Integration | igc | IntegrationComponent |
| Supply Chain Visibility Platform | Partner Integration | apc | ApplicationComponent |
| Identity and Access Management (IAM) Platform | Security | security | ApplicationComponent |

## 4. Coverage closure

| Metric | Before P4 | After P4 |
|---|---:|---:|
| Component records | 38 | 276 |
| Domains populated | 10 of 10 | 10 of 10 |
| F0 / F1 records | 0 / 0 | 34 / 63 |
| Composition edges | 14 | 218 |

## 5. Facet coverage

Only the component_kind facet is asserted (apc / igc / data / security). Hosting, execution,
criticality, deployment, security and automation facets are deployment-specific across the
corroborating vendors and are deferred to per-deployment CRs (documented in each README
section 7; the coverage report records the deferral rather than assuming completeness, per
G-09).

## 6. Embargo and doctrine hygiene

All P4 content is authored in generic terminology; a standards-body token scan and an em-dash /
en-dash scan (D-004) run over every emitted file in the P4 pipeline, and a vendor-token scan
runs over every canonical field.
