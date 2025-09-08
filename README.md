# Powerset Agents Core

Factory for creating self-improving BaseHeavenAgent instances that learn libraries through PayloadDiscovery sequences.

## Overview

Powerset Agents Core provides a standardized way to create HEAVEN framework agents that:
- Learn libraries through structured PayloadDiscovery learning sequences
- Track progress using STARLOG MCP for session management
- Navigate waypoints using Waypoint MCP for guided learning
- Use NetworkEditTool and BashTool for hands-on exploration
- Self-improve by creating new learning materials

## Installation

```bash
pip install powerset-agents-core
```

## Quick Start

```python
from powerset_agents_core import create_library_powerset_agent
from payload_discovery.core import load_payload_discovery

# Load learning sequence
pd = load_payload_discovery("/path/to/learning_sequence.json")

# Create agent configuration
agent_config = create_library_powerset_agent(
    pkg_path="pydantic_stack_core",
    help_command="python -c 'import pydantic_stack_core; help(pydantic_stack_core)'",
    payload_discovery=pd,
    name="MetaStackLearningAgent",
    starlog_path="/tmp/metastack_learning_session",
    description="Agent that learns the MetaStack library"
)

# Use with HEAVEN framework to create actual agent
# (Implementation depends on HEAVEN framework integration)
```

## Architecture

### BasePowersetAgentConfig
Base configuration for all powerset agents with:
- Agent identity (name, description) 
- HEAVEN configuration (model, max_iterations)
- Session paths (starlog_path, workspace_path)
- Standard MCP servers (waypoint, starlog)
- Standard tools (networkedittool, bashtool)

### LibraryPowersetAgentConfig  
Extends BasePowersetAgentConfig for library learning with:
- Target library (pkg_path, help_command)
- Learning sequence (PayloadDiscovery)

### Factory Function
`create_library_powerset_agent()` converts LibraryPowersetAgentConfig to HeavenAgentConfig with:
- Configured MCP servers and tools
- Generated system prompt for library learning
- Library-specific configuration embedded

## Agent Behavior

1. **Initialize**: Start STARLOG session for learning tracking
2. **Navigate**: Use Waypoint MCP to follow PayloadDiscovery sequence  
3. **Introspect**: Use help_command to explore the target library
4. **Explore**: Use NetworkEditTool and BashTool for hands-on learning
5. **Document**: Create examples, tests, and documentation
6. **Log**: Track discoveries and insights in STARLOG
7. **Improve**: Generate new learning materials for future sessions

## Dependencies

- `heaven-framework`: BaseHeavenAgent and core framework
- `starlog-mcp`: Session tracking and progress logging
- `payload-discovery`: Structured learning sequences and Waypoint MCP
- `pydantic>=2.0.0`: Configuration models

## License

MIT License