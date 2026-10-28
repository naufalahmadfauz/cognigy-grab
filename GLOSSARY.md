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

**Business line**:
The merchant's Grab service, such as GrabMart or GrabFood, that determines the applicable compensation guidance.
_Avoid_: Product when referring to an ordered item

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
