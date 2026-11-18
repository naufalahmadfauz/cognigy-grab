/* DF-011 v2: capture actually delivered Agent human-help offers on the Job Default branch.
   Do not create a consent offer from instructions, Tool args, or the Merchant's words.
   Permissible Agent output encodings are narrowly enumerated to handle platform
   differences without stringifying arbitrary input structures or logging PII. */
const state = context.shortTermMemory && context.shortTermMemory.uc4;
const output = input.aiAgentOutput;
function getText(value) {
  if (typeof value === "string") return value;
  if (Array.isArray(value)) return value.map(getText).filter(Boolean).join(" ");
  if (!value || typeof value !== "object") return "";
  for (const field of ["result", "text", "output", "message", "content"]) {
    if (typeof value[field] === "string") return value[field];
    if (Array.isArray(value[field])) {
      const v = getText(value[field]);
      if (v) return v;
    }
  }
  return "";
}
const generatedText = getText(output);
if (state && state.greetingDelivered !== true && generatedText.includes("Hi, I'm your Grab AI Assistant, and I'll be assisting you today. Please note that this call will be recorded for quality assurance and training purposes.")) {
  state.greetingDelivered = true;
}

if (state) {
  const utterance = generatedText.replace(/[\u2018\u2019]/g, "'").replace(/\s+/g, " ").trim();
  const normalized = utterance.toLowerCase();
  const originalRoleOffer = /would you like me to connect you with someone who can help further\s*\?/i.test(utterance);
  const equivalentPersonOffer = /(?:would you like|do you want)\s+(?:(?:me|us)\s+to\s+)?(?:connect|transfer)\s+you\s+(?:with|to)\s+(?:someone|a person|an agent)\b/i.test(utterance) ||
      /would you like to (?:speak|talk) (?:with|to) (?:someone|a person|an agent)\b/i.test(utterance);
  const offered = originalRoleOffer || equivalentPersonOffer;
  const scopeOffer = offered && /(?:i only handle issues about cancelled orders|i (?:can only|only) (?:help|assist) (?:with|on) cancelled orders)/i.test(normalized);
  const portalOffer = offered && /would you like me to connect you with someone who can help with your GrabMerchant portal access\s*\?/i.test(utterance);
  if (state.transfer && state.transfer.executed === true) {
    state.transferOffer = { pending: false, reason: "", source: "terminal" };
  } else if (offered) {
    state.transferOffer = {
      pending: true,
      reason: scopeOffer ? "out_of_scope" : (portalOffer ? "portal_unavailable" : "role_failed"),
      source: "agent_output",
      offeredInputId: typeof input.inputId === "string" ? input.inputId : ""
    };
  } else if (utterance !== "" && state.transferOffer && state.transferOffer.pending === true) {
    // A substantive new spoken response replaces the unanswered offer.
    state.transferOffer.pending = false;
  }
  // For privacy, log only whether capture occurred, the safe reason and output shape.
  if (offered && typeof api !== "undefined" && api && typeof api.log === "function") {
    api.log("info", "UC4 DF011 v2 offer captured: " + JSON.stringify({ pending: true, reason: state.transferOffer.reason, shape: Array.isArray(output) ? "array" : typeof output }));
  }
}
