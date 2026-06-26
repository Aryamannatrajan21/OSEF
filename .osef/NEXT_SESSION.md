# OSEF Next Session

## Instructions for the Next Agent Waking Up

Welcome to OSEF. You must read `.osef/AI_CONTEXT.md` first.

**Your Goal for Sprint 5:**
We have just completed the EPSDK release freeze. The host abstractions exist, but they have not been proven in battle.

Your immediate next step is to create a **Reference Plugin** that exercises the `ExtensionContext`, subscribes to the `EventBus`, queries the EKG, and generates a report. 

Do not touch core logic. Build the plugin exactly as a third-party developer would using only `src/osef/sdk`.
