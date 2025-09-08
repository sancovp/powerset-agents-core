#!/usr/bin/env python3
"""
MetaStack Powerset Agent - Hermes Style Example

This shows how to use the MetaStack agent with HEAVEN's Hermes runner
for structured agent execution with iterations.

Usage:
    python run_metastack_hermes.py
"""

import asyncio
import os
import logging
import traceback

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Set up environment
os.environ['HEAVEN_DATA_DIR'] = '/tmp/heaven_data'

from heaven_base.tool_utils.hermes_utils import use_hermes_dict
from metastack_powerset_agent import create_metastack_agent


async def main():
    print("🌟 MetaStack Powerset Agent - Hermes Style Example")
    print("="*60)
    
    # Create the MetaStack agent
    print("📝 Creating MetaStack agent...")
    logger.info("Creating MetaStack powerset agent")
    agent_config = create_metastack_agent()
    print(f"✅ Agent created: {agent_config.name}")
    logger.info(f"Agent created successfully: {agent_config.name}")
    
    # Goal for structured execution
    goal = """Build a comprehensive Pydantic model system for an e-commerce platform that includes:
1. User model (with authentication fields)
2. Product model (with inventory tracking)
3. Order model (with status tracking)
4. Shopping cart functionality

Include validation, relationships between models, and methods for generating formatted summaries."""
    
    print(f"\n🎯 Goal: {goal}")
    print(f"\n🔄 Running with 3 iterations...")
    print("🤖 Agent Process:")
    print("-" * 60)
    
    try:
        # Execute using Hermes runner
        logger.info("Executing agent with Hermes runner")
        result = await use_hermes_dict(
            goal=goal,
            iterations=3,
            agent=agent_config,
            target_container="mind_of_god",
            source_container="mind_of_god",
            return_summary=False,
            ai_messages_only=True
        )
        logger.info("Agent execution completed successfully")
        
        print("✅ Hermes execution completed!")
        print("="*60)
        print(f"📊 Status: {result.get('status', 'Unknown')}")
        print(f"🆔 History ID: {result.get('history_id', 'No history ID')}")
        
        if 'messages' in result:
            print(f"💬 Messages count: {len(result['messages'])}")
            print("\n🤖 Final AI Response:")
            print("-" * 40)
            
            # Show the final AI response
            for msg in result['messages']:
                if msg.get('type') == 'AIMessage':
                    content = msg.get('content', '')
                    print(content)
                    break  # Show only the final response
        else:
            print("📝 Result:")
            print(result)
            
    except Exception as e:
        logger.error(f"Error executing MetaStack agent with Hermes: {e}", exc_info=True)
        print(f"❌ Error: {e}")
        print(f"📊 Traceback: {traceback.format_exc()}")
        print("\nNote: Make sure you have:")
        print("- OPENAI_API_KEY environment variable set")
        print("- All required dependencies installed")
        print("- HEAVEN framework properly configured")
        print("- Docker container setup if using cross-container execution")


if __name__ == "__main__":
    asyncio.run(main())