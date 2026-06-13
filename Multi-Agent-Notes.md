# Multi-Agent AI

## Multi-Agent AI System

- In a multi-agent system, multiple AI agents collab, each handling a specific subtask to solve a problem too complex for a single agent alone.

> Multi-agent system example: Claude Code

Other multi-agent system: Planning Agent, Code Write Agent, Code Review Agent, Test Agent, etc.

```
┌─────────────────────────────────────────────────────────┐
│                   MULTI-AGENT AI SYSTEM                 │
│                                                         │
│               ┌─────────────────────┐                  │
│               │  Orchestrator Agent │                  │
│               │  (Task Planner)     │                  │
│               └──────────┬──────────┘                  │
│                          │ delegates subtasks           │
│         ┌────────────────┼────────────────┐            │
│         ▼                ▼                ▼            │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐   │
│  │  Planning   │  │ Code Write  │  │   Code      │   │
│  │   Agent     │  │   Agent     │  │  Review     │   │
│  └─────────────┘  └─────────────┘  │   Agent     │   │
│                                    └─────────────┘   │
│         ┌────────────────────────────────┐           │
│         │          Test Agent            │           │
│         └────────────────────────────────┘           │
│                          │                            │
│                          ▼                            │
│               ┌─────────────────────┐                │
│               │   Final Output /    │                │
│               │   Merged Result     │                │
│               └─────────────────────┘                │
└─────────────────────────────────────────────────────────┘
```

## Multi-Modal AI System

- Same AI model can process multiple different kinds of format.
  
ex. you are building an agent for healthcare -> need to process text, images, notes, etc.

```
┌─────────────────────────────────────────────────────────┐
│                  MULTI-MODAL AI SYSTEM                  │
│                                                         │
│  Input Modalities                                       │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌────────┐ │
│  │   Text   │  │  Images  │  │  Audio   │  │  Video │ │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └───┬────┘ │
│       │             │             │             │      │
│       └─────────────┴─────────────┴─────────────┘      │
│                           │                            │
│                           ▼                            │
│               ┌───────────────────────┐               │
│               │   Single AI Model     │               │
│               │  (unified processing) │               │
│               └───────────┬───────────┘               │
│                           │                            │
│                           ▼                            │
│               ┌───────────────────────┐               │
│               │    Unified Output     │               │
│               │ (cross-modal insight) │               │
│               └───────────────────────┘               │
│                                                         │
│  Healthcare example:                                    │
│  text notes + X-ray images → single diagnosis response  │
└─────────────────────────────────────────────────────────┘
```
