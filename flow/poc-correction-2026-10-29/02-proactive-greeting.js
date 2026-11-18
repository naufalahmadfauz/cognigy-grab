/* Native first-entry greeting only. Existing Once owns the session guard.
   Never speak ahead of an already-available Merchant utterance or on a timeout event.
   greetingDelivered records emission, not completed audio playback. */
const state = context.shortTermMemory?.uc4;
const hasMerchantText = typeof input.text === "string" && input.text.trim().length > 0;
const event = typeof input.data?.event === "string" ? input.data.event : "";
const isNativeStart = event === "" || event === "CALL_CREATED" || event === "CALL_IN_PROGRESS";
if (state && state.greetingDelivered !== true && !hasMerchantText && isNativeStart) {
  api.say("Hi, I'm your Grab AI Assistant, and I'll be assisting you today. Please note that this call will be recorded for quality assurance and training purposes. How may I help you today?");
  state.greetingDelivered = true;
}
