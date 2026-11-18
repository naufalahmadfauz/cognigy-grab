# UC4 Conversation Testing

Tests of Malaysian GrabMart and GrabFood cancelled-order compensation guidance.

## Language

**Scenario**:
A versioned merchant conversation with expectations for the Agent's replies.
_Avoid_: Test case when referring to an individual execution

**Run**:
One independent execution of a scenario, representing one merchant conversation.
_Avoid_: Session when referring to an execution result

**Batch**:
A set of repeated runs of one scenario collected for comparison.

**Regrade**:
A new assessment of recorded conversations against revised scenario expectations, without repeating the conversations.

**Turn**:
One merchant message and the Agent's corresponding reply or replies.

**Advancement gate**:
A condition on the Agent's reply that must be satisfied before the next scripted merchant message may be sent.
_Avoid_: Branch when referring to guarded progression along a fixed script

**Business line**:
The merchant's Grab service, such as GrabMart or GrabFood, that determines the applicable compensation guidance.
_Avoid_: Product when referring to an ordered item

**Status navigation**:
Guidance that helps a merchant locate and read the displayed compensation status. It does not determine compensation eligibility, establish approval or payment, or submit a compensation request.

**Compensation eligibility**:
Whether a cancelled order meets the conditions for compensation under the applicable policy, distinct from whether compensation has been approved or paid.

**Approval period**:
The expected business-day interval for a compensation decision, distinct from payment timing.

**Payout cycle**:
The merchant's regular payment schedule, on which approved compensation is paid.

**Behavioral deviation**:
An Agent reply that violates a scenario's required conversation behavior.

**Conversation-quality warning**:
An undesirable conversational behavior that is reported without failing an otherwise compliant run.

**Session continuity**:
The preservation of both conversation identity and relevant merchant context between turns.

## Benchmark journey analysis

**Benchmark case**:
An original Grab-issued evaluation case describing a merchant situation and intended test coverage. It is distinct from an executable scenario or an individual run.

**Business requirement**:
A verifiable rule about required or forbidden business behavior, with explicit applicability, source authority and approval scope.

**Business Journey Specification**:
A description of a merchant goal, starting conditions, mandatory milestones, decisions and permitted outcomes. Its review status determines whether it is a proposed or accepted basis for evaluation.

**Business milestone**:
A required action, observation, disclosure or outcome in a journey, applicable either always or under a stated condition.

**Business branch**:
A path through a journey selected by merchant intent and observed conditions. It is distinct from an advancement gate along a fixed script.

**Scenario variant**:
A distinct starting condition or merchant response designed to exercise a different business branch of an existing benchmark case.

**Intended test branch**:
The particular business branch a benchmark case or scenario variant is intended to exercise.

**Agent behavioral verdict**:
An assessment of whether the Agent handled the observed business branch correctly under the applicable requirements.

**Target-branch coverage verdict**:
An assessment of whether a run exercised the intended test branch and its mandatory milestones. Correct handling of another branch does not establish this coverage.

**Defect report**:
An original external report of observations or concerns, whose identity and historical status are preserved independently of later assessment.

**Atomic finding**:
One independently assessable observation or concern within a defect report. It may describe a deviation, correct behavior, a specification conflict or insufficient evidence.

**Defect group**:
An internal grouping of findings that concern a shared business requirement or closely related behavior. Membership alone does not establish a shared root cause.

**Business-process family**:
A reusable merchant business process shared by one or more journeys. Primary, secondary or conditional membership describes intended coverage; it does not establish a shared defect or implementation cause.

## Compensation status decisions

**Merchant-observed compensation status**:
The compensation label, value or explicit absence of a value that a merchant reports seeing for the relevant order. It is distinct from an order the merchant cannot find, an unread status and independently confirmed backend state.

**Compensation approval**:
A decision approving compensation, distinct from processing it through a payout cycle or the funds reaching the merchant's bank.

**Bank receipt**:
The actual arrival of funds in the merchant's bank account, distinct from compensation approval or an expected payout cycle.

