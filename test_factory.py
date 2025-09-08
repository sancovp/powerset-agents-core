#!/usr/bin/env python3
"""Test the powerset-agents-core factory with a simple example."""

import sys
import json
from pathlib import Path

# Add the package to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from powerset_agents_core import create_library_powerset_agent
from powerset_agents_core.config import LibraryPowersetAgentConfig

# Create a mock PayloadDiscovery for testing
class MockPayloadDiscovery:
    def __init__(self):
        self.root_files = ["README.md", "setup.py"]
        self.directories = ["src", "tests"]
        
    def model_dump(self):
        return {
            "root_files": self.root_files,
            "directories": self.directories,
            "waypoints": []
        }

def test_factory():
    """Test creating a library powerset agent configuration."""
    
    # Create mock PayloadDiscovery
    pd = MockPayloadDiscovery()
    
    # Create agent config using factory
    agent_config = create_library_powerset_agent(
        pkg_path="example_library",
        help_command="python -c 'import example_library; help(example_library)'",
        payload_discovery=pd,
        name="ExampleLibraryAgent",
        starlog_path="/tmp/example_learning_session",
        description="Agent that learns the example library",
        model="gpt-5-mini"
    )
    
    # Print full details for verification
    print("Created agent config:")
    print(f"  Type: {type(agent_config)}")
    print(f"  Name: {agent_config.name}")
    print(f"  Model: {agent_config.model}")
    print(f"  Provider: {agent_config.provider}")
    print(f"  Tools: {agent_config.tools}")
    print(f"  MCP Servers: {agent_config.mcp_servers}")
    print(f"  Max Tokens: {agent_config.max_tokens}")
    print(f"  Temperature: {agent_config.temperature}")
    print(f"  Additional KWs: {agent_config.additional_kws}")
    print(f"  Additional KW Instructions: {agent_config.additional_kw_instructions}")
    print(f"  System Prompt (first 200 chars): {agent_config.system_prompt[:200] if agent_config.system_prompt else 'None'}")
    
    return agent_config

if __name__ == "__main__":
    config = test_factory()