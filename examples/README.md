# Powerset Agents Examples

This directory contains examples showing how to run the powerset agents using different HEAVEN framework execution patterns.

## Available Examples

### Completion Style (Direct Execution)
- `run_metastack_completion.py` - MetaStack agent using completion runner
- `run_payloaddiscovery_completion.py` - PayloadDiscovery agent using completion runner

### Hermes Style (Structured Iterations)  
- `run_metastack_hermes.py` - MetaStack agent using Hermes runner

### Interactive CLI
- Use `python -m metastack_powerset_agent.cli` 
- Use `python -m payloaddiscovery_powerset_agent.cli`

## Prerequisites

1. **Environment Setup:**
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   export HEAVEN_DATA_DIR="/tmp/heaven_data"
   ```

2. **Dependencies:**
   - HEAVEN framework installed
   - powerset-agents-core library
   - All required Python packages

3. **For CLI Examples:**
   - HEAVEN HTTP server running: `python /home/GOD/core/image/http_server.py`

## Execution Patterns

### Completion Style
Best for: Simple, direct prompt → response interactions
```python
from heaven_base.tool_utils.completion_runners import exec_completion_style
result = await exec_completion_style(prompt="Build me X", agent=agent_config)
```

### Hermes Style  
Best for: Complex, multi-step tasks requiring iterations
```python
from heaven_base.tool_utils.hermes_utils import use_hermes_dict
result = await use_hermes_dict(goal="Build X", iterations=3, agent=agent_config)
```

### Interactive CLI
Best for: Conversational development sessions
```python
from heaven_base.cli import make_cli
cli = make_cli(agent_config=agent_config)
cli.run_sync()
```

## Agent Capabilities

### MetaStack Powerset Agent
- Learns `pydantic_stack_core` library
- Generates any Pydantic model system that produces string output
- Builds data validation, serialization, and business logic models

### PayloadDiscovery Powerset Agent
- Learns `payload_discovery` library  
- Creates prompt injection sequences for waypoint
- Builds learning curricula and structured educational content

## Expected Workflow

Each agent follows this pattern:
1. **Session Management**: Uses STARLOG for tracking progress
2. **Library Learning**: Uses waypoint with learning curriculum  
3. **Task Completion**: Builds what you requested using library knowledge
4. **GitHub Upload**: Uses waypoint to create and upload projects

## Troubleshooting

- **Import Errors**: Check that HEAVEN framework and agents are in PYTHONPATH
- **API Errors**: Verify OPENAI_API_KEY is set correctly  
- **Execution Errors**: Check logs for detailed traceback information
- **CLI Connection**: Ensure HEAVEN HTTP server is running for CLI examples