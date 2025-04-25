# FIDO2 Perimeter Authentication Guide

**Summary**  
Deploy FIDO2/WebAuthn for passwordless multi-factor authentication at the application perimeter.

## Prerequisites
- WebAuthn-compatible front-end
- Identity provider supporting FIDO2 (Azure AD, Okta, Auth0)
- TLS certificate for your application domain

## Steps
1. **Configure Identity Provider**  
   Enable FIDO2/WebAuthn in the IdP console and register your application.  
2. **Client Registration**  
   Implement registration flow to store credential ID and public key in user profile.  
3. **Authentication Flow**  
   - Use `navigator.credentials` API to prompt for authenticator.  
   - Verify assertion on server side using stored public key.  
4. **Fallback and Recovery**  
   Provide alternative recovery methods (e.g., email OTP) for lost authenticators.  
5. **Security Considerations**  
   - Enforce attestation checks.  
   - Reject non-compliant authenticators.  

## Example Snippet
```javascript
const cred = await navigator.credentials.create({
  publicKey: registrationOptions
});
```

## References
- W3C WebAuthn Specification  
- FIDO Alliance Best Practices  