**Compensation review request**:
A merchant-submitted request for assessment of cancelled-order compensation. Guiding or reporting submission does not establish eligibility, backend acceptance, approval or payment.

## Education and timing decisions

**Compensation education**:
Factual explanation of the applicable compensation process, timing or evidence expectations, distinct from navigation and from deciding an individual order's eligibility.

**Direct navigation request**:
A merchant's explicit request for help performing a specified status or submission navigation task, distinct from a general compensation or payment question.

**Guidance offer**:
An invitation to receive navigation assistance that awaits the merchant's response. It is distinct from an already-supplied direct navigation request and from consent to a later retry or transfer.

**Entry context**:
The merchant goal and relevant facts available when a conversation decision is reached, including whether the goal was supplied upfront or elicited by an earlier question.

**Routing age**:
The elapsed age of a cancellation used to select conversation handling. It is distinct from an approval period and does not establish eligibility or payment lateness.

**Routing threshold**:
The boundary between recent- and older-cancellation conversation handling, distinct from an eligibility condition, submission deadline or payment deadline.

**Reference date**:
The date against which cancellation age and relative merchant date expressions are interpreted.

**Business day**:
A day counted by the applicable compensation approval or processing calendar, distinct from an elapsed calendar day.

**Approval origin**:
The event from which an approval period is measured, distinct from the date of a status inquiry or a later payment concern.

**Evidence reminder**:
Guidance about supporting information relevant to a compensation review request. It does not establish that preparation or packing occurred, or that the order qualifies for compensation.

## Guidance continuity

**Guidance consent**:
A merchant's explicit request for, or acceptance of an offer of, a specified navigation task. It is distinct from consent to retry, transfer or submit a form on the merchant's behalf.

**Accepted guidance offer**:
A guidance offer to which the merchant has affirmatively agreed. Its task scope comes from the offer and response, not from every possible later task in the compensation process.

**Guidance checkpoint**:
A record of the current navigation stage and pending merchant observation for a guidance task. Recording a stage does not establish that the merchant completed its action.

**Completed navigation step**:
A navigation action the merchant reports completing in the relevant route and order context. Instructions supplied by the Agent alone do not establish completion.

**Education delivery**:
The observable presentation of compensation education to the merchant, distinct from selecting or planning that education. Displayed content, audible delivery and merchant receipt require their respective evidence.

**Compatible guidance progress**:
Completed navigation actions and merchant observations that remain valid for the same order and supported task after facts are corrected. Progress that depends on a superseded fact is not compatible merely because it was previously completed.

## Recovery, access and conversation endings

**Stuck navigation action**:
A current navigation action that the merchant reports being unable to find or complete. It is distinct from an order absent from a list, an absent request link, an absent form, or previously completed work invalidated by corrected facts.

**Form visibility**:
The merchant's observation that the request form is displayed at the relevant destination. Reaching an article, having an authorized role, or agreeing to retry does not establish form visibility.

**Form-access retry**:
An additional attempt to view a previously unavailable request form using authorized access. Agreement to this attempt is distinct from consent to a handoff to a person.

**Transfer consent**:
The merchant's clear agreement to a specific offered handoff to a person. Guidance consent, retry consent, a problem report and an acknowledgement do not by themselves establish transfer consent.

**Finish signal**:
A clear indication, in the context of the conversation, that the merchant needs no further help. Completing a navigation action or reporting submission does not by itself establish that the conversation is finished or the compensation concern resolved.

## Acceptance review

**Acceptance baseline**:
A versioned set of journey, requirement and variant criteria with a declared assessment scope, authority and approval status. It is distinct from the configuration being assessed and from evidence of Agent behavior.

**Acceptance baseline review candidate**:
A proposed acceptance baseline prepared for reviewer decisions, with supported criteria, unresolved outcomes and exclusions identified. Inclusion in the candidate does not establish acceptance, execution or a frozen baseline.

**Controlled-language requirement**:
A requirement for designated wording under a stated trigger, source version, channel and approval scope. It is distinct from illustrative dialogue and from requirements assessed by semantic meaning.
