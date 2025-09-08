#!/usr/bin/env python3
"""
PayloadDiscovery Powerset Agent - Completion Style Example

This shows how to use the PayloadDiscovery agent with HEAVEN's completion runner
for direct prompt → response execution.

Usage:
    python run_payloaddiscovery_completion.py "Create a curriculum for X"
"""

import asyncio
import os
import logging
import traceback
import argparse

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Set up environment
os.environ['HEAVEN_DATA_DIR'] = '/tmp/heaven_data'

from heaven_base.tool_utils.completion_runners import exec_completion_style
from payloaddiscovery_powerset_agent import create_payloaddiscovery_agent


async def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Run PayloadDiscovery Powerset Agent with custom prompt")
    parser.add_argument("prompt", help="The prompt to send to the agent")
    args = parser.parse_args()
    
    print("🌟 PayloadDiscovery Powerset Agent - Completion Style Example")
    print("="*60)
    
    # Create the PayloadDiscovery agent
    print("📝 Creating PayloadDiscovery agent...")
    logger.info("Creating PayloadDiscovery powerset agent")
    agent_config = create_payloaddiscovery_agent()
    print(f"✅ Agent created: {agent_config.name}")
    logger.info(f"Agent created successfully: {agent_config.name}")
    
    # Use the prompt from command line
    prompt = args.prompt
    
    print(f"\n💭 Prompt: {prompt}")
    print("\n🤖 Agent Response:")
    print("-" * 60)
    
    try:
        # Execute using completion style
        logger.info("Executing agent with completion style")
        result = await exec_completion_style(
            prompt=prompt,
            agent=agent_config
        )
        logger.info("Agent execution completed successfully")
        
        # Display the result
        if isinstance(result, dict) and 'messages' in result:
            for msg in result['messages']:
                if hasattr(msg, 'content'):
                    print(msg.content)
        else:
            print(result)
            
    except Exception as e:
        logger.error(f"Error executing PayloadDiscovery agent: {e}", exc_info=True)
        print(f"❌ Error: {e}")
        print(f"📊 Traceback: {traceback.format_exc()}")
        print("\nNote: Make sure you have:")
        print("- OPENAI_API_KEY environment variable set")
        print("- All required dependencies installed")
        print("- HEAVEN framework properly configured")


if __name__ == "__main__":
    asyncio.run(main())