# Risk Assessment — jQuery 1.12

| Risk | Severity | Notes |
|---|---|---|
| JSONP JavaScript execution | High | src/ajax/jsonp.js executes callback code returned by an external server. An untrusted response can execute malicious JavaScript. |
| Outdated development dependencies | High | package.json uses an old Grunt 0.4.5 toolchain and legacy development packages, increasing maintenance and compatibility risks. |
| Legacy browser compatibility | Medium | src/ajax/xhr.js includes ActiveX support for older Internet Explorer versions, adding complexity to the transport implementation. |
| Global JSONP callback management | Medium | src/ajax/jsonp.js temporarily modifies window properties. Callback conflicts or incomplete cleanup may cause unexpected behavior. |
| Selector integration coupling | Medium | src/selector-sizzle.js exposes Sizzle functions through jQuery APIs. Changes to this integration may affect selector behavior and backward compatibility. |
| Event handler lifecycle complexity | Medium | src/event.js supports delegation, namespaces, and one-time handlers. Complex handler combinations can make debugging and cleanup more difficult. |

## Prioritization

High-severity risks should be addressed first, particularly JSONP security and outdated development dependencies. Medium-severity risks should be managed through compatibility testing, regression tests, and gradual refactoring.

## Assessment Scope

This assessment is based on the inspected jQuery 1.12 source files and package metadata. Severity levels represent potential impact and maintenance risk, not confirmed incidents.
